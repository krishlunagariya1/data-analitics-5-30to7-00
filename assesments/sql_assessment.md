# Data Analytics SQL Assessment

## Assessment 1:

Table Name: `Worker`
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY   | JOINING_DATE     | DEPARTMENT  |
|-----------|------------|-----------|----------|------------------|-------------|
|1          | Monika     | Arora     | 100000   | 2/20/2014 9:00   |HR           |
|2          | Niharika   | Verma     | 80000    | 6/11/2014 9:00   |Admin        |
|3          | Vishal     | Singhal   | 300000   | 2/20/2014 9:00   |HR           |
|4          | Amitabh    | Singh     | 500000   | 2/20/2014 9:00   |Admin        |
|5          | Vivek      | Bhati     | 500000   | 6/11/2014 9:00   |Admin        |
|6          | Vipul      | Diwan     | 200000   | 6/11/2014 9:00   |Account      |
|7          | Satish     | Kumar     | 75000    | 1/20/2014 9:00   |Account      |
|8          | Geetika    | Chauhan   | 90000    | 4/11/2014 9:00   |Admin        |

___

## Create Table and Insert Records

### CREATE TABLE Query:
```sql
CREATE TABLE Worker (
    WORKER_ID INT PRIMARY KEY,
    FIRST_NAME VARCHAR(50) NOT NULL,
    LAST_NAME VARCHAR(50) NOT NULL,
    SALARY INT,
    JOINING_DATE DATETIME,
    DEPARTMENT VARCHAR(50)
);
```

### INSERT Query:
```sql
INSERT INTO Worker (WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) VALUES
(1, 'Monika', 'Arora', 100000, '2014-02-20 09:00:00', 'HR'),
(2, 'Niharika', 'Verma', 80000, '2014-06-11 09:00:00', 'Admin'),
(3, 'Vishal', 'Singhal', 300000, '2014-02-20 09:00:00', 'HR'),
(4, 'Amitabh', 'Singh', 500000, '2014-02-20 09:00:00', 'Admin'),
(5, 'Vivek', 'Bhati', 500000, '2014-06-11 09:00:00', 'Admin'),
(6, 'Vipul', 'Diwan', 200000, '2014-06-11 09:00:00', 'Account'),
(7, 'Satish', 'Kumar', 75000, '2014-01-20 09:00:00', 'Account'),
(8, 'Geetika', 'Chauhan', 90000, '2014-04-11 09:00:00', 'Admin');
```

___

### Question 1: Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending and DEPARTMENT Descending.

**Query:-**
```sql
SELECT *
FROM Worker
ORDER BY FIRST_NAME ASC, DEPARTMENT DESC;
```
**Output:-**
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY   | JOINING_DATE     | DEPARTMENT  |
|-----------|------------|-----------|----------|------------------|-------------|
|1          | Monika     | Arora     | 100000   | 2/20/2014 9:00   |HR           |
|2          | Niharika   | Verma     | 80000    |  6/11/2014 9:00  |Admin        |
|3          | Vishal     | Singhal   | 300000   | 2/20/2014 9:00   |HR           |
|4          | Amitabh    | Singh     | 500000   | 2/20/2014 9:00   |Admin        |
|5          | Vivek      | Bhati     | 500000   | 6/11/2014 9:00   |Admin        |
|6          | Vipul      | Diwan     | 200000   | 6/11/2014 9:00   |Account      |
|7          | Satish     | Kumar     | 75000    | 1/20/2014 9:00   |Account      |
|8          | Geetika    | Chauhan   | 90000    |   4/11/2014 9:00 |Admin        |
___

### Question 2: Write an SQL query to print details for Workers with the first names “Vipul” and “Satish” from the Worker table.

**Query:-**
```sql
SELECT *
FROM Worker
WHERE FIRST_NAME IN ('Vipul', 'Satish');
```
**Output:-**
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY   | JOINING_DATE     | DEPARTMENT  |
|-----------|------------|-----------|----------|------------------|-------------|
|6          | Vipul      | Diwan     | 200000   | 6/11/2014 9:00   |Account      |
|7          | Satish     | Kumar     | 75000    | 1/20/2014 9:00   |Account      |
___

### Question 3: Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets.

**Query:-**
```sql
SELECT *
FROM Worker
WHERE FIRST_NAME LIKE '_____h';
```
**Output:-**
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY   | JOINING_DATE       | DEPARTMENT  |
|-----------|------------|-----------|----------|--------------------|-------------|
|7 	        |Satish      |Kumar      | 75000 	| 2014-01-20 09:00:00| 	Account    |

___

### Question 4: Write an SQL query to print details of the Workers whose SALARY lies between 100000 and 500000.

**Query:-**
```sql
SELECT *
FROM Worker
WHERE SALARY BETWEEN 100000 AND 500000;
```

**Output:-**

|WORKER_ID	|FIRST_NAME	|LAST_NAME	| SALARY	| JOINING_DATE	      |  DEPARTMENT|
|-----------|-----------|-----------|-----------|---------------------|------------|
| 3	        |Vishal	    |Singhal	| 300000	| 2014-02-20 09:00:00 | HR	       |
| 1	        |Monika	    |Arora	    | 100000	| 2014-02-20 09:00:00 | HR	       |
| 4	        |Amitabh	|Singh	    | 500000	| 2014-02-20 09:00:00 | Admin	   |
| 5	        |Vivek	    |Bhati	    | 500000	| 2014-06-11 09:00:00 | Admin	   |
| 6	        |Vipul	    |Diwan	    | 200000	| 2014-06-11 09:00:00 | Account    |

___

### Question 5: Write an SQL query to fetch duplicate records having matching data in some fields of a table.

**Query:-**
```sql
SELECT SALARY, JOINING_DATE, DEPARTMENT
FROM Worker
GROUP BY SALARY, JOINING_DATE, DEPARTMENT
HAVING COUNT(*) > 1;
```

**Output:-**

| SALARY | DEPARTMENT | count |
|--------|------------|-------|
| 500000 | Admin      | 2     |

___

### Question 6. Write an SQL query to show the top 6 records of a table.

**Query:-**
```sql
SELECT *
FROM Worker
LIMIT 6;
```

**Output:-**
| WORKER_ID | FIRST_NAME | LAST_NAME | SALARY   | JOINING_DATE     | DEPARTMENT  |
|-----------|------------|-----------|----------|------------------|-------------|
|1          | Monika     | Arora     | 100000   | 2/20/2014 9:00   |HR           |
|2          | Niharika   | Verma     | 80000    | 6/11/2014 9:00   |Admin        |
|3          | Vishal     | Singhal   | 300000   | 2 /20/2014 9:00  |HR           |
|4          | Amitabh    | Singh     | 500000   | 2/20/2014 9:00   |Admin        |
|5          | Vivek      | Bhati     | 500000   | 6/11/2014 9:00   |Admin        |
|6          | Vipul      | Diwan     | 200000   | 6/11/2014 9:00   |Account      |

___

### Question 7. Write an SQL query to fetch the departments that have less than five people in them.

**Query:-**
```sql
SELECT DEPARTMENT
FROM Worker
GROUP BY DEPARTMENT
HAVING COUNT(*) < 5;
```
**Output:-**
| DEPARTMENT  |
|-------------|
| Account     |
| Admin       |
| HR          |

___

### Question 8. Write an SQL query to show all departments along with the number of people in there.

**Query:-**
```sql
SELECT DEPARTMENT, COUNT(*) AS NumberOfPeople
FROM Worker
GROUP BY DEPARTMENT;
```
**Output:-**
| DEPARTMENT  | NumberOfPeople |
|-------------|----------------|
| Account     | 2              |
| Admin       | 4              |
| HR          | 2              |
___

### Question 9. Write an SQL query to print the name of employees having the highest salary in each department.

**Query:-**
```sql
SELECT DEPARTMENT,FIRST_NAME,LAST_NAME, MAX(SALARY) as Highest_Salary FROM worker GROUP BY DEPARTMENT;
```
**Output:-**

| DEPARTMENT | FIRST_NAME | LAST_NAME | Higest_Salary |
|------------|------------|-----------|---------------|
| HR         | Vishal     | Singhal   |     300000    |
| Admin      | Amitabh    | Singh     |     500000    |
| Admin      | Vivek      | Bhati     |     500000    |
| Account    | Vipul      | Diwan     |     200000    |


---
---
## Assignment 2:

### School Database - Student Table

  Table Name: `Student`

  | StdID | StdName          | Sex    | Percentage | Class | Sec | Stream   | DOB        |
  |-------|------------------|--------|------------|-------|-----|----------|------------|
  | 1001  | Surekha Joshi    | Female | 82         | 12    | A   | Science  | 3/8/1998   |
  | 1002  | MAAHI AGARWAL    | Female | 56         | 11    | C   | Commerce | 11/23/2008 |
  | 1003  | Sanam Verma      | Male   | 59         | 11    | C   | Commerce | 6/29/2006  |
  | 1004  | Ronit Kumar      | Male   | 63         | 11    | C   | Commerce | 11/5/1937  |
  | 1005  | Dipesh Pulkit    | Male   | 78         | 11    | B   | Science  | 14/09/2003 |
  | 1006  | JAHANVI Puri     | Female | 60         | 11    | B   | Commerce | 11/7/2008  |
  | 1007  | Sanam Kumar      | Male   | 23         | 12    | F   | Commerce | 3/8/1998   |
  | 1008  | SAHIL SARAS      | Male   | 56         | 11    | C   | Commerce | 11/7/2008  |
  | 1009  | AKSHRA AGARWAL   | Female | 72         | 12    | B   | Commerce | 10/1/1996  |
  | 1010  | STUTI MISHRA     | Female | 39         | 11    | F   | Science  | 11/23/2008 |
  | 1011  | HARSH AGARWAL    | Male   | 42         | 11    | C   | Science  | 3/8/1998   |
  | 1012  | NIKUNJ AGARWAL   | Male   | 49         | 12    | C   | Commerce | 28/06/1998 |
  | 1013  | AKRITI SAXENA    | Female | 89         | 12    | A   | Science  | 11/23/2008 |
  | 1014  | TANI RASTOGI     | Female | 82         | 12    | A   | Science  | 11/23/2008 |

  ___

### CREATE TABLE Query:
```sql
CREATE TABLE Student (
    StdID INT PRIMARY KEY,
    StdName VARCHAR(50) NOT NULL,
    Sex VARCHAR(10),
    Percentage INT,
    Class INT,
    Sec VARCHAR(10),
    Stream VARCHAR(20),
    DOB DATE
);
```

### INSERT Query:
```sql
INSERT INTO Student (StdID, StdName, Sex, Percentage, Class, Sec, Stream, DOB) VALUES
(1001, 'Surekha Joshi', 'Female', 82, 12, 'A', 'Science', '1998-03-08'),
(1002, 'MAAHI AGARWAL', 'Female', 56, 11, 'C', 'Commerce', '2008-11-23'),
(1003, 'Sanam Verma', 'Male', 59, 11, 'C', 'Commerce', '2006-06-29'),
(1004, 'Ronit Kumar', 'Male', 63, 11, 'C', 'Commerce', '1937-11-05'),
(1005, 'Dipesh Pulkit', 'Male', 78, 11, 'B', 'Science', '2003-09-14'),
(1006, 'JAHANVI Puri', 'Female', 60, 11, 'B', 'Commerce', '2008-11-07'),
(1007, 'Sanam Kumar', 'Male', 23, 12, 'F', 'Commerce', '1998-03-08'),
(1008, 'SAHIL SARAS', 'Male', 56, 11, 'C', 'Commerce', '2008-11-07'),
(1009, 'AKSHRA AGARWAL', 'Female', 72, 12, 'B', 'Commerce', '1996-10-01'),
(1010, 'STUTI MISHRA', 'Female', 39, 11, 'F', 'Science', '2008-11-23'),
(1011, 'HARSH AGARWAL', 'Male', 42, 11, 'C', 'Science', '1998-03-08'),
(1012, 'NIKUNJ AGARWAL', 'Male', 49, 12, 'C', 'Commerce', '1998-06-28'),
(1013, 'AKRITI SAXENA', 'Female', 89, 12, 'A', 'Science', '2008-11-23'),
(1014, 'TANI RASTOGI', 'Female', 82, 12, 'A', 'Science', '2008-11-23');
```

  ___

### Question 1: To display all the records form STUDENT table. SELECT * FROM student ;

**Query:-**
```sql
Select *  from Student ;
```

  | StdID | StdName          | Sex    | Percentage | Class | Sec | Stream   | DOB        |
  |-------|------------------|--------|------------|-------|-----|----------|------------|
  | 1001  | Surekha Joshi    | Female | 82         | 12    | A   | Science  | 3/8/1998   |
  | 1002  | MAAHI AGARWAL    | Female | 56         | 11    | C   | Commerce | 11/23/2008 |
  | 1003  | Sanam Verma      | Male   | 59         | 11    | C   | Commerce | 6/29/2006  |
  | 1004  | Ronit Kumar      | Male   | 63         | 11    | C   | Commerce | 11/5/1937  |
  | 1005  | Dipesh Pulkit    | Male   | 78         | 11    | B   | Science  | 14/09/2003 |
  | 1006  | JAHANVI Puri     | Female | 60         | 11    | B   | Commerce | 11/7/2008  |
  | 1007  | Sanam Kumar      | Male   | 23         | 12    | F   | Commerce | 3/8/1998   |
  | 1008  | SAHIL SARAS      | Male   | 56         | 11    | C   | Commerce | 11/7/2008  |
  | 1009  | AKSHRA AGARWAL   | Female | 72         | 12    | B   | Commerce | 10/1/1996  |
  | 1010  | STUTI MISHRA     | Female | 39         | 11    | F   | Science  | 11/23/2008 |
  | 1011  | HARSH AGARWAL    | Male   | 42         | 11    | C   | Science  | 3/8/1998   |
  | 1012  | NIKUNJ AGARWAL   | Male   | 49         | 12    | C   | Commerce | 28/06/1998 |
  | 1013  | AKRITI SAXENA    | Female | 89         | 12    | A   | Science  | 11/23/2008 |
  | 1014  | TANI RASTOGI     | Female | 82         | 12    | A   | Science  | 11/23/2008 |

  ___
### Question 2: To display any name and date of birth from the table STUDENT. SELECT StdName, DOB, FROM student ;

**Query:-**
```sql
Select StdName, DOB from student ;
```

  | StdName          | DOB        |
  |------------------|------------|
  | Surekha Joshi    | 3/8/1998   |
  | MAAHI AGARWAL    | 11/23/2008 |
  | Sanam Verma      | 6/29/2006  |
  | Ronit Kumar      | 11/5/1937  |
  | Dipesh Pulkit    | 14/09/2003 |
  | JAHANVI Puri     | 11/7/2008  |
  | Sanam Kumar      | 3/8/1998   |
  | SAHIL SARAS      | 11/7/2008  |
  | AKSHRA AGARWAL   | 10/1/1996  |
  | STUTI MISHRA     | 11/23/2008 |
  | HARSH AGARWAL    | 3/8/1998   |
  | NIKUNJ AGARWAL   | 28/06/1998 |
  | AKRITI SAXENA    | 11/23/2008 |
  | TANI RASTOGI     | 11/23/2008 |

  ___
### Question 3: To display all students record where percentage is greater of equal to 80 FROM student table. SELECT * FROM student WHERE percentage >= 80;

**Query:-**
```sql
Select *  From Student where percentage >=80;
```

  | StdID | StdName        | Sex    | Percentage | Class | Sec | Stream  | DOB        |
  |-------|----------------|--------|------------|-------|-----|---------|------------|
  | 1001  | Surekha Joshi  | Female | 82         | 12    | A   | Science | 3/8/1998   |
  | 1013  | AKRITI SAXENA  | Female | 89         | 12    | A   | Science | 11/23/2008 |
  | 1014  | TANI RASTOGI   | Female | 82         | 12    | A   | Science | 11/23/2008 |
  ___
### Question 4: To display student name, stream and percentage where percentage of student is more than 80 SELECT StdName, Stream, Percentage FROM student WHERE percentage > 80;

**Query:-**
```sql
Select StdName, Stream, Percentage from Student where percentage > 80;
```

  | StdName        | Stream  | Percentage |
  |----------------|---------|------------|
  | Surekha Joshi  | Science | 82         |
  | AKRITI SAXENA  | Science | 89         |
  | TANI RASTOGI   | Science | 82         |
  ___
### Question 5: To display all records of science students whose percentage is more than 75 form student table. SELECT * FROM student WHERE stream = 'Science' AND percentage > 75;

**Query:-**
```sql
Select * From Student where Stream = 'Science' AND Percentage > 75;
```

  | StdID | StdName        | Sex    | Percentage | Class | Sec | Stream  | DOB        |
  |-------|----------------|--------|------------|-------|-----|---------|------------|
  | 1001  | Surekha Joshi  | Female | 82         | 12    | A   | Science | 3/8/1998   |
  | 1005  | Dipesh Pulkit  | Male   | 78         | 11    | B   | Science | 14/09/2003 |
  | 1013  | AKRITI SAXENA  | Female | 89         | 12    | A   | Science | 11/23/2008 |
  | 1014  | TANI RASTOGI   | Female | 82         | 12    | A   | Science | 11/23/2008 |
---