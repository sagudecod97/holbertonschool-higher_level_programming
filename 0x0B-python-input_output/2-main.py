#!/usr/bin/python3
read_lines = __import__('2-read_lines').read_lines

print("1 line:")
read_lines("my_file_0.txt", 1)
print("--")
print("25 lines:")
read_lines("my_file_0.txt", 25)
print("--")
print("Full content:")
read_lines("my_file_0.txt")
