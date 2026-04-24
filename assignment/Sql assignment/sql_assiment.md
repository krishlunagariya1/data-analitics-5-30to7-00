Question -1 : Statement to create the Contact table
**Answer:**
create table tbl_contact
(
    contactID int primary key,
    companyID int,
    FirstName varchar(45),
    LastName Varchar(45),
    street varchar(45),
    city varchar(45),
    state Varchar(2),
    zip varchar(10),
    Ismain boolean,
    Email varchar(45),
    phone varchar(12),
    companyID int REFERENCES company(companyID)
)

Question 2 : Statement to create the Employee table
**Answer:**
create table tbl_employee
(
    EmployeeID int primary key auto_increament,
    FirstName varchar(45),
    LastName Varchar(45),
    Salary Decimal(10,2),
    HireDate Date,
    JobTitle varchar(25),
    Email varchar(45),
    phone varchar(12)
)

Question 3 : Statement to create the ContactEmployee table
**Answer:**
create table tbl_contact_employee
(
    Contact_Employee_ID int primary key,
    contactID int,
    employeeID int,
    ContactDate Date,
    Description varchar(100),
    contactID int REFERENCES tbl_contact(contactID),
    EmployeeID int REFERENCES tbl_employee(EmployeeID)
)

```
create table tbl_comapny
(
    companyID int primary key auto_increment,
    CompanyName varchar(45),
    Street varchar(45),
    City varchar(45),
    State varchar(2),
    Zip varchar(10)
)
```


**ADD 10 Records in tbl_employee.**
```
Insert Into tbl_employee (FirstName, LastName, Salary, Hire_Date, JobTitle, Email, Phone) 
    Values  ('Brij', 'Shekhda', 50000, '2014-01-01', 'Sr.Manager', 'b@gmail.com', 2147483647), 
            ('Krish', 'Patel', 55000, '2014-02-01', 'Manager', 'k@gmail.com', 2147483647), 
            ('Het', 'Kakdiya', 60000, '2014-03-01', 'Sr.Manager-IT', 'h@gmail.com', 2147483647), ('Rahul', 'Sharma', 65000, '2014-04-01', 'Manager-CSE', 'r@gmail.com', 2147483647),
            ('Priya', 'Patel', 70000, '2014-05-01', 'Associate_Manager-IT', 'p@gmail.com', 2147483647), ('Lesley', 'Bland', 75000, '2014-06-01', 'Sr.Manager-Marketing', 'l@gmail.com', 2147483647), ('Sneha', 'Reddy', 80000, '2014-07-01', 'Manager-mMarketing', 's@gmail.com', 2147483647), ('Vikram', 'Singh', 85000, '2014-08-01', 'Ass.Manager-Marketing', 'v@gmail.com', 2147483647), ('Anjali', 'Mehta', 90000, '2014-09-01', 'Sr.Manager-DataSci.', 'a@gmail.com', 2147483647), ('Rohan', 'Desai', 95000, '2014-10-01', 'Manager-DataSci.', 'd@gmail.com', 2147483647)                        
```

Question - 4 : In the Employee table, the statement that changes Lesley Bland’s phone number to  
               215-555-8800.
**Answer:**
Update tbl_employee set Phone = '215-555-8800' where employeeID=6;
OR
update tble_employee set phone ='215-555-8800' where first_name = 'lesley' and last_name = 'bland';


Question - 5 : In the Company table, the statement that changes the name of “Urban
               Outfitters, Inc.” to “Urban Outfitters” 
**Answer:**
update tbl_company set companyName = 'Urban Outfitters' where companyName = 'UrbanOutfitters,Inc'.;


Question - 6 :  In ContactEmployee table, the statement that removes Dianne Connor’s contact
                event with Jack Lee (one statement).
HINT: Use the primary key of the ContactEmployee table to specify the correct record to remove.
**Answer:**
    


Question - 7 : Write the SQL SELECT query that displays the names of the employees that
               have contacted Toll Brothers (one statement). Run the SQL SELECT query in
               MySQL Workbench. Copy the results below as well. 
**Answer:**



Question - 8 : What is the significance of “%” and “_” operators in the LIKE statement?
**Answer:**


Question - 9 : Explain normalization in the context of databases.
**Answer:**

Question - 10 : What does a join in MySQL mean?
**Answer:**
### What Does a JOIN in MySQL Mean?

A **JOIN** lets you retrieve data from multiple tables in a single query by specifying how the rows relate.

- Tables are usually linked by a **foreign key** that matches a **primary key** in another table.
- When you perform a JOIN, MySQL “matches up” rows from the tables according to the join condition.
- The most common join types are:
  - **INNER JOIN** – returns only rows with matching values in both tables.
  - **LEFT (OUTER) JOIN** – returns all rows from the left table and matched rows from the right.
  - **RIGHT (OUTER) JOIN** – returns all rows from the right table and matched rows from the left.
  - **FULL JOIN** (simulated in MySQL) – returns rows when there is a match in one of the tables.
- Joins can also be chained to combine more than two tables at once.
- They are essential for normalized databases where related data is stored separately.
- The basic syntax includes `SELECT … FROM table1 JOIN table2 ON table1.col = table2.col;`
- Properly written joins allow you to answer complex questions without denormalizing data.
- Performance can vary depending on indexes and the size of the tables.
- In summary, a JOIN merges rows from related tables so you can work with combined information.

Question - 11 : What do you understand about DDL, DCL, and DML in MySQL?
**Answer:**

Question - 12 : What is the role of the MySQL JOIN clause in a query, and what are some
                common types of joins?
**Answer:**