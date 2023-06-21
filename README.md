README File:

# Practice Exam with MySQL Database

To help me with my studies and continue to practice programming with Python, I created this project to facilitate a PMP (Project Management Professional) practice exam by presenting a series of questions and evaluating the user's answers. The questions are fetched from a MySQL database, and the user interacts with the program through the console.

## Prerequisites

Before running this code, ensure that you have the following dependencies installed:

- Python 3.x
- mysql-connector-python library

You can install the mysql-connector-python library using the following command:

```
pip install mysql-connector-python
```

## Setup

To set up the project and prepare it for running, follow these steps:

1. Clone or download the project files to your local machine.
2. Create a MySQL database and table to store the PMP questions. The table should contain columns for question ID, question text, choices, correct answer, and explanation.
3. Open the `main.py` file and locate the `fetch_questions_from_database` function.
4. Within the function, update the database connection details (host, port, user, password, database) to match your MySQL configuration.
5. Save the changes to the `main.py` file.

## Usage

To start the PMP exam, execute the `main.py` script by running the following command:

```
python main.py
```

The program will connect to the MySQL database, fetch the PMP questions, and present them one by one to the user. The user can provide their answer by entering A, B, C, or D. After each answer, the program provides feedback and explanation. Press Enter to proceed to the next question.

Once all questions are answered, the program displays the exam completion message along with the user's score.

## Customization

You can customize the PMP questions by modifying the data stored in the MySQL database table. Update the question text, choices, correct answer, and explanation according to your requirements.

## Contribution

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please submit them through the issue tracker or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

**Note:** Make sure to replace "x.x.x.x" with the actual host IP address and "sample" with the appropriate database credentials in the code before running it.
