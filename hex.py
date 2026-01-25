print( "\033c\033[40;37m\ngive the file .dat script to show ? ")
a=input()
#a="hello.dat"
f1=open(a,"rb")
b=f1.read()
f1.close()
counter=0
counter2=0
for h in b:
    if counter==8:
        counter=0
    if counter==0:
        f=hex(counter2)
        f=f[2:]
        

        f="00000000"+f
        
        o0=len(f)
        oa=o0-8
        f=f[oa:]
        
        print("\n"+f+" ",end="")
    p=chr(h)
    f=hex(h)
    f=f[2:]
    f="00"+f
    o0=len(f)
    oa=o0-2
    f=f[oa:]

    if h<32:
        p=" "    
    print(f+" "+p+" ",end="")
    counter=counter+1
    counter2=counter2+1