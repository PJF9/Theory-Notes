class Queue:
    """
    This class is impleting the Queue data structure

    ...


    Attributes
    ----------
    queue: list
        This is the container. The list that will hold all the
        elements
    
    index: int
        This is the helping index to guide us inside the iterable.
        So we can use a Queue object inside a for loop
    

    Normal Methods
    --------------
    enqeueu(elem):
        This method inserts the given element to the end of the queue list
    
    deqeueu():
        This method deletes and inserts the first element of the queue list

    peek():
        This method is returning the first element of the queue list

    copy(copy_obj):
        This method is going to copy all the elements from the argumented 
        Queue object to the object we are working with

    clear():
        This method removes all the element from the queue list


    Dunder Methods
    --------------
    init(*args):
        This method is inisializing ( cunstruction ) the Queue object

    str():
        This method convert the Queue object into a string one so we can 
        print it on the console

    len():
        This method returns the length of the queue list

    iter():
        This method convert the Queue object into an iterator so we can
        use it inside a for loop

    next():
        This method applies only on iterators. It returns the next element
        of the Queue object

    getitem(index):
        This method helps us get an element of the Queue via the '[]' operator

    iadd(times):
        This method is expanding the Queue with elements same of the queue list
        elements data type, times ammount of times
    
    eq():
        This method helps us use the '==' operator in a condition between
        Queue objects
    
    lt():
        This method helps us use the '<' and the '>' operators in a condition 
        between Queue objects

    le():
        This method helps us use the '<=' and the '>=' operators in a condition
        between Queue objects
    """
    

    def __init__(self, *args):
        """
        This method is inisializing ( cunstruction ) the Queue object

        ...


        Parameters
        ----------
        *args: list
            This list is helps us contruct a Queue object with elements
        """

        self.queue = []
        for elem in args:
            self.queue.append(elem)
            
        self.index = 0


    def enqeueu(self, elem):
        """
        This method inserts the given element to the end of the queue list

        Syntax: self.enqueue(elem)
        
        ...


        Parameters
        ----------
        elem: any data type
            This is the element that will be inserted into the qeueu list
        """

        self.queue.append(elem)


    def dequeue(self):
        """
        This method deletes and inserts the first element of the queue list
        
        Syntax: var = self.dequeue()

        ...


        Raises
        ------
        IndexError:
            If the user tried to remove an element from an empty Queue object


        Return Value
        ------------
        queue.pop(0): any data type
            This is the deleted first element of the queue list

        """

        if self.queue != []:
            return self.queue.pop(0)
        else:
            raise IndexError("You can't dequeue in an empty Queue")


    def peek(self):
        """
        This method is returning the first element of the queue list

        Syntax: var = self.peek()

        ...


        Raises
        ------
        IndexError:
            If the user tries to peek on an empty Queue object


        Return Value
        --------------
        queue[0]: any data type
            The first element of the queue list
        """

        if self.queue != []:
            return self.queue[0]
        else:
            raise IndexError("Stack obejct is empty, has no elements")


    def copy(self, copy_obj):
        """
        This method is going to copy all the elements from the argumented 
        Queue object to the object we are working with

        Syntax: self = self.copy(copy_obj)

        ...


        Parameters
        ----------
        copy_obj: Queue
            This is the Queue object that we will copy the elemenets from

        
        Raises
        ------
        TypeError:
            If the user tries to copy an object with defferent data time than Queue

        
        Return Value
        ------------
        The Queue object
        """

        if not isinstance(copy_obj, Queue):
            raise TypeError(f"You can only copy Queue object")

        self.clear()

        for elem in copy_obj:
            self.enqeueu(elem)

        return self

    
    def clear(self):
        """
        This method removes all the element from the queue list

        Syntax: self.clear()

        ...
        """

        for _ in range(len(self)):
            self.dequeue()


    def __str__(self):
        """
        This method convert the Queue object into a string one so we can 
        print it on the console

        ...


        Return Value
        ------------
        ret_st: str
            The string that we have convert the Queue object
        """

        return f"{self.queue}"


    def __iter__(self):
        """
        This method convert the Queue object into an iterator so we can
        use it inside a for loop

        ...

        
        Return Value
        ------------
        The Queue object
        """

        return self


    def __next__(self):
        """
        This method applies only on iterators. It returns the next element
        of the Queue object

        ...


        Raises
        ------
        StopIteration:
            If the queue list left with no elements after the iteration.
            Helps us break out the for loop


        Return Value
        ------------
        ret_elem: any data type
            The element of the queue list that exists on the self.index position
        """

        if self.index > len(self) - 1:
            raise StopIteration
        
        ret_elem = self.queue[self.index]
        self.index += 1

        return ret_elem


    def __getitem__(self, index):
        """
        This method helps us get an element of the Queue via the '[]' operator

        ...


        Parameters
        ----------
        index: int
            This parameter is the index position of the element the user want
            to get


        Return Value
        ------------
        queue[index]: any data type
            The element of the given index position.
        """

        if not isinstance(index, int):
            raise TypeError("The given index position must be an intager")
        elif (index > len(self)) or (index < 0):
            raise IndexError("Invalid index position: index out of range")
        else:
            return self.queue[index]


    def __len__(self):
        """
        This method returns the length of the queue list

        ...


        Return Value
        ------------
        len(queue): int
            This is the length of the Queue object

        """

        return len(self.queue)


    def __iadd__(self, times):
        """
        This method is expanding the Queue with elements same of the queue list
        elements data type, times ammount of times

        ...


        Parameters
        ----------
        times: int


        Raises
        ------
        TypeError:
            If the user tries to add a Queue object with a defferente data type other
            than int

        IndexError:
            If the queue list is empty, because we are trying to take the data type of the
            first element. If is empty then we are going to fill it with 0


        Return Value
        ------------
        The Queue object
        """

        if not isinstance(times, int):
            raise TypeError("The right object of the += operator must be an intager")

        try:
            if isinstance(self.queue[0], int):
                for _ in range(times):
                    self.enqeueu(0)

            elif isinstance(self.queue[0], float):
                for _ in range(times):
                    self.enqeueu(0.0)

            elif isinstance(self.queue[0], str):
                for _ in range(times):
                    self.enqeueu("_")
            else:
                 for _ in range(times):
                    self.enqeueu(0)

        except IndexError:
            for _ in range(times):
                self.enqeueu(0)

        return self


    def __eq__(self, right_ob):
        """
        This method helps us use the '==' operator in a condition between
        Queue objects

        ...


        Parameters
        ----------
        right_ob: Queue
            This is the object that will take the other place at the conditions

        
        Raises
        ------
        TypeError:
            If the user tries to compare a Queue object with some defferent
            data type than Queue

        
        Return Value
        ------------
        equal: bool
            The output of the condition so we can use it on if statements
        """

        if not isinstance(right_ob, Queue):
            raise TypeError("The other object that joins the condition must be a Queue object")

        equal = True

        if len(self) == len(right_ob):
            for i in range(len(self)):
                if self[i] != right_ob[i]:
                    equal = False
                    break
        else:
            equal = False

        return equal


    def __lt__(self, right_ob):
        """
        This method helps us use the '<' and the '>' operators in a condition 
        between Queue objects

        ...


        Parameters
        ----------
        right_ob: Queue
            This is the object that will take the other place at the conditions

        
        Raises
        ------
        TypeError:
            If the user tries to compare a Queue object with some defferent
            data type than Queue

        
        Return Value
        ------------
        bool
            The output of the condition so we can use it on if statements
        """

        if not isinstance(right_ob, Queue):
            raise TypeError("The other object that joins the condition must be a Queue object")

        if len(self) < len(right_ob):
            return True

        return False


    def __le__(self, right_ob):
        """
        This method helps us use the '<=' and the '>=' operators in a condition
        between Queue objects

        ...


        Parameters
        ----------
        right_ob: Queue
            This is the object that will take the other place at the conditions

        
        Raises
        ------
        TypeError:
            If the user tries to compare a Queue object with some defferent
            data type than Queue

        
        Return Value
        ------------
        bool
            The output of the condition so we can use it on if statements
        """
        if not isinstance(right_ob, Queue):
            raise TypeError("The other object that joins the condition must be a Queue object")

        if (len(self) < len(right_ob)) or (self == right_ob):
            return True

        return False
