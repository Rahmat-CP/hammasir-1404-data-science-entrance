WITH RECURSIVE subemployee AS (
    SELECT emp_id,
        last_name,
        manager_id,
        salary
    FROM employees
    WHERE manager_id = 27
    UNION ALL
    SELECT e.emp_id,
        e.last_name,
        e.manager_id,
        e.salary
    FROM employees e
        INNER JOIN subemployee s ON e.manager_id = s.emp_id
)
SELECT AVG(salary) AS avg_salary
FROM subemployee;