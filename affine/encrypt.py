import math
symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(key_, msg_, encrypting_):
    k1 = math.floor(key_ / 100)
    k2 = key_ % 100
    if encrypting_:
        caesarMsg = caesar(k1, msg_, True)
        newMsg = multiplicative(k2, caesarMsg, True)
    else:
        multiplicativeMsg = multiplicative(k2, msg_, False)
        newMsg = caesar(k1, multiplicativeMsg, False)
    return newMsg

def caesar(key_, msg, encrypting_):
    if not encrypting_:
        key_ = 26 - key_
    newMsg = ''
    for i in msg:
        isInAlphabet = False
        currentLetter = i
        for j in symbols:
            if currentLetter.lower() == j:
                isInAlphabet = True
                break
        newSymb = currentLetter
        if isInAlphabet:
            for v in range(26):
                if currentLetter.lower() == symbols[v]:
                    k = v
                    break
            n = k + key_
            if n > 25:
                n -= 26
            newSymb = symbols[n]
            if currentLetter != currentLetter.lower():
                newSymb = newSymb.upper()
        newMsg += newSymb
    return newMsg

def multiplicative(key_, msg, encrypting_):
    newMsg = ''
    for i in msg:
        if i == ' ':
            newMsg += ' '
        else:
            curIndex = symbols.index(i) + 1
            newSym = symbols[ (curIndex * key_ % 26)]
            newMsg += newSym
    return newMsg

def bruteforce(_msg):
    messages = []
    for i in range(150, 10000):
        messages.append(encrypt(i, _msg, False))
    return messages
