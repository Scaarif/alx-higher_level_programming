def uppercase(str):
    for c in str:
        # is the char lowercase? if so, make it uppercase
        if ord(c) >= 97 and ord(c) <= 122:
            i = 65 + (ord(c) - 97)
        else:
            i = ord(c)
        print(f'{i:c}', end="")
    # new line at the end of str
    print()