#!/usr/bin/python3

def remove_char_at(str, n):
    s = str
    if 0 <= n <= len(str) - 1:
        s = ""
        for i in str:
            if i != str[n]:
                s += i
    return s
