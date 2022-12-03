class VigenereCipher(object):
    def __init__(self, key, alphabet):
        pass
    
    def encode(self, text):
        pass
    
    def decode(self, text):
        pass

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

c.encode('codewars') # 'rovwsoiv'
c.decode('rovwsoiv') #, 'codewars'

c.encode('waffles') #, 'laxxhsj'
c.decode('laxxhsj') #, 'waffles'

c.encode('CODEWARS') #, 'CODEWARS'
c.decode('CODEWARS') #, 'CODEWARS'
