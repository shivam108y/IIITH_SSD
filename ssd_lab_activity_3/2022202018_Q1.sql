select CONCAT_WS('', Fname,' ',Minit,' ',Lname) AS Full_name,Ssn,Dno as Dept_Id,Dname as Dept_Name from EMPLOYEE inner join DEPARTMENT on EMPLOYEE.Dno=DEPARTMENT.Dnumber;

