from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment,AssignmentStateEnum

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
    grade_assignment_payload = AssignmentSchema().load(incoming_payload)
    ##assignment = Assignment.get_by_id(grade_assignment_payload.id)
   ## if assignment is None:
     ##   return jsonify({'error': 'FyleError', 'message': 'Assignment does not exist'}), 400
    
   ## if assignment.state == AssignmentStateEnum.DRAFT:
     ##   return jsonify({'error': 'FyleError', 'message': 'Cannot grade a draft assignment'}), 400
    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
        )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)
