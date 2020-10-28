import functools


def count_element(function):
    @functools.wraps(function)
    def wrap(*args,**kwargs):
        result=function(*args,**kwargs)
        return result,len(result)
    return wrap

@count_element
def str_contact(s1,s2):
    return ''.join((s1,s2))

@count_element
def del_list(l,count):
    return l[:-(count)]


print(str_contact('asdasd','asdasdasdd'))
print(del_list('1234567',3))
