#Init

#Function
def WickedMadlib():
    print("Welcome to your fairy tale!")
    color = (input("Enter a bright color: "))
    noun = (input("Enter a noun: "))
    properNoun = (input("Enter a proper noun: "))
    name = (input("Enter a celebrity name: "))
    profession = (input("Enter a profession: "))
    verb = (input("Enter a verb: "))
    negativeAdjective = (input("Enter a negative adjective: "))
    object = (input("Enter an object: "))

    print("Here's YOUR version of... WICKED! Once upon a time, there was a little girl who was born" + " "+ '\033[1m' + color + '\033[0m'+ ". She grew up and went to a/n" + " "+'\033[1m'+ noun +'\033[0m'+ 
        " " + "called" + " " +'\033[1m'+ properNoun +'\033[0m'+ ". She and her enemy," + " " +'\033[1m'+ name + '\033[0m'+ ", eventually became friends. They went to meet the " +'\033[1m' + profession + '\033[0m'+
        ", who turned out to be evil! So, the girl had to " + '\033[1m'+ verb + '\033[0m'+ " away because the world thought she was " +'\033[1m'+ negativeAdjective + '\033[0m'+
        ". She turned a lot of people into objects, such as a/n " + '\033[1m' + object + '\033[0m'+ ", and pretended to get melted by a small child. Then " +'\033[1m' + name + '\033[0m'+ " had to celebrate her 'death'. The end!")


#Main
WickedMadlib()