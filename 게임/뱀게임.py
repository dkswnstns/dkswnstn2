import pygame
from pygame.locals import QUIT , Rect ,KEYDOWN ,K_UP, K_LEFT ,K_RIGHT , K_DOWN
                # 종료 , 그리기 , 키눌렀을떄 , 위키, 왼쪽키 , 오른쪽키 , 아래키
import random# 렌던 파일 불러오기
import sys # 시스텝 파일 불러오기

#2. 게임에 필요한 기본설정
pygame.init() #파이게임 초기값
화면= pygame.display.set_mode((1000,1000)) #화면구성
프레임 = pygame.time.Clock()   #프레임에 파이게임 시간 설정
#Frame Per Second : FPS : 초당 프레임[정지사진 ] 수

음식=[] #여러개 음식을 저장할 리스트
뱀=[] #여러개 뱀꼬리를 저장할 리스트
(가로,세로)=(50,50) # 가로길이 세로길이 #튜플선언

    #배경 넣기
배경= pygame.image.load("i14056713388.jpg")

        #배경 소리 넣기
pygame.mixer.music.load("music.mp3")


#함수 만들기
#1.음식함수 2.음식 이동함수 3.그리기 함수
def 음식생성( ):
    while True:
        위치 = (random.randint(0,가로-1),random.randint(0,세로-1))
        if 위치 in 음식 or 위치 in 뱀 :
             continue # while 다시실행
        else:
            음식.append(위치)#음식리스트에 위치 추가
            break

#2. 음식 이동 함수 : 뱀이 음식을 먹었을떄
def 음식이동(위치):
    임의변수=음식.index(위치) #해당 위치에 음식 찾기
    del 음식[임의변수] #해당 위치에 음식 삭제
    음식생성( ) # 음식생성 함수 호출 [세로운 음식 생성]

    #3.그리기 함수
def 그리기( 점수판,게임종료):


    #음식 그리기
    for food in 음식 : # 리스트내 갯수만큼 반복
        pygame.draw.ellipse(화면,(0,255,0),Rect(food[0]*20 , food[1]*20 ,20,20))
                #타원그리기(화면이름,칼라[RGB]),타원(x축,y축,가로크기, 세로크기)

    # 뱀그리기
    for body in 뱀: #리스트내 갯수만큼 반복
        pygame.draw.rect(화면,(0,255,255),Rect(body[0]*20,body[1]*20,20,20))


    # 점수 그리기
    if 점수판 !=None : # 점수판 에 내용이 있으면
        화면.blit(점수판,(10,10)) # x 좌표 y 좌표에 표기

    # 종료메세지 그리기
    if 게임종료: # 게임종료 메세지가 내용이 있응면
        게임종료메세지= my글꼴.render("게임 종료[획득점수는:"+str(점수)+"]",True , (255,255,255))
        화면.blit(게임종료메세지, (300, 500))  # x 좌표 y 좌표에 표기

    pygame.display.update()

# 4. 게임실행
my글꼴=pygame.font.SysFont("malgungothic",30) # 글꼴, 글자크기
키 = K_DOWN#아래키
게임종료= False#게임종료 그위치
뱀.append((int(세로/2),int(가로/2) ) ) #뱀을 하면 가운데 위치
점수=0
게임종료메세지=0
for i in range(30) : #30개의 음식 생성
    음식생성()

while True: # 계속 반복하기
    화면.blit(배경,(0,0))
    #키보드 동작하기
    for 동작 in pygame.event.get( ) : # 파이게임 이벤트 [동작] 있을경우
        if 동작.type == QUIT : # 이벤트가 종료이면
            pygame.quit()#파이게임 종료
            sys.exit( ) #시스템[모든코드] 종료
        elif 동작.type == KEYDOWN : # 키를 눌렀을때
            키 = 동작.key

    # 키를 눌렀을떄
    if not 게임종료 : # 게임종료가 false 이면
        if 키 == K_LEFT :
            머리=(뱀[0][0]-1  ,뱀[0][1])
        elif 키 == K_RIGHT :
            머리 = (뱀[0][0] +1, 뱀[0][1])
        elif 키 == K_UP:
            머리 = (뱀[0][0] , 뱀[0][1]-1)
        elif 키 == K_DOWN :
            머리 = (뱀[0][0], 뱀[0][1]+1)

        # 뱀 몽에 닿았을때 혹은 화면 밖으로 낚을때 게임 종료
        if 머리 in 뱀 or 머리[0] < 0 or 머리[0] >= 세로 or 머리[1] < 0 or 머리 [1] >=가로 :
            게임종료=True

        # 뱀 머리 추가
        뱀.insert( 0 , 머리 )

        #음식을 먹었을때 꼬리 추가 아님 추가 x
        if 머리 in 음식 : # 만약에 머리가 음식에 닿았을떄
            음식이동(머리 )#새로운 음식 추가
            #1점 추가
            점수 += 1
        else:#음식을 못 먹었으면
            뱀.pop() #리스트내 가장 뒤에있는 항목 제거

        점수판 = my글꼴.render("[획득점수는:" + str(점수) + "]", True , (255, 255, 0))

    그리기(점수판,게임종료)
    프레임.tick(5)