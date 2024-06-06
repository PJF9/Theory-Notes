class Node:
    """
    This class is represent a node that will included to the linked list
    A node is going to have three parts. One that stores the data that the
    user want, another that will store the memory address of the next 
    list element and one for the previous one

    ...

    
    Atributes
    ---------
    nodes: int
        This is the total node on the tree. It's usefull because by this method we
        can add or delete tree elements much eazier

    data: any data type
        This is the data of the node

    id: int
        The unic number of each node. The root node will get the 0 id number and then
        the other 0 + 1 id number and goes on

    left_: Node, NoneType ( defualt is NoneType )
        This is the refference that will be equal to the left node of the current one

    right_: Node, NoneType ( defualt is NoneType )
        This is the refference that will be equal to the right node of the current one


    Dunder Methods
    --------------
    init(self):
        This is the initializer ( constuctor ) of the node object
    """

    nodes = 0

    def __init__(self, data, left_=None, right_=None):
        """
        This is the initializer ( constuctor ) of the node object

        ...


        Parameters
        ----------
        data: any data type
            This parameter is the data of the node object

        left_: Node, NoneType ( defualt is NoneType )
            This is the refference that will be equal to the left node of the current one

        right_: Node, NoneType ( defualt is NoneType )
            This is the refference that will be equal to the right node of the current one
        """

        self.data = data
        self.left_ = left_
        self.right_ = right_
        self.id = Node.nodes
        
        Node.nodes += 1


class Tree:
    def __init__(self):
        self.root_ = None

    
    #? Creating a private method to help go to a specific node of the tree
    def __goto(self, Id):
        # Create a node refference that is showing to the root of the tree
        n = self.root_
        """
        Each method that requires to go throught the tree needs to be a recursive one 
        """
        def __rec_find(node):
            nonlocal n
            if node is not None:
                # Return the node we want
                if node.id == Id:
                    n = node
                    return node

                __rec_find(node.left_)
                __rec_find(node.right_)

        __rec_find(self.root_)

        return n


    def insert(self, Id, data, on_left=True):
        if Id == -1:
            new_node = Node(data)
            self.root_ = new_node
        elif self.root_ is None: # AtributeError
            print("You Haven't Create A Root Node ( use Id = -1, to create one )")
        elif (Id > Node.nodes - 1) or (Id < 0):
            print("Invalid Inputed Id...")
        else:
            n = self.__goto(Id)

            if n.left_ is None or n.right_ is None:
                if on_left:
                    n.left_ = Node(data)
                else:
                    n.right_ = Node(data)

    
    def replace(self, Id, data):
        if self.root_ is None:
            print("Your tree is empty")
        elif (Id > Node.nodes - 1) or (Id < 0):
            print("Invalid Inputed Id...")
        else:
            self.__goto(Id).data = data


    def pop(self, Id):
        if Id != self.root_.id:
            def __rec_pop(node):
                if node is not None:
                    # This try exept is for the none types ( can also make a decorator )
                    try:
                        if node.left_.id == Id:
                            node.left_ = None
                            Node.nodes -= 1
                    except:
                        pass
                    try:
                        if node.right_.id == Id:
                            node.right_ = None
                            Node.nodes -= 1
                    except:
                        pass
                    
                    __rec_pop(node.right_)
                    __rec_pop(node.left_)

            __rec_pop(self.root_)
        else:
            self.clear()


    def remove(self, data, dupl=False):
        var = False
        if data != self.root_.data:
            def __rec_remove(node):
                nonlocal var
                if var:
                    return

                if node is not None:
                    try:
                        if node.left_.data == data:
                            node.left_ = None 
                            Node.nodes -= 1
                            
                            if not dupl:
                                var = True
                                return
                    except:
                        pass
                    try:
                        if node.right_.data == data:
                            node.right_ = None
                            Node.nodes -= 1

                            if not dupl:
                                var = True
                                return
                    except:
                        pass

                    __rec_remove(node.left_)
                    __rec_remove(node.right_) 
                    
            __rec_remove(self.root_)
        else:
            self.clear()


    def clear(self):
        self.root_ = None
        Node.nodes = 0


    def print_ids(self):
        ret_str = ""
        def rec_print_id(node):
            if node is not None:
                nonlocal ret_str
                ret_str += str(node.id)
                ret_str += "("
                rec_print_id(node.left_)
                ret_str += ","
                rec_print_id(node.right_)
                ret_str += ")"
            else:
                ret_str += "_"

        rec_print_id(self.root_)

        return ret_str


    def __str__(self):
        ret_st = ""
        def __rec_str(node):
            # We need nonlocal because we want this ret_str to be equal to the outside ret_str
            nonlocal ret_st
            # This condition help us break for the recrusion loop
            if node is not None:
                ret_st += str(node.data)
                ret_st += "("
                __rec_str(node.left_) #* First call the recrusion for the left node of the current node
                ret_st += ","
                __rec_str(node.right_) #* And then for the right one
                ret_st += ")"
            else:
                ret_st += "_" #* If node is missing

        # Calling the recrusion for the first time
        __rec_str(self.root_)

        return ret_st



class Binary_Search_Tree(Tree):
    def __init__(self):
        super().__init__()

    def b_insert(self, data):
        if self.root_ is None:
            self.insert(-1, data, True)
        else:
            n = self.root_

            while True:
                if data == n.data:
                    print("This node already exist...")
                    break
                elif data < n.data:
                    if n.left_ is None:
                        n.left_ = Node(data)
                        break
                    else:
                        n = n.left_
                else:
                    if n.right_ is None:
                        n.right_ = Node(data)
                        break
                    else:
                        n = n.right_

    def inorder(self):
        ret_list = []

        def rec_inorder(node):
            nonlocal ret_list

            if node is not None:
                rec_inorder(node.left_)
                ret_list.append(node.data)
                rec_inorder(node.right_)

        rec_inorder(self.root_)

        return ret_list