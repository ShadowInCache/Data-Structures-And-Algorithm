# Write your MySQL query statement below
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d
ON d.id = e.departmentID
WHERE e.salary = (
    SELECT max(e2.salary)
    FROM Employee e2
    where e2.departmentID = e.departmentID
);