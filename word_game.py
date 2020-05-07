#This is a script that play the word game from 8 out of 10 cats play countdown
#Purpose of the script is to find the longes word that can be created given 9
#random leteers

def open_text_file (file_name):  #To open the text file from the root directory which contain
                        #all the words in the dictionary
    file_in = open(file_name, 'r')
    words_string = file_in.read()
    file_in.close()
    words_list = words_string.split("\n")
    return words_list

def proces_list_of_words(words_list):
    #remove words shorter than 4 letters and longer than 9 letters
    #remove words with any special characters
    #Remove words with numbers
    #Remove words if first letter is capital
    list_of_symbols = ['-', '_', '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                       '+', '=', '{', '}', '[', ']', ':', ';', "'", '<', '>', ',', '.',
                       '?', '/']
    list_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    list_of_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in range((len(words_list) - 1), -1, -1):
        if len(words_list[i]) <= 3 or len(words_list[i]) > 9:
            words_list.pop(i)

    for i in range((len(words_list) - 1), -1, -1):
        for symbol in list_of_symbols:
            if symbol in words_list[i]:
                words_list.pop(i)

    for i in range((len(words_list) - 1), -1, -1):
        for number in list_of_numbers:
            if number in words_list[i]:
                words_list.pop(i)

    for i in range((len(words_list) - 1), -1, -1):
        for letter in list_of_uppercase:
            if letter in words_list[i]:
                words_list.pop(i)
        

def user_input(number_of_turns):
    counter = 1
    random_letters_list = []

    while counter < number_of_turns + 1:
        user_input = input("Please enter the letter " + str(counter) + ": ").lower().strip()
        if len(user_input) > 1 or len(user_input) < 1 or not user_input.isalpha():
            print("ERROR")
            user_input = input("Please enter the letter " + str(counter) + ": ").lower().strip()
        else:
            counter += 1
            random_letters_list.append(user_input)
    return random_letters_list

def sort_to_ascending_order(letters_list):
    letters_list.sort()

def check_for_longest_word(words_list, letters_list):
    counter = 0
    word_letters_list = list()
    long_words_list = []
    for word in words_list:
        word_letters_list = list(word)
        #print(word_letters_list)
        len_word = len(word)
        for letter in letters_list:
            if letter in word_letters_list:
                index_letter = word_letters_list.index(letter)
                word_letters_list.pop(index_letter)
                counter += 1
                if counter >= 5 and len(word_letters_list) == 0:
                    long_words_list.append(word)
                    
    return long_words_list

def categorise(long_words_list):
    words_dict = {"Four Letter Words": [], "Five Letter Words": [], "Six Letter Words" :[],
                  "seven Letter Words": [], "Eight Letter Words": [],
                  "Nine Letter Words": []}
    for word in long_words_list:
        if len(word) == 4:
            words_dict["Four Letter Words"].append(word)
        elif len(word) == 5:
            words_dict["Five Letter Words"].append(word)
        elif len(word) == 6:
            words_dict["Six Letter Words"].append(word)
        elif len(word) == 7:
            words_dict["seven Letter Words"].append(word)
        elif len(word) == 8:
            words_dict["Eight Letter Words"].append(word)
        elif len(word) == 9:
            words_dict["Nine Letter Words"].append(word)    
    
    return words_dict

def print_words(words_dict):
    for key in words_dict.keys():
        print(key)
        print()
        count = 1
        for word in words_dict[key]:
            print(str(count) + " " + word)
            count += 1
        print()
def run_condition():
    yes_list = ['y', 'Yes', 'YES', 'Y']
    no_list = ['n', 'No', 'NO', 'N']
    condition = "run"
    while condition == "run":
        user_input = input("would you like to proceed for another round[Y/N]: ").strip()
        print()
        if user_input in yes_list:
            condition = "not run"
            return True
        elif user_input in no_list:
            condition = "not run"
            return False
        else:
            print("USER INPUT ERROR!!!")
            condition = "run"
    
def main():
    condition = True
    while condition == True:   
        words_list = open_text_file('words.txt')
        proces_list_of_words(words_list)
        random_letters_list = user_input(9)
        long_words_list = check_for_longest_word(words_list, random_letters_list)
        words_dict = categorise(long_words_list)
        print_words(words_dict)
        condition = run_condition()
        
main()
    
                
    
