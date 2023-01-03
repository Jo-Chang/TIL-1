# 정수 한 개를 입력 받고 0보다 크고, 짝수라면 True 아니면 False를 출력하세요.

num = int(input('정수를 입력하세요 > '))

if num > 0 and num % 2 == 0:
    print(True)
else:
    print(False)