# 문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.

chars = input('문자열을 입력하세요 > ')
chars = chars[::-1]

for i in chars:
    print(i)