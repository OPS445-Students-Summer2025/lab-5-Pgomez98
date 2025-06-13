#!/usr/bin/env python3
# Author ID: [seneca_id]

def read_file_string(file_name):
    file_name = open('data.txt', 'r')
    return file_name.read() 
    # Takes file_name as string for a file name, returns its entire contents as a string

def read_file_list(file_name):
    file_name = open('data.txt', 'r')
    return [line.strip() for line in file_name.readlines()]
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))