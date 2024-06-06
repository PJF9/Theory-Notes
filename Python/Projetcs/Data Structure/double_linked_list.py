import single_linked_list as sll


class Node:
    """
    This class is represent a node that will included to the linked list
    A node is going to have three parts. One that stores the data that the
    user want, another that will store the memory address of the next 
    list element and one for the previous one

    ...


    Atributes
    ---------
    data: any data type
        This is the data that the user wants

    next_: Node, NoneType
        This is a refference that is locatited at the same memory location
        as the next node of the list

    prev_: Node, NoneType
        This is a refference that is locatited at the same memory location
        as the prev node of the list


    Dunder Methods
    --------------
    init(data, next_=None, prev_=None):
        This method is the initializer ( constructor ) of the node object
    """

    def __init__(self, data, next_=None, prev_=None):
        """
        This method is the initializer ( constructor ) of the node object

        ...


        Parameters
        ----------
        data: any data type
            This is data that the user want to place at the node
        
        next_: Node, NoneType ( default is None )
            This variable is "pointing" to the next element of the list

        prev_: None, NoneType ( default is None )
            This variable is "pointing" to the previous element of the list
        """

        self.data = data
        self.next_ = next_
        self.prev_ = prev_


class Double_Linked_List:
    """
    This class implements the Double Linked List data structure

    ...


    Atributes
    ---------
    *args: list
        This is the sequence of the elements that the user want the list
        to contain

    head_: Node, NoneType
        This is the refference of the first element on the list

    teil_: Node, NoneType
        This is the refference of the last element on the list

    
    Normal Methods
    --------------
    push_front(self, data):
        This method inserts the given element to the start of the list

    push_back(self, data):
        This method inserts the given element to the end of the list

    insert_into(self, index, data):
        This method inserts the given element on the given index position
        of the list

    extend(self, right_ob):
        This method extends the current list object with the given one

    pop_front(self):
        This method deletes the first element of the list

    pop_back(self):
        This method deletes the last element of the list

    pop(self, index, total_pos=0):
        This method deletes total_pos elements after the given index postion
        ( including the index one )

    remove(self, data, dupl=False):
        This method deletes an element / or more base on the given element

    ndupl(self):
        This method deletes all the duplicates from the current list

    copy(self, right_ob):
        This method clears the current list and pass the given list's element
        to create a copy from it

    clear(self):
        This method clears the current list

    sort(self):
        This method sorts the list

    rev_sort(self):
        This method sorts the list from the oposite direction

    reverse(self):
        This method reverses the list

    slce(self, start, end, step=1):
        This method helps us with slicing ( returns a list )

    slicing(self, start, end, step=1):
        This method helps us with slicing ( yields the elements )

    count(self, data):
        This method counting how many times the given element appears
        on the list

    index(self, data):
        This method returns to us only the first index postion of the given element
        ( if not exist return -1 )

    indexes(self, data):
        This method returns to us all the index positions of the given elements
        on the list


    Dunder Methods
    --------------
    init(self, *args):
        This method initializes ( constructs ) the list object

    str(self):
        This method converts the list object into a string to help us printing
        it on the console

    len(self):
        This method returns the length of the list object

    getitem(self, index):
        This method overloads the '[]' operator to help us print the list
        more eazily

    setitem(self, index, data):
        This method overloads the '[]' operator to help us replace a list
        element or swap lists elements more eazily

    iter(self):
        This method converts the list object into an iterator mainly to use
        it in a 'for element in list' loop

    next(self):
        This method returns the current element of the list ( inside a forr loop )
        and going to the next element so it can return it on the next loop
    
    iadd(self, right_ob):
        This method overloads the '+=' operator so we can use it for double
        linked list objects

    isub(self, right_ob):
        This method overload the '-=' operator so we can use it for double
        linked list objects

    imul(self, times):
        This method overloads the '*=' operator so we can use it for double
        linked list objects
        
    add(self, right_ob):
        This method overloads the '+' operator so we can use it for double
        linked list objects

    sub(self, right_ob):
        This method overloads the '-' operator so we can use it for double
        linked list objects

    mul(self, right_ob):
        This method overloads the '*' operator so we can use it for double
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
    """
    
    def __init__(self, *args):
        """
        This method initializes ( constructs ) the list object
        
        ...


        Parameters
        ----------
        *args: list
            This parameter contains all the elements that the user want
            to be passed of the list at construction time
        """
        
        self.head_ = None
        self.teil_ = None

        for elem in args:
            self.push_back(elem)


    def push_front(self, data):
        """
        This method inserts the given element to the start of the list

        Syntax: self.push_front(data)

        ...


        Parameters
        ----------
        data: any data type
            This parameter is the element that will be inserted to the list
        """

        new_node = Node(data)

        if not self.head_ and not self.teil_:
            self.head_ = new_node
            self.teil_ = new_node
         
        else:
            new_node.next_ = self.head_
            self.head_.prev_ = new_node
            self.head_ = new_node


    def push_back(self, data):
        """
        This method inserts the given element to the end of the list

        Syntax: self.push_back(data)

        ...


        Parameters
        ----------
        data: any data type
            This parameter is the element that will be inserted to the list
        """

        new_node = Node(data)

        if not self.head_ and not self.teil_:
            self.push_front(new_node.data)
        else:
            new_node.prev_ = self.teil_
            self.teil_.next_ = new_node
            self.teil_ = new_node

    
    def insert_into(self, index, data):
        """
        This method inserts the given element on the given index position
        of the list

        Syntax: self.insert_into(index, data)

        ...


        Parameters
        ----------
        index: int
            This parameter is the index of the position we want to insert the 
            given element ( all the other will move one place to the right )

        data: any data type
            This is the data of the new element which is going to be inserted
            into the list


        Raises
        ------
        TypeError:
            When the user tries to pass as an index object one other than
            intager

        IndexError:
            When the user tries to add the new element into an invalid index
            position 
        """

        if not isinstance(index, int):
            raise TypeError("Index position object must be an intager")
        elif (index > len(self) - 1) or (index < 0):
            raise IndexError("Invalid index position: index out ouf bounds")
        elif (not self.head_ and not self.teil_ )or (index == 0):
            self.push_front(data)
        elif index == len(self) - 1:
            self.push_back(data)
        else:
            new_node = Node(data)

            if index > int(len(self) / 2):
                temp = self.teil_
                
                for i in range(len(self) - 1, int(len(self) / 2), -1):
                    if i == index:
                        new_node.prev_ = temp.prev_
                        new_node.next_ = temp

                        temp.prev_.next_ = new_node
                        temp.prev_ = new_node

                    temp = temp.prev_ 

            else:
                temp = self.head_

                for i in range(0, int(len(self) / 2) + 1):
                    if i == index:
                        new_node.prev_ = temp.prev_
                        new_node.next_ = temp

                        temp.prev_.next_ = new_node
                        temp.prev_ = new_node

                    temp = temp.next_ 


    def extend(self, right_ob):
        """
        This method extends the current list object with the given one

        Syntax: self.extend(right_ob)

        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List
            This is the object that will extend the current list object


        Raises
        ------
        TypeError:
            When the user tries to pass as a right_ob an object other than
            intager


        Return Value
        ------------
        The updated list object
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, sll.Single_Linked_List) \
            and not isinstance(right_ob, Double_Linked_List):
            raise TypeError("Right object must be a list type object")

        for elem in right_ob:
            self.push_back(elem)

        return self
    

    def pop_front(self):
        """
        This method deletes the first element of the list

        Syntax: self.pop_front()

        ...


        Raises
        ------
        IndexError:
            When the user tries to delete from an empty list
        """

        if not self.head_ and not self.teil_:
            raise IndexError("You can't delete from an empty list")
        elif len(self) == 1:
            self.head_ = None
            self.teil_ = None
        else:
            self.head_.next_.prev_ = None
            self.head_ = self.head_.next_
        


    def pop_back(self):
        """
        This method deletes the last element of the list

        Syntax: self.pop_back()

        ...


        Raises
        ------
        IndexError:
            When the user tries to delete from an empty list
        """

        if not self.head_ and not self.teil_:
            raise IndexError("You can't delete from an empty list")
        elif len(self) == 1:
            self.head_ = None
            self.teil_ = None
        else:
            self.teil_.prev_.next_ = None
            self.teil_ = self.teil_.prev_


    def pop(self, index, total_pos=0):
        """
        This method deletes total_pos elements after the given index postion
        ( including the index one )

        Syntax: self.pop(index, total_pos)

        ...


        Parameters
        ----------
        index: int
            This is the index position of the element the user wants to delete

        total_pop: int ( default is 0 )
            This is the total element the user wants to delete right to the index one


        Raises
        ------
        TypeError:
            When the user tries to pass an argument that is not intager

        IndexError:
            When the user tries to remove an element outside the list bounds
            -
            When the user tries to pass the second argument < 0
            -
            When the user tries to delete more elements than the list has
        """

        if not isinstance(index, int) and not isinstance(total_pos, int):
            raise TypeError("Index position and total_pos objects must be an intagers")
        elif (index > len(self) - 1) or (index < 0):
            raise IndexError("Invalid index position: intex out of bounds")
        elif total_pos < 0:
            raise IndexError("total_pos must be greater or equal than 0")
        elif index + total_pos > len(self) - 1:
            raise IndexError("Invalid index position: list has no such elements")
        elif index + total_pos == len(self) - 1:
            for _ in range(total_pos+1):
                self.pop_back()
        elif index == len(self) - 1:
            self.pop_back()
        elif index == 0:
            for _ in range(total_pos+1):
                self.pop_front()
        else:
            if index > int(len(self) / 2):
                temp = self.teil_

                for i in range(len(self) - 1, int(len(self) / 2), -1):
                    curr = temp
                    if i == index + total_pos:
                        for _ in range(total_pos):
                            curr = curr.prev_
                        
                        break

                    temp = temp.prev_

                curr.prev_.next_ = temp.next_
                temp.next_.prev = curr.prev_

            else:
                temp = self.head_

                for i in range(0, int(len(self) / 2) + 1):
                    curr = temp
                    if i == index:
                        for _ in range(total_pos):
                            curr = curr.next_

                        break

                    temp = temp.next_

                temp.prev_.next_ = curr.next_
                curr.next_.prev = temp.prev_


    def remove(self, data, dupl=False):
        """
        This method deletes an element / or more base on the given element

        Syntax: self.remove(data, dupl)

        ...


        Parameters
        ----------
        data: any data type
            This is the parameter that will delete all / or not the list elements
            that are equal to it

        dupl: bool ( default is False )
            This is the user choice for deleting all the dyplicates or only the
            first one


        Raises
        ------
        TypeError:
            When the user tries to pass as second argument an object other than boolean

        IndexError:
            When the user tries to delete from an empty list
        """

        if not isinstance(dupl, bool):
            raise TypeError("Second argument must be an boolean")
        elif not self.head_ and not self.teil_:
            raise IndexError("You can't delete from an empty list")
        else:
            if not dupl:
                for i in range(len(self)):
                    if self[i] == data:
                        self.pop(i)
                        break
            else:
                no_dupls = []

                for i in range(len(self)):
                    if (self[i] != data):
                        no_dupls.append(self[i])

                self.clear()

                for elem in no_dupls:
                    self.push_back(elem)

    
    def ndupl(self):
        """
        This method deletes all the duplicates from the current list

        Syntax: self.ndupl()

        ...
        """

        no_dupls = []

        for i in range(len(self)):
            if self[i] not in no_dupls:
                no_dupls.append(self[i])

        self.clear()

        for elem in no_dupls:
            self.push_back(elem)

    
    def copy(self, right_ob):
        """
        This method clears the current list and pass the given list's element
        to create a copy from it

        Syntax: self = self.copy(right_ob)

        ...


        Parameters
        ----------
        right_ob: listm Single_Linked_List, Double_Linked_List
            This is the object that the current list will copy it's elements

        
        Raises
        ------
        TypeError:
            When the user tries to pass as an argument an object other than the
            allowed ones


        Return Value
        ------------
        The updated object
        """
        
        if not isinstance(right_ob, list) and not isinstance(right_ob, sll.Single_Linked_List) \
            and not isinstance(right_ob, Double_Linked_List):
            raise TypeError("You can only copy list type objects")
            
        self.clear()

        for elem in right_ob:
            self.push_back(elem)

        return self


    def clear(self):
        """
        This method clears the current list

        Syntax: self.clear()

        ...
        """
        
        self.head_ = None
        self.teil_ = None


    def sort(self):
        """
        This method sorts the list

        Syntax: self.sort()

        ...


        Raises
        ------
        IndexError:
            When the user tries to sort an empty list
        """

        if not self.head_ and not self.teil_:
            raise IndexError("You can't sort an empty list")

        for i in range(len(self)):
            for j in range(len(self)):
                if self[i] < self[j]:
                    self[i], self[j] = self[j], self[i]


    def rev_sort(self):
        """
        This method sorts the list from the oposite direction

        Syntax: self.rev_sort()

        ...


        Raises
        ------
        IndexError:
            When the user tries to sort an empty list
        """

        if not self.head_ and not self.teil_:
            raise IndexError("You can't sort an empty list")

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
        IndexError:
            When the user tries to reverse an empty list
        """

        if not self.head_ and not self.teil_:
            raise IndexError("You can't reverse an empty list")

        for i in range(int(len(self) / 2)):
            self[i], self[len(self) - 1 - i] = self[len(self) - 1 -i], self[i]

    
    def slce(self, start, end, step=1):
        """
        This method helps us with slicing ( returns a list )

        Syntax: list = self.slce(start, end, step)

        ...


        Parameters
        ----------
        start: int
            This is the first index postion ( the starting one )
        
        end: int
            This is the last index position ( the ending one - Not inlcuded )

        step: int ( default is 1 )
            This is the step of the slice


        Raises
        ------
        TypeError:
            When the user tries to pass an arguments that is not an intager

        ValueError:
            When the user tries to pass step = 0

        IndexError:
            When the user tries to slice out of the list bounds


        Return Value
        ------------
        ret_list: list
            The result of the slice
        """

        if not isinstance(start, int) and not isinstance(end, int) and not isinstance(step, int):
            raise TypeError("All the arguments must be intagers")
        elif step == 0:
            raise ValueError("Third argument can't be 0")
        elif (start < 0) or (start > len(self)):
            raise IndexError("Invalid index position: index out of range")
        elif (end < 0) or (end > len(self)):
            raise IndexError("Invalid index position: index out of range")
        elif step > 0:
            if start + end > len(self):
                raise IndexError("Invalid index postion: list has no such elements")
        elif step < 0:
            if start - end < 0:
                raise IndexError("Invalid index postion: list has no such elements")
    
        ret_list = []

        for i in range(start, end, step):
            ret_list.append(self[i])

        return ret_list


    def slicing(self, start, end, step=1):
        """
        This method helps us with slicing ( yields the elements )

        Syntax: list = self.slicing(start, end, step)

        ...


        Parameters
        ----------
        start: int
            This is the first index postion ( the starting one )
        
        end: int
            This is the last index position ( the ending one - Not inlcuded )

        step: int ( default is 1 )
            This is the step of the slice


        Raises
        ------
        TypeError:
            When the user tries to pass an arguments that is not an intager

        ValueError:
            When the user tries to pass step = 0

        IndexError:
            When the user tries to slice out of the list bounds


        Yield Value
        ------------
        self[i]: any data type
            The current slice element
        """

        if not isinstance(start, int) and not isinstance(end, int) and not isinstance(step, int):
            raise TypeError("All the arguments must be intagers")
        elif step == 0:
            raise ValueError("Third argument can't be 0")
        elif (start < 0) or (start > len(self)):
            raise IndexError("Invalid index position: index out of range")
        elif (end < 0) or (end > len(self)):
            raise IndexError("Invalid index position: index out of range")
        elif step > 0:
            if start + end > len(self):
                raise IndexError("Invalid index postion: list has no such elements")
        elif step < 0:
            if start - end < 0:
                raise IndexError("Invalid index postion: list has no such elements")

        for i in range(start, end, step):
            yield self[i]


    def count(self, data):
        """
        This method counting how many times the given element appears
        on the list

        Syntax: var = self.count(data)

        ...


        Parameters
        ----------
        data: any data type
            This parameter is providing us the element to search for in the list


        Return Value
        ------------
        ret_count: int
            The total times that the given value appears on the list
        """

        ret_count = 0

        for elem in self:
            if elem == data:
                ret_count += 1

        return ret_count


    def index(self, data):
        """
        This method returns to us only the first index postion of the given element
        ( if not exist return -1 )

        Syntax: var = slef.index(data)

        ...


        Parameters
        ----------
        data: any data type
            This parameter is providing us the element to search for in the list


        Return Value
        ------------
        The index of the element if exist else -1
        """

        for i in range(len(self)):
            if self[i] == data:
                return i
        
        return -1

    
    def indexes(self, data):
        """
        This method returns to us all the index positions of the given elements
        on the list

        Syntax: list = self.indexes(data)

        ...


        Parameters
        ----------
        data: any data type
            This parameter is providing us the element to search for in the list


        Return Value
        ------------
        ret_list: list
            This is the list that contains all the index positions of the given
            element on the list
        """

        ret_list = []

        for i in range(len(self)):
            if self[i] == data:
                ret_list.append(i)

        return ret_list


    def __str__(self):
        """
        This method converts the list object into a string to help us printing
        it on the console

        ...


        Return Value
        ------------
        re_str: str
            This is the string that the list object is beeing converted into
        """

        re_str = "["
        temp = self.head_

        while temp is not None:
            if not temp.next_:
                re_str += str(temp.data)
            else:
                re_str += str(temp.data) + ", "
        
            temp = temp.next_

        re_str += "]"

        return re_str


    def __len__(self):
        """
        This method returns the length of the list object

        ...


        Return Value
        ------------
        lenght: int
            This is the length variable ( how many element the list has )
        """

        length = 0
        temp = self.head_

        while temp is not None:
            length += 1
            temp = temp.next_

        return length

    
    def __getitem__(self, index):
        """
        This method overloads the '[]' operator to help us print the list
        more eazily

        ...


        Parameters
        ----------
        index: int
            This parameter is the index position of the element the user
            wants to get


        Raises
        ------
        TypeError:
            When the user tries to pass as an index an object other than
            intager

        IndexError:
            When the user tries to pass as an invalid index as an index
            position


        Return Value
        ------------
        temp.data: any data type
            This is the data of the element the user want to get
        """

        if not isinstance(index, int):
            raise TypeError("Index position object must be an intager")
        elif (index > len(self) - 1) or (index < 0):
            raise IndexError("Invalid index positon: index out of bounds")
        else:
            if index > int(len(self) / 2) - 1:
                temp = self.teil_

                for i in range(len(self) - 1, int(len(self) / 2) - 1, -1):
                    if i == index:
                        return temp.data
                    
                    temp = temp.prev_
            else:
                temp = self.head_

                for i in range(0, int(len(self) / 2) + 1):
                    if i == index:
                        return temp.data

                    temp = temp.next_


    def __setitem__(self, index, data):
        """
        This method overloads the '[]' operator to help us replace a list
        element or swap lists elements more eazily

        ...


        Parameters
        ----------
        index: int
            This parameter is the index position of the element the user want
            to change the data

        data: any data type
            This parameter is the new data that the element on the index of the
            list will have


        Raises
        ------
        TypeError:
            When the user tries to pass as an index variable an object other than
            intager

        IndexError:
            When the user tries to pass an invalid index as an index position
        """

        if not isinstance(index, int):
            raise TypeError("Index position object must be an intager")
        elif (index > len(self) - 1) or (index < 0):
            raise IndexError("Invalid index position: index out of bounds")
        else:
            if index > int(len(self) / 2):
                temp = self.teil_

                for i in range(len(self) - 1, int(len(self) / 2), -1):
                    if i == index:
                        temp.data = data
                        break

                    temp = temp.prev_
            else:
                temp = self.head_

                for i in range(0, int(len(self) / 2) + 1):
                    if i == index:
                        temp.data = data

                    temp = temp.next_


    def __iter__(self):
        """
        This method converts the list object into an iterator mainly to use
        it in a 'for element in list' loop

        ...


        Return Value
        ------------
        The list object
        """

        self.help_index = 0
        
        return self


    def __next__(self):
        """
        This method returns the current element of the list ( inside a forr loop )
        and going to the next element so it can return it on the next loop

        ...


        Raises
        ------
        StopIteration:
            This exception helps us break out of the for loop when the elements
            of the list object finishes


        Return Value
        ------------
        ret_elem: any data type
            This is the current element of the list ( helpfull inside for loops )
        """

        if self.help_index == len(self):
            raise StopIteration

        ret_elem = self[self.help_index]
        self.help_index += 1

        return ret_elem


    def __iadd__(self, right_ob):
        """
        This method overloads the '+=' operator so we can use it for double
        linked list objects

        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List, int
            This is the object that we will add to the current one

        
        Raises
        ------
        TypeError:
            When the user tries to pass as a right object an object other
            than list type


        Return Value
        ------------
        The updated object
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, sll.Single_Linked_List) \
            and not isinstance(right_ob, Double_Linked_List) and not isinstance(right_ob, int):
            raise TypeError("Right object must be a list type object or an intager")

        elif isinstance(right_ob, int):
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
        This method overload the '-=' operator so we can use it for double
        linked list objects

        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List, int
            This is the object that we will add to the current one

        
        Raises
        ------
        TypeError:
            When the user tries to pass as a right object an object other
            than list type

        IndexError:
            When the user tries to delete more elements that the list has


        Return Value
        ------------
        The updated object
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, sll.Single_Linked_List) \
            and not isinstance(right_ob, Double_Linked_List) and not isinstance(right_ob, int):
            raise TypeError("Right object must be a list type object or an intager")

        elif isinstance(right_ob, int):
            if (right_ob > len(self)) or (right_ob < 0):
                raise IndexError("No such elements to delete")

            for _ in range(right_ob):
                self.pop_back()

        else:
            ret_list = []

            for i in range(len(self)):
                equal = False
                for j in range(len(right_ob)):
                    if self[i] == right_ob[j]:
                        equal = True
                        break

                if not equal:
                    ret_list.append(self[i])

            self.clear()

            for elem in ret_list:
                self.push_back(elem)
        
        return self


    def __imul__(self, right_ob):
        """
        This method overloads the '*=' operator so we can use it for double
        linked list objects

        ...

        
        Parameters
        ----------
        right_ob: int
            This is the total ammount of times that the user want to multiply
            the list


        Raises
        ------
        TypeError:
            When the user tries to pass as a right_ob an object other than intager


        Return Value
        ------------
        The updated list object
        """

        if not isinstance(right_ob, int):
            raise TypeError("Right object must be an intager")
        
        elif right_ob <= 0:
            self.clear()
        else:    
            for i in range((len(self) * right_ob) - len(self)):
                self.push_back(self[i])

        return self


    def __add__(self, right_ob):
        """
        This method overloads the '+' operator so we can use it for double
        linked list objects

        ...


        Parameters
        ----------
        right_ob: int, list, Single_Linked_List, Double_Linked_List
            This is the object that will be added to the current list obejct
            to store this result into anew list


        Raises
        ------
        TypeError:
            When the user tries to pass as a right_ob an object other than the
            allowed ones


        Return Value
        ------------
        ret_list: list
            This is the result of the addition
        """
        
        if not isinstance(right_ob, list) and not isinstance(right_ob, sll.Single_Linked_List) \
            and not isinstance(right_ob, Double_Linked_List) and not isinstance(right_ob, int):
            raise TypeError("Right object must be a list type object or an intager")
        
        ret_list = [elem for elem in self]

        if isinstance(right_ob, int):
            try:
                if isinstance(self[0], int):
                    for _ in range(right_ob):
                        ret_list.append(0)

                elif isinstance(self[0], float):
                    for _ in range(right_ob):
                        ret_list.append(0.0)

                elif isinstance(self[0], str):
                    for _ in range(right_ob):
                        ret_list.append("_")
                else:
                    for _ in range(right_ob):
                        ret_list.append(0)

            except IndexError:
                for _ in range(right_ob):
                    ret_list.append(0)
        else:
            for elem in right_ob:
                ret_list.append(elem)

        return ret_list


    def __sub__(self, right_ob):
        """
        This method overloads the '-' operator so we can use it for double
        linked list objects

        ...


        Parameters
        ----------
        right_ob: int, list, Single_Linked_List, Double_Linked_List
            This is the object that will subtruct the elements from the current
            list and pass the result to a new one

        
        Raises
        ------
        TypeError:
            When the user tries to pass as a right object an object other than
            the allowed ones

        IndexError:
            When the user tries to subtruct more element than the list has


        Return Values
        -------------
        ret_list: list
            This is the result of the subtruction 
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, sll.Single_Linked_List) \
            and not isinstance(right_ob, Double_Linked_List) and not isinstance(right_ob, int):
            raise TypeError("Right object must be a list type object or an intager")
        
        ret_list = []

        if isinstance(right_ob, int):
            if (right_ob > len(self)) or (right_ob < 0):
                raise IndexError("No such elements to delete")
            
            for i in range(len(self)):
                if i < len(self) - right_ob:
                    ret_list.append(self[i])
                else:
                    break
        else:
            for i in range(len(self)):
                equal = False
                for j in range(len(right_ob)):
                    if self[i] == right_ob[j]:
                        equal = True
                        break

                if not equal:
                    ret_list.append(self[i])

        return ret_list


    def __mul__(self, right_ob):
        """
        This method overloads the '*' operator so we can use it for double
        linked list objects

        ...


        Parameters
        ----------
        right_ob: int
            This is the multiplyier. The object that show us how many times the
            user wants to multiply the list and store the result to another list


        Raises
        ------
        TypeError:
            When the user pass as a right object an object other than intager


        Return Value
        ------------
        ret_list: list
            The result of the myltipication
        """

        if not isinstance(right_ob, int):
            raise TypeError("Right object must be an intager")
        
        ret_list = []

        if right_ob <= 0:
            return ret_list
        else:    
            for _ in range(right_ob):
                for i in range((len(self))):
                    ret_list.append(self[i])

            return ret_list


    def __eq__(self, right_ob):
        """
        This method overloads the '==' operator so we can compare list
        objects

        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List
            This is the obejct that the user will compare with the current list

        
        Raises
        ------
        TypeError:
            When the user tries to pass as an argument an object other than the
            allowed ones


        Return Value
        ------------
        The result of the comparison
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, sll.Single_Linked_List) \
            and not isinstance(right_ob, Double_Linked_List):
            raise TypeError("Right object must be a list type object")

        elif len(self) == len(right_ob):
            for i in range(len(self)):
                if self[i] != right_ob[i]:
                    return False
            
            return True
        
        return False


    def __lt__(self, right_ob):
        """
        This method overloads the '<' operator so we can compare list
        objects

        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List
            This is the obejct that the user will compare with the current list

        
        Raises
        ------
        TypeError:
            When the user tries to pass as an argument an object other than the
            allowed ones


        Return Value
        ------------
        The result of the comparison
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, sll.Single_Linked_List) \
            and not isinstance(right_ob, Double_Linked_List):
            raise TypeError("Right object must be a list type object")

        return len(self) < len(right_ob)

    
    def __gt__(self, right_ob):
        """
        This method overloads the '>' operator so we can compare list
        objects

        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List
            This is the obejct that the user will compare with the current list

        
        Raises
        ------
        TypeError:
            When the user tries to pass as an argument an object other than the
            allowed ones


        Return Value
        ------------
        The result of the comparison
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, sll.Single_Linked_List) \
            and not isinstance(right_ob, Double_Linked_List):
            raise TypeError("Right object must be a list type object")

        return len(self) > len(right_ob)

    
    def __le__(self, right_ob):
        """
        This method overloads the '<=' operator so we can compare list
        objects

        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List
            This is the obejct that the user will compare with the current list

        
        Raises
        ------
        TypeError:
            When the user tries to pass as an argument an object other than the
            allowed ones


        Return Value
        ------------
        The result of the comparison
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, sll.Single_Linked_List) \
            and not isinstance(right_ob, Double_Linked_List):
            raise TypeError("Right object must be a list type object")

        return len(self) < len(right_ob) or self == right_ob

    
    def __ge__(self, right_ob):
        """
        This method overloads the '>=' operator so we can compare list
        objects

        ...


        Parameters
        ----------
        right_ob: list, Single_Linked_List, Double_Linked_List
            This is the obejct that the user will compare with the current list

        
        Raises
        ------
        TypeError:
            When the user tries to pass as an argument an object other than the
            allowed ones


        Return Value
        ------------
        The result of the comparison
        """

        if not isinstance(right_ob, list) and not isinstance(right_ob, sll.Single_Linked_List) \
            and not isinstance(right_ob, Double_Linked_List):
            raise TypeError("Right object must be a list type object")

        return len(self) > len(right_ob) or self == right_ob
