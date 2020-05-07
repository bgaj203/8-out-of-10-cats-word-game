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


words_list = ['apple', 'ghosting', 'computer', 'random']
letters_list = ['a', 'p', 'p', 'l', 'e', 'q', 'w', 't', 'u']
long_words = check_for_longest_word(words_list, letters_list)
print(long_words)


words_dict = {"key 1": [1, 2, 3], "key2": [5, 6, 8]}
print(words_dict["key 1"])
words_dict["key 1"].append(8)
print(words_dict["key 1"])
                 
