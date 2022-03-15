import random
import math

# symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '?', '!', ',', '"', '-', ':', ';', '@']
symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class solutions:
    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []
    H = []
    I = []
    J = []
    K = []
    L = []
    M = []
    N = []
    O = []
    P = []
    Q = []
    R = []
    S = []
    T = []
    U = []
    V = []
    W = []
    X = []
    Y = []
    Z = []

f = open("message.txt", "r")
msgToBeEncrypted = f.read()
f.close()
def generateRandomKey():
    symbols_ = symbols.copy()
    iterations = len(symbols_)
    newK = []
    while iterations > 0:
        newIndex = random.choice(symbols_)
        newK.append(newIndex)
        symbols_.pop(symbols_.index(newIndex))
        iterations = len(symbols_)
    return newK

keySet = generateRandomKey()
print(keySet)

def translateMessage(key_, msg_, mode):
    newMsg = ''
    if mode == 'encrypt':
        for i in msg_.lower():
            if i in symbols:
                newMsg += key_[symbols.index(i)]
            else:
                newMsg += i
    else:
        for i in msg_.lower():
            if i in symbols:
                newMsg += symbols[key_.index(i)]
            else:
                newMsg += i
    return newMsg
def encryptMessage(key_, msg_):
    return translateMessage(key_, msg_, 'encrypt')
def decryptMessage(key_, msg_):
    return translateMessage(key_, msg_, 'decrypt')

encrypted = encryptMessage(keySet, msgToBeEncrypted)

