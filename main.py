# La DFS debera de ser expansiva, es decir, que si encuentra un estado que no ha sido visitado, lo expanda y lo agregue a la lista de visitados.

from models.tree import Tree
from models.node import Node
from models.actions import Actions

# Initial State of the puzzle
n = Node()
print("\t\t--Estado Inicial--")
# n.state.values = [ [2,1,0], [6,4,3], [5,7,8] ]
# n.state.indexOfZero = [0,2]
# n.state.id =210643578
print(n.toString())
MAX_DEPTH = 120
t = Tree(startingNode= n ,limit=MAX_DEPTH)
print(f'Profundidad maxima: {t.limit}')
#Expand Tree Up to 12 Times
t.dfsRecursive()
t.printPath()
print("\t\t-- Ejecución Terminada --")