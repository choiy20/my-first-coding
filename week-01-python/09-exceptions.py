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
# exception 이라는 클래스가 있음

class EvenNumberDevisonError(Exception): #Exception을 상속하기
    pass # 함수나 if문이나 print를 지금 당장 구현하지 않겠다.라는 뜻.

def divide_by_odd_number(first, second):
    if second % 2 == 0:
        raise EvenNumberDevisonError
    else:
        return first / second

print(divide_by_odd_number(6, 3))
print(divide_by_odd_number(6, 2))
