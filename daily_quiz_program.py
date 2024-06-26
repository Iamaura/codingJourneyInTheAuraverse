# Creating a 3 question quiz that will store users names, answers, and grade their input so that they can recieve their grade after they finish.

""""Empty List That Will Store Student Names"""
students = []

""""Empty List That Will Store Student Answers"""
answers = []

question_1 = 'Which of the following is a correct variable assignment in Python?'
question_2 = 'What is the correct syntax to output "Hello, World!" in Python?'
question_3 = 'Which of the following data types is used to store a sequence of characters in Python?'

options = ['a) 1_variable = 5', 'b) variable1 = 5', 'c) variable 1 = 5', 'd) variable-1 = 5']
options_2 = ['a) echo "Hello, World!"', 'b) print("Hello, World!")', 'c) printf("Hello, World!")', 'd) System.out.println("Hello, World!")']
options_3 = ['a) Integer', 'b) Float', 'c) String', 'd) List']

test_active = True 

prompt = "Good day! Here's a quick quiz for you to take!"
prompt += "Please enter your name whenever you're ready to begin the quiz."

while test_active:
    #   Enter your name so we can store you as a student 
    name = input("\nWhat is your name? ")
    students.append(name.title())

    print(f"\n{question_1}")
    for option in options:
        print(f"{option}")
    student_answer = input("\n Select an answer: ")
    if student_answer == 'stop':
        break
    else:
        answers.append(student_answer)

    print(f"\n{question_2}")
    for option_2 in options_2:
        print(f"{option_2}")
    student_answer = input("\n Select an answer: ")
    if student_answer == 'stop':
        break
    else:
        answers.append(student_answer)

    print(f"\n{question_3}")
    for option_3 in options_3:
        print(f"{option_3}")
    student_answer = input("\n Select an answer: ")
    if student_answer == 'stop':
        break
    else:
        answers.append(student_answer)


    repeat = f"\n{name}, you've finished the quiz. Do you feel confident with your answers?"
    repeat += " If so type 'yes' to receive your score or 'no' to retake the test: " 

    student_response = input(repeat)
    if student_response == 'yes':
        break

# The answer_key is indexed in sequence of the questions in the quiz
print("\n--- Your Final Score ---")
answer_key = ['b', 'b', 'c']

score = 0

if answers[0] == 'b':
    score += 1
else: 
    score = score
if answers[1] == 'b':
    score += 1 
else: 
    scoore = score
if answers[2] == 'c':
    score += 1
else: 
    score = score

print(f"\n{students[0]} scored a {score} out of 3!")

if score == 3:
    print("Congradulations! You received an A on your Quiz!")
elif score == 2:
    print("You received an D on your Quiz, you should try again.")
else:
    print("You received an F on your Quiz, you should study before taking it again")
