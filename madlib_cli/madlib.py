import re

print("***************-------Madlib--------********************")
print("Welcome to Madlib Cli Game")
print("Mad libs generator is a fun game that is usually played by kids.")
print("***************-------How to play--------********************")
print("Just write the words")
print("***************-----------------********************")


def read_template(file_path):
    # This func take the path of the file and return it's content as a string
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError as wrong_path:
        raise wrong_path


# print(read_template('assets\dark_and_stormy_night_template.txt'))

def parse_template(content):
    # This function takes the content of the text and returns 2 params
    # first returned is a string of the content without the words inside the {}
    # new_content = re.sub(r"{.*?}", "{}", content)
    # second returned is a tuple that has all the properties cut from the main content
    # new_tuple = tuple(re.findall(r"{(.*?)}", content))
    return re.sub(r"{.*?}", "{}", content), tuple(re.findall(r"{(.*?)}", content))


# path ='assets\dark_and_stormy_night_template.txt'
# print(parse_template(read_template(path)))
def merge(content, new_tuple):
    # This function takes the content of the text and append to it the user input
    return parse_template(content)[0].format(*new_tuple)


def input_handle(new_tuple):
    # This function to handle user input return new list

    user_inputs = []
    for word in new_tuple:
        user_input = input(f"Enter the  ({word}) :")
        user_inputs.append(user_input)
    return user_inputs


def start_game():
    # This function for starting all the game functionalities
    print(merge(parse_template(read_template("assets/user_interaction.txt"))[0],
                input_handle(parse_template(read_template("assets/user_interaction.txt"))[1])))


start_game()
