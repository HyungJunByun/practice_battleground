import tkinter as tk
from game import Game
from map import get_safe_distance
from PIL import Image, ImageTk  # PIL 라이브러리 사용

# 게임 인스턴스 생성
game = Game(100)

# Tkinter 윈도우 설정
root = tk.Tk()
root.title("Battle Ground Game Visualization")

# 캔버스 설정
canvas_width, canvas_height = 800, 800
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="lightblue")
canvas.pack(padx=10, pady=10)

#이미지 설정
original_img = Image.open('mapimg.PNG')
resized_img = original_img.resize((canvas_width, canvas_height), Image.LANCZOS)
img = ImageTk.PhotoImage(resized_img)

# 맵 크기 및 스케일링 팩터 설정
map_size = 100
scale_factor = min(canvas_width, canvas_height) / map_size

# 게임 진행과 시각화 업데이트를 위한 함수
def update_game():
    game.time_goes_by()  # 게임 상태 업데이트
    canvas.delete("all")  # 캔버스를 클리어

    # 안전 지역 그리기
    safe_dist = get_safe_distance(game.global_time) * scale_factor
    target_x, target_y = game.map.target_location[0] * scale_factor, game.map.target_location[1] * scale_factor

    # 맵 이미지 띄우기
    canvas.create_image(0, 0, anchor='nw', image=img)

    canvas.create_oval(
        target_x - safe_dist, target_y - safe_dist,
        target_x + safe_dist, target_y + safe_dist,
        outline='blue', width=2)



    # 타겟 위치 그리기
    canvas.create_oval(
        target_x - 5, target_y - 5,
        target_x + 5, target_y + 5,
        fill='green')

    # 플레이어 위치 그리기
    for player in game.players:
        if player.status == 'alive':
            player_x, player_y = player.location[0] * scale_factor, player.location[1] * scale_factor
            canvas.create_oval(
                player_x - 3, player_y - 3,
                player_x + 3, player_y + 3,
                fill='red')
    if game.alive_players_count > 1:  # 게임이 계속 진행 중인 경우
        root.after(1000, update_game)  # 1초 후에 함수 재호출
    else:
        # 게임이 종료된 경우 Game Over 메시지 표시
        canvas.create_text(canvas_width // 2, canvas_height // 2, text="이겼닭! 오늘 저녁은 치킨이닭!", font=('Helvetica', 24, 'bold'), fill="yellow")
        root.after(5000, root.destroy)  # 2초 후에 윈도우 자동 닫기


# 게임 업데이트 시작
update_game()

# Tkinter 이벤트 루프 실행
root.mainloop()
