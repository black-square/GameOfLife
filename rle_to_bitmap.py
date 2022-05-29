import numpy as np

class RepCount:
    def __init__(self):
        self.num_string = ''
    
    def push(self, c):
        self.num_string += c 

    def calc(self):
        rep = 1 if not self.num_string else int(self.num_string)
        self.num_string = ''
        return rep

# https://conwaylife.com/wiki/Run_Length_Encoded
class RLEParser:
    def __init__(self):
        self.repCount = RepCount()
        self.dfb_cur_str = ''
        self.bit_array = []
        self.x = 0
        self.y = 0

    def parse( self, rle_string, width, height):
        self.width = width
        self.height = height

        for c in rle_string:
            if c.isspace():
                continue

            self.dfb_cur_str += c

            if c.isdigit():
                self.repCount.push(c)
                continue

            if c == '$':
                self._finishLine( self.repCount.calc() )
                continue

            if c == '!':
                self._finishLine( self.height - self.y )
                assert( self.y == self.height )
                assert( len(self.bit_array) == self.width * self.height )
                return self.bit_array
                
            val = 1 if c == 'o' else 0 if c == 'b' else None
            rep = self.repCount.calc()

            assert( val is not None )

            self.bit_array.extend( [val] * rep )
            self.x += rep
            assert( self.x <= self.width )

    def _finishLine(self, rep):
        assert( self.x <= self.width )
        assert( self.y <= self.height )
        self.bit_array.extend( [0] * (self.width - self.x + (rep - 1) * self.width) )
        self.x = 0
        self.y += rep
        self.dfb_cur_str =''
        assert( self.x <= self.width )
        assert( self.y <= self.height )

def cutTopLeftCorner(bits, width, height):
    new_bits = []
    half_width, half_height = width // 2, height // 2

    for y in range(half_width):
        for x in range(half_height):      
            new_bits.append( bits[y * width + x] ) 
      
    return new_bits, half_width, half_height

def convertBitsToUint32List(bits):
    if len(bits) % 32 != 0:
        bits = bits + [0]*(32 - len(bits) % 32)

    return np.frombuffer(np.packbits(bits, bitorder='little').tobytes(), dtype=np.uint32)

def calcCompressedBitmap(data):
    index = []
    nodes = []
    node2index = {}

    for item in data:
        idx = node2index.get(item)

        if idx is None:
            idx = len(nodes)
            nodes.append(item)
            node2index[item] = idx
        
        index.append(idx)

    if len(index) % 32 != 0:
        index.extend([0]*(32 - len(index) % 32))

    packedIndex = np.frombuffer(bytearray(index), dtype=np.uint32)

    return packedIndex, nodes

def saveAsActveCellsList(bits, width, height):
    MAX_ARR_SIZE = 2000
    needComma = False

    with open('active_cells_out.txt', 'w') as f:
        n = 0
        for y in range(height):
            for x in range(width):           
                if bits[y * width + x]:
                    if n % MAX_ARR_SIZE == 0:
                        print('\n\n#define ACTIVE_CELLS{} '.format(n // MAX_ARR_SIZE), end='', file=f )
                        needComma = False
                 
                    if needComma:
                        print(', ', end='', file=f  ) 

                    if (n % MAX_ARR_SIZE) % 7 == 0:
                        print('\\', file=f)

                    print('ivec2({:3},{:3})'.format(x, y), end='', file=f )
                    #print('0x{:08X}u '.format((x % 256 << 8) | (y % 256)), end='', file=f )
                    needComma = True
                    n += 1

def saveAsActveCellsLogicOps(bits, width, height):
    with open('active_cells_logical_out.txt', 'w') as f:
        n = 0       
        for y in range(height):
            for x in range(width):           
                if bits[y * width + x]:
                    print('if( uv.x == {:3} && uv.y == {:3} ) return resOk; \\'.format(x, y), file=f )

def saveHexIntArray(data, file):
    n = 0
    needComma = False
    for item in data:
        if needComma:
            print(', ', end='', file=file  )

        if n % 9 == 0:
            print('\\', file=file) 

        print('0x{:08X}u'.format(item), end='', file=file )
        needComma = True
        n += 1

def saveAsBitmap(data):
    with open('bitmap_out.txt', 'w') as f:
        print('#define BITMAP ', end='', file=f )
        saveHexIntArray(data, f)

def saveCompressedBitmap(index, nodes):
    with open('bitmap_compressed_out.txt', 'w') as f:
        print('#define COMPRESSED_BITMAP_NODES ', end='', file=f )
        saveHexIntArray(nodes, f)
        print('\n\n#define COMPRESSED_BITMAP_INDEX ', end='', file=f )
        saveHexIntArray(index, f)

def main():
    import pi_star as d

    parser = RLEParser()
    bits = parser.parse( d.rle_string, d.width, d.height )

    if d.width == d.height and d.width % 2 == 0 and True:
        print( 'Cut top-left corner due to symmetry' )
        bits, d.width, d.height = cutTopLeftCorner(bits, d.width, d.height)

    print( 'Total cells: {} [{} x {}]'.format(len(bits), d.width, d.height) )
    print( 'Alive cells: {}'.format(sum(bits)) )

    saveAsActveCellsList(bits, d.width, d.height)
    saveAsActveCellsLogicOps(bits, d.width, d.height)

    words = convertBitsToUint32List(bits)

    print( 'Bitmap size: {}'.format(len(words)) )
    print( 'Bitmap unique elements: {}'.format(len(set(words))) )

    saveAsBitmap(words)
    pkIdx, pkNodes = calcCompressedBitmap(words)

    print( 'Packed bitmap size: [{} + {}]'.format(len(pkIdx), len(pkNodes)) )
    saveCompressedBitmap(pkIdx, pkNodes)

if __name__ == '__main__':
    main( )