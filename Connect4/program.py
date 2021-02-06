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
'''
0000000
0000000
0000000
0000111
1110000
0000000
0000000

'''
#0000100000010000001000000000000100000010000001000
#0000000000010000001000000100000000000010000001000

#0000100000010000000000000000000000000000000000000
#0000000000010000001000000000000000000000000000000

#0000100000010000001000000000000000000000000000000
#0000000000010000001000000100000000000000000000000
#0000000000010000001000000000000000000000000000000

#0000100000010000001000000100000000000000000000000
#0000000000010000001000000100000010000000000000000
transposition_table = dict()
def convert_bitboard(boardState):
    for i in boardState:
        i.insert(0,0)
    boardState.insert(0,[0,0,0,0,0,0,0])
    bb_string_1 = ''
    bb_string_2 = ''
    board_state_num = 0
    for i in range(0,7):
        for j in range(0,7):
            ch = boardState[j][i]
            board_state_num =  board_state_num*10 + ch
            if(ch==0):
                bb_string_1+='0'
                bb_string_2+='0'
            if(ch==1):
                bb_string_1+='1'
                bb
            if(ch==2):
                bb_string_2+='1'
            
    bitboard_1 = int(bb_string_1,2)
    bitboard_2 = int(bb_string_2,2)
    
    return bitboard_1,bitboard_2,board_state_num
def checkHorizontalFour(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>7)
    if temp &(temp>> 14):
        return 50
def checkTLBRFour(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>6)
    if temp &(temp>> 12):
        return 50
def checkBLTRFour(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>8)
    if temp &(temp>> 16):
        return 50
def checkVerticalFour(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>1)
    if temp &(temp>> 2):
        return 50


def checkHorizontalThree(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>7)
    if temp>1:
        return 15
def checkTLBRThree(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>6)
    if temp>1:
        return 15
def checkBLTRThree(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>8)
    if temp>1:
        return 15
def checkVerticalThree(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>1)
    if temp>1:
        return 15


def checkHorizontalTwo(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>7)
    if temp>=1:
        return 5
def checkLDTwo(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>6)
    if temp>=1:
        return 5
def checkRDTwo(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>8)
    if temp>=1:
        return 5
def checkVerticalTwo(bitboard):
    temp = bitboard
    temp = (temp) &(temp>>1)
    if temp>=1:
        return 5

def evaluationFunction(bitboard_player_1,bitboard_palyer_2,coeff):
    fours_1 = checkHorizontalFour(bitboard_player_1)+checkTLBRFour(bitboard)+checkBLTRFour(bitboard)+checkVerticalFour(bitboard)
    threes_1 = checkHorizontalThree(bitboard_player_1)+checkTLBRThree(bitboard_player_1)+checkBLTRThree(bitboard_player_1)+checkVerticalThree(bitboard_player_1)
    two_1 = checkHorizontalTwo(bitboard_player_1)+checkLDTwo(bitboard_player_1)+checkRDTwo(bitboard_player_1)+checkVerticalTwo(bitboard_player_1)
    fours_2 = checkHorizontalFour(bitboard_player_2)+checkTLBRFour(bitboard_player_2)+checkBLTRFour(bitboard_player_2)+checkVerticalFour(bitboard_player_2)
    threes_2 = checkHorizontalThree(bitboard_player_2)+checkTLBRThree(bitboard_player_2)+checkBLTRThree(bitboard_player_2)+checkVerticalThree(bitboard_player_2)
    two_2 = checkHorizontalTwo(bitboard_player_2)+checkLDTwo(bitboard_player_2)+checkRDTwo(bitboard_player_2)+checkVerticalTwo(bitboard_player_2)
    SCORE = coeff*(fours_1+threes_1+two_1)+(-coeff)*(fours_2+threes_2+two_2)
    return SCORE


