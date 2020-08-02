import random
import string
from words import choose_word
from images import IMAGES

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if secret_word == get_guessed_word(secret_word, letters_guessed):
          return True 
    return False

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    letters_left = string.ascii_lowercase
    i = 0
    alphabet = ""
    while i < len(letters_left):
      if letters_left[i] not in  letters_guessed:
        alphabet = alphabet + letters_left[i]
      i = i + 1
    return alphabet

def get_hint(secret_word,letters_guessed):
  hint = []
  i = 0
  while i<len(secret_word):
    letter = secret_word[i]
    if letter not in letters_guessed:
      if letter not in hint:
        hint.append(letter)
    i = i + 1
  return random.choice(hint)


def is_word_guess(secret_word,letters_guessed):
    if get_guessed_word(secret_word, letters_guessed) in secret_word:
      return True
    return False

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai


    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print ("Welcome to the game, Hangman!")
    level = input("which level you want\n1.Easy \n2.Medium \n3.Hard ")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    letters_guessed = ""
    total_chances = chances = 8
    print(secret_word)
    i = 0
    images = [0,1,2,3,4,5,6,7]
    if level == "2":
      total_chances=chances=6
      images = [0,2,3,5,6,7]
    elif level == "3":
      total_chances=chances = 4
      images = [1,3,5,7]
    else:
      if level != "1":
        print("your choice is invalid ")
    while chances > 0:
      available_letters = get_available_letters(letters_guessed)
      print ("Available letters: " +" "+str(available_letters))
      guess = input("Please guess a letter: ")
      if guess == "hint":
        print("your hint is",get_hint(secret_word,letters_guessed))
      elif len(guess) == 1:
        letter = guess.lower()
        if letter in secret_word:
            letters_guessed = letters_guessed+ letter
            print ("Good guess: "+" "+str(get_guessed_word(secret_word, letters_guessed)))
            print ("")

            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
                print ("")
                break
        else:
            print ("Oops! That letter is not in my word: "+" "+str(get_guessed_word(secret_word, letters_guessed)))
            print("you have "+str(chances)+" more chances to guess letter")
            print(IMAGES[images[total_chances-chances]])
            chances  = chances - 1
            i = i + 1
            letters_guessed = letters_guessed+letter
            print ("")
      else:
        print("__INVALID guess__please guess again")
        continue
    else:
      print("sorry you have lost your all chances "+" "+"your secrete word was"+" "+secret_word)
    
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)

