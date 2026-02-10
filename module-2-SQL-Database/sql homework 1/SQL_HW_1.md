# Students Based Database - SQL Homework 1

## 1. Create a Database Named "school"

```sql
CREATE DATABASE school;
```

---

## 2. Create Table "country"

```sql
CREATE TABLE country (
    country_id INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(100) 
);
```

---

## 3. Create Table "students"

```sql
CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    grade INT,
    country_id INT,
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

