# 📝 Exam 04 – SQL (PostgreSQL) & SQLAlchemy

---

## 📌 Mini Project 1 – PostgreSQL: **Student Management System**

*(10 ta task)*

---

### 1. Jadval yaratish

**Task:** `students(id, name, age, group)` va `grades(id, student_id, subject, grade)` jadvallarini yarating.

---

### 2. Ma’lumot qo‘shish

**Task:** 5 ta talaba va ularga kamida 2 tadan baho yozing.

---

### 3. Oddiy SELECT

**Task:** Faqat `students` jadvalidan barcha talabalarning ismi va guruhini chiqarish.

**Output:**

```
Ali  | Group A
Laylo| Group B
...
```

---

### 4. JOIN

**Task:** Talabalarni fan va baholari bilan birgalikda chiqarish.

---

### 5. Filter

**Task:** `age > 20` bo‘lgan talabalarni chiqarish.

---

### 6. Aggregation

**Task:** Har bir talabaning o‘rtacha bahosini hisoblang.

**Output:**

```
Ali   | 85
Laylo | 92
```

---

### 7. GROUP BY

**Task:** Har bir guruh bo‘yicha talaba sonini hisoblang.

---

### 8. MAX

**Task:** Eng yuqori baho olgan talabani chiqaring.

---

### 9. LIKE

**Task:** Ismi `A` harfi bilan boshlanadigan talabalarni chiqarish.

---

### 10. DELETE

**Task:** “Group C” dagi barcha talabalarni o‘chirib tashlang.

---

---

## 📌 Mini Project 2 – SQLAlchemy: **Task Manager App**

*(10 ta task)*

---

### 1. Model yaratish

**Task:** `User(id, name, email)` va `Task(id, title, status, user_id)` modellari yarating.

---

### 2. Session orqali qo‘shish

**Task:** 3 ta user va har biriga kamida 2 tadan task qo‘shing.

---

### 3. Query all

**Task:** Barcha tasklarni `title` va `status` bilan chiqarish.

---

### 4. Relationship

**Task:** Har bir userning tasklarini chiqarish.

**Output:**

```
Ali → ['Fix bug', 'Write docs']
Laylo → ['Design UI', 'Deploy app']
```

---

### 5. Filter

**Task:** `status='done'` bo‘lgan tasklarni chiqarish.

---

### 6. Update

**Task:** `"Write docs"` taskining statusini `"done"` ga o‘zgartirish.

---

### 7. Delete

**Task:** `"Deploy app"` taskini o‘chirib tashlash.

---

### 8. Order By

**Task:** Tasklarni `title ASC` bo‘yicha chiqarish.

---

### 9. COUNT

**Task:** Har bir user nechta taskga ega ekanligini hisoblang.

**Output:**

```
Ali   | 2
Laylo | 2
Hasan | 1
```
