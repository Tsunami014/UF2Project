b2i = lambda b: int.from_bytes(b, byteorder='little')

class Block:
    def __init__(self, data):
        self.flags = data[8+12]
        self.address = int.from_bytes(data[12:16], byteorder='little')
        self.size = int.from_bytes(data[16:20], byteorder='little') # Usually 256
        self.seq = int.from_bytes(data[20:24], byteorder='little')
        self.total = int.from_bytes(data[24:28], byteorder='little')
        self.file_size = data[28:32]
        self.data = [i.strip() for i in data[32:32+self.size].hex(' ').split('00') if i.strip()]
    
    def __str__(self):
        return f'Block: {self.seq}/{self.total} @ {self.address}: {self.data}'
    def __repr__(self): return self.__str__()

blocks = []
d = 'Some data'
with open('Sample uf2 files/arcade-test.uf2', 'rb') as f:
    while f.readable() and d:
        d = f.read(512)
        if d:
            blocks.append(Block(d))

pass