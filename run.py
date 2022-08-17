unique_numbers = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]


def welcome_message():
    """
    Display the welcome message
    """
    message = """
    Welcome, this game will challenge your reading ability
    to solve mathimatic problems. If you can't solve them right away.
    The program will help you along the way, by simplyfiying it for
    you.
    """
    print(message)


def start_game():
    """
    Starts the game
    """
    start_message = """
    Would you like to start? Press (Y) for yes and (N) for no
    """
    print(start_message)
    while True:
        user_input = input('Enter answer here: ').lower()
        if user_input.isalpha():
            if "y" in user_input:
                question = ["The cow has three tables"]
                random_question(question)
                break
            elif "n" in user_input:
                quit_game_message()
                break
            else:
                print('Must be (Y) or (N) to continue')
        else:
            print('Must be (Y) or (N) to continue')
    

def random_question(question):
    """
    This will hold a random question, but for testing purpose only hold one.
    """
    print(question)
    while True:
        user_input_question = input('Enter answer here: ')
        if user_input_question.isnumeric():
            check_if_correct(user_input_question, question)
            break
        else:
            print('Your answer must only containt numbers 0-9')


def check_if_correct(answer, question):
    """
    Checks if the answer is correct to the question, this will later
    on check the question and do the math it self to get the correct
    answer. But for now it only holds "5" for checking purpose.
    """
    print(f"\nYour question was\n {question}\n And your answer was: {answer}")

    # For some reason this comes out false.... But the variable answer output is 5
    print(answer)
    if answer == 5:
        print("You are correct!")
    else:
        print("Try again!")


def quit_game_message():
    """
    If the user don't want to play anymore, this will give a goodbye message
    """
    quit_game = """
    Sorry to see you leave, but hope you learned something along the way!
    """
    print(quit_game)


def convert_into_list(data):
    """
    Converts a sentence into a list
    """
    return ([i for item in data for i in item.split()])


def words_into_numbers(data):
    """
    Converts the alphabetic number into an integer
    """
    new_list = []
    # for x in range(len(data)):
    for count, item in enumerate(data):
        if data[count] in unique_numbers:
            new_list.append(unique_numbers.index(data[count]))
        else:
            new_list.append(data[count])
    return new_list


def main():
    """
    Runs the games functions in order
    """
    welcome_message()
    start_game()


main()




# print(question)
# my_list = convert_into_list(question)
# question_with_number = words_into_numbers(my_list)
# print(question_with_number)
