"""
Cointains alphabetic numbers between 0-19
"""
unique_numbers = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]

operators = [
        "divided", "multiplied", "minus", "add",
        ]


def welcome_message():
    """
    Display the welcome message
    """
    message = """
    Welcome, this game will test your reading ability
    to solve mathimatic problems. If you can't solve them right away.
    The program will help you along the way, by simplyfiying it for you.
    """
    print(message)


def random_question():
    """
    This will hold the code for randomize the questions
    """
    return ["What is five multiplied by five"]


def start_game():
    """
    Starts the game
    """
    print("Would you like to start? Press (Y) for yes and (N) for no")
    while True:
        user_input = input("Enter answer here: ").lower()
        divider()
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
            print("Must be (Y) or (N) to continue")


def answer_question(question):
    """
    This will hold a random question, but for testing purpose only hold one.
    """
    question_unjoin = question
    question_joined = ' '.join(str(x) for x in question)
    print(question_joined)

    while True:
        user_input_question = input("Enter answer here: ")
        divider()
        if user_input_question.isnumeric():
            check_if_correct(user_input_question, question_unjoin)
            break
        else:
            print("Your answer must only containt numbers 0-9")


def check_if_correct(answer, question):
    """
    Checks if the answer is correct to the question, this will later
    on check the question and do the math it self to get the correct
    answer. But for now it only holds "5" for checking purpose.
    """
    correct_answer = math_function(question)

    control_list = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "/", "*", "-", "+",
    ]

    if int(answer) == correct_answer:
        print(f"\n{answer} is correct! Good job!\n")
        play_again()
    else:
        print("    Try again!")
        divider()
        # ------------------------
        for item in question:
            if item in control_list:
                print("Do you want the answer? Y or N")
                break
            else:
                print("Do you want to simplyfy the question?: Y or N")
        # ------------------------
    user_input(control_list, question, correct_answer)


def user_input(control_list, question, correct_answer):
    """ Checks the user input """
    while True:
        user_input = input("Enter answer here: ").lower()
        divider()
        if user_input.isalpha():
            if "y" == user_input:
                for item in question:
                    if item in control_list:
                        print(f"This is the correct answer: {correct_answer}")
                        break
                    else:
                        simplyfied = simplyfy_to_function(question)
                        answer_question(simplyfied)
                break
            elif "n" == user_input:
                answer_question(question)
                break
            else:
                print("Must be (Y) or (N) to continue")
        else:
            print("Must be (Y) or (N) to continue")


def divider():
    """
    This will add an divider so you can see where you are better
    """
    print('----------------------------------------')


def simplyfy_to_function(question):
    """
    This will simplyfy the question with numbers and operators instead
    of the alphabetic once like "five divided by four" into "5/4"
    """
    stage_one = convert_into_list(question)
    stage_two = words_into_numbers(stage_one)
    stage_three = word_into_operations(stage_two)
    stage_four = delete_remaining_words(stage_three)
    return stage_four


def convert_into_list(question):
    """
    Converts a sentence into a list and make all lowercase letters
    """
    control_list = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "/", "*", "-", "+",
    ]
    for item in question:
        if item in control_list:
            return question
    lower_list = ([i for item in question for i in item.split()])
    for count, item in enumerate(lower_list):
        lower_list[count] = lower_list[count].lower()
    return lower_list


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


def word_into_operations(data):
    """
    Converts the alphabetic operator into an operator
    """
    for count, item in enumerate(data):
        if item in operators:
            if item == "divided":
                data[count] = "/"
            elif item == "multiplied":
                data[count] = "*"
            elif item == "minus":
                data[count] = "-"
            elif item == "add":
                data[count] = "+"
    return data


def delete_remaining_words(data):
    """
    This will delete the remaining words so your only
    left with the operators and numbers
    """
    control_list = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "/", "*", "-", "+",
    ]
    keep_list = []
    for item in data:
        if item in control_list:
            keep_list.append(item)
        else:
            pass
    return keep_list


def math_function(data):
    """
    Change to incoming data into a working math function.
    """
    function = simplyfy_to_function(data)
    for x in function:
        if x == "/":
            function.remove(x)
            value = function[0]/function[1]
        elif x == "*":
            function.remove(x)
            value = function[0]*function[1]
        elif x == "+":
            function.remove(x)
            value = function[0]+function[1]
        elif x == "-":
            function.remove(x)
            value = function[0]-function[1]
    return value


def play_again():
    """
    Allows you to choose to play again
    """
    divider()
    print("Do you want to play again?: Y or N")
    while True:
        user_input = input("Enter answer here: ").lower()
        if user_input.isalpha():
            if "y" == user_input:
                divider()
                answer_question(random_question())
                break
            elif "n" == user_input:
                divider()
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
