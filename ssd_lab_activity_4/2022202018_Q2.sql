DELIMITER $$
CREATE PROCEDURE SelectAllCustomers
(
    IN   CITY VARCHAR(30)   
 )
BEGIN 
SELECT CUST_NAME FROM customer WHERE  WORKING_AREA = CITY ; 
END $$
DELIMITER ;

Call SelectAllCustomers("Bangalore");
