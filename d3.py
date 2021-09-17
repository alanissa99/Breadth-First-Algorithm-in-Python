import string
from DictHash import DictHash
from ArrayQfile import ArrayQ
import sys

if len(sys.argv) < 3:
    print("Start- och slutord saknas")
    print("Använd programmet så här: \n\t python3", sys.argv[0], " [startord] [slutord]")
    sys.exit()

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent


alphabet_string = string.ascii_lowercase        #string of all english lower case letters
alphabet_list = list(alphabet_string)           #list of all lower case letters
alphabet_list.append("å")                       #Next 3 lines add the swedish alphabet
alphabet_list.append("ä")
alphabet_list.append("ö")


def makechildren(word):
    children = []
    for i in range(len(word)):      #For each letter in the word

        for  bokstav in alphabet_list:                          #So that i get every letter in the alphabet
            
            if i==0:                                             #If its the first letter in the word
                generated = bokstav + word[1:]                  #The word generated

                if generated != word:                               #Check that your not generating the word itself
                    if generated_words[generated] != True:          #Check that you havent already created the word previously 
                        if swedish_words[ generated ] == True:      #Check if its a real word
                            children.append( generated )
                            generated_words.store( generated, True)  #Add the word into my dictionary 

            if i==1:                                                #If its the second letter in the word
                generated = word[0] + bokstav + word[2]

                if generated != word:
                    if generated_words[generated] != True:
                        if swedish_words[ generated ] == True:
                            children.append( generated )
                            generated_words.store( generated, True)
            
            if i==2:                                                #If its the third letter i the word
                generated = word[:2] + bokstav

                if generated != word:
                    if generated_words[generated] != True:
                        if swedish_words[ generated ] == True:
                            children.append( generated )
                            generated_words.store( generated, True)


    return children




##########All the 3 letter swedish words
file = open( "word3.txt", "r" ) 
content = file.readlines()
words = []
for rad in content:
    words.append(rad.strip())

########## Dictionary with all swedish words
swedish_words = DictHash()  #Creating a dictionary with all the swedish words
for word in words:
    swedish_words.store( word, True )   #Adding every word in the hash table

########## Dictionary with generated words
generated_words = DictHash()  #Creating a Dictionary with all the swedish words


startord = sys.argv[1]      #first input in terminal
startnod = ParentNode(startord)

slutord = sys.argv[2]       #second input in terminal
queueOfWords = ArrayQ()         #A que of words and their children
queueOfWords.enqueue( startnod )                    #Put in the start word in the que

currentNode = None
while not queueOfWords.isEmpty():                 #While the que isnt empty
    currentNode = queueOfWords.dequeue()                        #Remove the first node in the que
    nextWord = currentNode.word                                 #The word that i will use to generate kids
    
    if nextWord == slutord:                 #If desired word is found then leave the loop
        break               #exit while loop
    
    else:
        children = makechildren( nextWord )           #Create all the children
        
        for child in children:
            if child == slutord:                #if the child created is the desired word
                finalNode = ParentNode(child, currentNode)  #finalNode points to the node of the desired word
                queueOfWords.enqueue(finalNode)

            else:                      
                queueOfWords.enqueue( ParentNode( child, currentNode ) )             #Add every childnode in the que pointing to the parent


def writechain(Node):
    if Node.parent == None:
        print(Node.word)
    
    else:
        writechain(Node.parent)
        word = Node.word
        print(word)         

writechain(finalNode)
    








