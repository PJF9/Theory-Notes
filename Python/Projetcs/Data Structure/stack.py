class Stack:
    """
    Todo: __iadd__(self, intager)

    This class is implementing the Stack data structure

    ...


    Attributes
    ----------
    stack: list
        This is the container list, that will store all the
        Stack's element

    index: int
        This is a helping index that cna guide us inside the iterator.
        An iterator is build when we use a for loop

    
    Normall Methods
    ---------------
    push(elem):
        This method inserts the given element at the end of the stack list

    pop():
        This method deletes and returns the last element of the stack list

    peek():
        This method returns the last element of the stack list

    copy(right_obj):
        This method is copying the given Stack object to the object we are
        working with

    clear():
        Deletes all the stack's list elements


    Dunder Methods
    --------------
    init(*args):
        This method initializes ( coinstructs ) the Stack object

    str():
        This method converts the Stack object into a string to help us
        printing it on the console

    len():
        This method returns the length of the Stack object

    iter():
        This method is converting the Stack object into an iterator.
        This is usefull in the for loops. If we skip this method then we 
        couldn't use the (for elem in loop) statement

    next():
        This method returns the next element of the stack list. Again this
        is very usefull inisde a for loop. The same logic as the iter() method.
        This method goes to the  next element of the iterator

    getitem(index):
        This method is returning the element of the stack list that exist in the
        given index position using the '[]' operator

    iadd(times):
        This method is expanding the Stack with elements same of the stack list
        elements data type, times ammount of times

    eq(right_ob):
        This method helps us compare two Stack objects with the '==' operator

    lt(right_ob):
        This method helps us compare two Stack objects with the '<' and '>'
        operators

    le(right_obj):
        This method helps us compare two Stack objects with the '<=' and '<='
        operators
    """ 

    def __init__(self, *args):
        """
        This method initializes ( coinstructs ) the Stack object

        ...


        Parameters
        ----------
        *args: list
            This list is helps us contruct a Stack object with elements
        """

        self.stack = []
        for elem in args:
            self.stack.append(elem)

        self.index = 0


    def push(self, elem):
        """
        This method inserts the given element at the end of the stack list

        Syntax: self.push(elem)

        ...


        Parameters
        ----------
        elem: any data type
            This parameter is the element that will be inserted into the stack list
        """

        self.stack.append(elem)

    
    def pop(self):
        """
        This method deletes and returns the last element of the stack list

        Syntax: var = self.pop()

        ...


        Raises
        ------
        IndexError:
            If the user tries to delete an element from an empty Stack object

        
        Return Value
        ------------
        stack.pop(): any data type
            This is the last element of the stack list
        """

        if self.stack != []:
            return self.stack.pop()
        
        raise IndexError("You can't delete from an empty Stack")

    
    def peek(self):
        """
        This method returns the last element of the stack list

        Syntax: var = self.peek()

        ...


        Raises
        ------
        IndexError:
            If the user tries to peek on an empty Stack object


        Return Value
        -----------
        stack[-1]: any data type
            This is the last element of the stack list
        """

        if self.stack != []:
            return self.stack[-1]
        else:
            raise IndexError("Stack object is empty, has no elements")


    def copy(self, copy_obj):
        """
        This method is copying the given Stack object to the object we are
        working with

        Syntax: self = self.copy(right_obj)

        ...


        Parameters
        ----------
        copy_obj: Stack
            This is the Stack object that we will copy into the one that we are
            working with


        Raises
        ------
        TypeError:
            If the user tries to copy an object with defferent data type than Stack


        Return Value
        ------------
        The Stack object
        """

        if not isinstance(copy_obj, Stack):
            raise TypeError("You can only copy Stack objects")

        self.clear()

        for elem in copy_obj:
            self.push(elem)

        return self


    def clear(self):
        """
        Deletes all the stack's list elements

        Syntax: self.clear()

        ...
        """
        
        for _ in range(len(self)):
            self.pop()


    def __str__(self):
        """
        This method converts the Stack object into a string to help us
        printing it on the console

        ...


        Return Value
        ------------
        The stack list that is converted into a string
        """

        return f"{self.stack}"        


    def __len__(self):
        """
        This method returns the length of the Stack object

        ...


        Return Value
        ------------
        Returns the length of the stack list
        """

        return len(self.stack)

    
    def __iter__(self):
        """
        This method is converting the Stack object into an iterator.
        This is usefull in the for loops. If we skip this method then we 
        couldn't use the (for elem in loop) statement

        ...


        Return Value
        ------------
        The Stack object
        """

        return self


    def __next__(self):
        """
        This method returns the next element of the stack list. Again this
        is very usefull inisde a for loop. The same logic as the iter() method.
        This method goes to the  next element of the iterator

        ...


        Raises
        ------
        StopIteration:
            To help us break out of the for loop when the Stack object has no
            more elements


        Return Value
        ------------
        ret_elem: any data type
            This is the element that the index attribute is showing on the iterator
        """

        if self.index > len(self) - 1:
            raise StopIteration
        
        ret_elem = self.stack[self.index]
        self.index += 1

        return ret_elem


    def __getitem__(self, index):
        """
        This method is returning the element of the stack list that exist in the
        given index position using the '[]' operator

        ...


        Raises
        ------
        TypeError:
            If the user give an invalid data type for indexing

        IndexError:
            If the user give an invalid index position


        Return Value
        ------------
        stack[index]: any data type
            This is the element that exist on the given index position
        """

        if not isinstance(index, int):
            raise TypeError("Index must be an intager")
        
        elif (index > len(self) - 1) or (index < 0):
            raise IndexError("Invalid index position: index out of range")
            
        else:
            return self.stack[index]


    def __iadd__(self, times):
        """
        This method is expanding the Stack with elements same of the stack list
        elements data type, times ammount of times

        ...


        Parameters
        ----------
        times: int


        Raises
        ------
        TypeError:
            If the user tries to add a Stack object with a defferente data type other
            than int

        IndexError:
            If the syack list is empty, because we are trying to take the data type of the
            first element. If is empty then we are going to fill it with 0


        Return Value
        ------------
        The Stack object
        """

        if not isinstance(times, int):
            raise TypeError("The right object of the += operator must be an intager")

        try:
            if isinstance(self.stack[0], int):
                for _ in range(times):
                    self.push(0)

            elif isinstance(self.stack[0], float):
                for _ in range(times):
                    self.push(0.0)

            elif isinstance(self.stack[0], str):
                for _ in range(times):
                    self.push("_")
            else:
                for _ in range(times):
                    self.push(0)

        except IndexError:
            for _ in range(times):
                self.push(0)

        return self


    def __eq__(self, right_ob):
        """
        This method helps us compare two Stack objects with the '==' operator

        ...


        Raises
        ------
        TypeError:
            If the user tries to compare a Stack object with a defferent object


        Return Value
        ------------
        equal: bool
            The result of the comparisson of the 2 Stack object
        """
        
        equal = True

        if not isinstance(right_ob, Stack):
            raise TypeError("You can only compare two Stack objects")
        elif len(self) != len(right_ob):
            equal = False
        else:
            for index in range(len(self)):
                if self[index] != right_ob[index]:
                    equal = False
                    break
            
        return equal
    

    def __lt__(self, right_ob):
        """
        This method helps us compare two Stack objects with the '<' and '>'
        operators

        ...


        Raises
        ------
        TypeError:
            If the user tries to compare a Stack object with a defferent object


        Return Value
        ------------
        equal: bool
            The result of the comparisson of the 2 Stack object
        """

        if not isinstance(right_ob, Stack):
            raise TypeError("You can only compare two Stack objects")
        else:
            return len(self) < len(right_ob)


    def __le__(self, right_ob):
        """
        This method helps us compare two Stack objects with the '<=' and '<='
        operators

        ...


        Raises
        ------
        TypeError:
            If the user tries to compare a Stack object with a defferent object


        Return Value
        ------------
        equal: bool
            The result of the comparisson of the 2 Stack object
        """

        if not isinstance(right_ob, Stack):
            raise TypeError("You can only compare two Stack objects")

        return (len(self) < len(right_ob)) or (self == right_ob)
