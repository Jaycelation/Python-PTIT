class CaThi:
    def __init__(self, id, ngay, gio, phong):
        self.id = 'C{:03d}'.format(id) 
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
    
    def __str__(self):
        return f"{self.id} {self.ngay} {self.gio} {self.phong}"

def idate(date):
    res = date.split("/")
    x = ""
    for i in res[::-1]:
        x += i
        x += "/"
    return x[:-1]

ca_thi = []
with open("CATHI.in", 'r') as file:
    n = int(file.readline().strip())
    for i in range(n):
        ngay = file.readline().strip()
        gio = file.readline().strip()
        phong = file.readline().strip()

        ca_thi.append(CaThi(i+1, ngay, gio, phong))
    
    ca_thi.sort(key = lambda x : (idate(x.ngay), x.gio, x.id))

    print(*ca_thi, sep='\n')