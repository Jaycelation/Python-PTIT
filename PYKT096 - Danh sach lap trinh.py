class ThiSinh:
    def __init__(self, id, ten, team_id, truong):
        self.id = 'C{:03d}'.format(id)
        self.ten = ten
        self.team_id = team_id
        self.truong = truong
    
    def __str__(self):
        return f"{self.id} {self.ten} {self.team_id} {self.truong}"

ds_theo_team = dict({})
ds_theo_truong = dict({})
list = []
for i in range(int(input())):
    id = 'Team{:02d}'.format(i+1)
    team_id = input().strip()
    truong = input().strip()
    ds_theo_team[id] = team_id
    ds_theo_truong[id] = truong

for i in range(int(input())):
    ten = input().strip()
    id = input().strip()
    team_id = ds_theo_team[id]
    truong = ds_theo_truong[id]

    list.append(ThiSinh(i+1, ten, team_id, truong))
list.sort(key=lambda x : x.ten)
print(*list, sep='\n')