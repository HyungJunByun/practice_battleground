import player
import map
import event
from random import randint

class Game:
    def __init__(self, num_player):
        self.num_player=num_player #게임에 참여하는 플레이어 수, 정수형 데이터
        self.players=[] #player 클래스의 객체들을 아이템으로 하는 리스트
        for i in range(self.num_player):
            self.players.append(player.Player(i)) #각 플레이어 객체 생성
        self.map=map.Map()
        self.global_time=0
        self.alive_players_count=self.num_player #생존 플레이어 수
    def __str__(self):
        return('global time: %s, target_location: %s'%(self.global_time, self.map.target_location))


    def time_goes_by(self):
        self.global_time += 1  # global_time 1증가

        maxvar = int(map.get_safe_distance(self.global_time))  #var의 최댓값. 정수를 취해준다

        for player in self.players:
            if player.status == 'alive':
                x_var = randint(-maxvar, maxvar)
                y_var = randint(-maxvar, maxvar)
                #player_target_x값 정하기. 0~100안에서
                if (self.map.target_location[0]+x_var<=100) and (self.map.target_location[0]+x_var>=0):
                    player_target_x=self.map.target_location[0]+x_var
                elif self.map.target_location[0]+x_var>100:
                    player_target_x=100
                else:
                    player_target_x =0
                #player_target_y값 정하기. 0~100안에서
                if (self.map.target_location[1]+y_var<=100) and (self.map.target_location[1]+y_var>=0):
                    player_target_y=self.map.target_location[1]+y_var
                elif self.map.target_location[1]+y_var>100:
                    player_target_y=100
                else:
                    player_target_y =0
                player_target_location=(player_target_x, player_target_y) #player만의 새로운 타겟 로케이션
                player.run(player_target_location)
                self.map.safe_zone_effect(player, self.global_time)
                player.status_update()
                print(player)

        battle_groups=[] #생존, 같은 위치인 생존자들의 이차원 리스트
        #battle_groups 리스트 생성
        for player in self.players: #모든 플레이어중
            if player.status == 'alive': #살아있는 플레이어에 대해
                if len(battle_groups)==0: #battle_players리스트 길이가 0이라면
                    battle_groups.append([player]) #새 플레이어 리스트를 추가
                else: #battle_players리스트 길이가 0이 아니라면
                    for i in range(len(battle_groups)): #위치가 같은 플레이어 그룹이 이미 있는지 탐색
                        if battle_groups[i][0].location==player.location: #있다면
                            battle_groups[i].append(player) #그 그룹에 추가하고
                            break #탐색중단
                        if i==len(battle_groups)-1: #없어서 끝까지 탐색했다면
                            battle_groups.append([player]) #새 플레이어 리스트를 추가
        battle_groups=[group for group in battle_groups if len(group)>1] #2명이상이 같은 장소에 있는 유의미한 그룹만 남김

        if len(battle_groups)>0: #싸움이 일어나는 경우
            print('battles between players!')
            for group in battle_groups:
                event.battle(group) #각 그룹별 전투 실행
                for player in group:
                    player.status_update() #전투 후 생존여부 업데이트

        self.alive_players_count=0 #생존자 수 카운팅을 위해 생존자 수 초기화
        for player in self.players:
            if player.status=='alive':
                self.alive_players_count+=1

        print(self.__str__())
        print('=====================================')
        if self.alive_players_count==1: #게임이 끝나는 경우
            for player in self.players:
                if player.status=='alive':
                    print('Game over. Final player details:')
                    print('player: %d, location: %s, health: %d, status: %s'%(player.id, player.location, player.health, player.status))









