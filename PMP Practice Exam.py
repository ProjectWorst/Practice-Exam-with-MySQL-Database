#Pratice Exam questions with MySQL Database

# The random module is used for generating random numbers or making random choices.
# For this program, the purpose would be to jump randomly to different questions and also randomize the order of answer choices if desired.  
import random
# The mysql.connector module is used for connecting to a MySQL database and executing SQL queries.
import mysql.connector

# Define a class called 'PMPQuestion' to represent a single PMP (Project Management Professional) question.
class PMPQuestion:
    
    # Use an '__init__' method that initializes the question object with several attributes: 'question_number', 'question', 'choices', 'correct_answer', and 'explanation'.
    def __init__(self, question_number, question, choices, correct_answer, explanation):
        self.question_number = question_number
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer
        self.explanation = explanation

    # The 'display_question' method prints the question number, question, and choices to the console.
    def display_question(self):
        print(f"Question #{self.question_number}:")
        print(f"{self.question}\n")
        for i, choice in enumerate(self.choices, start=65):
            print(f"{chr(i)}.  {choice}")
        print()

    # The 'check_answer' method compares the user's answer with the correct answer, provides the explanation, and returns a Boolean value indicating whether the answer is correct.
    def check_answer(self, user_answer):
        is_correct = user_answer == self.correct_answer
        if is_correct:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", chr(ord("A") + self.correct_answer - 1) + ". " + self.choices[self.correct_answer - 1])
        print(self.explanation)
        print()
        return is_correct

# This 'fetch_questions_from_database' function connects to a MySQL database and fetches PMP questions along with their details from a table named 'question'.
# This table contains all PMP question numbers, questions, choices, correct choice, and explanations for each correct choice. 
def fetch_questions_from_database():
    # Connect to your MySQL database
    db = mysql.connector.connect(
        host= "x.x.x.x.", # The host name or IP address of the MySQL server
        port= "3306", # Port 3306 is the default port for the MySQL protocol
        user= "sample", # The username you use to log into your MySQL database
        password= "sample", # The password you use to log into your MySQL database
        database= "sample" # The database name or schema name
     )
    
    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # This executes an SQL query to retrieve the question rows from the 'question' table, ordered by their IDs.
    query = "SELECT id, question_text, choice1, choice2, choice3, choice4, correct_answer, explanation FROM question ORDER BY id"
    cursor.execute(query)
    # This fetches all rows within the 'question' table and stores the data in the 'question_rows' variable.
    question_rows = cursor.fetchall()

    # This iterates over the 'question' rows and creates 'PMPQuestion' objects, and appends them to the 'question_pool' list.
    question_pool = []
    for row in question_rows:
        question = PMPQuestion(row[0], row[1], row[2:6], row[6], row[7])
        question_pool.append(question)

    # After fetching all the data, this closes the cursor and database connections.
    cursor.close()
    db.close()

    # Returns the 'question_pool' list containing the fetched questions. 
    return question_pool

# This is the main function that executes the quiz.
def main():

    # This calls the 'fetch_questions_from_database' function to retrieve the question pool from the database.
    question_pool = fetch_questions_from_database()

    # Creates a variable to store the number of questions in the exam to equal the total number of questions available from the database table. 
    num_questions = len(question_pool)

    # Starts the score variable at 0 before starting the exam. 
    score = 0

    # Sets the question variable to 1 to start the exam from the first question. 
    question_number = 1  

    # Enter a while loop that continues until the 'question_number' exceeds the total number of questions.
    while question_number <= num_questions:
        # Inside the loop, this retrieves the current question from the 'question_pool' based on the 'question_number'.
        question = question_pool[question_number - 1]  # Adjust index to start at 0
        
        # Displays the question to the user and repeatedly asks for their answer until a valid answer (A, B, C, or D) is provided.
        while True: 
            question.display_question()
            user_answer = input("Enter your answer: ").upper()
            if user_answer in ["A", "B", "C", "D"]:
                # Checks the user's answer using the 'check_answer' method of the 'PMPQuestion' object and increments the score if the answer is correct.
                if question.check_answer(ord(user_answer) - ord("A") + 1):
                    score += 1
                break  # Break out of the loop to move to the next question
            else:
                print("Invalid answer. Please enter A, B, C, or D.")
                print()

        # After each question and answer, it prompts the user to press Enter to continue to the next question.
        input("Press Enter to continue.")

        # Increment the question number and then continue the while loop for the next question. 
        # This will continue until all questions are answered or the user exits the program. 
        question_number += 1

    # Finally, when all questions are answered, it prints the Exam completion message along with the user's score.
    print("------------------------")
    print("Exam complete!")
    print("Your score:", score, "/", num_questions)

# This ensures that the main function is only executed when the script is run directly.
# It prevents the main function from running if the script is imported into another script or module.
if __name__ == "__main__":
    main()
