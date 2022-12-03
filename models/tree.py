import os
from collections import deque
from models.node import Node
from models.actions import Actions
class Tree:
    # Create a tree of 4 states/children
    def __init__(self,startingNode : Node = None, limit : int = None):
        self.root = Node() if startingNode == None else startingNode
        self.limit = limit if limit != None else 1
        self.travelCost = 0
        self.visited = {}
        self.solution = None
    
    def _findPath(self, node : Node):
        path = []
        while node != None:
            path.append(node)
            node = node.parent
        path.reverse()
        return path
    
    def printPath(self):
        # print(len(self.visited))
        
        if(self.solution != None):
            print("\t\t--Solucion encontrada--")
            print(f'Costo de viaje: {self.travelCost}')
            print(f'Profunidad: {self.solution.depth}')
            print(self.solution.toString())
            print("".rjust(50,"-"))
            
            print("\t--Pasos para llegar a la solución--")
            print(f'El camino a la solucion tiene {self.solution.depth} pasos')
            input("Presione enter para ver el camino")
            counter = self.solution.depth
            path = self._findPath(self.solution)
            nextInd = 1
            for i in path:
                os.system('cls')
                print(f'Estados restantes: {counter}')
                print("Siguiente Estado:", end=" ")
                if(nextInd == len(path)):
                    print("N/A")
                else:
                    if(path[nextInd].action == Actions.UP):
                        print("Arriba")
                    elif(path[nextInd].action == Actions.RIGHT):
                        print("Derecha")
                    elif(path[nextInd].action == Actions.DOWN):
                        print("Abajo")
                    elif(path[nextInd].action == Actions.LEFT):
                        print("Izquierda")
                    else:
                        print()
                print("".rjust(50,"-"))
                print(i.toString())
                print("".rjust(50,"-"))
                input("Presione enter para continuar . . .")
                counter -= 1
                nextInd += 1
    
    # DFS Recursive Search
    def dfsRecursive(self,limit : int = None):
        self.limit = self.limit if limit == None else limit
        self.visited = {}
        self.travelCost = 0
        self.solution = self._dfs(self.root)
        if(self.solution != None):
            return self.solution
        return None
    
    # DFS  Recursive Search
    def _dfs(self, actualNode : Node):
        # If we are inside the limit
        if(actualNode.depth <= self.limit):
            self.travelCost += 1
            
            # Adding the current state to the visited list
            self.visited[actualNode.state.id] = True
            
            # Check if the state is the goal
            if(actualNode.isSolution()):
                self.travelCost -= 1
                return actualNode
            
            # Expand and iterate throgh childs if not in limit
            if(actualNode.depth != self.limit):
                actualNode.expand(1)
                for i in range(4):
                    currentChild : Node = actualNode.children[i]
                    if currentChild == None:
                        continue
                    if self.visited.get(currentChild.state.id) != None:
                        continue
                    result = self._dfs(currentChild)
                    if(result != None):
                        return result
            return None
        else:
            return None
    
    # DFS  Iterative Search
    def dfsIterative(self):
        self.visited = {}
        frontier = deque()
        frontier.append(self.root)
        
        while frontier:
            # Get Last Element Inserted
            node : Node = frontier.pop()
            # If we are inside the limit
            if(node.depth <= self.limit):
                self.travelCost += 1
                
                # If the state has been already visited
                if(self.visited.get(node.state.id) != None):
                    continue
                
                # Marking Node as Visited
                self.visited[node.state.id] = True
                
                # If the actual state is the goal
                if(node.isSolution()):
                    self.travelCost -= 1
                    self.solution = node
                    return node
                
                # If the Node can Expand
                if(node.depth != self.limit):
                    node.expand(1)
                    for i in range(4):
                        if(node.children[i] != None):
                            frontier.append(node.children[i])
        return None

    # BFS Search
    def bfs(self):
        self.visited = {}
        frontier = deque()
        frontier.append(self.root)
        
        while frontier:
            node : Node = frontier.popleft()
            
            #Check if the state has been already visited 
            if(self.visited.get(node.state.id) != None):
                continue
            # Add to Visited Dictionary
            self.visited[node.state.id] = True
            
            # If the actual state is the goal
            if(node.isSolution()):
                self.solution = node
                return node
            
            if(node.depth != self.limit):
                node.expand(1)
                for i in range(4):
                    if(node.children[i] != None):
                        frontier.append(node.children[i])
        return None
    
    def betterFirstSearch(self):
        self.visited = {}
        pass