from copy import deepcopy

from models.state import State
from models.actions import Actions
class Node:
    
    def __init__(self, state: State = None, parent=None, depth: int =None, action : Actions=None, children : list =None):
        self.state = State() if state == None else state
        self.parent = parent if parent != None else None
        self.depth = 0 if depth == None else depth
        self.children = [None, None, None, None] if children == None else children
        self.action = None if action == None else action
        self.exists = True 
        
    # State to String
    def toString(self):
        return self.state.toString()

    # Node is Solution
    def isSolution(self):
        return self.state.isSolution()

    # Expand the tree
    def expand(self,depth : int = 1):
        if(depth == 0):
            return
        for i in range(4):
            if self.children[i] != None:
                continue
            values = deepcopy(self.state.values) # copy of the values
            indx = deepcopy(self.state.indexOfZero) # copy of the index of zero
            newState : State = State(values=values,indexOfZero=indx)
            newState.move(Actions(i))
            if(newState.exists):
                self.children[i]= Node(newState,self,self.depth+1,Actions(i))
                if(depth-1):
                    self.children[i].expand(depth-1)