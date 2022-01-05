import datetime

string = "p"
while string != "q":
    if statuschecker():
        user_input = input("press space to start")
        if user_input == "q":
            continue
        elif user_input == " ":
            record()
        else:
            print("invalid input")

    else:
        user_input = input("press space to end")
        if user_input == "q":
            continue
        elif user_input == " ":
            record()
        else:
            print("invalid input")