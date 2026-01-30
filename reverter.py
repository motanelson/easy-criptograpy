print( "\033c\033[40;37m\give the file .txt reverter ? ")
a="vr.txt"
#a=input()
print( "\033c\033[40;37m\give the file .dat reverter ? ")
b="vr.dat"
#b=input()
f1=open(a,"r")
z=f1.read()
f1.close()
x=z.split("\n")
n=""
m=""
for y in x:
    n=""
    for g in y:
        n=g+n
    m=n+"\n"+m
f1=open(b,"w")
f1.write(m)
f1.close()

