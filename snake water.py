import random
choice = ["s","w","g"]

chances = 10
no_of_chance = 0
human_point = 0
Computer_point = 0
print("----------Snake water gun game----------")
print("Please enter 's' for snake, 'w' for water & 'g' for gun" )
while(no_of_chance<chances):
    h = input("Enter Snake or Water or Gun:")
    c = random.choice(choice)

    if (h==c):
        print("Tie both 0 points to each")

    elif(h == "s" and c == 'g'):
        Computer_point+=1
        print(f"Your choice is {h} and computer choice is {c}")
        print("Computer won this round")
        print(f"your points are {human_point}\n computer points are {Computer_point}")

    elif(h == "g" and c == "s"):
        human_point+=1
        print(f"Your choice is {h} and computer choice is {c}")
        print("Congratulations you won this round")
        print(f"your points are {human_point}\n computer points are {Computer_point}")

    elif(h == "s" and c == "w"):
        human_point+=1
        print(f"Your choice is {h} and computer choice is {c}")
        print("Congratulations you won this round")
        print(f"your points are {human_point}\n computer points are {Computer_point}")

    elif(h == "w" and c == "s"):
        Computer_point+=1
        print(f"Your choice is {h} and computer choice is {c}")
        print("Computer won this round")
        print(f"your points are {human_point}\n computer points are {Computer_point}")

    elif(h == "g" and c == "w"):
        Computer_point+=1
        print(f"Your choice is {h} and computer choice is {c}")
        print("Computer won this round")
        print(f"your points are {human_point}\n computer points are {Computer_point}")

    elif(h == "w" and c == "g"):
        human_point+=1
        print(f"Your choice is {h} and computer choice is {c}")
        print("Congratulations you won this round")
        print(f"your points are {human_point}\n computer points are {Computer_point}")

    else:
        print("You have entered wrong choice")
        print("Enter 's' for snake, 'w' for water & 'g' for gun")

    no_of_chance+=1
    print(f"{no_of_chance} chances used out of {chances}")

print("****Game Over****")
print("Your points:",human_point)
print("Computer points:",Computer_point)
if(Computer_point == human_point):
    print("game drawn")

elif(Computer_point>human_point):
    print("You loss the game better luck next time")

elif(Computer_point<human_point):
    print("congratulations you won the game")




    

