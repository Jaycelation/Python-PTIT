
class Hoadon:
    def __init__(self, id, name, old, new):
        self.id = 'KH{:02d}'.format(id)
        self.name = name
        self.old = old
        self.new = new
        self.calc()
    def calc(self):
        val = self.new - self.old
        if val <= 50:
            self.total = val * 100
            self.total *= 1.02
        elif val <= 100:
            self.total = 50 * 100 + (val - 50) * 150
            self.total *= 1.03
        else:
            self.total = 50 * 100 + 50 * 150 + (val - 100) * 200
            self.total *= 1.05
        self.total = round(self.total)

    def __str__(self):
        return f'{self.id} {self.name} {self.total}'

listHD = []
for i in range(int(input())):
    name = input()
    old = int(input())
    new = int(input())

    listHD.append(Hoadon(i+1, name, old, new))

listHD.sort(key=lambda x : (-x.total))
print(*listHD, sep='\n')