#!/usr/bin/env python3

def write_name_to_file():
    with open("Farnoosh.txt", "w") as file:
        file.write("Farnoosh")

if __name__ == "__main__":
    write_name_to_file()

def helloWorld():
    print('Hello World')

helloWorld()

