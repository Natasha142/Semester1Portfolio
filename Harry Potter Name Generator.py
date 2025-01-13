#Harry Potter Character Generator
#Init

#Function
def HarryPotterCharacter():
    print ("Welcome to Your Harry Potter Character 2001")
    print ("Answer the questions to find out which Harry Potter character you are (literally)")
    ans = input ("Introvert (I) or Extrovert (E)?")
    if ans == "I":
        ans = input ("Ravenclaw (Raven) or Hufflepuff (Puff)?")
        if ans == "Raven":
            ans = input("Quirky (Quirk) or Driven (Driv)?")
            if ans == "Quirk":
                print ("You are Luna Lovegood!")
            else:
                print ("You are Rowena Ravenclaw!")
        if ans == "Puff":
            ans = input ("Handsome (Hand) or Animals (Anim)?")
            if ans == "Hand":
                print ("You are Cedric Diggory!")
            else:
                print ("You are Newt Scamander!")

    if ans == "E":
        ans = input ("Gryffindor (Gryff) or Slytherin (Slyth)?")
        if ans == "Gryff":
            ans = input ("Hero (Hero) or Bookish (Book)?")
            if ans == "Hero":
                print ("You are Harry Potter!")
            else:
                print ("You are Hermione Granger!")
        if ans == "Slyth":
            ans = input ("Evil (Evil) or Blonde (Blon)?")
            if ans == "Evil":
                print ("You are Lord Voldemort/ Tom Riddle!")
            else:
                print ("You are Draco Malfoy!")

#Main
HarryPotterCharacter()
