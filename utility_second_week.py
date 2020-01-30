"""
This is a utility file which contains Linked List having different methods.

Author: Shruti Zarbade
Date : 22/01/2020
"""
from utility import Utility
utility_object = Utility()


class Node:
    """
    This is the class node in which init function is used which defines the two variable
    data and next where data define the information of the node and next indicates the address of
    the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

#====================================================================================================


class LinkedList:
    """
    This is the class Linked List in which various method of linked list are defined such as remove,
    insert,size,pop,remove,add, etc which is used to drive the linked list program.

    """
    def __init__(self):
        self.start = None

    def append(self, data):  # add the content at the end given by user
        """This function add the content at the end of a list"
        :param data: the data which we have to add
        :return: Return the list with the content given at the last
        """
        new_node = Node(data)

        if self.start is None:
            self.start = new_node
        else:
            temp_node = self.start
            while temp_node.next is not None:
                temp_node = temp_node.next
            temp_node.next = new_node

    def remove(self, data):  # remove the particular word from the list
        """
        remove the content given by user by finding its place and then remove it
        :param data: data which we have to delete
        :return: return list by removing the particular content
        """
        current_node = self.start

        if current_node and current_node.data == data:
            self.start = current_node
            current_node = current_node.next
        prev = None
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

    def search(self, data):  # it search the word given by user and return True if found  else return False
        """
        This function search the content given by user
        :param data: user give the input which they have to search
        :return: return True if found else return False
        """

        # Initialize current to start
        current = self.start

        # loop till current not equal to None
        while current is not None:
            if current.data == data:
                return True  # data found
            else:
                current = current.next

        return False  # Data Not found

    def is_empty(self):  # It checks the list is empty or not and return empty list
        """
        This function checks weather the list is empty
        :return: It return the empty list by making self.start as none
        """
        return self.start is None

    def size(self):  # it gives the size of list
        """
        this function checks the size of a list
        :return: return the count of a list
        """
        current = self.start
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def delete_first(self):  # delete first item in a list
        """
        This function delete the first element in a list
        :return: return the list by removing the first element
        """
        tempNode = self.start
        if tempNode is None:
            return -1
        self.start = tempNode.next
        return tempNode.data

    def pop(self):  # delete the element in the list
        """This function delete the last element in a list
        :return: return the list by removing the last element
        """
        current = self.start
        previous = self.start

        if current is None:
            return "No item in list"
        if current.next is None:
            self.start = None

        while current.next is not None:
            previous = current
            current = current.next

        previous.next = None
        return current.data

    def display(self):  # display the content as output
        """This function is used for display the content in a list
        :return: return the output
        """
        current = self.start
        while current is not None:
            print(current.data, end=' ')
            current = current.next

    def insert_at_first(self, data):  # insert the item at position 1
        """
        This function add the element at the first
        :param data: the data given by user which have to add in a list
        :return: return the list by adding the element at the first
        """
        new_node = Node
        new_node.data = data
        new_node.next = self.start
        self.start = new_node

    def insert(self, data):  # insert the data the position by using sorting
        """
        This function is added the content by using sorting the list
        :param data: the data which we have to insert
        :return: it return the list by inserting the element at a particular position
        """
        current = self.start
        previous = None

        while current is not None:
            if current.data > data:
                break
            previous = current
            current = current.next

        new_node = Node(data)
        if previous is None:
            # self.start = new_node
            new_node.next = self.start
            self.start = new_node
        else:
            previous.next = new_node
            new_node.next = current

 #====================================== # Unordered List======================================================


class UnorderedList:
    def __init__(self):
        """
        This is an an init function in which we call the linked list class to
        used the function of linked list in this class

        """
        self.list = LinkedList()

    def unordered_list(self):
        """This  method is the unordered list in which user give one word if the word is found
        in a list it will remove from the list otherwise the word is added to the list
        it will return the updated list.
        :return:
        """
        file = open("word_file.txt", 'r')  # text file is open
        for line in file:
            words_in_line = line.split(' ')
            for word in words_in_line:
                self.list.append(word)
        self.list.display()
        print()
        x = input("Enter a word: ").strip()
        if self.list.search(x):  # search the word given by user
            print("Word found and removed from the file \n")  # word found
            self.list.remove(x)  # the word is removed from the list
        else:
            print('not found')  # not found
            self.list.append(x)  # the word is added to the list
        self.list.display()
        print()

#========================================Ordered List=================================================


class OrderedList:

    def __init__(self):
        self.list = LinkedList()

    def ordered_list(self):
        """ In this method the ordered list is given this function insert the number in
        sorted form in a linked list and user give one number if it present in a list
        it will remove the list otherwise it will add in a list

        :return: it return the sorted list if number is found it remove else it add
        """
        with open("number_file.txt", 'r') as f:
            for line in f:
                for number in line.split():
                    self.list.insert(int(number))  # sort the list in ascending order
        self.list.display()
        print()
        x = int(input("Enter a number: "))  # enter the input by user
        if self.list.search(x):  # search the content in a list
            print("Number Found")
            self.list.remove(x)  # remove if the word is found
        else:
            print("Not Found")
            self.list.insert(x)  # add the content if not found
        self.list.display()
        print()

#=======================================================================================================


class Stack:
    """
    This class defines the parentheses in and expression.
    It checks the open and close brackets in and expression if the bracket is open it should
    be close otherwise it return false, it checks the number of open and close bracket and
    provides a empty list which means it is balanced otherwise list is not balanced.
    """

    def __init__(self):
        self.stack = LinkedList()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def size(self):
        return self.stack.size()

    def is_empty(self):
        self.stack.is_empty()

    def display(self):
        self.stack.display()

#========================================================================================================


class BalancedParentheses:
    """
    This is class for balanced parentheses in various method are used
    this function check the parentheses in an expression if open brace is found it
    will push into the stack and after counting it will pop from the stack and if the stack is empty
    after the pop if empty stack is there then it will return true otherwise it will give false.
    """

    def __init__(self):
        self.balanced = Stack()

    def balanced_parentheses(self, string):
        """This define the balanced parentheses it check the open and close brace in an
        equation and return true and false.

        :param string: the user enter the expression
        :return:it return true if parentheses and open and close properly
        """
        try:
            open_paren = "([{<"
            close_paren = ")]}>"
            for bracket in string:
                if bracket in open_paren:
                    self.balanced.push(bracket)
                elif bracket in close_paren:
                    if self.balanced.is_empty():
                        balanced = False
                        break
                    self.balanced.pop()

            else:
                if self.balanced.is_empty():
                    balanced = True
                else:
                    balanced = False
            if balanced:
                print("Balanced")
            else:
                print("Unbalanced")
            return balanced

        except Exception:
            print("Invalid Input")


#=============================================================================================================


class Queue:
    """This class stores items in a First In First Out manner.
    the following class creates and empty queue and performs the following methods """
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, data):  # This method adds an item to the end of the queue
        self.queue.append(data)

    def dequeue(self):  # This method delete an item from the first
        self.queue.delete_first()

    def is_empty(self):  # check the list is empty or not
        self.queue.is_empty()

    def size(self):  # gives the size of a queue
        self.queue.size()

    def display(self):
        self.queue.display()

    def cash_counter(self):
        """This is a function where people come to deposit cash or withdraw cash
        Input: Asking individuals to deposit or withdraw the amount """
        cash = 2000  # Initiating a variable which consists of the amount the bank has
        deposit = 0
        withdraw = 0
        while True:
            print("1  Deposit Cash")
            print("2  Withdraw Cash")
            print("3  Exit")
            # Taking user inputs for the type of transaction
            choice = int(input("Please enter a value: "))  # If the user wants to deposit the cash
            if choice == 1:
                # self.enqueue(1)  # Amount to be deposited
                amount = int(input("Enter the amount to be deposited: "))
                if amount == 0:
                    print("Enter Amount!")
                else:
                    deposit += amount
                    cash += amount  # Adding the deposit to the total cash
                    print("Balanced: ", cash)
                    print("Cash Deposited Successfully\n")
                self.dequeue()  # If the user wants to withdraw cash

            elif choice == 2:
                withdraw += 1
                self.enqueue(1)

                amount = int(input("Enter the amount to withdraw: "))
                if cash >= amount:
                    deposit -= amount
                    cash -= amount  # Subtracting the withdrawal amount from the total cash
                    print("Balanced: ", cash)
                    print("Cash Withdrawal Successful\n")
                else:
                    print("Insufficient balance \n")
                    self.dequeue()

            elif choice == 3:
                quit()

            else:
                print("Invalid input")

#=====================================================================================================


class Dequeue:
    """This method is used to add and the delete the item from both the rear and front side
    various method like remove front, remove rear, add rear,add front are comes in the dequeue
    class.It helps us to implement various method based on dequeue concept.

    """
    def __init__(self):
        self.dequeue = LinkedList()

    def remove_front(self):
        self.dequeue.delete_first()

    def remove_rear(self):
        return self.dequeue.pop()

    def add_front(self, data):
        self.dequeue.insert_at_first(data)

    def add_rear(self, data):
        self.dequeue.append(data)

    def is_empty(self):
        self.dequeue.is_empty()

    def size(self):
        return self.dequeue.size()

    def display(self):
        self.dequeue.display()

#===============================================================================================================


class Palindrome:
    """
    This class defines the palindrome in which various function are define
    """

    def __init__(self):
        self.dequeue = Dequeue()

    def palindrome(self, string):
        """This defines the function which check that a given string is palindrome or not
        using dequeue.
        :param string: user gives string which we check it is palindrome or not
        :return:It returns true or false
        """
        for letter in string:
            self.dequeue.add_rear(letter)
        string1 = ""
        for i in range(len(string)):
            a = self.dequeue.remove_rear()
            string1 = string1 + a
        string2 = string1[::-1]
        return string1 == string2

#============================================================================================================


class BinarySearchTree:
    """Number of Binary search trees
    This class contains methods which can perform the below mentioned methods
    """
    def __init__(self):
        pass

    def factorial(self, n):
        """This method calculates the factorial of a number

        :returns:factorial: the calculated factorial of the number n
        """
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact

    def catalan_formula(self, nodes):
        """This method uses the catalan formula to find out the number of binary search trees
        :parameter:nodes: Number of nodes of the binary search tree
        :returns: Returns the number of binary search trees that can be created using these many nodes
        """
        binary_search_tree_numbers = int(self.factorial(nodes*2)/(self.factorial(nodes+1) * self.factorial(nodes)))
        return binary_search_tree_numbers

    def binary_search_tree(self):
        """This method takes in a number of test cases and prints of the number of binary
        search trees for the respective number of nodes
        """
        test_cases = int(input("Enter a number of test cases: "))
        for i in range(test_cases):
            nodes_input = int(input("Enter the number of nodes: "))
            print("Binary search trees ", self.catalan_formula(nodes_input))

#================================================================================================


class PrimeNumber:
    """
    This class define the various method based on the prime number
    """
    def __init__(self):
        self.prime = LinkedList()

    def prime_number_twodarray(self):
        """this method define the prime number from 0 t0 1000 in two d array

        :return: it return the two d array list
        """
        prime_list_2d = []
        lower = 0
        upper = 100
        while True:
            li = []
            for num in range(lower, upper+1):
                x = utility_object.is_prime(num)  # calling the is prime function
                if x is True:
                    li.append(num)  # add the num in li list
                if num >= upper-1:
                    break
            prime_list_2d.append(li)  # append the li to the 2d array list
            lower = upper
            upper = upper+100
            if upper >= 1001:
                break
        return prime_list_2d

    def anagram(self):
        """
        This function check the prime angaram and return the prime anagram list
        :return: return the prime anagram list
        """
        anagram_list = []
        prime_list = utility_object.prime_number()
        for i in prime_list:
            for j in prime_list:
                if i != j and (self.prime.insert(str(i)) == self.prime.insert(str(j))):
                    anagram_list.append(i)
        return anagram_list

#===============================================================================================================

























