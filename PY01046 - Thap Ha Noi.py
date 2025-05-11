def tower_of_hanoi(n, src, aux, des):
    if n == 1:
        print(f"{src} -> {des}")
        return 
    tower_of_hanoi(n-1, src, des, aux)
    print(f"{src} -> {des}")
    tower_of_hanoi(n-1, aux, src, des)

n = int(input())
tower_of_hanoi(n, 'A', 'B', 'C')