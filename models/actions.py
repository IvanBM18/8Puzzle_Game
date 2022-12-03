from enum import Enum
class Actions(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    NONE = -1
    
    # def at(self, index):
    #     if(index == 0):
    #         return Actions.UP
    #     elif(index == 1):
    #         return Actions.RIGHT
    #     elif(index == 2):
    #         return Actions.DOWN
    #     elif(index == 3):
    #         return Actions.LEFT
    #     elif(index == -1):
    #         return Actions.NONE