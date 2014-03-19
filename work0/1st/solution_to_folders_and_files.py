from subprocess import call
import inspect  # function for getting functions names and source
import hackBg_25_02  # file containing all the solutions

"""
    This file implements a program that takes all the different names
    of functions out of a file , creates directories with those names ,
    creates two files in each directory (solution.py and test.py) ,
    fills the solution file with the code from the imported file,
    commits each time a folder and it's containing files are created
    and finally makes a push

"""

# gets functions names out of the solutions file
al_F = inspect.getmembers(hackBg_25_02, inspect.isfunction)

for func_name in al_F:

# gets the source of the functions
    source_of_func = inspect.getsourcelines(func_name[1])
# makes directories
    call(["mkdir", func_name[0]])
    solution_file = open(func_name[0] + "/solution.py", "w")
    for line in source_of_func[0]:
    # filles the solution files with the source code
        solution_file.write(line)
    solution_file.close()
    call(["touch", func_name[0] + "/test.py"])
    call(["git", "add", "."])
    call(["git", "commit", "-m Added folder named " + func_name[0] +\
          " , solution and test files."])
    print("making dir --" + func_name[0] + "\n")

call(["git", "push", "origin", "master"])
