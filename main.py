import random
def word_list():
    with open("5_letter_words.txt", "r") as file:
        wordsfilelist = [line.strip() for line in file]
    return wordsfilelist
    
def random_word(inlist):
    return inlist[random.randint(0, len(inlist)-1)]
    
def is_real_word(guess, checklist):
    return guess in checklist
    
def next_guess(checklist):
    uguess = input("Please enter a guess: ")
    uguess = uguess.lower()
    while not is_real_word(uguess, checklist):
        print("That's not a real word!")
        uguess = input("Please enter a guess: ")
        uguess = uguess.lower()
    return uguess
    
def check_guess(uguess, answer):
    result = ""
    for i in range(len(uguess)):
        if uguess[i] not in answer:
            result += '_'
        elif uguess[i] == answer[i]:
            result += 'X'
        elif uguess.find(uguess[i]) == i and uguess[i] in answer:
            result += 'O'
        elif uguess.count(uguess[i]) == answer.count(uguess[i]):
            result += 'O'
        else:
            result += '_'
                
    return result


def play():
    wordlist = word_list()
    answer = random_word(wordlist)
    won = False
    tries = 0
    while won is False and tries < 6:
        guess = next_guess(wordlist)
        guessreturn = check_guess(guess, answer)
        print(guessreturn)
        if guessreturn == 'XXXXX':
            won = True
        tries += 1
    if won:
        print('You won!')
    else:
        print('You lost!')
        print(f'The word was: {answer}')
