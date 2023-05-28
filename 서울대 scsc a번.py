def calculate_expression(expression):
    operator = None
    A = None
    B = None

    # 연산자와 피연산자 추출
    if '+' in expression:
        operator = '+'
        A, B = expression.split('+')
    elif '-' in expression:
        # '-'를 연산자로 사용하는 경우는 A-B 형태로만 가정합니다.
        operator = '-'
        parts = expression.split('-')
        A = parts[0]
        B = ''.join(parts[1:])
    elif '*' in expression:
        operator = '*'
        A, B = expression.split('*')
    elif '/' in expression:
        # '/'를 연산자로 사용하는 경우는 A/B 형태로만 가정합니다.
        operator = '/'
        parts = expression.split('/')
        A, B = expression.split('/')
        if '-' in expression:
            A = parts[0]
            B = '-'.join(parts[1:])

    # '/' 이전까지의 부분을 8진수로 변환

    if A.endswith('/'):
        A = int(A[:-1], 8)
    else:
        A = int(A, 8)

        
    print(A)
    print(B)
    # 피연산자 B를 8진수로 변환
    B = int(B, 8)

    # 연산 수행
    if operator == '+':
        result = A + B
    elif operator == '-':
        result = A - B
    elif operator == '*':
        result = A * B
    elif operator == '/':
        if B == 0:
            return "invalid"
        result = A / B

    # 결과를 8진수로 변환하여 반환
    return oct(int(result))[2:]

# 수식 입력 받기
expression = input()

# 수식 계산
result = calculate_expression(expression)

# 결과 출력
print(result)
