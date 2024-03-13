def input_from_user():
    print("Your input will be shown to you below.")
    
    text = input("Please enter text here: ")
    
    print(text)

def question_time():
    question = input("Would you like to input another text? (y/n): ").lower()
    if question == "y":
        input_from_user()
    else:
        print("Ok bye.")

input_from_user()
question_time()


