text="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ftext = "SVOOL#R#ZN#HLFIZE#ILB#.#ZMW#R#ZN#Z#HGFWVMG#LU#XOZHH#+"
text2="abcdefghijklmnopqrstuvwxyz"
def sys(z):
    if z=="a":
        z=text[25]
    elif z=="b":
        z=text[24]
    elif z=="c":
        z=text[23]   
    elif z=="d":
        z=text[22]
    elif z=="e":
        z=text[21]
    elif z=="f":
        z=text[20]
    elif z=="g":
        z=text[19]
    elif z=="h":
        z=text[18]
    elif z=="i":
        z=text[17]
    elif z=="j":
        z=text[16]
    elif z=="k":
        z=text[15]
    elif z=="l":
        z=text[14]
    elif z=="m":
        z=text[13]
    elif z=="n":
        z=text[12]
    elif z=="o":
        z=text[11]
    elif z=="p":
        z=text[10]
    elif z=="q":
        z=text[9]
    elif z=="r":
        z=text[8]
    elif z=="s":
        z=text[7]
    elif z=="t":
        z=text[6]
    elif z=="u":
        z=text[5]
    elif z=="v":
        z=text[4]
    elif z=="w":
        z=text[3]
    elif z=="x":
        z=text[2]
    elif z=="y":
        z=text[1]
    elif z=="z":
        z=text[0]
    elif z=="A":
        z=text2[25]
    elif z=="B":
        z=text2[24]
    elif z=="C":
        z=text2[23]   
    elif z=="D":
        z=text2[22]
    elif z=="E":
        z=text2[21]
    elif z=="F":
        z=text2[20]
    elif z=="G":
        z=text2[19]
    elif z=="H":
        z=text2[18]
    elif z=="I":
        z=text2[17]
    elif z=="J":
        z=text2[16]
    elif z=="K":
        z=text2[15]
    elif z=="L":
        z=text2[14]
    elif z=="M":
        z=text2[13]
    elif z=="N":
        z=text2[12]
    elif z=="O":
        z=text2[11]
    elif z=="P":
        z=text2[10]
    elif z=="Q":
        z=text2[9]
    elif z=="R":
        z=text2[8]
    elif z=="S":
        z=text2[7]
    elif z=="T":
        z=text2[6]
    elif z=="U":
        z=text2[5]
    elif z=="V":
        z=text2[4]
    elif z=="W":
        z=text2[3]
    elif z=="X":
        z=text2[2]
    elif z=="Y":
        z=text2[1]
    elif z=="Z":
        z=text2[0]
    elif z==" ":
        z="#"
    elif z=="1":
        z="@"
    elif z=="2":
        z="$"
    elif z=="3":
        z="%"
    elif z=="4":
        z="^"
    elif z=="5":
        z="&"
    elif z=="6":
        z="*"
    elif z=="7":
        z="-"
    elif z=="8":
        z="+"
    elif z=="9":
        z="?"
    elif z=="0":
        z="!"
    elif z=="#":
        z=" "
    elif z=="@":
        z="1"
    elif z=="$":
        z="2"
    elif z=="%":
        z="3"
    elif z=="^":
        z="4"
    elif z=="&":
        z="5"
    elif z=="*":
        z="6"
    elif z=="-":
        z="7"
    elif z=="+":
        z="8"
    elif z=="?":
        z="9"
    elif z=="!":
        z="0"
    else:
        z=z
    return z


def encoder(ftext):
    new = ""
    x=len(ftext)
    for y in range(0,x):
        
        z=ftext[y]
        c=sys(z)
        new = new+c
    return new 
xx = encoder(ftext)
print(xx)