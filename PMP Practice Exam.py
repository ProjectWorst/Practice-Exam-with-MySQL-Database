#PMP Exam questions

import random
import mysql.connector

class PMPQuestion:
    def __init__(self, question_number, question, choices, correct_answer, explanation):
        self.question_number = question_number
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer
        self.explanation = explanation

    def display_question(self):
        print(f"Question #{self.question_number}:")
        print(f"{self.question}\n")
        for i, choice in enumerate(self.choices, start=65):
            print(f"{chr(i)}.  {choice}")
        print()

    def check_answer(self, user_answer):
        is_correct = user_answer == self.correct_answer
        if is_correct:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", chr(ord("A") + self.correct_answer - 1) + ". " + self.choices[self.correct_answer - 1])
        print(self.explanation)
        print()
        return is_correct

def fetch_questions_from_database():
    # Connect to your MySQL database
    db = mysql.connector.connect(
        host= "sample",
        port= "sample",
        user= "sample",
        password= "sample",
        database= "sample"
     )
    
    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Fetch questions from the database
    query = "SELECT id, question_text, choice1, choice2, choice3, choice4, correct_answer, explanation FROM question ORDER BY id"
    cursor.execute(query)
    question_rows = cursor.fetchall()

    # Create a list of PMPQuestion objects based on the fetched rows
    question_pool = []
    for row in question_rows:
        question = PMPQuestion(row[0], row[1], row[2:6], row[6], row[7])
        question_pool.append(question)

    # Close the database connection
    cursor.close()
    db.close()

    return question_pool


def main():
    question_pool = fetch_questions_from_database()

    num_questions = len(question_pool) # Total number of questions available in the database

    score = 0

    question_number = 1  # Start at Question 1

    while question_number <= num_questions:
        question = question_pool[question_number - 1]  # Adjust index to start at 0

        while True:  # Keep asking for input until a valid answer is provided
            question.display_question()
            user_answer = input("Enter your answer: ").upper()
            if user_answer in ["A", "B", "C", "D"]:
                if question.check_answer(ord(user_answer) - ord("A") + 1):
                    score += 1
                break  # Break out of the loop to move to the next question
            else:
                print("Invalid answer. Please enter A, B, C, or D.")
                print()

        # Prompt to press Enter key to continue
        input("Press Enter to continue.")

        question_number += 1

    print("------------------------")
    print("Quiz complete!")
    print("Your score:", score, "/", num_questions)

if __name__ == "__main__":
    main()
