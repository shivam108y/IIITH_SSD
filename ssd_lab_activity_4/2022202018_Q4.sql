DELIMITER $$
 CREATE PROCEDURE cur_move()
 BEGIN
	DECLARE C_NAME varchar(80) ;
	DECLARE C_CITY varchar(80) ;
	DECLARE C_GRADE DECIMAL(10,0);	
	DECLARE C_COUNTRY varchar(80) ;
	DECLARE finished integer default 0; 

 	DECLARE c1_cursor CURSOR FOR  SELECT CUST_NAME , CUST_CITY , CUST_COUNTRY , GRADE
    FROM customer WHERE AGENT_CODE like "A00%" ;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;
	 OPEN c1_cursor;

	get_emp: LOOP

			FETCH c1_cursor INTO C_NAME,C_CITY,C_COUNTRY,C_GRADE;

 			IF finished = 1 THEN

 			LEAVE get_emp;

	END IF;

 select C_NAME,C_CITY,C_COUNTRY,C_GRADE;

 END LOOP get_emp;

 CLOSE c1_cursor;

 END$$
 DELIMITER ;
 
  call cur_move();
