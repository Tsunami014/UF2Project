from enum import Enum

class Flags(Enum):
    no_flags = 0
    """Should not exist, but added for completeness"""
    not_main_flash = 0x00000001
    """this block should be skipped when writing the device flash; it can be used to store "comments" in the file, \
typically embedded source code or debug info that does not fit on the device flash"""
    file_container = 0x00001000
    """Is a block of data which contains a file. For more info see https://github.com/microsoft/uf2?tab=readme-ov-file#file-containers"""
    familyID_present = 0x00002000
    """when set, the `fileSize/familyID` holds a value identifying the board family (usually corresponds to an MCU)"""
    MD5_checksum_present = 0x00004000
    """https://github.com/microsoft/uf2?tab=readme-ov-file#md5-checksum"""
    extension_tags_present = 0x00008000
    """https://github.com/microsoft/uf2?tab=readme-ov-file#extension-tags"""

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
        fs = int.from_bytes(data[8:12], byteorder='little')
        
        #if fs == 0:
        #    self.flags = Flags.no_flags
        if fs == 0x00000001:
            self.flags = Flags.not_main_flash
        elif fs == 0x00001000:
            self.flags = Flags.file_container
        elif fs == 0x00002000:
            self.flags = Flags.familyID_present
        elif fs == 0x00004000:
            self.flags = Flags.MD5_checksum_present
        elif fs == 0x00008000:
            self.flags = Flags.extension_tags_present
        else:
            raise ValueError(f'Unknown flag {fs}')
        self.address = data[12:16]
        self.size = int.from_bytes(data[16:20], byteorder='little') # Usually 256
        self.seq = int.from_bytes(data[20:24], byteorder='little')
        self.total = int.from_bytes(data[24:28], byteorder='little')
        self.file_size = int.from_bytes(data[28:32], byteorder='little') # File size or board family ID or zero
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
