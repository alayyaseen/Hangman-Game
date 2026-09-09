import random
#This will display the options 
def Display():
    print("Choose a Category: ","\n","1. Fruits","\n","2. Countries","\n","3. Animals","\n","4. Random")
    choose=input("Choose an option (1-4): ")
    correct=False
    while correct==False:
        if choose>="1" and choose<="4":
            correct=True
        else:
            choose=input("Enter a valid number (1-4): ")
                
    choose=int(choose)
    if choose==1:
        Fruits()
    
    elif choose==2:
        Countries()
        
    elif choose==3:
        Animals()
    elif choose==4:
        Random()


#this will generate a random number and use a category randomly
def Random():
    randomNum=int((random.randint(0,100))/3)
    if randomNum==0:
        print("Hint it is a fruit")
        Fruits()
    elif randomNum==1:
        print("Hint it is a Country")
        Countries()
    else:
        print("Hint it is an Animal")
        Animals()




#this will find a word randomly to use from fruits
def Fruits():
    FruitFile=open("Fruit.txt","r")
    index=random.randint(1,100)
    for x in range (index):
        line=FruitFile.readline().strip()
    word=line
    FruitFile.close()
    Control(word)

#this will find a word randomly to use from animals
def Animals():
    AnimalFile=open("Animals.txt","r")
    index=random.randint(1,100)
    for x in range (index):
        line=AnimalFile.readline().strip()
    word=line
    AnimalFile.close()
    Control(word)
    

#this will find a word randomly to use from countries
def Countries():
    CountryFile=open("Country.txt","r")
    index=random.randint(1,192)
    for x in range (index):
        line=CountryFile.readline().strip()
    word=line
    CountryFile.close()
    Control(word)
    

#This will created an encrypted version of the word with dashes
def Encrypt(TheWord):
    EncryptedWord=""
    for index in range(len(TheWord)):
        letter=TheWord[index]


        if letter!="" and (letter>="a" and letter<="z"):
            EncryptedWord=EncryptedWord+"_"
        elif letter!="" and (letter>="A" and letter<="Z"):
            EncryptedWord=EncryptedWord+"_"
        else:
            EncryptedWord=EncryptedWord+letter

    print(EncryptedWord)
    return EncryptedWord

    

    
#This will take a letter as an input and check wether it exists in the word and replaces it with a dash if it exists
def Guesses(word,EncryptArray):
    
    letter=input("Guess a letter: ").lower()
    while (letter<="a" or letter>="z") or (letter<="A" or letter>="Z"):
        letter=input("Enter a Letter (A-Z or a-z): ").lower()

    length=len(word)
    CorrectPosition=[]
    flag=False
    for index in range(length):
        if word[index].lower()==letter:
            CorrectPosition.append(index)
            flag=True
    if flag==False:
        return ("wrong")
    else:
        ArrayLength=len(CorrectPosition)
        
        for index in range(ArrayLength):
            position=CorrectPosition[index]
            if position==0:
                EncryptArray[position]=letter.upper()
            else:
                EncryptArray[position]=letter
        NewEncryptWord=""
        for index in range(len(EncryptArray)):
            NewEncryptWord=NewEncryptWord+EncryptArray[index]
        if NewEncryptWord==word:
            return ("done")

        return NewEncryptWord
    
            
#This is the main program that calls the functions        
def Control(word):
    EncryptedWord=Encrypt(word)
    EncryptedArray=[]
    for index in range(len(EncryptedWord)):
        EncryptedArray.append(EncryptedWord[index])
    wrong=0
    complete=False
    num_of_tries=10
    while wrong<=num_of_tries and complete==False:
        answer=(Guesses(word,EncryptedArray))
        if answer=="wrong":
            print("WRONGGGG!!!!")
            wrong=wrong+1
        elif answer=="done":
            complete=True
        else:
            print(answer)
    if wrong>num_of_tries:
        print("YOU LOSTTTT ")
    else:
        print("YOU WONNNNNNNNNN")
    print("The Word was", word)
    again=input("Do You wanna play again (Yes/No)? ")
    while again.lower()!="yes" and again.lower()!="no":
        again=input("Yes or No: ")
    if again.lower()=="yes":
        Display()
    










Display()







