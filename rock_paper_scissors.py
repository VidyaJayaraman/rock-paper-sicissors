import random
import time

choices = ["R", "P", "S"]

user_points = [0]
ai_points = [0]

while True:

    print("\nR = Rock 🏔️")
    time.sleep(0.5)

    print("P = Paper 📄")
    time.sleep(0.5)

    print("S = Scissors ✂️")
    time.sleep(0.5)

    print("EXIT")

    user = input("\nYour Choose: ").upper().strip()

    if user == "R" or user == "P" or user == "S":

        ai = random.choice(choices)

        print("\nAI Choice:", end=" ")
        time.sleep(1)
        print(ai)

        if user == "R" and ai == "S" or user == "S" and ai == "P" or user == "P" and ai == "R":
            print("\nYou won!")
            user_points[0] += 1

        elif user == "S" and ai == "R" or user == "P" and ai == "S" or user == "R" and ai == "P":
            print("\nYou lost!")
            ai_points[0] += 1

        else:
            print("\nDraw!")

        time.sleep(1)

    elif user == "EXIT":
        print("\nGame Over!")
        break

    else:
        print("\nInvalid choice!")

    print("\nYour points:", user_points[0])
    print("AI points:", ai_points[0])