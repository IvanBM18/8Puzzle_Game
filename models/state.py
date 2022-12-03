import random
from models.actions import Actions
class State:
    def __init__(self, values : list = None,indexOfZero : list= None):
        self._possibleValues = [0,1,2,3,4,5,6,7,8]
        self._goal = [[0,1,2],[3,4,5],[6,7,8]]
        if(indexOfZero == None):
            self.indexOfZero = [-1,-1]
        else:
            self.indexOfZero = indexOfZero
        if(values == None):
            self.values = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
            self._randomValues()
        else:
            self.values = values
        self.exists = True
        self._setID()
        
    def _randomValues(self):
        for i in range(3):
            for j in range(3):
                value = random.choice(self._possibleValues)
                self.values[i][j] = value
                if(value == 0):
                    self.indexOfZero = [i,j]
                self._possibleValues.remove(value)
        self._possibleValues= []
    
    def toString(self) -> str:
        return '\n'.join(map(lambda x:' '.join(map(lambda y:str(y), x)), self.values))
    
    def isSolution(self) -> bool:
        return self.id == 12345678
    
    # Move the zero to the direction specified
    def move(self,action:Actions):
        valid = True
        if(action == Actions.UP):
            valid = self._moveUp()
        elif(action == Actions.RIGHT):
            valid = self._moveRight()
        elif(action == Actions.DOWN):
            valid = self._moveDown()
        elif(action == Actions.LEFT):
            valid = self._moveLeft()
        self._setID()
        self.exists = valid
    
    def _moveUp(self) -> bool:
        if(self.indexOfZero[0] == 0):
            return False
        else:
            self.values[self.indexOfZero[0]][self.indexOfZero[1]] = self.values[self.indexOfZero[0]-1][self.indexOfZero[1]]
            self.values[self.indexOfZero[0]-1][self.indexOfZero[1]] = 0
            self.indexOfZero[0] -= 1
            return True
    
    def _moveRight(self) -> bool:
        if(self.indexOfZero[1] == 2):
            return False
        else:
            self.values[self.indexOfZero[0]][self.indexOfZero[1]] = self.values[self.indexOfZero[0]][self.indexOfZero[1]+1]
            self.values[self.indexOfZero[0]][self.indexOfZero[1]+1] = 0
            self.indexOfZero[1] += 1
            return True
    
    def _moveDown(self) -> bool:
        if(self.indexOfZero[0] == 2):
            return False
        else:
            self.values[self.indexOfZero[0]][self.indexOfZero[1]] = self.values[self.indexOfZero[0]+1][self.indexOfZero[1]]
            self.values[self.indexOfZero[0]+1][self.indexOfZero[1]] = 0
            self.indexOfZero[0] += 1
            return True
    
    def _moveLeft(self) -> bool:
        if(self.indexOfZero[1] == 0):
            return False
        else:
            self.values[self.indexOfZero[0]][self.indexOfZero[1]] = self.values[self.indexOfZero[0]][self.indexOfZero[1]-1]
            self.values[self.indexOfZero[0]][self.indexOfZero[1]-1] = 0
            self.indexOfZero[1] -= 1
            return True
        
    # Get a ID for the current state
    def _setID(self) -> int:
        id = int(''.join(map(lambda x:''.join(map(lambda y:str(y), x)), self.values)))
        self.id = id
        