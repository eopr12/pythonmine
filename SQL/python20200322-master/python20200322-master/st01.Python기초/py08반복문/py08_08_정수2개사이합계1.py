# 1이상의 정수 n1과 n2를 입력 받는다. 
# 그리고 n1부터 입력 받은 정수 n2 까지의 합을 계산하고
# 그 결과를 출력하는 프로그램을 작성하시오.
# 
# for 문과 if~esle 문이 결합된 예제
#
# ▪ 실행결과예시
# 시작 정수를 입력하세요:  2
# 종료 정수를 입력하세요:  6
# 2+3+4+5+6 = 20

시작정수 = input("시작 정수를 입력하세요: ")
종료정수 = input("종료 정수를 입력하세요: ")

시작정수 = int(시작정수) # 정수 변환
종료정수 = int(종료정수) # 정수 변환

sum = 0
for i in range(시작정수,종료정수+1, 1 ):
    sum = sum + i

    print( i, end="")

    # i가 종료정수 와 같으면 "="을 출력하고
    #                 아니면 "+"을 출력
    if i == 종료정수 :
        print( "=", end="")
    else:
        print( "+", end="")

print( sum )


# 문자열을 사용하는 방법
# str1 = ""
# str1 = str1 + "2+"  # ==> "2+"
# str1 = str1 + "3+"  # ==> "2+3+"
# str1 = str1 + "4+"  # ==> "2+3+4+"

sum = 0
str1 = ""
for i in range(시작정수,종료정수+1, 1 ):
    sum = sum + i
    str1 = str1 + str(i)

    # i가 종료정수 와 같으면 "="을 출력하고 아니면 "+"을 출력
    if i == 종료정수 :
        str1 = str1 + "="
    else:
        str1 = str1 + "+"

str1 = str1 + str( sum )
print( str1 )