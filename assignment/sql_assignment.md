# SQL Assignment 

# For this assignment, you will finish building the contact management database for MarketCo

---

# 1) Statement to Create the `Contact` Table

```sql
CREATE TABLE Contact (
    ContactID INT PRIMARY KEY,
    CompanyID INT,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    Street VARCHAR(45),
    City VARCHAR(45),
    State VARCHAR(2),
    Zip VARCHAR(10),
    IsMain BOOLEAN,
    Email VARCHAR(45),
    Phone VARCHAR(12),

    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);
```

## Output Structure

| ContactID | CompanyID | FirstName | LastName | Street | City | State | Zip | IsMain | Email | Phone |
|-----------|-----------|-----------|----------|--------|------|-------|-----|--------|--------|-------|

---

# 2) Statement to Create the `Employee` Table

```sql
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    Salary DECIMAL(10,2),
    HireDate DATE,
    JobTitle VARCHAR(25),
    Email VARCHAR(45),
    Phone VARCHAR(12)
);
```

## Output Structure

| EmployeeID | CompanyID | FirstName | LastName | Street | City | State | Zip | Email | Phone |
|------------|-----------|-----------|----------|--------|------|-------|-----|--------|-------|

---

# 3) Statement to Create the `ContactEmployee` Table

```sql
CREATE TABLE ContactEmployee (
    ContactEmployeeID INT PRIMARY KEY,
    ContactID INT,
    EmployeeID INT,
    ContactDate DATE,
    Description VARCHAR(100),

    FOREIGN KEY (ContactID) REFERENCES Contact(ContactID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);
```

## Output Structure

| ContactID | EmployeeID | ContactDate |
|-----------|------------|-------------|

---

# 4) Update Lesley Bland’s Phone Number

```sql
UPDATE Employee
SET Phone = '215-555-8800'
WHERE FirstName = 'Lesley'
AND LastName = 'Bland';
```

## Example Output

| EmployeeID | FirstName | LastName | Phone |
|------------|------------|-----------|--------|
| 101 | Lesley | Bland | 215-555-8800 |

---

# 5) Change Company Name

```sql
UPDATE Company
SET CompanyName = 'Urban Outfitters'
WHERE CompanyName = 'Urban Outfitters, Inc.';
```

## Example Output

| CompanyID | Old Name | New Name |
|------------|-----------|-----------|
| 1 | Urban Outfitters, Inc. | Urban Outfitters |

---

# 6) Remove Dianne Connor’s Contact Event with Jack Lee

```sql
DELETE FROM ContactEmployee
WHERE ContactEmployeeID = 1;
```

> Replace `1` with the correct `ContactEmployeeID`.

## Example Output

| Message |
|----------|
| 1 row deleted successfully |

---

# 7) SQL SELECT Query for Employees Who Contacted Toll Brothers

```sql
SELECT Employee.FirstName, Employee.LastName
FROM Employee

JOIN ContactEmployee
ON Employee.EmployeeID = ContactEmployee.EmployeeID

JOIN Contact
ON ContactEmployee.ContactID = Contact.ContactID

JOIN Company
ON Contact.CompanyID = Company.CompanyID

WHERE Company.CompanyName = 'Toll Brothers';
```

## Output Table

| FirstName | LastName |
|------------|-----------|
| Jack | Lee |
| Dianne | Connor |

---

# 8) Significance of `%` and `_` in the `LIKE` Statement

| Symbol | Meaning | Example |
|--------|----------|----------|
| `%` | Represents zero or more characters | `'A%'` |
| `_` | Represents exactly one character | `'A_'` |

## Example Query

```sql
SELECT * FROM Employee
WHERE FirstName LIKE 'J%';
```

## Example Output

| EmployeeID | FirstName | LastName |
|------------|------------|-----------|
| 101 | Jack | Lee |
| 102 | James | Smith |

---
# SQL Assignment Solutions

## 9) Explain normalization in the context of databases

### Definition
Normalization is the process of organizing data in a database to reduce data redundancy (duplicate data) and improve data integrity.

It divides large tables into smaller related tables and connects them using keys such as Primary Key and Foreign Key.

---

## Objectives of Normalization

- Remove duplicate data
- Improve data consistency
- Reduce data anomalies
- Save storage space
- Improve database structure

---

## Types of Normal Forms

### 1. First Normal Form (1NF)
Rules:
- Each column must contain atomic (single) values
- No repeating groups

### Example
❌ Wrong Table

| StudentID | Subjects |
|---|---|
| 1 | Math, Science |

✅ Correct Table

| StudentID | Subject |
|---|---|
| 1 | Math |
| 1 | Science |

---

### 2. Second Normal Form (2NF)
Rules:
- Table must already be in 1NF
- Remove partial dependency

This means non-key columns should depend on the whole primary key.

---

### 3. Third Normal Form (3NF)
Rules:
- Table must already be in 2NF
- Remove transitive dependency

Non-key columns should depend only on the primary key.

---

## Advantages of Normalization

| Advantage | Description |
|---|---|
| Reduces redundancy | Avoids duplicate data |
| Improves consistency | Same data stored once |
| Better integrity | Accurate relationships |
| Easier maintenance | Updates become simple |

---

## Disadvantages of Normalization

| Disadvantage | Description |
|---|---|
| More tables | Database becomes complex |
| More JOIN operations | Queries may become slower |

---

# 10) What does a JOIN in MySQL mean?

## Definition

A JOIN in MySQL is used to combine rows from two or more tables based on a related column between them.

Usually, tables are connected using:
- Primary Key
- Foreign Key

---

## Why JOIN is Used

JOIN helps retrieve related data stored in different tables.

Example:
- Employee details in one table
- Department details in another table

JOIN combines both tables to display complete information.

---

## Basic Syntax

```sql
SELECT columns
FROM table1
JOIN table2
ON table1.column_name = table2.column_name;
```

---

## Example

### Employee Table

| EmployeeID | Name | DepartmentID |
|---|---|---|
| 1 | Krish | 101 |

### Department Table

| DepartmentID | DepartmentName |
|---|---|
| 101 | IT |

---

## Query

```sql
SELECT Employee.Name, Department.DepartmentName
FROM Employee
JOIN Department
ON Employee.DepartmentID = Department.DepartmentID;
```

---

## Output

| Name | DepartmentName |
|---|---|
| Krish | IT |

---

## Advantages of JOIN

- Combines related data
- Reduces duplicate storage
- Makes database more normalized
- Helps generate reports easily

---

# 11) What do you understand about DDL, DCL, and DML in MySQL?

## 1. DDL (Data Definition Language)

DDL commands are used to define and modify database structure.

### Common DDL Commands

| Command | Purpose |
|---|---|
| CREATE | Create database/table |
| ALTER | Modify table structure |
| DROP | Delete database/table |
| TRUNCATE | Remove all records |

---

## Example

```sql
CREATE TABLE Student (
    ID INT,
    Name VARCHAR(50)
);
```

---

## 2. DML (Data Manipulation Language)

DML commands are used to manage data inside tables.

### Common DML Commands

| Command | Purpose |
|---|---|
| INSERT | Add data |
| UPDATE | Modify data |
| DELETE | Remove data |
| SELECT | Retrieve data |

---

## Example

```sql
INSERT INTO Student (ID, Name)
VALUES (1, 'Krish');
```

---

## 3. DCL (Data Control Language)

DCL commands are used to control user permissions and security.

### Common DCL Commands

| Command | Purpose |
|---|---|
| GRANT | Give permissions |
| REVOKE | Remove permissions |

---

## Example

```sql
GRANT SELECT ON Student TO user1;
```

---

## Difference Between DDL, DML, and DCL

| Feature | DDL | DML | DCL |
|---|---|---|---|
| Full Form | Data Definition Language | Data Manipulation Language | Data Control Language |
| Purpose | Structure | Data Handling | Permission Control |
| Works On | Tables/Database | Records/Data | Users |

---

# 12) What is the role of the MySQL JOIN clause in a query, and what are some common types of joins?

## Role of JOIN Clause

The JOIN clause is used to combine data from multiple tables based on a related column.

It helps:
- Retrieve connected data
- Reduce duplicate information
- Improve database organization

---

# Common Types of JOINs in MySQL

---

## 1. INNER JOIN

Returns only matching rows from both tables.

### Syntax

```sql
SELECT *
FROM table1
INNER JOIN table2
ON table1.id = table2.id;
```

### Example

If records match in both tables, they are displayed.

---

## 2. LEFT JOIN (LEFT OUTER JOIN)

Returns:
- All rows from the left table
- Matching rows from the right table

If no match exists, NULL values are shown.

### Syntax

```sql
SELECT *
FROM table1
LEFT JOIN table2
ON table1.id = table2.id;
```

---

## 3. RIGHT JOIN (RIGHT OUTER JOIN)

Returns:
- All rows from the right table
- Matching rows from the left table

### Syntax

```sql
SELECT *
FROM table1
RIGHT JOIN table2
ON table1.id = table2.id;
```

---

## 4. FULL JOIN

Returns all matching and non-matching rows from both tables.

> Note:
MySQL does not directly support FULL JOIN.
It can be achieved using UNION.

---

## 5. CROSS JOIN

Returns the Cartesian product of both tables.

Every row from the first table combines with every row from the second table.

### Syntax

```sql
SELECT *
FROM table1
CROSS JOIN table2;
```

---

# JOIN Comparison Table

| JOIN Type | Returns |
|---|---|
| INNER JOIN | Matching rows only |
| LEFT JOIN | All left + matching right |
| RIGHT JOIN | All right + matching left |
| FULL JOIN | All rows from both tables |
| CROSS JOIN | All possible combinations |

---
