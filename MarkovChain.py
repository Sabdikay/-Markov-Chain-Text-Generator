import random

#Defining graph in terms of verticles
class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent = {} #nodes from this vertex
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge_to(self,next_word,weight = 0): #adding an edge to the vertex we input with weight
        self.adjacent[next_word] = weight

    def increment_edge(self,next_word):#incrementing the weight of the edge
        self.adjacent[next_word]=self.adjacent.get(next_word,0) + 1

    def get_probability_map(self):
        #Generate probability mapping for weighted choices.
        self.neighbors = list(self.adjacent.keys())
        self.neighbors_weights = list(self.adjacent.values())


    def next_word(self):#randomly selecting word based on weights!!!
        if self.neighbors:
            return random.choices(self.neighbors, weights=self.neighbors_weights)[0]
        return None

#Putting together in a graph
class Graph:
    def __init__(self):
        self.vertices = {}

    """def get_vertex_words(self): #returning all possible words
        return set(self.vertices.keys())"""


    def add_vertex(self,value):
        if value not in self.vertices:
            self.vertices[value] = Vertex(value)

    def get_vertex(self,value):
        if value not in self.vertices:#if word not in the graph
            self.add_vertex(value)
        return self.vertices[value] #getting the Vertex object

    """def get_next_word(self,current_vertex):
        return self.vertices[current_vertex.value].next_word()"""


    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()




