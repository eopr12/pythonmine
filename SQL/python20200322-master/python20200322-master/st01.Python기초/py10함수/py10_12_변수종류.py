
####################
# 변수의 종류
# 전역변수 : a , b  ==> 함수에서 접근이 가능하다.
# 지역변수 : i , sum, x, y 
# 매개변수 : x, y
####################


####################
# get_sum() 함수를 만드시오
# 첫번째 매개변수: x
# 두번째 매개변수: y
def get_sum(x, y):
    sum = 0
    for i in range(x, y + 1, 1):
        sum = sum + i
    print(a)
    return sum
	
	
def main():
    ####################
    # get_sum 함수 호출
    a = 3
    b = 7
    get_sum(a, b)
	
main()
