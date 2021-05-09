

#문제 61 # prince 변수에ㅓ는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라.(힌트:슬라이싱)
price=['20180718',100,130,140,150,160,170]
print(price[1:])
        #[슬라이싱] =   [1:]    =2번째값부터 끝까지

#문제 62 # 슬라이싱을 사용해서 홀수만 출력하라
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[: : 2])
        #[슬라이싱]=[1::2]=1번째 값부터 끝까지 2개씩 이동 = 1 3 5 7 9

#문제63 # 슬라이싱을 사용해서 짝수만 출력하라
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums[1::2])
        #[슬라이싱]=[1::2] = 1번째값부터 끝까지 2개씩 이동 =  1 3 5 7 9

#문제 64 # 슬라이싱을 사용하여 리스트의 숫자를 역 방향으로 출력하라
nums=[1,2,3,4,5]
print(nums[: : -1])
    # [슬라이싱]=[::-1] =뒤로 이동

#문제 65 # interest 리스트에는 아래의 데이터가 바인딩되어 있다
interest=['삼성전자','LG전자','Naver']
print(interest[0],interest[2])

# 문제 66 # interest 리스트에는 아래의 데이터가 바인딩되어 있다
interest=['삼성전자','LG전자','Naver','SK하이닉스','미래에셋대우']
print(" ".join(interest))
        # join 함수 : 리스트 내 항목을 합칠때 사용

#문제 67# interest 리스트에는 아래의 데이터가 바인딩되어 있다.   
interest=['삼성전자','LG전자','Naver','SK하이닉스','미래에셋대우']
print("/".join(interest))

#68 # interest 리스트에는 아래의 데이터가 바인딩되어 있다
interest=['삼성전자','LG전자','Naver','SK하이닉스','미래에셋대우']
print("\n".join(interest))
    #
#69 # 회사이름이 슬래시('/')로 구분되어 하나의 문자열로 저장되어 있다
string="삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

# 70 # 리스트에 있는 값을 오름차순으로 정렬하세여
#오름차순
data= [2,4,3,1,5,10,9]
data.sort()
print(data)
#내림차순
data.sort(reverse=True)
print(data)