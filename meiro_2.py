from tkinter import*;import random

win = Tk()
cv = Canvas(win, width = 470,height = 470)
cv.pack()

#行と列用のリスト
grid_y=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,160,160,160,160,160,160,160,160,160,160,160,160,160,160,160,190,190,190,190,190,190,190,190,190,190,190,190,190,190,190,220,220,220,220,220,220,220,220,220,220,220,220,220,220,220,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,280,280,280,280,280,280,280,280,280,280,280,280,280,280,280,310,310,310,310,310,310,310,310,310,310,310,310,310,310,310,340,340,340,340,340,340,340,340,340,340,340,340,340,340,340,370,370,370,370,370,370,370,370,370,370,370,370,370,370,370,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,430,430,430,430,430,430,430,430,430,430,430,430,430,430,430]
grid_x=[10,40,70,100,130,160,190,220,250,280,310,340,370,400,430]*15
#壁用のリスト
kabe=[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1]

#色用のリスト[壁色,道色]
iro=["#ffffff","#7D7F93"]

#壁を選ぶ用リスト
neighbor_cells=[-1,1,-15,15]

#盤面の状態を表すラベル
STATE_LABELS = {
    0: '通路',
    1: '正解道',
    2: '変われない壁',
    3: '付けたしの壁'
}

tate=0;yoko=0
move_down=0;move_right=0;move_up=0;move_left=0
selected=0

road_all={i:3 for i in range(0,225)}

#変われない道を設定
def set_kabe():
    global road_all
    for i in range(len(kabe)):
        if kabe[i] == 1:
            road_all[i] = 2

def main():
    global kabe, grid_x, grid_y
    set_kabe()
    print(road_all)
    correct_road()  #正解道を作成
    make_maze()  #迷路を作成

    win.mainloop()

def make_maze():
    for i in range(0, 225):
        if road_all[i] == 2:
            paint(i, iro[1])
        elif road_all[i] == 3:
            paint(i, "#e1f8d9")
        else:
            paint(i, iro[0])

def correct_road():
    global selected, tate, yoko, move_down, move_right, road_all, move_up, move_left
    tate=12; yoko=12
    
    #初期位置を16マス目とする
    selected=16
    road_all[selected]=1
    while tate!= 0 and yoko != 0:    #下にも右にも進めなくなるまで
        if tate > 0 and yoko > 0:   #下にも右にも進める時
            move_down = random.randint(2,tate)  #ランダムで下に進むマス数を決める            
            if move_down%2 == 0:  #下に進むマス数が偶数の時
                for i in range(1,move_down+1):  #1マスずつ下に進む
                    selected += 15  #1マス下に進む
                    road_all[selected] = 1
                    print("下に進む")
                #move_down = 0分下に進む
            else:
                move_down += 1
                for i in range(1,move_down+1):  #1マスずつ下に進む
                    selected += 15  #1マス下に進む
                    road_all[selected] = 1
                    print("下に進む")
            tate -= move_down   #まだ進めるマス数を減らす
            
            move_right = random.randint(2,yoko)
            if move_right%2 == 0:
                for i in range(1,move_right+1):
                    selected += 1  #1マス右に進む
                    road_all[selected] = 1
                    print("右に進む")
            #move_right = 0分右に進む
            else:
                move_right += 1
                for i in range(1,move_right+1):
                    selected += 1  #1マス右に進む
                    road_all[selected] = 1
                    print("右に進む")
            yoko -= move_right
        if yoko <= 0:  #下には進めるが右には進めない時
            for _ in range(1,tate+1):
                selected += 15
                road_all[selected] = 1
                print("下に進む")
            tate = 0
        elif tate <= 0:  #右には進めるが下には進めない時
            for _ in range(1,yoko+1):
                selected += 1
                road_all[selected] = 1
                print("右に進む")
            yoko = 0
    print(f"tate:{tate}, yoko:{yoko}, selected:{selected}")

#指定したマス目を指定した色で塗りつぶす
def paint(a,b):
    cv.create_rectangle(
    grid_x[a],grid_y[a],grid_x[a]+30,grid_y[a]+30,
    fill=b)

main()