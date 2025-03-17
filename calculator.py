def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# 사용자 입력 받기
def calculator():
    print("계산기 프로그램")
    print("연산자를 선택하세요:")
    print("덧셈: +, 뺄셈: -, 곱셈: *, 나눗셈: /")
    
    operator = input("연산자 입력: ")
    
    num1 = float(input("첫 번째 숫자 입력: "))
    num2 = float(input("두 번째 숫자 입력: "))
    
    if operator == "+":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operator == "-":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operator == "*":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operator == "/":
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("유효하지 않은 연산자입니다.")

# 계산기 실행
calculator()