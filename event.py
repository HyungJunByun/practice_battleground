from random import randint

MAX_LOCATION=100

def get_random_location(): #player의 랜덤한 위치를 튜플 형태로 반환
    x=randint(0,MAX_LOCATION)
    y=randint(0,MAX_LOCATION)
    return (x,y)

def battle(player_list):
    winneridx=randint(0,len(player_list)-1) #battle의 승리자 인덱스
    for i in range(len(player_list)):
        if i==winneridx:
            print('player %d, wins'%player_list[i].id)
            player_list[i].health+=10 #승리 플레이어의 체력 10증가
        else:
            player_list[i].health=0  #패배 플레이어의 체력 0으로 변경
            print('player %d, loses'%player_list[i].id)
