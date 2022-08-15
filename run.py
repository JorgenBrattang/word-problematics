"""
This holds the question, that will be converted by respected
functions to get the correct number for the string entered.
Example: three = 3
"""
question = ["The cow has three tables"]

unique_numbers = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]


def convert_into_list(data):
    """
    Converts a sentence into a list
    """
    return ([i for item in data for i in item.split()])


def words_into_numbers(data):
    new_list = []
    # for x in range(len(data)):
    for count, item in enumerate(data):
        if data[count] in unique_numbers:
            new_list.append(unique_numbers.index(data[count]))
        else:
            new_list.append(data[count])
    return new_list


print(question)
my_list = convert_into_list(question)
question_with_number = words_into_numbers(my_list)
print(question_with_number)
