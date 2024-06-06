import double_linked_list as dll


class Node:
    """ 
    This class is represent a node that will included to the linked list
    A node is going to have two parts. One that stores the data that the
    user want and another that will store the memory address of the next 
    list element

    ...


    Atributes
    ---------
    data: any data type
        This is the data that the user wants

    next_: Node, NoneType
        This is a refference that is locatited at the same memory location
        as the next node of the list


    Dunder Methods
    --------------
    init(data, next_=None):
        This method is the initializer ( constructor ) of the node object
    """

    def __init__(self, data, next_=None):
        """
        This method is the initializer ( constructor ) of the node object

        ...


        Parameters
        ----------
        data: any data type
            This is data that the user want to place at the node
        
        next_: Node, None ( default is None )
            This variable is "pointing" to the next element of the list
        """
        
        self.data = data
        self.next_ = next_


class Single_Linked_List:
    """
    This is implementing the Single Linked List data struncture

    ...


    Attributes
    ----------
    *args: list
        This is the starting elemenents that the list contains
    
    head: Node, NoneType
        This is the refference of the first element on the list

    help_index: int
        This index variable will help us go throught the element of
        the list inside a loop ( used on __next__() method )

    
    Normal Methods
    --------------
    push_front(self, element):
        This method inserts a given element to the start of the list

    push_back(self, element):
        This method inserts a given element to the end of the list

    insert_into(self, index, element):
        This method inserts a given element to the given index
        position of the list
    
    extend(self, list_ob):
        This method extends the list with the given one ( the given
        list goes to the end of the current one )

    pop_front(self):
        This method deletes the first element of the list
        
    pop_back(self):
        This method deletes the last element of the list

    pop(self, index, total_places=0):
        This method deletes an element of the list based on the given
        index

    remove(self, value, dupl=False):
        This method deletes, an element / or more, of the list bases on the 
        given value

    ndupl(self):
        This method is deleting all the duplicate elements of the list

    clear(self):
        This method erases all the list element

    copy(self, list_ob):
        This method takes all the elements from the given list and append them
        to the cleared current list

    sort(self):
        This method sorts the current list

    rev_sort(self):
        This method sorts the list by the oposite direction

    reverse(self):
        This method reverses the list

    slce(self, start, end, step=1):
        This method applies the slicing method to the list

    slicing(self, start, end, step=1):
        This method is the same like slce but instead of a list
        it returns an iterator that we can loop over 

    count(self, value):
        This method has as argument an element and iterate throught the list
        and counting the total time this item exists

    index(self, value):
        This method return the index position of the given element on the list

    indexes(self, value):
        This method returns a list with all the index positons that the given
        element exist on the list


    Dunder Methods
    --------------
        init(self, *args):
            This method initializes ( constructs ) the list object

        iter(self):
            This method converts the list obejct into an itarator so we 
            can use it on a for loop

        next(self):
            This method applies on an iterator and returns us the next
            iterator element

        getitem(self, index):
            This method overloads the [] operator so we can print list
            elements eazily

        setitem(self, index, value):
            This method overloads the [] operator so we can set a list
            element eazily
        
        len(self):
            This method returns the lenght of the list

        str(self):
            This method converts the list into a string so we can print it

        iadd(self, right_ob):
            This method overloads the '+=' operator so we can use it for 
            linked list objects

        isub(self, right_ob):
            This method overload the '-=' operator so we can use it for 
            linked list objects

        imul(self, times):
            This method overloads the '*=' operator so we can use it for 
            linked list objects
            
        add(self, right_ob):
            This method overloads the '+' operator so we can use it for 
            linked list objects

        sub(self, right_ob):
            This method overloads the '-' operator so we can use it for 
            linked list objects

        mul(self, right_ob):
            This method overloads the '*' operator so we can use it for 
            linked list objects

        eq(self, right_ob):
            This method overloads the '==' operator so we can compare list
            objects

        lt(self, right_ob)
            This method overloads the '<' operator so we can compare
            list objects

        le(self, right_ob)
            This method overloads the '<=' operator so we can compare 
            list objects

        gt(self, right_ob)
            This method overloads the '>' operator so we can compare
            list objects

        ge(self, right_ob)
            This method overloads the '>=' operator so we can compare 
            list objects


        Private Methods
        ---------------
        gotto(self, index):
            This method returns the node.data of the element that exists on 
            the given index position of the list
    """

    def __init__(self, *args):
        """
        This method initializes ( constructs ) the list object

        ...


        Parameters
        ----------
        *args: list
            This is the elements that the user want to contain at the contruction 
            of the list
        """

        self.head = None
        self.help_index = 0
        
        for elem in args:
            self.push_back(elem)


    def __gotto(self, index):
        """
        This method returns the node.data of the element that exists on 
        the given index position of the list

        ...


        Parameters
        ----------
        index: int
            This parameter is the index position that we want to get on the list

        
        Raises
        ------
        IndexError:
            When the user inserts an invalid index position
        
        TypeError:
            When the user doesn't pass an intager as an index object


        Return Values
        -------------
        temp.data: any data type
            This is the data of the element that the user wants to go on the list
        """

        temp = self.head
        if not isinstance(index, int):
            raise TypeError("Index object must be an intager")
        elif (index > len(self) - 1) or (index < 0):
            raise IndexError("Invalid index position: index out of bounds")
        else:
            for _ in range(index):
                temp = temp.next_

            return temp.data


    def push_front(self, element):
        """
        This method inserts a given element to the start of the list

        Syntax: self.push_front(element)

        ...


        Parameters
        ----------
        element: any data type
            This parameter is the element that the user wants to add on the list
        """
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_ = self.head
            self.head = new_node

        
    def push_back(self, element):
        """
        This method inserts a given element to the end of the list

        Syntax: self.push_back(element)

        ...


        Parameters
        ----------
        element: any data type
            This parameter is the element that the user wants to add on the list
        """
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next_ is not None:
                temp = temp.next_

            temp.next_ = new_node


    def insert_into(self, index, element):
        """
        This method inserts a given element to the given index
        position of the list

        Syntax: self.insert_into(index, element)

        ...


        Parameters
        ----------
        index: int
            This is the index that the user wnats to add the element
        
        element: any data type
            The element that the user wants to add to the list

        
        Raises
        ------
        IndexError:
            When the user tries to insert an element to an invalid index 
            position

        TypeError:
            When the user tries to pass as an index an object deferent that 
            intager
        """
        
        if not isinstance(index, int):
            raise TypeError("Index object must be an intager")
        elif ((index > len(self) - 1) or (index < 0)) and ((self.head is not None) or (index != 0)):
            raise IndexError("Invalid index position: index out of range")
        else:
            new_node = Node(element)

            if self.head is None:
                self.head = new_node
            elif index == 0:
                self.push_front(element)
            else:
                temp = self.head
                for _ in range(index):
                    temp = temp.next_

                new_node.next_ = temp.next_
                temp.next_ = new_node


    def extend(self, list_ob):
        """
        This method extends the list with the given one ( the given
        list goes to the end of the current one )

        Syntax: self.extend(list_ob)

        ...


        Parameters
        ----------
        list_ob: list, Single_Linked_List, Double_Linked_List
            This parameter is the list that will give it's elements to the current
            list object


        Raises
        ------
        AtributeError:
            When the user tries to copy form an unkown object


        Return Value
        ------------
        The updated object
        """

        if not isinstance(list_ob, Single_Linked_List) and not isinstance(list_ob, list) \
            and not isinstance(dll.Double_Linked_List):
            raise AttributeError("You can only extend the list with only iterables objects")
        
        for index in range(len(list_ob)):
            self.push_back(list_ob[index])

        return self


    def pop_front(self):
        """
        This method deletes the first element of the list

        Syntax: self.pop_front()

        ...


        Raises
        ------
        TypeError:
            When the user tries to delete from an empty list
        """

        if self.head is None:
            raise TypeError("You can't delete from an empty list")
        else:
            self.head = self.head.next_


    def pop_back(self):
        """
        This method deletes the last element of the list

        Syntax: self.pop_back()

        ...


        Raises
        ------
        TypeError:
            When the user tries to delete an element from an empty
            list
        """

        if self.head is None:
            raise TypeError("You can't delete from an empty list")
        elif len(self) == 1:
            self.pop_front()
        else:
            temp = self.head
            for _ in range(len(self) - 2):
                temp = temp.next_
            
            temp.next_ = None

    
    def pop(self, index, total_places=0):
        """
        This method deletes an element of the list based on the given
        index

        Syntax: self.pop(index, total_places)

        ...


        Parameters
        ----------
        index: int
            This parameter is the starting index position that will be erazed
            from the list
        
        total_places: int
            This parameter is the total position to the right that will be
            erazed ( not including the index one )


        Raises
        ------
        TypeError:
            When the user passes as an index or a total_places an object
            defferent than intager
            -
            When the user tries to delete from an empty list

        IndexError:
            When the user tries to pass an index that is out of the valid
            positions
        """

        if not isinstance(index, int) and not isinstance(total_places, int):
            raise TypeError("Index and total size parameters must be intagers")
        elif self.head is None:
            raise TypeError("You can't delete from an empty list")
        elif (index > len(self) - 1) or (index < 0):
            raise IndexError("Invalid index position: index out of range")
        elif (index + total_places > len(self) - 1):
            raise IndexError("Invalid index position: not such elements to delete")

        elif index == 0:
            for _ in range(total_places + 1):
                self.pop_front()
        else:
            temp = self.head

            for _ in range(index - 1):
                temp = temp.next_

            curr = temp.next_
            for _ in range(total_places):
                curr = curr.next_

            temp.next_ = curr.next_


    def remove(self, value, dupl=False):
        """
        This method deletes, an element / or more, of the list bases on the 
        given value

        Syntax: self.remove(value, dupl)

        ...


        Parameters
        ----------
        value: any data type
            This parameter is the data that we want to delete from the list
        
        dupl: bool ( default is False )
            This parameter is the choice of deleting only the first element
            that has the given value or not


        Raises
        ------
        TypeError:
            When the user tries to pass the second parameter with a data type
            other than bool
            -
            When the user tries to delete from an empty list
        """

        if not isinstance(dupl, bool):
            raise TypeError("The second argument must be always a bool")
        elif self.head is None:
            raise TypeError("You can't delete from an empty list")
        else:
            if not dupl:
                temp = self.head
                for index in range(len(self)):
                    if (temp.data == value):
                        self.pop(index)
                        break

                    temp = temp.next_
            else:
                not_dupl = []
                for index in range(len(self)):
                    if (self[index] != value):
                        not_dupl.append(self[index])

                self.clear()

                for elem in not_dupl:
                    self.push_back(elem)


    def ndupl(self):
        """
        This method is deleting all the duplicate elements of the list

        Syntax: self.ndupl()

        ...


        Raises
        ------
        TypeError:
            When the user tries to delete from an empty list
        """

        if not self.head:
            raise TypeError("Your list is empty")

        not_dupl = []
        for elem in self:
            if elem not in not_dupl:
                not_dupl.append(elem)

        self.clear()

        for elem in not_dupl:
            self.push_back(elem)


    def clear(self):
        """
        This method erases all the list element

        Syntax: self.clear()

        ...
        """

        self.head = None


    def copy(self, list_ob):
        """
        This method takes all the elements from the given list and append them
        to the cleared current list

        Syntax: self.copy(list_ob)

        ...


        Parameters
        ----------
        list_ob: list, Single_Linked_List, Double_Linked_List
            The list object we want to copy from


        Raises
        ------
        AtributeError:
            When the user tries to copy from an non list obejct

        
        Return Value
        ------------
        The updated object
        """

        if not isinstance(list_ob, Single_Linked_List) and not isinstance(list_ob, list) \
            and not isinstance(list_ob, dll.Double_Linked_List):
            raise AttributeError("You can only copy list objects")

        self.clear()

        for elem in list_ob:
            self.push_back(elem)

        return self


    def sort(self):
        """
        This method sorts the current list

        Syntax: self.sort()

        ...


        Raises
        ------
        TypeError:
            When the user tries to sort an empty list
        """

        if not self.head:
            raise TypeError("You can't sort an empty list")

        for i in range(len(self)):
            for j in range(len(self)):
                if self[i] < self[j]:
                    self[i], self[j] = self[j], self[i]


    def rev_sort(self):
        """
        This method sorts the list by the oposite direction

        Syntax: self.rev_sort()

        ...


        Raises
        ------
        TypeError:
            When the user tires to sort an empty list
        """

        if not self.head:
            raise TypeError("You can't sort an empty list")

        for i in range(len(self)):
            for j in range(len(self)):
                if self[i] > self[j]:
                    self[i], self[j] = self[j], self[i]


    def reverse(self):
        """
        This method reverses the list

        Syntax: self.reverse()

        ...


        Raises
        ------
        TypeError:
            When the user tries to reverse an empty list
        """

        if not self.head:
            raise TypeError("You can't rverse an mepty list")

        for i in range(int(len(self) / 2)):
            self[i], self[len(self) - 1 - i] = self[len(self) - 1 - i], self[i]
        

    def slce(self, start, end, step=1):
        """
        This method applies the slicing method to the list

        Syntax: self.slce(startm end, step)

        ...


        Parameters
        ----------
        start: int
            This parameter is the starting index of the list

        end: int
            This parameter is the ending index ( the algorithm applies
            and for this index position )

        step: int
            This parameter is the step of the slicing


        Raises
        ------
        TypeError:
            When the user tries to pass on any parameter an object defferent
            than intager
            -
            When the user's step is 0

        IndexError:
            When the user tries to slice a more elements that the list contains


        Return Value
        ------------
        ret_list: list
            This is the list that contains the elements from the slicing
        """

        if not isinstance(start, int) or not isinstance(end, int) or not isinstance(step, int):
            raise TypeError("All the parameters must be intagers")
        elif step == 0:
            raise TypeError("Step must be not 0")
        elif start + end > len(self):
            raise IndexError("Invalid index position: no such elements on the list")

        ret_list = []
        for i in range(start, end+1, step):
            ret_list.append(self[i])

        return ret_list


    def slicing(self, start, end, step=1):
        """
        This method is the same like slce but instead of a list
        it returns an iterator that we can loop over

        Syntax: self.slicing(start, end, step)

        ...
        

        Parameters
        ----------
        start: int
            This parameter is the starting index of the list

        end: int
            This parameter is the ending index ( the algorithm applies
            and for this index position )

        step: int
            This parameter is the step of the slicing


        Raises
        ------
        TypeError:
            When the user tries to pass on any parameter an object defferent
            than intager
            -
            When the user's step is 0

        IndexError:
            When the user tries to slice a more elements that the list contains


        Yield Value
        -----------
        The element of the current index position
        """

        if not isinstance(start, int) and not isinstance(end, int) and not isinstance(step, int):
            raise TypeError("All the parameters must be intagers")
        elif step == 0:
            raise TypeError("Step must be not 0")
        elif start + end > len(self):
            raise IndexError("Invalid index position: no such elements on the list")

        for i in range(start, end+1, step):
            yield self[i]


    def count(self, value):
        """
        This method has as argument an element and iterate throught the list
        and counting the total time this item exists

        Syntax: self.count(value)

        ...


        Parameters
        ----------
        value: any data type
            This is the element we want to search on the list

        
        Return Value
        ------------
        ret_count: int
            This is the total times that the given element appears on the list
        """

        ret_count = 0
        
        for elem in self:
            if elem == value:
                ret_count += 1

        return ret_count


    def index(self, value):
        """
        This method return the index position of the given element on the list

        Syntax: self.index(value)

        ...


        Parameters
        ----------
        value: any data type
            This is the element that the user wants to search on the list

        
        Return Value
        ------------
        i: int
            This is the index position of the first element that appear on the list
            and has the given data
        
        -1: int
            If the given value doesn't exist on the list
        """

        for i in range(len(self)):
            if self[i] == value:
                return i

        return -1


    def indexes(self, value):
        """
        This method returns a list with all the index positons that the given
        element exist on the list

        Syntax: self.indexes(value)

        ...


        Parameters
        ----------
        value: any data type
            This is the element that the user wants to search on the list

        
        Return Value
        ------------
        list_indexes: list
            This is the list that contains all the index positions of the
            given element on the list
        """
        
        list_indexse = []

        for i in range(len(self)):
            if self[i] == value:
                list_indexse.append(i)

        return list_indexse


    def __iter__(self):
        """
        This method converts the list obejct into an itarator so we 
        can use it on a for loop

        ...


        Return Value
        ------------
        The object
        """

        return self


    def __next__(self):
        """
        This method applies on an iterator and returns us the next
        iterator element

        ...


        Raises
        ------
        StopIteration:
            This breaks us out of the for loop


        Return Value
        ------------
        ret_elem: any data type
            This is the element that equal to the current refference variable
        """

        if self.help_index == len(self):
            raise StopIteration
        
        ret_elem = self[self.help_index]
        self.help_index += 1

        return ret_elem
        

    def __getitem__(self, index):
        """
        This method overloads the [] operator so we can print list
        elements eazily

        ...


        Parameters
        ----------
        index: int
            This is the index that we want to get from the list

        
        Raises
        ------
        TypeError:
            When the user tries to pass as an index a defferent object than
            an intager

        IndexError:
            When the user tries to pass an invalid index position


        Return Value
        ------------
        __gotto(index): any data type
            This is the data of the index position on the list that the user wants
        """
        
        if not isinstance(index, int):
            raise TypeError("Index object must be an intager")
        elif (index > len(self) - 1) or (index < 0):
            raise IndexError("Invalid index position: index out of bounds")
        else:    
            temp = self.head

            for i in range(len(self)):
                if i == index:
                    return self.__gotto(index)
                
                temp = temp.next_


    def __setitem__(self, index, value):
        """
        This method overloads the [] operator so we can set a list
        element eazily

        ...


        Parameters
        ----------
        index: int
            This is the index position of the element we want to set
            ( to replace )

        value: any data type
            This is the data that the user will replace the list element

        
        Raises
        ------
        TypeError:
            When the user tries to pass an index position with an object
            other than intager

        IndexError:
            When the user tries to pass an invalid index
        """
        
        if not isinstance(index, int):
            raise TypeError("Index position must be an intager")
        elif (index > len(self) - 1) or (index < 0):
            raise IndexError("Invalid index position: index out of bounds")
        else:
            temp = self.head
            for i in range(len(self)):
                if i == index:
                    temp.data = value

                temp = temp.next_


    def __len__(self):
        """
        This method returns the lenght of the list

        ...


        Return Value
        ------------
        lenght: int
            This is the length of the list 
        """
        
        length = 0
        temp = self.head
        
        while temp is not None:
            temp = temp.next_
            length += 1

        return length


    def __str__(self):
        """
        This method converts the list into a string so we can print it

        ...


        Return Value
        ------------
        list_data: str
            This is the converted list into string
        """
        
        list_data = "["
        temp = self.head

        for index in range(len(self)):
            if index == len(self) - 1:
                list_data += str(temp.data)
            else:
                list_data += str(temp.data) + ", "

            temp = temp.next_

        list_data += "]"

        return list_data


    def __iadd__(self, right_ob):
        """
        This method overloads the '+=' operator so we can use it for 
        linked list objects
        -
        If right_ob is intager then we are extend the list right_ob times
        with the data type of the elements of the list
        -
        If not then we will extend the given object to the list

        ...


        Parameters
        ----------
        right_ob: list, int, Single_Linked_List, Double_Linked_List
            This is the object that we will add to the current one


        Raises
        ------
        TypeError:
            When the user tries to pass as a right object one with deffernt
            data type that allowed


        Return Value
        ------------
        The updated obejct
        """

        if not isinstance(right_ob, int) and not isinstance(right_ob, list) \
            and not isinstance(right_ob, Single_Linked_List) and not isinstance(right_ob, dll.Double_Linked_List):
            raise TypeError("Right object must be either an intager or a list object")
        if isinstance(right_ob, int):
            try:
                if isinstance(self[0], int):
                    for _ in range(right_ob):
                        self.push_back(0)

                elif isinstance(self[0], float):
                    for _ in range(right_ob):
                        self.push_back(0.0)

                elif isinstance(self[0], str):
                    for _ in range(right_ob):
                        self.push_back("_")

                else:
                    for _ in range(right_ob):
                        self.push_back(0) 

            except IndexError:
                for _ in range(right_ob):
                    self.push_back(0)

        else:
            for elem in right_ob:
                self.push_back(elem)
            
        return self


    def __isub__(self, right_ob):
        """
        This method overload the '-=' operator so we can use it for 
        linked list objects
        -
        If right_ob is intager then we will delete right_ob values starting at
        the end of the list
        -
        Else we will delete the same elements of the 2 list object

        ...


        Parameters
        ----------
        right_ob: int, list, Single_Linked_List, Double_Linked_List
            This is the obejct that we will activate the algorithm


        Raises
        ------
        TypeError:
            When the user tries to use this method with an object other
            than list type object

        AtributeError:
            When the user tries to delete more elements that the list contains
        

        Return Value
        ------------
        The updated list
        """
        
        if not isinstance(right_ob, int) and not isinstance(right_ob, list) \
             and not isinstance(right_ob, Single_Linked_List) and not isinstance(right_ob, dll.Double_Linked_List):
            raise TypeError("Right object must be either an intager or a list object")

        if isinstance(right_ob, int):
            if right_ob > len(self):
                raise AttributeError("List has no such elements")

            for _ in range(right_ob):
                self.pop_back()

        else:
            ret_list = []
            eq = False
            for i in range(len(self)):
                for j in range(len(right_ob)):
                    if self[i] == right_ob[j]:
                        eq = True
                        break
                
                if not eq:
                    ret_list.append(self[i])
                    
                eq = False
            
            self.clear()

            for elem in ret_list:
                self.push_back(elem)

        return self

    
    def __imul__(self, times):
        """
        This method overloads the '*=' operator so we can use it for 
        linked list objects

        ...


        Parameters
        ----------
        times: int
            This is the total times that we want to repeat the list
        
        
        Raises
        ------
        TypeError:
            When the user tries to pass as times an object other than
            intager


        Return Value
        ------------
        The updated object
        """

        if not isinstance(times, int):
            raise TypeError("Right object must only be an intager")
        
        if times <= 0:
            self.clear()
        else:        
            for i in range((len(self) * times) - len(self)):
                self.push_back(self[i])

        return self


    def __add__(self, right_ob):
        """
        This method overloads the '+' operator so we can use it for 
        linked list objects

        ...


        Parameter
        ---------
        right_ob: list, Single_Linked_List, Double_Linked_List
            This is the object that we will add with the current one


        Raises
        ------
        TypeError:
            When the user tries to add a linked list with objects other
            than list type object


        Return Value
        ------------
        ret_list: list
            This is the total addition    
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, Single_Linked_List) \
            and not isinstance(right_ob, dll.Double_Linked_List):
            raise TypeError("Right object must be a list type object")

        ret_list = [elem for elem in self]

        for elem in right_ob:
            ret_list.append(elem)

        return ret_list

    
    def __sub__(self, right_ob):
        """
        This method overloads the '-' operator so we can use it for 
        linked list objects

        ...


        Parameters
        ----------
        right_ob: list, Sibgle_Linked_List, Double_Linked_List
            This is the list object which we will subtruct with the current one

        
        Raises
        ------
        TypeError:
            When the user tries to subtuct a linked list object with one other
            than list type


        Return Value
        ------------
        ret_list: list
            This is the result list
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, Single_Linked_List) \
            and not isinstance(right_ob, dll.Double_Linked_List):
            raise TypeError("Right object must be a list type object")
        
        ret_list = []
        eq = False
        for i in range(len(self)):
            for j in range(len(right_ob)):
                if self[i] == right_ob[j]:
                    eq = True
                    break
                
            if not eq:
                ret_list.append(self[i])
                
            eq = False

        return ret_list

    
    def __mul__(self, right_ob):
        """
        This method overloads the '*' operator so we can use it for 
        linked list objects

        ...


        Parameters
        ----------
        right_ob: int
            This is the total times that we will multiply the elements
            of the first list

        
        Raises
        ------
        TypeError:
            When the user passes as a right obejct one other than intager


        Return Value
        ------------
        ret_list: list, []
            This is the result list
        """

        if not isinstance(right_ob, int):
            raise TypeError("Right object must be and intager")
        
        if right_ob > 0:
            ret_list = []
            
            for _ in range(right_ob):
                for j in range(len(self)):
                    ret_list.append(self[j])
            
            return ret_list

        else:
            return []


    def __eq__(self, right_ob):
        """
        This method overloads the '==' operator so we can compare list
        objects
        
        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List
            This is the comparison object

        
        Raises
        ------
        TypeError:
            When the user uses at the comparison an object other that list type


        Return Value
        ------------
        The result of the comparison
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, Single_Linked_List) \
            and not isinstance(right_ob, dll.Double_Linked_List):
            raise TypeError("Right object must be a list type object")

        if len(self) == len(right_ob):
            for i in range(len(self)):
                if self[i] != right_ob[i]:
                    return False

            return True

        return False


    def __lt__(self, right_ob):
        """
        This method overloads the '<' operator so we can 
        compare list objects
        
        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List
            This is the comparison object

        
        Raises
        ------
        TypeError:
            When the user uses at the comparison an object other that list type


        Return Value
        ------------
        The result of the comparison
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, Single_Linked_List) \
            and not isinstance(right_ob, dll.Double_Linked_List):
            raise TypeError("Right object myst be a list type object")
        
        return len(self) < len(right_ob)


    def __le__(self, right_ob):
        """
        This method overloads the '<=' operator so we can 
        compare list objects
        
        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List
            This is the comparison object

        
        Raises
        ------
        TypeError:
            When the user uses at the comparison an object other that list type


        Return Value
        ------------
        The result of the comparison
        """
        
        if not isinstance(right_ob, list) and not isinstance(right_ob, Single_Linked_List) \
            and not isinstance(right_ob, dll.Double_Linked_List):
            raise TypeError("Right object must be a list type object")

        return len(self) < len(right_ob) or self == right_ob


    def __gt__(self, right_ob):
        """
        This method overloads the '>' operator so we can 
        compare list objects
        
        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List
            This is the comparison object

        
        Raises
        ------
        TypeError:
            When the user uses at the comparison an object other that list type


        Return Value
        ------------
        The result of the comparison
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, Single_Linked_List) \
            and not isinstance(right_ob, dll.Double_Linked_List):
            raise TypeError("Right object myst be a list type object")
        
        return len(self) > len(right_ob)


    def __ge__(self, right_ob):
        """
        This method overloads the '>=' operator so we can 
        compare list objects
        
        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List
            This is the comparison object

        
        Raises
        ------
        TypeError:
            When the user uses at the comparison an object other that list type


        Return Value
        ------------
        The result of the comparison
        """
        
        if not isinstance(right_ob, list) and not isinstance(right_ob, Single_Linked_List) \
            and not isinstance(right_ob, dll.Double_Linked_List):
            raise TypeError("Right object must be a list type object")

        return len(self) > len(right_ob) or self == right_ob
