#####################################################################################################
# Implementation of the Tennis Kata in Python.
# found in https://learn.madetech.com/katas/tennis/
# The code below can probably be optimised further.
#####################################################################################################
class TennisKata:
    def __init__(self):
        self.player1Score = 0
        self.player2Score = 0

    def score(self):        
        if self.player1Score >= 3 and self.player2Score >= 3 and self.player1Score == self.player2Score:
            return 'Deuce'
        elif self.player1Score >= 3 and self.player1Score >= 3 and self.player1Score - self.player2Score == 1: 
            return "Player One Advantage"
        elif self.player1Score >= 3 and self.player1Score >= 3 and self.player2Score - self.player1Score == 1: 
            return "Player Two Advantage"

        elif self.player1Score >= 4 and self.player1Score >= self.player2Score - 2 : 
            return "Player One Wins"
        elif self.player2Score >= 4 and self.player2Score >= self.player1Score - 2 : 
            return 'Player Two Wins' 
        return self.getLiteralScore(self.player1Score) + " " +  self.getLiteralScore(self.player2Score)    

    def playerOneWinsTheBall(self, count = 1):
        for x in range(count):
            self.player1Score = self.player1Score + 1

    def playerTwoWinsTheBall(self, count = 1):
        for x in range(count):
            self.player2Score = self.player2Score + 1

    def getLiteralScore(self, score: int):
        match score:
            case 0:
                return "Love"
            case 1:
                return "Fifteen"
            case 2:
                return "Thirty"
            case 3:
                return "Forty"
            case _:
                return "Unknown Score"