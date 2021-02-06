boardState = []
for i in range(0,6):
    row = []
    for j in range(0,7):
        row.append(0)
    boardState.append(row)
print(boardState)

'''
0000000
0001200
0001111
0222000
0000000
0000000
'''

'''
for blue - 1
0000000
0000000
0001000
0001111
0000000
0000000
0000000
'''

'''
for yellow - 2
0000000
0000000
0000000
0000000
0111100
0000000
0000000
'''

def convert_bitboard(boardState):
    bitboard = '00000000000100000010000100000010000000000'
    bitboard = '00000000000000000010000001000010000010000'#new 
    0000001....1...1..0


    bitboard = int(bitboard,2)
    return boardState,bitboard
def check_4_horizontal(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>7)
    if temp &(temp>> 14):
        return True


bs,bb = convert_bitboard([])
print(bb)