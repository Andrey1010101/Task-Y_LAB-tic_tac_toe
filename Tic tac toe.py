"""
Игра: «Обратные крестики-нолики».
"""
import random
import time

defeat = []
stop = False

def all_defeat():
    '''Генерация всех возможных, проигрышных комбинаций'''

    global defeat

    for i in range(6):
        defeat.append(board[i:50:11])
        defeat.append(board[10 + i:60:11])
        defeat.append(board[20 + i:70:11])
        defeat.append(board[30 + i:80:11])
        defeat.append(board[40 + i:90:11])
        defeat.append(board[50 + i:100:11])
    
        defeat.append(board[9 - i: 49: 9])
        defeat.append(board[19 - i: 59: 9])
        defeat.append(board[29 - i: 69: 9])
        defeat.append(board[39 - i: 79: 9])
        defeat.append(board[49 - i: 89: 9])
        defeat.append(board[59 - i: 99: 9])

        defeat.append(board[0 + i:5 + i])
        defeat.append(board[10 + i:15 + i])
        defeat.append(board[20 + i:25 + i])
        defeat.append(board[30 + i:35 + i])
        defeat.append(board[40 + i:45 + i])
        defeat.append(board[50 + i:55 + i])
        defeat.append(board[60 + i:65 + i])
        defeat.append(board[70 + i:75 + i])
        defeat.append(board[80 + i:85 + i])
        defeat.append(board[90 + i:95 + i])

    for i in range(60):
        defeat.append(board[0 + i:49 + i: 10])

def draw_board(board):
    """Визуализация игрового поля"""
    
    x = '|'
    print('\n')
    print('--|--|--|--|--|--|--|--|--|--|')
    for i in range(len(board)):
        if len(board[i]) == 1:
            x = ' |'
        else:
            x = '|'
        print(board[i] + x, end='')
        if i % 10 == 9:
            print('')
            print('--|--|--|--|--|--|--|--|--|--|')
    print('\n')
    
def bot (player_token):
    """Ход компьютера"""
    
    valid = False
    while not valid:
        motion = random.randint(0, 99)
        if str(board[motion]) not in "XO":
            time.sleep(1.5)
            board[motion] = player_token
            print('>>>>> Компьютер сделал ход на: ', motion)
            valid = True
            check_defeat(board, player_token)   

def take_input(player_token):
    """Ход игрока"""

    valid = False
    while not valid:
        try:
            player_answer = int(input(("Куда поставим " + player_token+"? ")))
            if player_answer >= 0 and player_answer <= 99:
                if str(board[player_answer]) not in "XO":
                    board[player_answer] = player_token
                    valid = True
                    check_defeat(board, player_token)
                else:
                    print("Эта клеточка уже занята")
            else:
                print("Некорректный ввод. Введите число от 0 до 99 чтобы походить.")
        except ValueError:
            print("Введите число от 0 до 99 чтобы сделать ход.")
            
def check_defeat(board, player_token):
    """Проверка проиграл ли игрок"""

    global defeat, stop
    
    finish = 1
    for i in defeat:
        for j in i:
            index = int(j)
            if board[index] != player_token:
                finish = 0
                break
            else:

                finish = finish + 1
                if finish == 5:
                    print('\n')
                    print('>>>>>>> Игрок ' + player_token + ' проиграл! <<<<<<<<<')
                    stop = True 
                    
def main(board,):
    """Определяем чей ход"""
    
    global stop    
    counter = 0
    
    while not stop:         
        draw_board(board)              
        if counter % 2 == 0:
            take_input("X")
        else:
            bot("O")
        counter += 1

def info():
    """Выводим на экран информацию о игре"""
    
    print('\nПриветствую вас в игре «Обратные крестики-нолики» на поле 10 x 10\
    \nс правилом «Пять в ряд» – проигрывает тот,у кого получился вертикальный,\
    \nгоризонтальный или диагональный ряд из пяти своих фигур (крестиков/ноликов).\
    \nX - всегда ходит первым!')

board = [str(num) for num in range(0, 100)] #Генерация игрового поля
   
info()
time.sleep(2)

all_defeat()

main(board)
