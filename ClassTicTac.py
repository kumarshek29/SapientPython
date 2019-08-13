from random import *
from time import *


class Play:
    def __init__(self):
        print("Menu: ")
        print("1 - Play Single Player, against the Computer")
        print("2 - Play Multiplayer with a friend on the same computer")
        print("3 - Do not play at all, let computer play with itself :)")
        Play.Choice = input("Please Enter your Choice: ")
        while Play.Choice not in ['1','2','3']:
            Play.Choice = input("Please type 1,2 or 3 as your Choice: ")
        if Play.Choice == '1':
            Play.GameType = "S"
        elif Play.Choice == '2':
            Play.GameType = "M"
        else:
            print("\nComputer v Computer it is...\n") 
            Play.GameType = "Computer v Computer" 
        Board()
        Play.Type = choice(['X','O'])
        Play.Round()


        if Play.GameWon == True:
            print(Play.WinningType, "Wins!")
        else:
            print("Draw!")
        PlayAgain = input("Do you want to play again? Y/es or N/o: ")
        if PlayAgain in ["Yes", "yes", "y", "Y"]:
            print()
            Play()

    def Round():
        Play.GameWon = False
        while not Play.GameWon:
            if Play.GameType in ["S","M"]:
                Play.Move()
                Play.CheckWin()
                Play.ChangeType()
            if Play.GameType != "M" and Play.GameWon == False:
                print(Play.Type+"'s Go...")
                sleep(1)
                Computer.GetComputersChoice()
                Play.CheckWin()
                Play.ChangeType()

    def Move():
        Play.VerifyPosition()
        Board.PrintBoard()

    def ChangeType():
        if Play.Type == 'X':
            Play.Type = 'O'
        else:
            Play.Type = 'X'

    def VerifyPosition():
        Valid = False
        print(Play.Type+"'s Go...")#O's Go... / X's Go...
        while not Valid:
            Position = input("Please type where you wish to place: ")
            while Position.isdigit() == False or int(Position) > 9 or int(Position) <= 0:
                Position = input("Please type a valid integer between 1 and 9: ")
            Play.Position = int(Position)
            if Board.Places[Play.Position-1] == 'X' or Board.Places[Play.Position-1] == 'O':
                Valid = False
                print("That is an invalid square, please try again ")
            else:
                Valid = True
        Board.Places[Play.Position-1] = Play.Type

    def CheckWin():
        if ((Board.Places[0]== Play.Type) and (Board.Places[1] == Play.Type) and (Board.Places[2] == Play.Type)) or (
            (Board.Places[3]== Play.Type) and (Board.Places[4] == Play.Type) and (Board.Places[5] == Play.Type)) or (
            (Board.Places[6]== Play.Type) and (Board.Places[7] == Play.Type) and (Board.Places[8] == Play.Type)) or (
            (Board.Places[0]== Play.Type) and (Board.Places[3] == Play.Type) and (Board.Places[6] == Play.Type)) or (
            (Board.Places[1]== Play.Type) and (Board.Places[4] == Play.Type) and (Board.Places[7] == Play.Type)) or (
            (Board.Places[2]== Play.Type) and (Board.Places[5] == Play.Type) and (Board.Places[8] == Play.Type)) or (
            (Board.Places[0]== Play.Type) and (Board.Places[4] == Play.Type) and (Board.Places[8] == Play.Type)) or (
            (Board.Places[2]== Play.Type) and (Board.Places[4] == Play.Type) and (Board.Places[6] == Play.Type)):
            Play.WinningType = Play.Type
            Play.GameWon = True
        if Play.GameWon != True:
            DrawCheck = 0
            for i in range(0,9):
                if Board.Places[i] == ' ':
                    DrawCheck = DrawCheck + 1
            if DrawCheck == 0:
                Play.GameWon = 'Draw'

class Computer:
    def GetComputersChoice():
        Computer.FindEmptySpaces()
        Computer.ComputerMove()
        Board.PrintBoard() # Prints the Board

    def FindEmptySpaces():
        Computer.EmptySpaces = []
        for i in range(0,9):
            if Board.Places[i] == ' ':
                Computer.EmptySpaces.append(i)

    def ComputerMove():
        Computer.Change = False
        OriginalType = Play.Type 
        for j in range(0,2):
            for i in range(0,len(Computer.EmptySpaces)):
                if not Computer.Change: 
                    Computer.CheckComputerWin((Computer.EmptySpaces[i])) 
                if Computer.Change:    
                    Board.Places[Computer.EmptySpaces[i]] = OriginalType 
                    Play.Type = OriginalType
                    return
            Play.ChangeType()
        Play.Type = OriginalType
        Board.Places[choice(Computer.EmptySpaces)] = OriginalType

    def CheckComputerWin(SpaceToCheck):
        if (SpaceToCheck in [6,3,0] and Board.Places[SpaceToCheck + 1] == Play.Type and Board.Places[SpaceToCheck + 2] == Play.Type) or (
            SpaceToCheck in [7,4,1] and Board.Places[SpaceToCheck + 1] == Play.Type and Board.Places[SpaceToCheck - 1] == Play.Type) or (
            SpaceToCheck in [8,5,2] and Board.Places[SpaceToCheck - 1] == Play.Type and Board.Places[SpaceToCheck - 2] == Play.Type) or (
            SpaceToCheck in [6,7,8] and Board.Places[SpaceToCheck - 3] == Play.Type and Board.Places[SpaceToCheck - 6] == Play.Type) or (
            SpaceToCheck in [5,4,3] and Board.Places[SpaceToCheck - 3] == Play.Type and Board.Places[SpaceToCheck + 3] == Play.Type) or (
            SpaceToCheck in [2,1,0] and Board.Places[SpaceToCheck + 3] == Play.Type and Board.Places[SpaceToCheck + 6] == Play.Type) or (
            SpaceToCheck == 0 and Board.Places[SpaceToCheck + 4] == Play.Type and Board.Places[SpaceToCheck + 8] == Play.Type) or ( 
            SpaceToCheck == 2 and Board.Places[SpaceToCheck + 2] == Play.Type and Board.Places[SpaceToCheck + 4] == Play.Type) or ( 
            SpaceToCheck == 6 and Board.Places[SpaceToCheck - 2] == Play.Type and Board.Places[SpaceToCheck - 4] == Play.Type) or ( 
            SpaceToCheck == 8 and Board.Places[SpaceToCheck - 4] == Play.Type and Board.Places[SpaceToCheck - 8] == Play.Type) or ( 
            SpaceToCheck == 4 and ((Board.Places[SpaceToCheck + 2] == Play.Type and Board.Places[SpaceToCheck - 2] == Play.Type) or (
                Board.Places[SpaceToCheck + 4] == Play.Type and Board.Places[SpaceToCheck - 4] == Play.Type))):                     
            Computer.Change = True
class Board:
    def __init__(self):
        if Play.GameType in ["S", "M"]:
            Board.Places = ['1','2','3',
                            '4','5','6',
                            '7','8','9']
            Board.PrintBoard()
        Board.Places = [' ',' ',' ',
                        ' ',' ',' ',
                        ' ',' ',' ']
        if Play.GameType not in ["S","M"]:
            Board.PrintBoard()
            sleep(1)

    def PrintBoard():
        print('',Board.Places[6],'|',Board.Places[7],'|',Board.Places[8],'')
        print('---|---|---')
        print('',Board.Places[3],'|',Board.Places[4],'|',Board.Places[5],'')
        print('---|---|---')
        print('',Board.Places[0],'|',Board.Places[1],'|',Board.Places[2],'')
        print()


Play()
