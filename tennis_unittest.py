#####################################################################################################
# Tests
# The code below could be refactored further to perhaps input some kind of game score array to the 
# tests to reduce the line count. Some more tests of edge cases would also help.
#####################################################################################################
import unittest

from tennis import TennisKata   # The test framework

class Test_Tennis(unittest.TestCase):
    def setUp(self) -> None:
        self.tennis = TennisKata()
        return super().setUp()

    def test_deuce(self):

        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()

        self.tennis.playerTwoWinsTheBall()
        self.tennis.playerTwoWinsTheBall()
        self.tennis.playerTwoWinsTheBall()
        self.tennis.playerTwoWinsTheBall()

        self.assertEqual(self.tennis.score(), "Deuce")

    def test_PlayerOneOutrightWinWith5balls(self):

        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
        
        self.tennis.playerTwoWinsTheBall()

        self.assertEqual(self.tennis.score(), "Player One Wins")        
   
    def test_PlayerOneOutrightWinWith4balls(self):

        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
  
        
        self.tennis.playerTwoWinsTheBall()

        self.assertEqual(self.tennis.score(), "Player One Wins")        


    def test_PlayerTwoOutrightWin(self):

        self.tennis.playerTwoWinsTheBall()
        self.tennis.playerTwoWinsTheBall()
        self.tennis.playerTwoWinsTheBall()
        self.tennis.playerTwoWinsTheBall()
        self.tennis.playerTwoWinsTheBall()
        
        self.tennis.playerOneWinsTheBall()

        self.assertEqual(self.tennis.score(), "Player Two Wins")       

    def test_Fifteen_Love(self):

        self.tennis.playerOneWinsTheBall()

        self.assertEqual(self.tennis.score(), "Fifteen Love")       
    
    def test_Thirty_Fifteen(self):

        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
        self.tennis.playerTwoWinsTheBall()

        self.assertEqual(self.tennis.score(), "Thirty Fifteen")   

    def test_Player_one_advantage(self):

        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()

        self.tennis.playerTwoWinsTheBall()
        self.tennis.playerTwoWinsTheBall()
        self.tennis.playerTwoWinsTheBall()

        self.assertEqual(self.tennis.score(), "Player One Advantage")   

    def test_Player_two_advantage(self):

        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()
        self.tennis.playerOneWinsTheBall()


        self.tennis.playerTwoWinsTheBall()
        self.tennis.playerTwoWinsTheBall()
        self.tennis.playerTwoWinsTheBall()
        self.tennis.playerTwoWinsTheBall()
        
        self.assertEqual(self.tennis.score(), "Player Two Advantage")   

if __name__ == '__main__':
    unittest.main()
