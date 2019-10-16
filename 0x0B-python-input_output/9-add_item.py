#!/usr/bin/python3
import sys
import json

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    lst = load_from_json_file("add_item.json")
except:
    lst = []

for i in range(1, len(sys.argv)):
    lst.append(sys.argv[i])

save_to_json_file(lst, "add_item.json")
