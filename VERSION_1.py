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

question=[q1,q2,q3,q4,q5]

for q in question:
    if q==q1:
        print(q1)
        ans=input("Enter your answer: ").upper()
        if ans==a1:
            print("Correct!")
            score+=1          #score = score + 1
            print("Your score is:",score)
        else:
            print("Wrong!")
            print("Your score is:",score)
    elif q==q2:
        print(q2)
        ans=input("Enter your answer: ").upper()
        if ans==a2:
            print("Correct!")
            score+=1          #score = score + 1
            print("Your score is:",score)
        else:
            print("Wrong!")
            print("Your score is:",score)
    elif q==q3:
        print(q3)
        ans=input("Enter your answer: ").upper()
        if ans==a3:
            print("Correct!")
            score+=1          #score = score + 1
            print("Your score is:",score)
        else:
            print("Wrong!")
            print("Your score is:",score)
    elif q==q4:
        print(q4)
        ans=input("Enter your answer: ").upper()
        if ans==a4:
            print("Correct!")
            score+=1          #score = score + 1
            print("Your score is:",score)
        else:
            print("Wrong!")
            print("Your score is:",score)
    elif q==q5:
        print(q5)
        ans=input("Enter your answer: ").upper()
        if ans==a5:
            print("Correct!")
            score+=1          #score = score + 1
            print("Your score is:",score)
        else:
            print("Wrong!")
            print("Your score is:",score)

print("Quiz Over! Your final score is:",score,"out of 5.")
if score==5:
    print("Excellent! You got all answers correct!")
elif score>=3:
    print("Good job! You got",score,"out of 5 correct!")
else:
    print("Better luck next time! You got",score,"out of 5 correct!")