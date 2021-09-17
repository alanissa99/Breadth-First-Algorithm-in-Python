class DictHash:
    def __init__(self):
        self.dictionary={}                      #The class consists just of my dictionary
    
    def store(self,nyckel,data):                #Function to add keys and data into my dictionary
                                                      #If the key already exists in the dictionary->Update the data, otherwise simply add into dictionary
         self.dictionary[nyckel]=data


    def search(self,nyckel):                    #A function to check if a key exists in my dictionary
        if nyckel in self.dictionary:
            return self.dictionary[nyckel]
        else:                                   #Incase the key doesnt exist
            return False

    def __getitem__(self,nyckel):
        return self.search(nyckel)

    def __contains__(self,nyckel):               #Why can i all of sudden have my "if nyckel in self.dictionary"? 
        if nyckel in self.dictionary:
            return True
        else:
            return False
