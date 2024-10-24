def EvenWord():
    UserInput = input("Enter a string: ") #promps user
        
    words = UserInput.split()   #splits the string by every word

    for word in words:          #iterates over the words
        if len(word)%2 == 0:    #if the word have an even lenght
            print(word)         #print out the word

EvenWord()