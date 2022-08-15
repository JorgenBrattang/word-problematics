question = ["The cow has three tables"]


def convert(data):
    """
    Converts a sentence into a list
    """
    return ([i for item in data for i in item.split()])
     

my_list = (convert(question))


unique_numbers = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]

new_list = []
for x in range(len(my_list)):
    if my_list[x] in unique_numbers:
        new_list.append(unique_numbers.index(my_list[x]))
    else:
        new_list.append(my_list[x])

print(question)
print(new_list)