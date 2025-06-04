lst_car = {}
fee_car = {
    ("Xe_con", 5): 10000,
    ("Xe_con", 7): 15000,
    ("Xe_tai", 2): 20000,
    ("Xe_khach", 29): 50000,
    ("Xe_khach", 45): 70000
}

def tinh(loai, so_ghe):
    x = fee_car.get((loai, so_ghe), 0)
    return x

for _ in range(int(input())):
    lc = list(input().split())
    bien_so = lc[0]
    loai = lc[1]
    so_ghe = int(lc[2])
    tt = lc[3]
    ngay = lc[4]
    if tt != 'OUT':
        phi = tinh(loai, so_ghe)
        if ngay in lst_car:
            lst_car[ngay] += phi
        else:
            lst_car[ngay] = phi

for ngay, tong_phi in lst_car.items():
    print(f"{ngay}: {tong_phi}")
