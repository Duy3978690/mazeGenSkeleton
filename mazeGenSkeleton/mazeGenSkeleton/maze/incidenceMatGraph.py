# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', 'Tran Duc Duy'
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class IncMatGraph(Graph):
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
            for edge_column in self.edges:
                edge_column.append(0)



    def addVertices(self, vertLabels:List[Coordinates]):
        for label in vertLabels:
            self.addVertex(label)




    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        if self.hasVertex(vert1) and self.hasVertex(vert2):
            new_edge_column = [0] * len(self.vertices)
            new_edge_column[self.vertices.index(vert1)] = 1
            new_edge_column[self.vertices.index(vert2)] = 1
            if addWall:
                new_edge_column.append(1)  # Assuming a special flag for walls, extend the matrix
            self.edges.append(new_edge_column)
            return True
        return False
    


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        ### Implement me! ###
        # remember to return booleans
        pass



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        edge_column_index = None
        for i, edge_column in enumerate(self.edges):
            if edge_column[self.vertices.index(vert1)] == 1 and edge_column[self.vertices.index(vert2)] == 1:
                edge_column_index = i
                break
        if edge_column_index is not None:
            self.edges.pop(edge_column_index)
            return True
        return False
        


    def hasVertex(self, label:Coordinates)->bool:
        return label in self.vertices



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        for edge in self.edges:
            if edge[self.vertices.index(vert1)] == 1 and edge[self.vertices.index(vert2)] == 1:
                return True
        return False



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        pass



    def neighbours(self, label:Coordinates)->List[Coordinates]:
        neighbours = []
        if self.hasVertex(label):
            for edge_column in self.edges:
                if edge_column[self.vertices.index(label)] == 1:
                    for i, value in enumerate(edge_column):
                        if value == 1 and i != self.vertices.index(label):
                            neighbours.append(self.vertices.index(i))
        return neighbours