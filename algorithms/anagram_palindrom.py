#!/usr/bin/python

def is_anagram_of_palindrom(input_str):
    stack = []

    for char in input_str:
        if not stack:
            stack.append(char)
        elif char in stack:
            stack.remove(char)