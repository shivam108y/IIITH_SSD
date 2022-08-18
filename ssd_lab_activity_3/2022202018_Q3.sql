select Mgr_ssn,COUNT(Essn) as Number_of_projects from DEPARTMENT inner join PROJECT inner join WORKS_ON on Dnum=Dnumber and Mgr_ssn=Essn WHERE Pname='ProductY' GROUP BY Mgr_ssn ;

