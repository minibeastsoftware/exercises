# This first part is w/o RegEx

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

import re

#Using RegEx

def hasPhoneNumber(text):
    phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    match = phoneNumRegex.search(text)
    print(f"Phone number found: ({match.group(1)}) {match.group(2)}")
    return

hasPhoneNumber('My number is 415-555-4242.')
