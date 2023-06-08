#!/usr/bin/python3
import hidden_4 as hidden

if __name__ != "__main__":
    exit()

for names in dir(hidden):
    if names[0:2] != "__":
        print(names)
