# Student Manager CLI

A lightweight command-line student manager in Python. Stores student name and score in a simple CSV file (`students.txt`) and computes grade (A/B/C/F) based on score.

## Features

- Add new student
- List all students
- Update student score with validation (0-100)
- Save students to file (`students.txt`)
- Load students from file
- Grade calculation logic:
    - 90+ => A
    - 75+ => B
    - 60+ => C
    - <60 => F

## Project Structure

- `student.py`
    - `Student` class
    - `get_grade()`
    - `introduce()`
    - `set_score()`
    - `to_csv_line()`
    - `__str__()`

- `manager.py`
    - `add_student(students, name, score)`
    - `find_student(students, name)`
    - `save_students(students, filename)`
    - `load_students(filename)`

- `main.py`
    - Interactive CLI menu
    - Uses `student` and `manager` modules

- `students.txt`
    - Persisted data in CSV format: `name,score`

## Quick Start

1. Install Python 3.8 or newer (recommended)
2. Run:
    ```bash
    python main.py
    ```
3. Follow menu steps:
    - `1` Add student
    - `2` Show all students
    - `3` Change student score
    - `4` Save current students to file
    - `5` Load students from file
    - `6` Exit

## Example Workflow

- Start program
- Add two students
- Save to `students.txt`
- Exit
- Run again
- Load students from file
- List students

## Implementation Notes

- `Student.set_score()` raises `ValueError` for invalid values (non-number or out of 0-100 range).
- `manager.load_students()` safely ignores malformed lines and non-numeric scores.

## Future improvements

- Add delete student functionality
- Add JSON persistence option
- Add search/filter support
- Add test coverage (e.g., `pytest`)
