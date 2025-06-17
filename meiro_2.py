from tkinter import*;import random

win = Tk()
cv = Canvas(win, width = 470,height = 470)
cv.pack()


#行と列用のリスト
grid_y=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,160,160,160,160,160,160,160,160,160,160,160,160,160,160,160,190,190,190,190,190,190,190,190,190,190,190,190,190,190,190,220,220,220,220,220,220,220,220,220,220,220,220,220,220,220,250,250,250,250,250,250,250,250,250,250,250,250,250,250,250,280,280,280,280,280,280,280,280,280,280,280,280,280,280,280,310,310,310,310,310,310,310,310,310,310,310,310,310,310,310,340,340,340,340,340,340,340,340,340,340,340,340,340,340,340,370,370,370,370,370,370,370,370,370,370,370,370,370,370,370,400,400,400,400,400,400,400,400,400,400,400,400,400,400,400,430,430,430,430,430,430,430,430,430,430,430,430,430,430,430]
grid_x=[10,40,70,100,130,160,190,220,250,280,310,340,370,400,430]*15
#壁用のリスト
kabe=[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1]

#柱(道になり得ないマス)のリスト
#pole=[32,34,36,38,40,42,62,64,66,68,70,72,92,94,96,98,100,102,122,124,126,128,130,132,152,154,156,158,160,162,182,184,186,188,190,192]

#色用のリスト[壁色,道色]
iro=["#ffffff","#7D7F93"]
#半端壁(壁にも道にもなれるマス)のリスト
#flex_cells=[33,35,37,39,41,47,49,51,53,55,57,63,65,67,69,71,77,79,81,83,85,87,93,95,97,99,101,107,109,111,113,115,117,123,125,127,129,131,137,139,141,143,145,147,153,155,157,159,161,167,169,171,173,175,177,183,185,187,189,191]

#後壁(外壁の内側1マス目)のリスト
#bkb=[19,21,23,25,61,91,121,151,73,103,133,163,199,201,203,205]

#内道(壁になり得ない、かつ外壁の内側2マス目以内のマス)のリスト
#rd=[48,50,52,54,56,78,80,82,84,86,108,110,112,114,116,138,140,142,144,146,168,170,172,174,176]

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


road_all={i:3 for i in range(0,225)}
all_cells=[i for i in range(0,225)]
#kabe_all=kabe+pole
replacable_cells={}
selected=0

#変われない道を設定
def set_kabe():
    global road_all, replacable_cells
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
        
    """
    #後壁
    num=[0,1,2,3]
    for a in range(4):
        b=random.choice(num)
        replace(bkb[4*a+b],1)
        num.remove(b)
    """

#盤面の作成

def make_maze():
    for i in range(0, 225):
        if road_all[i] == 2:
            paint(i, iro[1])
        elif road_all[i] == 3:
            paint(i, "#e1f8d9")
        else:
            paint(i, iro[0])

def base():
   #盤面
   b=0
   for a in kabe:
       paint(b,iro[a])
       b+=1


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

"""
    #半端壁生成
   for a in range(0,10):
       ll=[]
       k=[6,5,5,4,4,4,4,3,3,3,3,3,2,2,1,1,0]
       j=random.choice(k)
       
       ll=list(range(6))
       for b in range(j):
           c=random.choice(ll)
           d=flex_cells[6*a+c]
           replace(d,1)
           ll.remove(c)
"""
def check():
    c=0
    for a in pole:
        for b in range(4):
            c+=kabe[a+neighbor_cells[b]]
        if ((a/10)%2 == 0) and (c>=3):
            b=neighbor_cells[random.randint(0,3)]
            replace(a+b,0)

    #箱チェック
    check_cells(rd,4,1)

    #柱チェック
    check_cells(pole,3,1)

def check_cells(pole,q,r):
    for a in pole:
        c=0
        for b in range(4):
            c+=kabe[a+neighbor_cells[b]]
        if c>=q:
            d=neighbor_cells[random.randint(0,3)]
            replace(a+d,0)
        elif c==0:
            d=neighbor_cells[random.randint(0,3)]
            replace(a+d,r)
    
    
def replace(a,b):
    del kabe[a]
    kabe.insert(a,b)
    paint(a,iro[kabe[a]])
            

#指定したマス目を指定した色で塗りつぶす
def paint(a,b):
    cv.create_rectangle(
    grid_x[a],grid_y[a],grid_x[a]+30,grid_y[a]+30,
    fill=b)


def test_paint():
    for i in range(10):
        paint(flex_cells[i],"#ff0000")
main()