import string_utils
import sys

def tab_to_spaces(file_name):
    file = open(file_name, "r")
    content = file.read()
    file.close()
    file = open(file_name, "w")
    temp = string_utils.tabs_to_spaces(content)
    file.write(temp)

entered_args = sys.argv[1]
tab_to_spaces(entered_args)
