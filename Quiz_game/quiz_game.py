print("Welcome to my computer quiz!")

playing:str = input("Do you want to play? y/n ")
if playing.lower() != "y":
    quit()
print("Okay! Let's Play")
score = 0
answer:str = input("What is CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer:str = input("What is GPU stands for? ").lower()
if answer == "graphics processing unit": 
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print(f"Your score is {score}")
print(f"your score percent is {(score*score)//100}%")