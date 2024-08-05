print("Welcome to my computer quiz!")

playing:str = input("Do you want to play? y/n ")
if playing.lower() != "y":
    quit()
print("Okay! Let's Play")
score = 0
answer:str = input("What is CPU").lower()
if answer == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")