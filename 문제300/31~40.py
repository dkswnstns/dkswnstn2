#31 예상: : 문자끼리는 더하기 할수 없고 연결된다
a="3"#문자 [ " " 안에 있으면 문자]
b="4"# 문자
print( int(a) + int(b))

#32문제 32: 예상 : 문자와 숫자끼리는 연산 할구 없다 하지만 곱은 문자의 배로 출력
print("hi"*3)

#33
print("-"*80)

#34
t1="python"
t2="java"
t3= t1 +" "+t2+" " # 문자끼리 + 로 연결
print(t3*4)        # 문자 반복 * 사용

#35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
        # 이름: 김민수 나이:10
print("이름 : %s나이:%d"%(name1,age1) )
print("이름:%s 나이 : %d"%(name2,age2))

#문제 36 format() 함수 사용
        # {} 안에 들어갈 데이터를 format 함수 안에 넣기
name1="김민수"
age1=10
name2="일철희"
age2=13
print("이름 :{}나이:{}".format(name1,age1))
print("이름:{} 나이 : {}".format(name2,age2))

#37
name1="김민수"
age1=10
name2="일철희"
age2=13
print(f"이름: {name1} 나이 : {age1}")
print(f"이름: {name2} 나이 : {age2}")

#문제 38
상장주식수 = "5,969,782,5550"
컴마제거 = 상장주식수.replace(",","" )
타입변환 = int(컴마제거)
print(타입변환)

# 문제 39
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7] )

#문제 40
data= "             삼성전자            "
공백제거=data.strip( )
print(공백제거)