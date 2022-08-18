select Mgr_ssn as Manager_Ssn,Dnumber as Dept_Id,COUNT(Essn) as Number_of_Dependents from DEPARTMENT inner join DEPENDENT inner join (select Dnumber as deptNo,COUNT(Dnumber) as Dnum from DEPT_LOCATIONS GROUP BY DEPT_LOCATIONS.Dnumber) b on Mgr_ssn=Essn and b.deptNo=Dnumber and b.deptNo=Dnumber WHERE Dnum>1 GROUP BY Mgr_ssn,Dnumber;

