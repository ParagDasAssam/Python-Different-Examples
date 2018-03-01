import os
My_dictionary = {}
exit = 1
name_list = []
while(exit == 1):
    print "Enter 1 to enter a word "
    print "Enter 2 to see the words with meaning "
    print "Enter 3 to delete a word "
    print "Enter 4 to see list of words "
    print "Enter 5 to clear screen "
    print "Enter 6 to exit "
    choice_made = input("Enter your options ")
    if(choice_made == 1):
        new_word = raw_input("\nEnter the word : ")
        meaning = raw_input("\nEnter the meaning :")
        My_dictionary[new_word] = meaning
        print "\nThe new word is: " + new_word
        print "\nThe meaning is: " + My_dictionary[new_word] + "\n"
    elif(choice_made == 2):
        print"\nAll the words are: \n"
        for n in My_dictionary.keys():
            print n + ' : ' + My_dictionary[n]
        print " "
    elif(choice_made == 3):
        del_word = raw_input("\nEnter the word: ")
        flag = 1
        for n in My_dictionary.keys():
            if(n == del_word):
                del My_dictionary[del_word]
                flag = 0
        if(flag == 0):
            print"\n The word has been removed: "
        else:
            print"\n The word does't exist: "

    elif(choice_made == 4):
        for n in My_dictionary.keys():
            print n

    elif(choice_made == 5):
        os.system('clear')
    else:
        break
