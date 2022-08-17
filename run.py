"""
Cointains alphabetic numbers between 0-19
"""
unique_numbers = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]


def line_break():
    """
    Line break in code
    """
    return print(f"\n")


def welcome_message():
    """
    Display the welcome message
    """
    message = """
    Welcome, this game will challenge your reading ability
    to solve mathimatic problems. If you can't solve them right away.
    The program will help you along the way, by simplyfiying it for you.
    """
    print(message)


def random_question():
    """
    This will hold the code for randomize the questions
    """
    return ["The cow has five tables"]


def start_game():
    """
    Starts the game
    """
    print("Would you like to start? Press (Y) for yes and (N) for no")
    while True:
        user_input = input("Enter answer here: ").lower()
        if user_input.isalpha():
            if "y" == user_input:
                answer_question(random_question())
                break
            elif "n" == user_input:
                quit_game_message()
                break
            else:
                print(f"\nYou entered {user_input}\nMust be (Y) or (N)")
        else:
            line_break()
            print("Must be (Y) or (N) to continue")


def answer_question(question):
    """
    This will hold a random question, but for testing purpose only hold one.
    """
    print(f"\n{question}")
    while True:
        user_input_question = input("Enter answer here: ")
        if user_input_question.isnumeric():
            check_if_correct(user_input_question, question)
            break
        else:
            line_break()
            print("Your answer must only containt numbers 0-9")


def check_if_correct(answer, question):
    """
    Checks if the answer is correct to the question, this will later
    on check the question and do the math it self to get the correct
    answer. But for now it only holds "5" for checking purpose.
    """
    if answer == str(5):
        print(f"\n{answer} is correct! Good job!\n")
        play_again()
    else:
        print("    Try again!")
        line_break()
        print("Do you want to simplyfy the question?: Y or N")
        while True:
            simplyfy_input = input("Enter answer here: ").lower()
            if simplyfy_input.isalpha():
                if "y" == simplyfy_input:
                    simplyfy_word_into_num(question)
                    break
                elif "n" == simplyfy_input:
                    answer_question(question)
                    break
                else:
                    print("Must be (Y) or (N) to continue")
            else:
                print("Must be (Y) or (N) to continue")


def simplyfy_word_into_num(question):
    """
    This will simplyfy the question with numbers instead
    of the alphabetic number like "Three into 3"
    """
    my_list = convert_into_list(question)
    question_with_number = words_into_numbers(my_list)
    make_string = ' '.join(str(x) for x in question_with_number)
    answer_question(make_string)


def convert_into_list(question):
    """
    Converts a sentence into a list
    """
    return ([i for item in question for i in item.split()])


def words_into_numbers(data):
    """
    Converts the alphabetic number into an integer
    """
    new_list = []
    for count, item in enumerate(data):
        if data[count] in unique_numbers:
            new_list.append(unique_numbers.index(data[count]))
        else:
            new_list.append(data[count])
    return new_list


def play_again():
    """
    Allows you to choose to play again
    """
    print("Do you want to play again?: Y or N")
    while True:
        play_again_input = input("Enter answer here: ").lower()
        if play_again_input.isalpha():
            if "y" == play_again_input:
                answer_question(random_question())
                break
            elif "n" == play_again_input:
                print("Hope you had fun!")
                break
            else:
                print("Must be (Y) or (N) to continue")
        else:
            print("Must be (Y) or (N) to continue")


def quit_game_message():
    """
    If the user don't want to play anymore, this will give a goodbye message
    """
    quit_game = """
    Sorry to see you leave, but hope you learned something along the way!
    """
    print(quit_game)


def intro():
    """
    Starts up the game
    """
    welcome_message()
    start_game()


intro()

# question = ["The cow has three tables"]
# print(question)
# my_list = convert_into_list(question)
# print(my_list)
# question_with_number = words_into_numbers(my_list)
# print(question_with_number)
# print(' '.join(str(x) for x in question_with_number))
