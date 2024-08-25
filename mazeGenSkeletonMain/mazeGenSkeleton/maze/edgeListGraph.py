from typing import List
from maze.util import Coordinates
from maze.graph import Graph

class EdgeListGraph(Graph):
    """
    Represents an undirected graph using an edge list. This class implements
    the methods required to manipulate and query the graph.
    """

    def __init__(self):
        # Initialize the graph with empty lists for vertices and edges
        self.vertices = []
        self.edges = []

    def addVertex(self, label: Coordinates):
        """
        Adds a vertex to the graph if it doesn't already exist.
        
        :param label: The coordinates of the vertex to be added.
        """
        if not self.hasVertex(label):
            self.vertices.append(label)

    def addVertices(self, vertLabels: List[Coordinates]):
        """
        Adds multiple vertices to the graph.
        
        :param vertLabels: A list of coordinates for the vertices to be added.
        """
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        """
        Adds an edge between two vertices, optionally marking it as a wall.
        
        :param vert1: The coordinates of the first vertex.
        :param vert2: The coordinates of the second vertex.
        :param addWall: A boolean indicating if the edge should be marked as a wall.
        :return: True if the edge was successfully added, False otherwise.
        """
        if self.hasVertex(vert1) and self.hasVertex(vert2) and not self.hasEdge(vert1, vert2):
            self.edges.append((vert1, vert2, addWall))
            return True
        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        """
        Updates the wall status of an edge between two vertices.
        
        :param vert1: The coordinates of the first vertex.
        :param vert2: The coordinates of the second vertex.
        :param wallStatus: A boolean indicating the new wall status.
        :return: True if the wall status was successfully updated, False otherwise.
        """
        if self.hasEdge(vert1, vert2):
            for i, (v1, v2, _) in enumerate(self.edges):
                if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                    self.edges[i] = (v1, v2, wallStatus)
                    return True
        return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        """
        Removes an edge between two vertices if it exists.
        
        :param vert1: The coordinates of the first vertex.
        :param vert2: The coordinates of the second vertex.
        :return: True if the edge was successfully removed, False otherwise.
        """
        if self.hasEdge(vert1, vert2):
            for i, (v1, v2, _) in enumerate(self.edges):
                if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                    self.edges.pop(i)
                    return True
        return False

    def hasVertex(self, label: Coordinates) -> bool:
        """
        Checks if a vertex exists in the graph.
        
        :param label: The coordinates of the vertex to be checked.
        :return: True if the vertex exists, False otherwise.
        """
        return label in self.vertices

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        """
        Checks if an edge exists between two vertices.
        
        :param vert1: The coordinates of the first vertex.
        :param vert2: The coordinates of the second vertex.
        :return: True if the edge exists, False otherwise.
        """
        if self.hasVertex(vert1) and self.hasVertex(vert2):
            for v1, v2, _ in self.edges:
                if (v1 == vert1 and v2 == vert2) or (v2 == vert1 and v1 == vert2):
                    return True
        return False

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        """
        Retrieves the wall status of an edge between two vertices.
        
        :param vert1: The coordinates of the first vertex.
        :param vert2: The coordinates of the second vertex.
        :return: True if the edge is marked as a wall, False otherwise.
        """
        if self.hasEdge(vert1, vert2):
            for v1, v2, wallStatus in self.edges:
                if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                    return wallStatus
        return False

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        """
        Returns a list of neighbouring vertices for a given vertex.
        
        :param label: The coordinates of the vertex for which neighbors are to be found.
        :return: A list of coordinates representing the neighboring vertices.
        """
        neighbours = []
        if self.hasVertex(label):
            for v1, v2, _ in self.edges:
                if v1 == label:
                    neighbours.append(v2)
                elif v2 == label:
                    neighbours.append(v1)
        return neighbours
