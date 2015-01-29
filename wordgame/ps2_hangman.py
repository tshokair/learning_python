# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    #inFile = open('words.txt', 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def generate_new_word(word_length):
    l=0
    correct_flag=0
    word=list("")
    while l<word_length:
        word.append("_")
        l=l+1
    return word

def turn_word_to_string(word_as_list):
    word_guess_string=""
    j=0
    while j<len(word_as_list):
    #print(word_guess[j])
        word_guess_string+=word_as_list[j]
        j+=1
    return word_guess_string
def update_word(word_length, word_guess, letter_guess, word_answer):
    l=findOccurences(word_answer,letter_guess)
    new_word=word_guess
    k=0
    while k<len(l):
        new_word[l[k]]=letter_guess
        k+=1
    return new_word
def print_hangman(k):
    if k==0:
        print ("______")
        print ("  |   " )
    elif k==1:
        print("______")
        print("  |   ")
        print("  0   ")
    elif k==2:
        print("______")
        print("  |   ")
        print("  0   ")
        print("  ()  ")

    elif k==3:
        print("______")
        print("  |   ")
        print("  0   ")
        print(" /()  ")

    elif k==4:
        print("______")
        print("  |   ")
        print("  0   ")
        print(" /()\ ")
    elif k==5:
        print("______")
        print("  |   ")
        print("  0   ")
        print(" /()\ ")
        print("  /   ")
    elif k==6:
        print("______")
        print("  |   ")
        print("  0   ")
        print(" /()\ ")
        print("  /\  ")


word = choose_word(wordlist)
n=len(word)
print("Let's get started.")
print("The word has",n,"letters in it, you may only choose",6,"incorrect letters")

k=0
guessed_letters=""
word_guess=generate_new_word(n)
j=0

while k<6:
    guess=input("Guess a letter: ")
    guess=guess.lower()
    guessed_letters+=guess
    if guess in word:
        j=0
        word_guess=update_word(n,word_guess,guess,word)
        word_guess_string=turn_word_to_string(word_guess)
        if word_guess_string==word:
            print("You got it! The word was:",word)
            break
        print("Good guess:",word_guess_string)
        print("Your letter choices so far are:",guessed_letters)
    else:
        k=k+1
        word_guess_string=turn_word_to_string(word_guess)
        print(word_guess_string,", you have",6-k," wrong guesses left")
        print("Your letter choices so far are:",guessed_letters)
    print_hangman(k)



if k==6:
    print ("Sorry you lose, the word was:",word)
