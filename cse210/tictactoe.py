# W01 Tic-Tac-Toe
# Author: Andrew Swayze


def main():

    boardArray = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
    }

    player = 'X'
    move_number = 0


    for i in range(10):
        boardDisplay(boardArray)
        print(f"{player}'s turn to choose a square (1-9): ")

        move = input()        

        boardArray[move] = player
        move_number += 1

        if move_number >= 5:
            if ((boardArray['1'] == boardArray['2'] == boardArray['3']) or
                (boardArray['4'] == boardArray['5'] == boardArray['6']) or
                (boardArray['7'] == boardArray['8'] == boardArray['9']) or
                (boardArray['1'] == boardArray['4'] == boardArray['7']) or
                (boardArray['2'] == boardArray['5'] == boardArray['8']) or
                (boardArray['3'] == boardArray['6'] == boardArray['9']) or
                (boardArray['1'] == boardArray['5'] == boardArray['9']) or
                (boardArray['3'] == boardArray['5'] == boardArray['7'])):
                print("\nGood Game. Thanks for playing!")                
                print(f"{player} won the game!\n") 
                break

        elif move_number == 9:
            print("Good game. Thanks for playing!")                
            print("It's a tie!")
            break

        if player =='X':
            player = 'O'
        else:
            player = 'X'        



def boardDisplay(boardArray):
    print(f"{boardArray['1']}|{boardArray['2']}|{boardArray['3']}")
    print('-+-+-')
    print(f"{boardArray['4']}|{boardArray['5']}|{boardArray['6']}")
    print('-+-+-')
    print(f"{boardArray['7']}|{boardArray['8']}|{boardArray['9']}")
    

if __name__ == "__main__":
    main()