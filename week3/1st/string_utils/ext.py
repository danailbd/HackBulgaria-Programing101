import os
import sys

def ext(extention):
    files = [file for file in os.listdir('.') if os.path.isfile(file)]
    for i in files:
        if os.path.splitext(i)[1] == extention:
            print(i + ', ')
