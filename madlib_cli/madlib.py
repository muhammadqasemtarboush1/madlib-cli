import re


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
    #  This function takes the content of the text and returns 2 params
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