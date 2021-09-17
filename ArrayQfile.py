from array import array

class ArrayQ:

    def __init__(self):
        self._array=[]
        self._front=None
        self._end=None              #Jag vet att det här är onödig

    def enqueue(self,data):
        self._array.append(data)
        if self._front==None:       #If there is no elements in the array, then the incoming data will be both front and last
            self._front=data
            self._end=data
        else:                               #Otherwise, the incoming data is pushed to the end
            self._end=data

    def dequeue(self):
        x=self._array.pop(0)
        if len(self._array)==0:              #If there are no elements in the array, then both front and end become None
            self._front=None
            self._end=None
        else:                               #Otherwise, since we remove from the front of the array, we need to redefine the front attribute
            self._front=self._array[0]
        return x

    def isEmpty(self):
        if self._front==None:
            return True
        else:
            return False