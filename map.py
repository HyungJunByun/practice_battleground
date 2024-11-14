import event
from random import randint

def distance(loc1, loc2):
    return ((loc1[0]-loc2[0])**2+(loc1[1]-loc2[1])**2)**(1/2) #loc1과 loc2사이 거리 반환

def get_safe_distance(time):
    if time<=4:
        return 150 #처음에는 자기장이 없음
    elif time<=14:
        return 150-94/10*(time-4) #1단 자기장 이동
    elif time<=24:
        return 56 #1단 자기장
    elif time<=29:
        return 56-18/6*(time-24) #2단 자기장 이동
    elif time<=35:
        return 38 #2단 자기장
    elif time<=38:
        return 38-19/5*(time-35) #3단 자기장 이동
    elif time<=43:
        return 19 #3단 자기장
    elif time<=45:
        return 19-10/4*(time-43) #4단 자기장 이동
    elif time<=49:
        return 9 #4단 자기장
    elif time<=54:
        return 5 #5단 자기장
    elif time<=55:
        return 3 #6단 자기장
    elif time<=58:
        return 2 #7단 자기장
    elif time<=59:
        return 1 #8단 자기장
    else:
        return 0 #9단 자기장

class Map:
    def __init__(self):
        x = randint(10, 90)
        y = randint(10, 90)
        self.target_location=(x,y) #safe_zone의 중심. 2차원 좌표를 나타내는 튜플

    def safe_zone_effect(self, player_obj, time):
        dist=distance(self.target_location, player_obj.location)
        if dist>get_safe_distance(time): #safe_zone 밖에 있는 경우
            if time <= 4:
                player_obj.health -= 0  # 처음에는 자기장이 없음
            elif time <= 14:
                player_obj.health -= 12  # 1단 자기장 이동
            elif time <= 24:
                player_obj.health -= 12  # 1단 자기장
            elif time <= 29:
                player_obj.health -= 18  # 2단 자기장 이동
            elif time <= 35:
                player_obj.health -= 18  # 2단 자기장
            elif time <= 38:
                player_obj.health -= 24  # 3단 자기장 이동
            elif time <= 43:
                player_obj.health -= 24  # 3단 자기장
            elif time <= 45:
                player_obj.health -= 30  # 4단 자기장 이동
            elif time <= 49:
                player_obj.health -= 30  # 4단 자기장
            elif time <= 54:
                player_obj.health -= 90  # 5단 자기장
            elif time <= 55:
                player_obj.health -= 150  # 6단 자기장
            elif time <= 58:
                player_obj.health -= 240  # 7단 자기장
            elif time <= 59:
                player_obj.health -= 330  # 8단 자기장
            else:
                player_obj.health -= 420  # 9단 자기장