originalword=input("What\'s the word you want the pig latin for")
pyg="ay"
if len(originalword)>0 and originalword.isalpha():
    print (originalword)
    word=originalword.lower()
    first= word[0]
    new_word=word + first + pyg
    new_word=new_word[1:len(new_word)]
    print (new_word)
else :
    print ("empty")
