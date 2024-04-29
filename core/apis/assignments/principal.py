from flask import Blueprint,make_response,jsonify
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment,AssignmentStateEnum
from datetime import datetime


from .schema import AssignmentSchema, AssignmentGradeSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)

@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of graded and submitted assignments"""
    students_assignments = Assignment.get_graded_and_submitted_assignments_by_student(p.student_id)
    students_assignments_dump = AssignmentSchema().dump(students_assignments, many=True)
    return APIResponse.respond(data=students_assignments_dump)


@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = incoming_payload
    assignment = Assignment.query.filter_by(id=grade_assignment_payload['id']).first()
    assignment_dump = AssignmentSchema().dump(assignment)
    print(assignment_dump, "aaaaa")
    if assignment.state == AssignmentStateEnum.DRAFT.value or assignment_dump['teacher_id'] is None:
        return make_response(jsonify({'error': 'FyleError', 'message': 'draft assignment can be submitted'}),400)
    graded_assignment = Assignment.mark_grade(
        _id=assignment.id,
        grade=incoming_payload['grade'],
        teacher_id=assignment.teacher_id,
        auth_principal=p
        )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
