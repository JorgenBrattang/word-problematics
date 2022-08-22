def user_input(control_list, question, correct_answer):
    """ Checks the user input """
    while True:
        user_input = input("Enter answer here: ").lower()
        # divider()
        if user_input.isalpha():
            if "y" == user_input:
                for item in question:
                    if item in control_list:
                        print(f"This is the correct answer: {correct_answer}")
                        break
                    else:
                        # simplyfied = simplyfy_to_function(question)
                        # answer_question(simplyfied)
            elif "n" == user_input:
                # answer_question(question)
                break
            else:
                print("Must be (Y) or (N) to continue")
        else:
            print("Must be (Y) or (N) to continue")


