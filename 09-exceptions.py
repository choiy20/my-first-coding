# exceptions

# ZeroDivisionError
# 1 / 0

def divide_by(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return "You cannot divide it by 0"

#  4 / 2 = 2
print(divide_by(4, 2))
print(divide_by(4, 0))

#예외 만들기
# exception

class EvenNumberDevisonError(Exception):
    pass

def divide_by_odd_number(first, second):
    if second % 2 == 0:
        raise EvenNumberDevisonError
    else:
        return first / second

print(divide_by_odd_number(6, 3))
print(divide_by_odd_number(6, 2))    
