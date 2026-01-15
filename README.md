# Task Management Application (Media Meter Technical Exam)

A simple command-line task manager application built in Python, allowing users to add, view, update, delete, and filter tasks.

## Features
- Add a new task with title, description, due date, priority, and status
- List all tasks, with optional filtering by status, priority, or due date.
- Update a task’s details, including status (`Pending`, `In Progress`, `Completed`).
- Mark a task as completed.
- Delete tasks.
- Tasks are stored in a MySQL database.

## Setup Instructions

### 1. Set up a Python virtual environment

```bash
# Create a virtual environment named "venvname"
python -m venv venvname

# Activate the virtual environment
# Windows
venvname\Scripts\activate

# macOS / Linux
source venvname/bin/activate

### Install Dependencies
pip install -r requirements.txt

### Create a Database
CREATE DATABASE IF NOT EXISTS task_manager;
USE task_manager;

CREATE TABLE IF NOT EXISTS tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    due_date DATE NOT NULL,
    priority ENUM('Low', 'Medium', 'High') NOT NULL,
    status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);