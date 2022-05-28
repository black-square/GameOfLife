import numpy as np
import pi_star as d

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

def main():
    parser = RLEParser()
    bits = parser.parse( d.rle_string, d.width, d.height )

    if d.width == d.height and d.width % 2 == 0 and True:
        print( 'Cut top-left corner due to symmetry' )

        new_bits = []

        for y in range(d.height // 2):
            for x in range(d.width // 2):      
                new_bits.append( bits[y * d.width + x] ) 

        bits = new_bits
        d.width //= 2   
        d.height //= 2

    print( 'Total cells: {} [{} x {}]'.format(len(bits), d.width, d.height) )
    print( 'Alive cells: {}'.format(sum(bits)) )

    MAX_ARR_SIZE = 2000
    needComma = False

    with open('active_cells_out.txt', 'w') as f:
        n = 0
        for y in range(d.height):
            for x in range(d.width):           
                if bits[y * d.width + x]:
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

    with open('active_cells_logical_out.txt', 'w') as f:
        n = 0       
        for y in range(d.height):
            for x in range(d.width):           
                if bits[y * d.width + x]:
                    print('if( uv.x == {:3} && uv.y == {:3} ) return resOk; \\'.format(x, y), file=f )


    if len(bits) % 32 != 0:
        bits.extend([0]*(32 - len(bits) % 32))

    result = np.frombuffer(np.packbits(bits, bitorder='little').tobytes(), dtype=np.uint32)

    print( 'Bitmap size: {}'.format(len(result)) )

    with open('bitmask_out.txt', 'w') as f:
        n = 0
        for item in result:
            print('0x{:08X}u, '.format(item), end='', file=f )

            n += 1

            if n % 9 == 0:
                print('\\', file=f)

if __name__ == '__main__':
    main( )