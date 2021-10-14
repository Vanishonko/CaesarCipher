import math

def encrypt(key_, inp):
    if key_*2 <= len(inp):
        outp = ''

        x = key_
        y = math.floor( ( len(inp) / key_ ) + 1)

        array = []
        curr = 0
        for x_ in range(y):
            array.append([])
            array[x_] = []
            for y_ in range(x):
                array[x_].append([])
                if curr < len(inp):
                    array[x_][y_] = inp[curr]
                else:
                    array[x_][y_] = ' '
                curr += 1


        curr = 0

        for y_ in range(x):
            for x_ in range(y):
                outp += array[x_][y_]
        return outp
    else:
        return "error. please have the key be less than half the message"

def decrypt(_k, _inp):
    newKey = math.floor ( ( len(_inp) / _k ) + 1)
    return encrypt(newKey, _inp)

def bruteforce(_inp):
    messages = []
    for i in range(int(len(_inp)/2)):
        messages.append(encrypt(i+1, _inp))
    return messages
        