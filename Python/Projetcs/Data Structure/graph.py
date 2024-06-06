from queue import Queue


"""
    Creating the node class
"""
class Node:
    def __init__(self, data, neighbours=None):
        self.data = data
        if neighbours is Node:
            neighbours = []
        else:
            self.neighbours = neighbours


"""
    Creating the graph class
"""
class Graph:
    def __init__(self):
        self.nodes = []


    def __str__(self):
        ret_st = ""
        for node in self.nodes:
            ret_st += f"\n{node.data}: "
            if node.neighbours is not None:
                for n in node.neighbours:
                    ret_st += f" {n.data}"

        return ret_st

    
    def __index_of(self, data):
        for index in range(len(self.nodes)):
            if self.nodes[index].data == data:
                return index


    def add_vertex(self, data="", neighbours=None):
        if neighbours is None:
            neighbours = []
        self.nodes.append(Node(data, neighbours))


    def add_edge(self, data1, data2):
        index1 = self.__index_of(data1)
        index2 = self.__index_of(data2)

        self.nodes[index1].neighbours.append(self.nodes[index2])
        self.nodes[index2].neighbours.append(self.nodes[index1])


    def get_neighbours(self, data):
        return self.nodes[self.__index_of(data)].neighbours


    """
    This method is finding the quickest path to go to a node

    starting_node_data: This is the data of the node we want to start the algorithm
    end_node_data: This is the data if the node we want to end
    """
    def breadth_first_search(self, starting_node_data, end_node_data):
        # This qeueu is help us 1. Break out of the loop, 2. Get the neighbour loop again
        q = Queue()
        discovered = [starting_node_data] #* In this list will inserted all the neighbour nodes from the starting one
        q.enqeueu(starting_node_data)
        # This dictionary is going to collect all the previous nodes for each node ( only one "parent" ) to the path
        parent = {}

        # The main loop
        while len(q) > 0:
            v = q.dequeue() #* Get the curr node

            # Breaking condition
            if v == end_node_data:
                break
            
            # Get each neighbour of the curr node
            for neighbour in self.get_neighbours(v):
                # Add to the list
                if neighbour.data not in discovered:
                    discovered.append(neighbour.data)

                # Pass the current node as the parent of the next node
                parent[neighbour.data] = v
                q.enqeueu(neighbour.data) #* Keep the algorithm going

        # Finding the path
        """
        If I think about it I will get it ( mindlowing )
        """
        path = [end_node_data]
        while path[0] != starting_node_data:
            path = [parent[path[0]]] + path

        # Return the path list
        return path


g = Graph()
for person in ["Bob", "Carl", "Anne", "Diana", "Luisa"]:
    g.add_vertex(person)

g.add_edge("Bob", "Carl")
g.add_edge("Bob", "Anne")
g.add_edge("Bob", "Diana")
g.add_edge("Anne", "Diana")
g.add_edge("Anne", "Luisa")
g.add_edge("Luisa", "Carl")
g.add_edge("Diana", "Carl")


print(g, "\n")
g.breadth_first_search("Carl", "Anne")