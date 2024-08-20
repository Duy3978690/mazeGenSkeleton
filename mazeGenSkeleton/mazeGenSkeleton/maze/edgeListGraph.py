# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>'Tran Duc Duy'24, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class EdgeListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        self.vertices = []
        self.edges = []



        
    def addVertex(self, label:Coordinates):
        if not self.hasVertex(label):
            self.vertices.append(label)



    def addVertices(self, vertLabels:List[Coordinates]):
        for label in vertLabels:
            self.addVertex(label)




    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:


        


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        ### Implement me! ###
        # remember to return booleans
        pass



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        pass
        


    def hasVertex(self, label:Coordinates)->bool:
        return label in self.vertices
        pass



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        pass



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        pass
        
    


    def neighbours(self, label:Coordinates)->List[Coordinates]:
        ### Implement me! ###
        # remember to return list of coordinates
        pass
        