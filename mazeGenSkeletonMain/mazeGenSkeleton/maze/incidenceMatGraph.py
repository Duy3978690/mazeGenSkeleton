from typing import List
from maze.util import Coordinates
from maze.graph import Graph

class IncMatGraph(Graph):
    """
    Represents an undirected graph using an incidence matrix.
    This class implements the methods required to manipulate and query the graph.
    """

    def __init__(self):
        # Initialize the graph with empty lists for vertices and edges (incidence matrix columns)
        self.vertices = []
        self.edges = []

    def addVertex(self, label: Coordinates):
        """
        Adds a vertex to the graph if it doesn't already exist.
        Also, appends a 0 to each edge column in the incidence matrix to accommodate the new vertex.

        :param label: The coordinates of the vertex to be added.
        """
        if not self.hasVertex(label):
            self.vertices.append(label)
            # Extend each existing edge column in the incidence matrix with 0 (no connection)
            for edge_column in self.edges:
                edge_column.append(0)

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
        The edge is represented as a column in the incidence matrix.

        :param vert1: The coordinates of the first vertex.
        :param vert2: The coordinates of the second vertex.
        :param addWall: A boolean indicating if the edge should be marked as a wall.
        :return: True if the edge was successfully added, False otherwise.
        """
        if self.hasVertex(vert1) and self.hasVertex(vert2):
            # Create a new edge column initialized with 0's for all vertices
            new_edge_column = [0] * len(self.vertices)
            # Mark the presence of the edge between vert1 and vert2
            new_edge_column[self.vertices.index(vert1)] = 1
            new_edge_column[self.vertices.index(vert2)] = 1
            if addWall:
                # Store the status of the wall as the last element in the column
                new_edge_column.append(1)
            self.edges.append(new_edge_column)
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
            edge_index = None
            vertex_index_1 = self.vertices.index(vert1)
            vertex_index_2 = self.vertices.index(vert2)
            # Find the edge column that connects vert1 and vert2
            for i, edge in enumerate(self.edges):
                if edge[vertex_index_1] == 1 and edge[vertex_index_2] == 1:
                    edge_index = i
                    break
            if edge_index is not None:
                # Update the last element of the edge column to represent the new wall status
                self.edges[edge_index][-1] = int(wallStatus)
                return True
        return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        """
        Removes an edge between two vertices if it exists.

        :param vert1: The coordinates of the first vertex.
        :param vert2: The coordinates of the second vertex.
        :return: True if the edge was successfully removed, False otherwise.
        """
        edge_column_index = None
        if self.hasEdge(vert1, vert2):
            vertex_index_1 = self.vertices.index(vert1)
            vertex_index_2 = self.vertices.index(vert2)

        # Find the edge column that connects vert1 and vert2
        for i, edge_column in enumerate(self.edges):
            if edge_column[vertex_index_1] == 1 and edge_column[vertex_index_2] == 1:
                edge_column_index = i
                break
        if edge_column_index is not None:
            # Remove the edge column from the incidence matrix
            self.edges.pop(edge_column_index)
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
            vertex_index_1 = self.vertices.index(vert1)
            vertex_index_2 = self.vertices.index(vert2)

        for edge in self.edges:
            if edge[vertex_index_1] == 1 and edge[vertex_index_2] == 1:
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
            vertex_index_1 = self.vertices.index(vert1)
            vertex_index_2 = self.vertices.index(vert2)

        if self.hasEdge(vert1, vert2):
            for edge in self.edges:
                if edge[vertex_index_1] == 1 and edge[vertex_index_2] == 1:
                    return bool(edge[-1]) 
        return False

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        """
        Returns a list of neighboring vertices for a given vertex.

        :param label: The coordinates of the vertex for which neighbors are to be found.
        :return: A list of coordinates representing the neighboring vertices.
        """
        neighbours = []
        if self.hasVertex(label):
            vertex_label_idx = self.vertices.index(label)
            # Iterate over all edges to find neighbors
            for edge_column in self.edges:
                if edge_column[vertex_label_idx] == 1:
                    for i, value in enumerate(edge_column[:-1]):
                        if value == 1 and i != vertex_label_idx:
                            # Append the vertex corresponding to the neighbor
                            neighbours.append(self.vertices[i])
        return neighbours
