MySQL and SQL Basics Project

Project Overview

This project is designed to introduce you to the fundamental concepts of databases, SQL, and MySQL. By completing a series of hands-on tasks and exercises, you will gain practical experience in creating, querying, and manipulating relational databases.

Resources

The following materials provide the foundation for your learning. You should read or watch these before beginning the exercises:

What is Database & SQL?

Install MySQL (MySQL Server)

A Basic MySQL Tutorial

Basic SQL Statements: DDL and DML

Basic Queries: SQL and Relational Algebra (RA)

SQL Technique: Functions

SQL Technique: Subqueries

What Makes the Big Difference Between a Backtick and an Apostrophe?

MySQL Cheat Sheet

MySQL 8.0 SQL Statement Syntax

Note: If any of the above resources are temporarily unavailable, refer to the consolidated documentation provided here.

Learning Objectives

By the end of this project, you will be able to explain and demonstrate:

Databases & RDBMS

What a database is

What a relational database is

What SQL stands for

What MySQL is

Database Creation & Management

How to install and start MySQL Server (Ubuntu 20.04 & 22.04)

How to create a new database in MySQL

SQL Data Definition Language (DDL)

What DDL stands for

How to CREATE and ALTER tables

SQL Data Manipulation Language (DML)

What DML stands for

How to SELECT data from a table

How to INSERT, UPDATE, and DELETE records

Advanced SQL Techniques

How to write and understand subqueries

How to use built‑in MySQL functions

Project Requirements

Environment: Ubuntu 20.04 LTS with MySQL 8.0.25 (or later) installed.

Credentials: In the sandbox, use root/root on 20.04 or default socket login on 22.04.

Editors: vi, vim, or emacs only.

File Conventions:

All SQL files must end with a single newline.

All files must start with a comment describing the task.

-- Task: Describe what this query does

Use uppercase for all SQL keywords (e.g., SELECT, WHERE).

Add a brief comment above each query explaining its purpose.

Testing: Your files will be evaluated with wc to ensure they meet length and formatting criteria.

File Structure

project-folder/
├── README.md
├── 0-list_databases.sql
├── 1-create_database.sql
├── 2-alter_table.sql
├── 3-data_manipulation.sql
├── 4-subqueries.sql
└── 5-functions.sql

Each .sql file corresponds to one or more learning objectives. Rename or add files as needed, but follow the naming pattern <index>-<description>.sql.

Usage

Start MySQL Server (if not already running):

sudo service mysql start

Run SQL Scripts:

cat 0-list_databases.sql | mysql -uroot -p

Replace root -p with appropriate credentials if prompted.

Submission

Ensure all SQL files have descriptive comments and pass the style checks.

Push your changes to the repository and verify file sizes with wc -l and wc -m.

Additional Tips

Experiment with sample data to deepen your understanding.

Refer back to the MySQL Cheat Sheet for quick syntax reminders.

When in doubt, read the official MySQL 8.0 documentation on syntax and functions.

Happy querying, and enjoy mastering SQL with MySQL!

