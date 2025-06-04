class GameThu:
    def __init__(self, id, ten, gio, phut):
        self.id = id
        self.ten = ten
        self.gio = gio
        self.phut = phut

    def __str__(self):
        return f"{self.id} {self.ten} {self.gio} gio {self.phut} phut"
    
list = []
for i in range(int(input())):
    id = input()
    ten = input()
    x = input().split(":")
    gioX = int(x[0])
    phutX = int(x[1])
    y = input().split(":")
    time1 = gioX * 60 + phutX
    gioY = int(y[0])
    phutY = int(y[1])
    time2 = gioY * 60 + phutY
    time = time2 - time1
    gio = time // 60
    phut = time % 60
    
    list.append(GameThu(id, ten, gio, phut))

list.sort(key=lambda x : (-x.gio, -x.phut))
print(*list, sep="\n")