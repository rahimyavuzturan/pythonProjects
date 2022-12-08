#klasik bir tictactoe oyunu

# tahtayı çiz

board = {'1' : ("-"),'2' : ("-"),'3' : ("-"),
         '4' : ("-"),'5' : ("-"),'6' : ("-"),
         '7' : ("-"),'8' : ("-"),'9' : ("-")}

#tahtanın durumunu fonksiyon ile belirt
def show_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

#x ve o için yazma fonksiyonu
def play_x(n):
    board[f'{n}'] = 'X'

def play_o(m):
    board[f'{m}'] = 'O'

#check finish fonksiyonu
def check_finish(board):
    isFinished = False
    if (board['1'] == board['2'] == board['3']) and board['1'] != '-':
        isFinished =  True
    elif (board['4'] == board['5'] == board['6']) and (board['4'] != '-'):
        isFinished =  True
    elif (board['7'] == board['8'] == board['9']) and (board['8'] != '-'):
        isFinished =  True
    elif (board['1'] == board['5'] == board['9']) and (board['5'] != '-'):
        isFinished =  True
    elif (board['7'] == board['5'] == board['3']) and (board['3'] != '-'):
         isFinished =  True
    elif (board['1'] == board['4'] == board['7']) and (board['4'] != '-'):
        isFinished =  True
    elif (board['2'] == board['5'] == board['8']) and (board['2'] != '-'):
        isFinished =  True
    elif (board['3'] == board['6'] == board['9']) and (board['3'] != '-'):
        isFinished = True
    else:
        isFinished = False
    return isFinished

#oyunu oynanabilir hale getir
print('1' + '|' + '2' + '|' + '3')
print('4' + '|' + '5' + '|' + '6')
print('7' + '|' + '8' + '|' + '9')

for i in range(10):
    if i%2 == 0:
        x = int(input("Please enter a slot for x = "))
        if board[f'{x}'] == '-':
            play_x(x)
            show_board(board)
            if check_finish(board) == 1:
                print("***** X KAZANDI *****")
                break
            else:
                pass
        else:
            x = int(input("yazdığınız slot oynanmış lütfen farklı slot seçin"))
            play_x(x)
            show_board(board)
            if check_finish(board) == 1:
                print("***** X KAZANDI *****")
                break
            else:
                pass
    elif i%2 == 1:
        if i == 9:
            print("it is a tie")
        else:
            o = int(input("Please enter a slot for o = "))
            if board[f'{o}'] == '-':
                play_o(o)
                show_board(board)
                if check_finish(board) == 1:
                    print("***** O KAZANDI *****")
                    break
                else:
                    pass
            else:
                o = int(input("yazdığınız slot oynanmış lütfen farklı slot seçin"))
                play_o(o)
                show_board(board)
                if check_finish(board) == 1:
                    print("***** O KAZANDI *****")
                    break
                else:
                    pass