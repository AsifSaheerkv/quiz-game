print("welcome to Quiz,nice to meet u")
Name = input("what is your name ")

playing = input(Name + ", Do you want to play? ")


if playing.lower() != "yes":
    quit()
    
print("Welcome to the game")

score=0

answer = input("What does CPU Stand For? ")
if answer.lower() == "central processing unit":
    print('Correct !')
    score += 1
else:
    print("Oops! wrong Answer")
    

answer = input("What does RAM Stands for? ")
if answer.lower() == "random access memory":
    print('Correct !')
    score += 1
else:
    print("Oops! wrong Answer")
    

answer = input("What does  ROM Stands for? ")
if answer.lower() == "read only memory":
    print('Correct !')
    score += 1

else:
    print("Oops! wrong Answer")
    

answer = input("What does  OS Stands for?")
if answer.lower() == " operational system":
    print('Correct !')
    score += 1

else:
    print("Oops! wrong Answer")
    

answer = input("What does  GUI Stands for? ")
if answer.lower() == "graphics processing unit":
    print('Correct !')
    score += 1

else:
    print("Oops! wrong Answer")
    

answer = input("What does   URL Stands for? ")
if answer.lower() == "uniform resource locator":
    print('Correct !')
    score += 1

else:
    print("Oops! wrong Answer")

print("you got " + str(score) + " Questions correct ")
    
print("you got " + str((score / 6) *100) + " %. ")


