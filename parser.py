class File:
    def __init__(self, blocks):
        self.blocks = blocks
    
    def getAllData(self):
        d = []
        for i in self:
            d.extend(i.data)
        return d
    
    def compressBlocks(self):
        d = []
        for i in self:
            d.append(' 00 '.join(i.data))
        return d
    
    def __iter__(self):
        return iter(self.blocks)
    def __len__(self):
        return len(self.blocks)
    def __getitem__(self, it):
        return self.blocks[it]
    
    def __str__(self):
        return f'<File with {len(self.blocks)} blocks>'
    def __repr__(self): return self.__str__()

class Block:
    def __init__(self, data):
        self.flags = data[8+12]
        self.address = data[12:16]
        self.size = int.from_bytes(data[16:20], byteorder='little') # Usually 256
        self.seq = int.from_bytes(data[20:24], byteorder='little')
        self.total = int.from_bytes(data[24:28], byteorder='little')
        self.file_size = data[28:32]
        self.data = [i.strip() for i in data[32:32+self.size].hex(' ').split('00') if i.strip()]
    
    def __eq__(self, other):
        return self.data == other.data
    
    def __str__(self):
        return f'<Block {self.seq}/{self.total} @ {self.address.hex(" ")}: '+str(self.data).replace("'", "")+'>'
    def __repr__(self): return self.__str__()

def parseF(file):
    blocks = []
    d = 'Some data'
    with open(file, 'rb') as f:
        while f.readable() and d:
            d = f.read(512)
            if d:
                blocks.append(Block(d))
    return File(blocks)

if __name__ == '__main__':
    f = parseF('Sample uf2 files/arcade-test.uf2')
    pass
