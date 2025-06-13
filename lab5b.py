#!/usr/bin/env python3
# Author ID: [135843233]
def append_file_string(file_name, string_of_lines):
    file = open(file_name, 'a')
    file.write(string_of_lines)
    file.close()
    # Takes two strings, appends the string to the end of the file

def write_file_list(file_name, list_of_lines):
    file = open(file_name, 'w')
    for line in list_of_lines:
        file.write(line + '\n')
    file.close()
    # Takes a string and list, writes all items from list to file where each item is one line

def copy_file_add_line_numbers(file_name_read, file_name_write):
    file_r = open(file_name_read, 'r')
    file_w = open(file_name_write, 'w')
    line_num = 1
    for line in file_r:
        file_w.write(str(line_num) + ':' + line.strip() + '\n')
        line_num += 1
    file_r.close()
    file_w.close()
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file

def read_file_string(file_name):
    file = open(file_name, 'r')
    contents = file.read()
    file.close()
    return contents

def read_file_list(file_name):
    file = open(file_name, 'r')
    lines = []
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

  