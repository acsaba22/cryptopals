import os, sys

# sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))


# sys.path.append(os.path.abspath(os.path.join('..', 'd03')))

# # # Now do your import
# # from config.config import *

# from d03 import main

if __name__ == "__main__":
    print(os.getcwd())
    with open(os.path.join(os.getcwd(), '04/input.txt')) as file:
        for line in file:
            print(line)
