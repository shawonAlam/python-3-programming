VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney = amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)
        
    def __str__(self):
        return ("{} ({})".format(self.name, self.prizeMoney))



# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def __init__(self, name):
        WOFPlayer.__init__(self, name)

    def getMove(self, category, obscuredPhrase, guessed):
        self.category = category
        self.guessed = guessed
        self.obscuredPhrase = obscuredPhrase
        sss= self.name + " has $" + str(self.prizeMoney) + "\n\n" + "Category: " + self.category + "\n" + "Phrases: " + self.obscuredPhrase + "\n" + "Guessed: " + self.guessed + "\n\n" + "Guess a letter, phrase, or type 'exit' or 'pass':"
        print(sss)
        
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    prizemoney = 0
    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty
        
    def smartCoinFlip(self):
        rand_number = random.randint(1, 10)
        if rand_number > self.difficulty:
            return True
        elif rand_number <= self.difficulty:
            return False
    def getPossibleLetters(self, guessed):
        list = []
        if self.prizemoney >= 250:
            for l in LETTERS:
                list.append(l)
        else:
            for l in LETTERS:
                if l not in VOWELS:
                    list.append(l)
        return list

    def getMove(self, category, obscuredPhrase, guessed):
        list = self.getPossibleLetters(guessed)
        FlipResult = self.smartCoinFlip()
        if len(list) == 0:
            return 'pass'
        else:
            if FlipResult == True:
                # SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
                for l in self.SORTED_FREQUENCIES:
                    if l in list:
                        return l
            elif FlipResult == False:
                return random.choice(list)



