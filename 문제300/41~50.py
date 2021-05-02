#41 : upper() 함수 : 대문자로 변환 해주는 함수
ticker="btc_krw"
print(ticker.upper() )

#42 : lower()함수 : 소문자로 변환 해주는 함수
ticker="btc_krw"
print(ticker.lower())

#43
ticker="btn_krw"
print(ticker.capitalize())

#44
file_name="보고서.xlsx" # 엑셀 파일
print(file_name.endswith("xlsx"))

#45
file_name="보고서.xlsx"
print(file_name.endswith(("xlsx")))

#46
file_name="2020_보고서.xlsx"
print(file_name.startswith("2020"))

#47
a="hello world"
print(a.split())

#48
ticker="btc_krw"
print(ticker.split("-"))

#49
date="2020-05-01"
print(date.split("-"))
#50
data="039490      "
print(data.split())