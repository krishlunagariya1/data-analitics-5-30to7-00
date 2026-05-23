# Working with Database using SQL – Assignment Solutions

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

| Field Name | Data Type |
|------------|------------|
| ContactID | INT |
| CompanyID | INT |
| FirstName | VARCHAR(45) |
| LastName | VARCHAR(45) |
| Street | VARCHAR(45) |
| City | VARCHAR(45) |
| State | VARCHAR(2) |
| Zip | VARCHAR(10) |
| IsMain | BOOLEAN |
| Email | VARCHAR(45) |
| Phone | VARCHAR(12) |

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

| Field Name | Data Type |
|------------|------------|
| EmployeeID | INT |
| FirstName | VARCHAR(45) |
| LastName | VARCHAR(45) |
| Salary | DECIMAL(10,2) |
| HireDate | DATE |
| JobTitle | VARCHAR(25) |
| Email | VARCHAR(45) |
| Phone | VARCHAR(12) |

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

| Field Name | Data Type |
|------------|------------|
| ContactEmployeeID | INT |
| ContactID | INT |
| EmployeeID | INT |
| ContactDate | DATE |
| Description | VARCHAR(100) |

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

# 9) Explain Normalization in Databases

Normalization is the process of organizing data in a database to:

- Reduce data redundancy
- Avoid duplicate data
- Improve data integrity
- Increase efficiency

## Types of Normal Forms

| Normal Form | Purpose |
|-------------|----------|
| 1NF | Remove repeating groups |
| 2NF | Remove partial dependency |
| 3NF | Remove transitive dependency |

---

# 10) What Does JOIN Mean in MySQL?

A `JOIN` combines rows from two or more tables using related columns.

## Example Query

```sql
SELECT Employee.FirstName, Company.CompanyName
FROM Employee
JOIN Company
ON Employee.EmployeeID = Company.CompanyID;
```

## Example Output

| FirstName | CompanyName |
|------------|--------------|
| Jack | Toll Brothers |
| Lesley | Urban Outfitters |

---

# 11) Explain DDL, DCL, and DML in MySQL

| Type | Full Form | Purpose | Examples |
|------|------------|----------|----------|
| DDL | Data Definition Language | Defines database structure | CREATE, ALTER, DROP |
| DML | Data Manipulation Language | Manipulates data | INSERT, UPDATE, DELETE |
| DCL | Data Control Language | Controls permissions | GRANT, REVOKE |

---

# 12) Role of JOIN Clause and Common Types of JOINs

The `JOIN` clause retrieves related data from multiple tables.

## Types of JOINs

| JOIN Type | Description |
|------------|-------------|
| INNER JOIN | Returns matching rows from both tables |
| LEFT JOIN | Returns all rows from left table |
| RIGHT JOIN | Returns all rows from right table |
| FULL JOIN | Returns all matching and non-matching rows |

---

## INNER JOIN Example

```sql
SELECT Employee.FirstName, Contact.ContactID
FROM Employee

INNER JOIN ContactEmployee
ON Employee.EmployeeID = ContactEmployee.EmployeeID

INNER JOIN Contact
ON ContactEmployee.ContactID = Contact.ContactID;
```

## Example Output

| FirstName | ContactID |
|------------|------------|
| Jack | 1 |
| Lesley | 2 |

---