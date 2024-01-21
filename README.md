# Student-Database-Management-System
This is a Student Database Management System I have created way back in grade 12. This was the final project of my high school. Sure was fun, applied quite a bit of the concepts I had learnt. We connect MySQL to Python and keep interacting back and forth between the two. All the data is stored on MySQL and is handled via Python.

---

## Database Connection Setup

To run this project on your local machine, you'll need to set up the database connection. Follow these steps:

### 1. Install MySQL

Make sure you have MySQL installed on your machine. You can download MySQL from the [official website](https://dev.mysql.com/downloads/).

### 2. Configure MySQL Server

Follow the installation instructions to set up and configure MySQL Server on your machine. During the installation, make note of the MySQL username, password, and the port number.

### 3. Set Up a Database

Create a new database for this project. You can use a MySQL client (such as MySQL Workbench or phpMyAdmin) or run SQL commands from the command line:

CREATE DATABASE <name>;

### 4. Update Database Configuration

In the project code, locate the database configuration details in the beginning. Update the following parameters with your MySQL connection details:

DATABASE_CONFIG = {

    'host': 'localhost',
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'database': 'project_database',
    'port': 3306,  # Change if your MySQL server is running on a different port
    
}

### 6. Run the Project

You should now be able to run the project on any IDE.

---
