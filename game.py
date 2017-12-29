print ("A Little game to decide whether you are on the right track or not")
print ("Disclaimer : The Game is just based on personal experience basis no proffesional advice whatsoever")
myvar=int(input("Please Enter your age"))
if myvar>18:
    print("You are elgible for this game")
elif myvar<18:
    print("Enter neither in the upcoming question")
    
ques1=input("Please mention whether you are \'working\' or you are a \'student\'")
if ques1=="working":
    print("Do you enjoy what you do:")
    ans1=input("Enter Yes or No")
    if ans1==Yes:
        print("You are on the right track")
    elif ans1==No:
        print("You need to rethink your decision and do what you love because you only live once ,If you want you can re run the game and put the option as student")
elif ques1=="student":
    print("What\'s your passion in life:")
    ans2=input("Enter any of following choices \n1.Cooking \n2.Dancing \n3.Singing \n4.Acting \n5.English literature \n6.History \n7.Civil Services \n8.Physics \n9.Maths \n10.Zoology \n11.Botany \n12.Chemitry \n13.Anyhting related to commerce \n14.Phsycology  \n15.Legal studies \n16.Aeronautical sciences \n17.BDS \n18.MBBS \n19.Journalism \n20.Mass communication \n21.Sports" )
    if ans2=="Cooking"or"Dancing" or "Singing" or "Acting" or "Sports":
        print("Just follow your heart and your passion Don\'t woory about the society or the relatives")
    elif ans2=="English literature" or "Civil Services" or "Legal Studies" or "History" or "Journalism" or "Mass communication" or "Phsycology":
        print("Take up  the respective subjects as your major and take up humanities in 11th and 12th")
    elif ans2=="Physics" or "Maths":
        print("I know there are both physics and maths lovers but Iam just answering on the basis of any of the subjects : \n Either specilaize in any of the subjects \n Or contribute to programming world ,the world needs you")
        
    elif ans2=="Zoology" or "Botany":
        print("Take up a specialization in the subject and try and teach the same to the other world")
    elif ans2=="BDS" or "MBBS":
        print("Take up the medical stream and help as many people as you can ")
    elif ans2=="Aeronautical sciences" or "Chemistry":
        print("Just go for the calling")
    elif ans2=="Anyhting related to commerce":
        print ("Couldn\'t mention all the names of the respective subjects but if you want to become an entrepeneur and this is what makes you happy ,go for it")
    else :
        print("There are numerous choices of subjects and stuff that one can do and pursue but it only and only depends on what you want to do and if  you genuinely love something and you are passionate about that thing ,please follow it . Enjoy what you do and you will be successful")      
else:
    print("Enjoy your life and eventually think about it:);)")
print ("This was quite a weird game but wanted to help the beginners and even grownups in some way ,even if it is this miniscule")  
