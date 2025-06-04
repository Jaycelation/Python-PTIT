from math import sqrt
def khoang_cach(vector_x, vector_y):
    val = 0
    for i in range(len(vector_x)):
        val += (vector_x[i] - vector_y[i]) ** 2
    return sqrt(val)

def tich_vo_huong(vector_x, vector_y):
    val = 0
    for i in range(len(vector_x)):
        val += vector_x[i] * vector_y[i]
    return val


for _ in range(int(input())):
    vector_x = list(map(int, input().split()))
    vector_y = list(map(int, input().split()))
    print(f"{khoang_cach(vector_x, vector_y):.2f} {tich_vo_huong(vector_x, vector_y)}")