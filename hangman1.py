import random
fo=open("quiz.txt","r")
data=fo.read()
words_list=data.split("\n")
#print(words_list)
'''for countries'''
countries=words_list[0]
country_list=countries.split(",")
#print(country_list)
'''for animals'''
animals=words_list[1]
animal_list=animals.split(",")
#print(animal_list)
'''for indian cities'''
cities=words_list[2]
cities_list=cities.split(",")
#print(cities_list)
fo.close()
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O  |
  /|  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
    ===''']
#this function is used to select category
def getCategory():
    category=int(input("What Category you want to play in?\n 0==country, 1==animals, 2==cities"))
    if category==0:
        words=country_list
        return words
    elif category==1:
        words=animal_list
        return words
    elif category==2:
        words=cities_list
        return words
    else:
        print("Invalid")
#this function selects a random word from list
def RandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

#this function displays hangman pics, missed letters
def Board(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)], end='\n')
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    #replacing blanks with guessed letter
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    #printing secret word with unguessed letters as blanks
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess
def playAgain():
     # This function returns True if the player wants to play again otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters= ''
words=''
quiz_words=getCategory()
secretWord = RandomWord(quiz_words)
gameIsDone = False

while True:
    Board(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord +'"! You have won!')
            gameIsDone = True
            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    quiz_words=getCategory()
                    secretWord = RandomWord(quiz_words)
                else:
                    break

    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            Board(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses,the word was "' + secretWord + '"')
            gameIsDone = True

            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    quiz_words=getCategory()
                    secretWord = RandomWord(quiz_words)
                else:
                    break























