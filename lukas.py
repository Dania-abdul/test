

"""
Each function (assignment(), challenge(), etc.) contains nearly identical code 
for validating user input

try to avoid repetition by creating a reusable helper function for handling user input

for example 

create a helper function
then call it out 

def get_input():
  ......

def assignment():
    retun get_input()


"""


def assignment():
    user_input = input("Is the assignment finished? (Yes or No): ").strip().lower()
    if user_input == "yes":
        return True
    elif user_input == "no":
        return False
    else:
        print("Only yes or no, please try again")
        assignment()


def challenge():
    user_input = input("Is the challenge finished? (Yes or No): ").strip().lower()
    if user_input == "yes":
        return True
    elif user_input == "no":
        return False
    else:
        print("Only yes or no, please try again")
        challenge()



def thesis():
    user_input = input("Is the thesis finished? (Yes or No): ").strip().lower()
    if user_input == "yes":
        return True
    elif user_input == "no":
        return False
    else:
        print("Only yes or no, please try again")
        thesis()


def company():
    user_input = input("Is the company happy? (Yes or No): ").strip().lower()
    if user_input == "yes":
        return True
    elif user_input == "no":
        return False
    else:
        print("Only yes or no, please try again")
        company()


def basecamp():
    if assignment() and challenge():
        return True

def internship():
    if thesis() or company():
        return True

def graduation():
    basecamp_status = basecamp()
    internship_status = internship()
    if basecamp_status and internship_status:
        print("Congrats you graduated!")
    elif basecamp_status or internship_status:
        if internship_status:
            print("Only the internship is finished, please finish basecamp.")
        elif basecamp_status:
            print("Only the basecamp is finished, please finish the internship.")

        # print("Only one of the two")
    else:
        print("Neither basecamp or the internship is finished.")

graduation()