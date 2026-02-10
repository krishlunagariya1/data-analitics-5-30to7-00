# Students Based Database - SQL Homework 1

## 1. Create a Database Named "school"

```sql
CREATE DATABASE school;
USE school;
```

---

## 2. Create Table "country"

```sql
CREATE TABLE country (
    country_id INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(100) NOT NULL
);
```

---

## 3. Create Table "students"

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    grade INT NOT NULL,
    country_id INT NOT NULL,
    FOREIGN KEY (country_id) REFERENCES country(country_id)
);
```

---

## 4. Insert Records into "country" Table

```sql
INSERT INTO country (country_name) VALUES 
('United States'),
('Canada'),
('United Kingdom'),
('Australia'),
('Germany');
```

---

## 5. Insert Records into "students" Table

```sql
INSERT INTO students (name, age, grade, country_id) VALUES 
('John Smith', 20, 85, 1),
('Emma Johnson', 19, 90, 2),
('Michael Brown', 21, 78, 1),
('Sophia Lee', 20, 92, 3),
('David Wilson', 22, 88, 4),
('Olivia Davis', 19, 95, 5),
('James Martinez', 21, 80, 1);
```

---

## 6. Select All Students Along with Their Country Names

```sql
SELECT 
    s.id,
    s.name,
    s.age,
    s.grade,
    c.country_name
FROM students s
INNER JOIN country c ON s.country_id = c.country_id
ORDER BY s.id;
```

**Result:**
| id | name | age | grade | country_name |
|----|------|-----|-------|--------------|
| 1 | John Smith | 20 | 85 | United States |
| 2 | Emma Johnson | 19 | 90 | Canada |
| 3 | Michael Brown | 21 | 78 | United States |
| 4 | Sophia Lee | 20 | 92 | United Kingdom |
| 5 | David Wilson | 22 | 88 | Australia |
| 6 | Olivia Davis | 19 | 95 | Germany |
| 7 | James Martinez | 21 | 80 | United States |

---

## 7. Find the Average Age of Students in Each Grade

```sql
SELECT 
    grade,
    AVG(age) AS average_age,
    COUNT(*) AS student_count
FROM students
GROUP BY grade
ORDER BY grade;
```

**Result:**
| grade | average_age | student_count |
|-------|-------------|---------------|
| 78 | 21.00 | 1 |
| 80 | 21.00 | 1 |
| 85 | 20.00 | 1 |
| 88 | 22.00 | 1 |
| 90 | 19.00 | 1 |
| 92 | 20.00 | 1 |
| 95 | 19.00 | 1 |

---

## 8. Find the Total Number of Students in Each Country

```sql
SELECT 
    c.country_name,
    COUNT(s.id) AS total_students
FROM country c
LEFT JOIN students s ON c.country_id = s.country_id
GROUP BY c.country_id, c.country_name
ORDER BY total_students DESC;
```

**Result:**
| country_name | total_students |
|----|---------|
| United States | 3 |
| Canada | 1 |
| United Kingdom | 1 |
| Australia | 1 |
| Germany | 1 |

---

## 9. Find the Student with the Highest Grade

```sql
SELECT 
    id,
    name,
    age,
    grade,
    country_id
FROM students
WHERE grade = (SELECT MAX(grade) FROM students);
```

**Alternative using ORDER BY:**

```sql
SELECT 
    id,
    name,
    age,
    grade,
    country_id
FROM students
ORDER BY grade DESC
LIMIT 1;
```

**Result:**
| id | name | age | grade | country_id |
|----|------|-----|-------|-----------|
| 6 | Olivia Davis | 19 | 95 | 5 |

---

## 10. Update the Grade of a Student with a Specific ID

```sql
-- Example: Update the grade of student with ID 3 to 92
UPDATE students
SET grade = 92
WHERE id = 3;
```

**Verification:**
```sql
SELECT id, name, grade FROM students WHERE id = 3;
```

---

## 11. Delete a Student with a Specific ID

```sql
-- Example: Delete student with ID 7
DELETE FROM students
WHERE id = 7;
```

**Verification:**
```sql
-- Verify deletion
SELECT COUNT(*) AS total_students FROM students;
```

---

## Complete Setup Script (All-in-One)

```sql
-- Create database
CREATE DATABASE school;
USE school;

-- Create country table
CREATE TABLE country (
    country_id INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(100) NOT NULL
);

-- Create students table
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    grade INT NOT NULL,
    country_id INT NOT NULL,
    FOREIGN KEY (country_id) REFERENCES country(country_id)
);

-- Insert countries
INSERT INTO country (country_name) VALUES 
('United States'),
('Canada'),
('United Kingdom'),
('Australia'),
('Germany');

-- Insert students
INSERT INTO students (name, age, grade, country_id) VALUES 
('John Smith', 20, 85, 1),
('Emma Johnson', 19, 90, 2),
('Michael Brown', 21, 78, 1),
('Sophia Lee', 20, 92, 3),
('David Wilson', 22, 88, 4),
('Olivia Davis', 19, 95, 5),
('James Martinez', 21, 80, 1);
```
