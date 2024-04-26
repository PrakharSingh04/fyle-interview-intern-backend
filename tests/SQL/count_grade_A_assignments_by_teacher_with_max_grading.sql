-- Write query to find the number of grade A's given by the teacher who has graded the most assignmentsSELECT teacher_id, COUNT(*) AS grade_A_assignments_count
SELECT id,COUNT(*) AS graded_assignments_count
FROM assignments
WHERE grade = 'A'
GROUP BY teacher_id 
ORDER BY COUNT(*) DESC
LIMIT 1;



