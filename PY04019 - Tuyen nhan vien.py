class NhanVien:
    def __init__(self, id, name, score):
        self.id = 'TS0{}'.format(id)
        self.name = name 
        self.score = score

    def status(self):
        if self.score > 9.5:
            return 'XUAT SAC'
        if self.score >= 8:
            return 'DAT'
        if self.score >= 5:
            return 'CAN NHAC'
        return 'TRUOT'
    
    def __str__(self):
        return f'{self.id} {self.name} {self.score:.2f} {self.status()}'

listNV = []
for i in range(int(input())):
    name = input()
    scoreLt = float(input())
    scoreTh = float(input())
    scoreLt /= 10 if scoreLt > 10 else 1
    scoreTh /= 10 if scoreTh > 10 else 1
    score = (scoreLt + scoreTh) / 2
    listNV.append(NhanVien(i + 1, name, score))

listNV.sort(key=lambda x: -x.score)
print(*listNV, sep='\n')
