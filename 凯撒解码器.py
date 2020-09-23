print('以3为偏移量的凯撒密码器解密器')
_a = input("请输入要解密的内容:")
for _c in _a:
    if "a"<=_c<="z":
        print(chr((ord(_c)-ord("a")-3)%26+ord("a")),end="")
    elif"A"<=_c<="Z":
        print(chr((ord(_c)-ord("A")-3)%26+ord("A")),end="")
    elif" "<=_c<="/":
        print(chr((ord(_c)-ord(" ")-3)%16+ord(" ")), end="")
    elif"0"<=_c<="9":
        print(chr((ord(_c)-ord("0")-3)%10+ord("0")), end="")
    elif":"<=_c<="@":
        print(chr((ord(_c)-ord("：")-3)%7+ord("：")), end="")
    elif"["<=_c<="`":
        print(chr((ord(_c)-ord("[")-3)%6+ord("[")), end="")
    elif"{"<=_c<="~":
        print(chr((ord(_c)-ord("{")-3)%4+ord("{")), end="")