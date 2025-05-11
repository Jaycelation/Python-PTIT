def time_to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

class LuongMua:
    def __init__(self, matram, tentram, trungbinh):
        self.matram = matram
        self.tentram = tentram.strip()
        self.trungbinh = trungbinh

    def __str__(self):
        return f"{self.matram} {self.tentram} {self.trungbinh:.2f}"

n = int(input().strip())  
tram_data = {} 

for i in range(n):
    tentram = input().strip()
    batdau = time_to_minutes(input().strip())
    ketthuc = time_to_minutes(input().strip())
    do = int(input().strip())

    thoigian = ketthuc - batdau

    if tentram in tram_data:
        tram_data[tentram][1] += do
        tram_data[tentram][2] += thoigian
    else:
        if i+1 < 10:
            tram_data[tentram] = [f"T0{i+1}", do, thoigian]
        else:
            tram_data[tentram] = [f"T{i+1}", do, thoigian]

luong_mua_list = []
for tentram, (matram, tong_mua, tong_thoi_gian) in tram_data.items():
    trungbinh = (tong_mua * 60) / tong_thoi_gian
    luong_mua_list.append(LuongMua(matram, tentram, trungbinh))

for tram in luong_mua_list:
    print(tram)
