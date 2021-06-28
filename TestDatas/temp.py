# -!- coding: utf-8 -!-
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
c = "零 一 二 三 四 五 六 七 八 九".split(" ")
Chinese = {str(i):c[i] for i in range(10)}
a = [i for i in 17]
def change(a2):
    out = ''
    for i in range(len(a2)):
        if int(a2[i]) < 5:
            out += '5'
            return(i,out)
        out += a2[i]
    return('000',out)
b,out = change(a)
if b != '000':
    for i in range(b,len(a)):
        out += a[i]
else:
    out += '5'
temp = ''
for i in out:
    temp += Chinese[i]
print(temp)