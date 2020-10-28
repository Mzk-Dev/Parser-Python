import string
# def is_ascii(str):
#     for i in str :
#         lambda i:i==True if ord(i)<=127 else i==False
#         if i==False:
#             return False
#         elif i==str[-1]:
#             if all(i)==True :
#                 return True
is_ascii=lambda x:all([ord(y)<=127 for y in x])
is_ascii_punctuation=lambda x:all(x for x  in string.punctuation)
is_ascii_printable=lambda x:all(x for x in string.printable)
