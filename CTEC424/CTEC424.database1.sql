/* department table created*/
CREATE table department
(
    departmentID int
);

/* department ID table created*/
CREATE table departmentID
(
    departmentID int
);

/* location table created*/
CREATE table location 
(
    locationID int
);

/*creating users and granting priveleges */
CREATE USER  Genesis IDENTIFIED BY password1;
CREATE USER Professor IDENTIFIED by password1; 
GRANT DBA to Professor;
GRANT DBA to Genesis;
