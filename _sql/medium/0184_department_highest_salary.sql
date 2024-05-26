SELECT department.NAME AS Department,
    employee.NAME AS Employee,
    employee.salary AS Salary
FROM employee
    LEFT JOIN department ON employee.departmentid = department.id
WHERE (departmentid, salary) IN (
        SELECT departmentid,
            Max(salary)
        FROM employee
        GROUP BY departmentid
    )