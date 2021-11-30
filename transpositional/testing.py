import random as r
import encrypt as e
from essential_generators import DocumentGenerator

gen = DocumentGenerator()

def blackBox():
    nTests = r.randint(3, 15)
    passedTests = 0
    for i in range(0, nTests):
        msg = gen.sentence()
        rK = r.randint(5, 10)
        encMsg = e.encrypt(rK, msg)
        decMsg = e.decrypt(rK, encMsg[:-1])
        if msg == decMsg.strip():
            passedTests+=1
        else:
            print("Test number ", i+1, " failed. The key was ", rK, " and the msg was ", msg, " , encrypted as ", encMsg, " and decrypted as ", decMsg)
    print("Tests passed - ", passedTests, ", tests run - ", nTests)

blackBox()
