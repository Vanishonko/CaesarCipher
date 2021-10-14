symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(key_, msg_, encrypting_):
    if not encrypting_:
        key_ = 26 - key_
    newMsg = ''
    for i in msg_:
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

def bruteforce(_msg):
    messages = []
    for i in range(1, 26):
        messages.append(encrypt(i, _msg, False))
    return messages
