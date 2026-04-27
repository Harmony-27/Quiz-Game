# Version 2 - Improved Quiz Game

# This version works the same as Version 1,
# but the code is shorter and easier.

# Version 1 had long code and repeated conditions.
# Version 2 uses a better method with loop and list.

# Now new questions can be added easily.

print("Welcome to Quiz Game!")
score = 0
q1="Capital of India?\nA. Mumbai\nB. Delhi\nC. Kolkata\nD. Chennai"
a1="B"
q2="Which language is used for programming?\nA. HTML\nB. Python\nC. CSS\nD. Design"
a2="B"
q3="What is 5 + 3?\nA. 6\nB. 7\nC. 8\nD. 9"
a3="C"
q4="Which planet is known as the Red Planet?\nA. Earth\nB. Venus\nC. Mars\nD. Jupiter"
a4="C"
q5="Which animal is known as the King of the Jungle?\nA. Tiger\nB. Lion\nC. Elephant\nD. Bear"
a5="B"

questions = [
    (q1, a1),
    (q2, a2),
    (q3, a3),
    (q4, a4),
    (q5, a5)
]

for q, a in questions:
    print(q)
    user_answer = input("Your answer: ").upper()
    if user_answer == a:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is", a)

print("Quiz Over! Your final score is:",score,"out of 5.")
if score==5:
    print("Excellent! You got all answers correct!")
elif score>=3:
    print("Good job! You got",score,"out of 5 correct!")
else:
    print("Better luck next time! You got",score,"out of 5 correct!")