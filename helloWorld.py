def input_from_user():
    print("Your input will be shown to you below.")
    
    text = input("Please enter text here: ")
    
    print(text)

def question_time():
    question_bool = False
    while question_bool == False:
        question = input("Would you like to input another text? (y/n): ").lower()
        if question == "y":
            input_from_user()
            question_bool = True
        elif question == "n":
            print("Ok bye.")
            question_bool = True
        else:
            print("You have entered an incorrect statement.")

input_from_user()
question_time()


