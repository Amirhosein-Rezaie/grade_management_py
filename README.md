# 🎓 Grade Management

<p align="center">
  A simple Student Grade Management System built with <b>Python</b> and <b>SQLite</b>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/Interface-Terminal-black">
</p>

---

## ✨ Features

| 👨‍🎓 Students | 📚 Subjects | 📝 Grades |    📊 Analysis   |
| :------------: | :---------: | :-------: | :--------------: |
|       Add      |     Add     |    Add    |  Student Average |
|     Delete     |    Delete   |    Edit   |  Subject Average |
|      Edit      |    Delete   |   Delete  | Highest / Lowest |
|     Search     |     Edit    |    View   |                  |

---

## 🗄️ Database

The project uses **SQLite** with three main tables:

```text
students ──────< grades >────── subjects
```

* `students` — Student information
* `subjects` — Subject information
* `grades` — Grades and relationships

---

## 🧩 Structure

```text
Analysis_Grades/
├── database/
├── students/
├── subjects/
├── grades/
├── tools/
├── main.py
└── database.sqlite3
```

---

## 🛠️ Technologies

* 🐍 Python
* 🗄️ SQLite
* 💻 Terminal

No external Python packages are required.

---

## 🚀 Run

```bash
git clone <repository-url>
cd Analysis_Grades
python main.py
```

---

## 🎯 Purpose

A practical project for reviewing **Python, OOP, SQL, SQLite, CRUD operations, modules, and project structure**, while taking a first step toward **Data Science and Machine Learning**.

---

<p align="center">
  Made with 🐍 Python + 🗄️ SQLite
</p>
