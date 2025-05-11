# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
# Press the green button in the gutter to run the script.
import math
if __name__ == '__main__':
    n=int(input())
    for _ in range(n):
        a=input()
        sum=0
        res=1e9+10
        for i in a:
            if i.isdigit():
                sum=sum*10+(ord(i)-ord('0'))
            else:
                if sum!=0 :
                    res=min(sum,res)
                sum=0
        print(res)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/