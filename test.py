# test.py

import sys



def write1(input):
    # Open or create a file named 'test.txt' in write mode
    with open("test.txt", 'a') as file:
            file.write(input + '\n')
        


if __name__ == "__main__":

    print("Hello world")
    write1("run")

    data_to_save = sys.argv[1]
    write1(data_to_save)


