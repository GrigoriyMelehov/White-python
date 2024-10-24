import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
========''', '''
  +---+
  0   |
      |
      |
========''', '''
  +---+
  0   |
  |   |
      |
========''', '''
  +---+
  0   |
 /|   |
      |
========''', '''
  +---+
  0   |
 /|/  |
      |
========''', '''
  +---+
  0   |
 /|/  |
 /    |
========''', '''
  +---+
  0   |
 /|/  |
 / /  |
========''']
words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон'.split()

def getRandomWord(wordList):
    #эта функция возвращает случайную строку из переданного списка.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks ='_'*len(secretWord)

    for i in range(len(secretWord)): #заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #показывает секретное слово с пробелами между букв
        print(letter, end='')
    print()

def getGuess(alreadyGuessed):
    #возврвщает букву, введенную игроком.проверка что 1 и буква
    while True:
        print('введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите 1 букву')
        elif guess in alreadyGuessed:
            print('Вы уже вводили эту букву, введи другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('введи БУКВУ, олень!')
        else:
            return guess

def playAgain():
    #фуккция возвращает TRUE если играть заново, в противном FALSE
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И ц А')
missedLetters =''
correctLetters =''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

#позволяет игроку ввести букву
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

#проверяет выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слова-"' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

#проверяет, превысил ли игрок лимит попыток и проиграл
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('Вы исчерпали попытки! \n НЕугадано букв: ' + str(len(missedLetters)) + ' угадано букв ' + str(len(correctLetters)) + ' было загадано слово "' + secretWord +'".')
        gameIsDone = True

#запрашивает, хочет ли игрок сыграть заново(только если игра завершена).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
    
