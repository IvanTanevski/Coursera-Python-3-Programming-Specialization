# COURSE 4 PROJECT - WHEEL OF FORTUNE

# The code below is the required code necessary to pass the assignment. The rest of the code is given by Coursera
# to make the WHEEL OF FORTUNE game code completed to play. Instructions for the code copied in README file
# ** self parameter somewhere is ommited as instructed by Coursera and not needed in their runtime environment.

import random
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():

    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    
    def addMoney(self, amt):
        self.prizeMoney += amt
     
    def goBankrupt(self):
        self.prizeMoney = 0
        
    def addPrize(self, prize):
        self.prizes.append(prize)
        
    def __str__(self):
        return ("{} (${})".format(self.name, self.prizeMoney))
        
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    
    def getMove(category, obscuredPhrase, guessed):
        prompt = input(("{} has ${}/n/n Category: {}/nPhrase: {}/nGuessed: {}/n/n"+
                       "Guess a letter, phrase, or type 'exit' or 'pass':").format(
                       self.name, self.prizeMoney, self.category, self.obscuredPhrase, self.guessed))
        return prompt
 
 # Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.prizeMoney = 0
        self.prizes = []
    
    def smartCoinFlip(self):
        rnd = random.randint(1, 10)
        if rnd > self.difficulty:
            return True
        else:
            return False
    
    def getPossibleLetters(self, guessed):
        lst = []
        if self.prizeMoney > VOWEL_COST:
            for letter in LETTERS:
                if letter not in guessed:
                    lst.append(letter)
        else:
            for letter in LETTERS:
                if letter not in guessed and letter not in VOWELS:
                    lst.append(letter)
        return lst

    def getMove(self, category, obscuredPhrase, guessed):
        lst = self.getPossibleLetters(guessed)
        if len(lst) == 0:
            return 'pass'
        else:
            bol = self.smartCoinFlip()
            if bol:
                for letter in self.SORTED_FREQUENCIES[::-1]:
                    if letter in lst:
                        return letter
            else:
                rnd = random.choice(lst)
                return rnd