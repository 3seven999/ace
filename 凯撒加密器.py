_a = input("请输入要加密的内容:")
_b = input("请输入偏移量：")
for _c in _a:
    if "a"<=_c<="z":
        print(chr((ord(_c)-ord("a")+int(_b))%26+ord("a")),end="")
    elif"A"<=_c<="Z":
        print(chr((ord(_c)-ord("A")+int(_b))%26+ord("A")),end="")
    elif" "<=_c<="/":
        print(chr((ord(_c)-ord(" ")+int(_b))%16+ord(" ")), end="")
    elif"0"<=_c<="9":
        print(chr((ord(_c)-ord("0")+int(_b))%10+ord("0")), end="")
    elif":"<=_c<="@":
        print(chr((ord(_c)-ord("：")+int(_b))%7+ord("：")), end="")
    elif"["<=_c<="`":
        print(chr((ord(_c)-ord("[")+int(_b))%6+ord("[")), end="")
    elif"{"<=_c<="~":
        print(chr((ord(_c)-ord("{")+int(_b))%4+ord("{")), end="")



