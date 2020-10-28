import sys
import re

call = re.compile(r"(?P<b1>[(])?[- ]?(?P<b2>\d{3})?[- ]?(?P<b3>[)])?[- ]?(?P<b4>\d{3})?[- ]?(?P<b5>\d{4})", re.VERBOSE)

for numb in sys.stdin:
    number = call.match(numb)
    if number:
        print("("+(number.group('b2'))+")",number.group('b4'),number.group('b5'))
    else:
        print("Enter normal number!")
