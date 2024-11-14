import event
import map
from random import randint

class Player:
    def __init__(self, ID):
        self.id=ID #플레이어 id. 정수형 숫자
        self.health=100 #플레이어 체력
        self.location=event.get_random_location()
        self.status='alive' #플레이어의 생존여부

    def run(self, target_location):
        if self.location[0]>target_location[0]: #x좌표가 타겟보다 더 큰 경우
            self.location=(self.location[0]-1, self.location[1]) #x방향 이동후 업데이트
        elif self.location[0]<target_location[0]: #x좌표가 타겟보다 더 작은 경우
            self.location=(self.location[0]+1, self.location[1]) #x방향 이동후 업데이트

        if self.location[1]>target_location[1]: #y좌표가 타겟보다 더 큰 경우
            self.location=(self.location[0], self.location[1]-1) #x방향 이동후 업데이트
        elif self.location[1]<target_location[1]: #y좌표가 타겟보다 더 작은 경우
            self.location = (self.location[0], self.location[1]+1)  # x방향 이동후 업데이트

    def status_update(self):
        if self.health<=0: #플레이어 체력이 0이하로 떨어져 사망한 경우
            self.status='dead'

    def __str__(self):
        return('player: %d, location: %s, health: %d, status: %s'%(self.id, self.location, self.health, self.status))