""" 
Written by Ibrahim Sydock

I pledge that I have neither given nor received help from anyone other than the 
instructor/TA/Group for all program components included here!
"""

# For exiting cleanly
import sys
# For easy letter frequency computing
from collections import Counter

#list of lowercase alphabet
CONST_ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

# store cipher text from user input
cipher_text = ""

# store letters retrieved so the user can easily view it again.
cipher_freq = ""

#-------------------------------------------Subbing Letters-------------------------------------------------------
#accepts a string formatted like the alphabet and substitues any changed letters
def substitute(cipher_key):
    
    # don't override original cipher text and convert into a list
    new_cipher_text = list(cipher_text)
    
    # keep track of what letter indexes have already been changes
    marked_indecies = []
    
    """ 
    Iterates through the cipher text for all the letters of the alphabet
    when a match of a letter is found in the text, it is converted to the new letter of the cipher_key alphabet
    the index of the letter of the text is then saved, 
        so that substitutions of the same letter doesn't occur
    """
    for a_idx, alph in enumerate(CONST_ALPHABET):
        for t_idx, lett in enumerate(new_cipher_text):
            
            #ignore already converted letters
            if t_idx in marked_indecies:
                continue
            else:
                # replace original alphabet with new key alphabet
                if alph == lett:
                    new_cipher_text[t_idx] = cipher_key[a_idx]
                    marked_indecies.append(t_idx)
                    
        #end cipher text loop
    #end alphabet loop
    
    # print results, converting back to a string
    print("Result of guess: \n", "".join(new_cipher_text), sep="")

#------------------------------------------Getting Letter Freq----------------------------------------------------
# accepts a string and prints the frequency of each letter
def compute_letter_frequency():
    
    # uses collection's Counter to get every letter and their frequency in a dictionary
    letter_freq = Counter(str(cipher_text))
    
    # make sure the use of this var is referencing the global one
    global cipher_freq
    
    msg = "\nLetters retrieved from the cipher text and their frequencies: \n"
    cipher_freq += msg
    print(msg, end="")
    
    # Sorts dictionary by most common letter and prints results in a nice format
    # also stored so that the user may reference it on command    
    for value, count in letter_freq.most_common():
        
        line_str = "[" + str(value) + " : " + str(count) + "] "
        cipher_freq += line_str
        print( line_str, end="")
    

#-------------------------------------------------Main-------------------------------------------------------------
# Main method to get input from user
if __name__ == '__main__':
    #welcome msg
    print( ("This program takes in a string of text that has been encrypted by substitution. This means "
          "that the string's alphabet has had some or all of its letters substituted by other letters. "
          "For example, an A in the encrypted text could represent a B in the decrypted text. You may "
          "enter your own encrypted text or enter nothing to try and solve a sample cipher."))
    # loop until valid cipher text input is retrieved (cannot contain nums)
    while(True):
        
        cipher_text = input("Please enter your alphabetical cipher text: ").lower() # retrieving input
        
        # Sample cipher for user to practice program with
        if not cipher_text:
            cipher_text = "hybbl wlrbc"
            print("\nSample cipher to solve:", cipher_text)
        elif not cipher_text.isalpha():
            # input was empty or had numbers, keep in loop
            print("\nERROR: Input must only be alphabetical!") 
            continue
        
        compute_letter_frequency() # compute frequencies
        break
    
    # msg to let user know how to guess the key to the cipher
    print( ("\n\nPlease enter a key to decrypt the cipher text. For example, \"abcdefghijklmnopqrstuvwxyz\" is" 
          " the current key, so if you wanted to substitute the letter \"a\" with \"b\" in the cipher text " 
              "you would enter: \"bbcdefghijklmnopqrstuvwxyz\" ") )
    
    #----------------------------------Key Guessing--------------------------------------
    # Getting input for cipher guesses
    while(True):
        
        cipher_key = input("Enter your guess: ").lower() # retrieving input
        
        # check for commands, then validate input
        if cipher_key == "exit" or cipher_key == "e":
            sys.exit(0)
        if cipher_key == "freq":
            print(cipher_freq)
        elif not cipher_key or len(cipher_key) != 26 or not cipher_key.isalpha():
            # want str length to specifically be 26 chars, cause that's the length of the alphabet
            print("\nERROR: key must be 26 characters of the alphabet with no spacing!")
        else:
            substitute(cipher_key)
            print( ("\nDid you solve it? If not, continue to guess! "
                  "Otherwise, enter \"exit\" or close the program if you're done. "
                  "(NOTE: Your guess will ONLY to be applied to the ORIGINAL cipher text!) \n"
                  "You can also enter \"freq\" to view the letter frequencies again, if desired."))
