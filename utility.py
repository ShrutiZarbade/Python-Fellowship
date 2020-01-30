"""
   This is a utlity file which contains utility class having different methods.
   Author: Shruti Zarbade
   Date : 13/01/2019
"""
import random
import math
import datetime
import cmath


class Utility:

    # Basic Core Programs

    @staticmethod
    def replace_string(string):
        """Method is used to replace the username:

        This method is used to replace a username with name given by user

        :param string: It will take string as a input and replace it with username
        :return: This function will return the new_string as output
        """

        string1 = "Hello, <<username>> How are you?"

        # validating user input
        if len(string) > 3 and string.isalnum() and (string.isnumeric() == False):
            new_string = string1.replace("<<username>>", string).title()
            return new_string

        else:
            print("Length of username should be greater than 3 character or the string given is a numeric value")
            # if name is less than 3 character then it shows else part

    @staticmethod
    def flip_coin(flip):
        """This Methods is randomly gives head and tail

           This method will return the number of times head and tails occurs and its percentage.

        :param flip: It will take a flip number from a user
        :return:head and tails percentage
        """

        heads = 0
        tails = 0
        for i in range(flip):
            trails = random.uniform(0, 1)  # it takes random number between 0 and 1
            if trails > 0.5:
                print("heads")
                heads += 1  # counts the number of heads occurs
            else:
                print("tails")
                tails += 1  # counts the number of tails occurs
        print("Number of head: ", heads)
        print("Number of tails: ", tails)

        heads_percentage = 100 * heads / flip  # calculate  the  percentage of heads coming
        print("Percentage of heads: ", heads_percentage)

        tails_percentage = 100 * tails / flip
        print("percentage of tails: ", tails_percentage)  # calculate  the  percentage of tails coming

    @staticmethod
    def leap_year(year):
        """
            Method is given the year is a leap year or not

            This takes the year from the user and gives that the year is leap year or not
        :return: leap year or not
        """
        if (year > 1000) and (year < 9999):  # It check that digit should be of four digit
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:   # condition to check leap year
                return "It is a leap year"
            else:
                return "It is not a leap year"

        else:
            return "It's not a 4 digit"  # this part return that the number should be of 4 digit

    @staticmethod
    def power_of_2(n):
        """ Method is used to give the power of 2.

            In this user gives the power and it return the 2 raise to power of n.

        :param n: User gives n upto  which it calculate the power of 2
        :return: It returns the table upto n value.
        """
        if n < 31:
            arr = []
            for i in range(1, n + 1):  # it checks from range 1 to 31
                num = 2 ** i  # the 2**i gives the exponent of 2
                print(num)
                arr.append(num)
            return arr
        else:
            return "Number is greater than 31"

    @staticmethod
    def harmonic_number(n):
        """Methods is used to give the harmonic number.

            The n is given by user and the value of n in harmonic series.

        :param n: n is number given by user we find harmonic number of n
        :return: It will return the harmonic number of n.
        """

        harmonic = 1
        for i in range(2, n+1):
            harmonic += 1/i  # It adds 1/i in h every time to get harmonic series addition

        return harmonic

    @staticmethod
    def prime_factorization(n):
        """ Method gives us prime factor of a number.

            It takes a number from a user to find its prime factor.

        :return: It returns all the prime factor of number given by user.
        """
        arr = []
        for i in range(2, n):
            while n % i == 0:  # it check the condition
                print("Factor is: ", i)
                arr.append(i)  # it append the empty list by the value of i
                n = n/i
        if n > 1:
            print("factor is: ", n)
            arr.append(n)  # it append the arr list further
        return arr

    # Functional Programs

    @staticmethod
    def two_darray(m, n):
        matrix = []
        print("Enter the entries row wise:")
        for i in range(m):  # loop for row entries
            a = []
            for j in range(n):  # loop for column entries
                a.append(int(input()))
            matrix.append(a)

        # For printing the matrix
        for i in range(m):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()

    @staticmethod
    def number_of_triplets(arr, n):
        """Methods to find the number of triplets whose sum is equal to 0

           In this array is given from that they find out 3 numbers whose sum is equals to 0

        :param arr:It is a 10 number array we have given
        :param n: It gives the length of array
        :return: It returns the 3 number whose sum is 0.
        """
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n-2):
                    if arr[i] + arr[j] + arr[k] == 0:
                        print("triplets is: ", arr[i],  arr[j], arr[k])

    @staticmethod
    def distance(x, y):
        """ Method gives us distance between two points.

            This method calculate the distance between point (x,y) and origin (0,0)
            the x and y is taken from the user.

        :return: It returns the distance between point(x,y) and (0,0)
        """
        # formula to find distance between two point
        distance = math.sqrt(math.pow((x-0), 2) + math.pow((y-0), 2))
        return round(distance, 4)  # returns the value of distance calculated by the formula

    @staticmethod
    def wind_chill(t, v):
        """ Method calculates the  wind chill

        this takes  two parameters t and v from the user and calculate the temperature
        using the formula of w.

        :param t: It takes temperature in Fahrenheit from the user.
        :param v: It takes wind speed in miles per hour from the user.
        :return: It returns the effective temperature w.
        """

        if t < 50 or v > 120 or v < 3:
            w = (35.74+0.6215*t+(0.4275*t-35.75) * math.pow(v, 0.16))
            # formula to find effective temperature of wind chill
            return round(w, 3)
        else:
            return "values are not in range"

    @staticmethod
    def quadratic_eqn(a, b, c):
        """ Method is to find the roots of quadratic equation
        
            This will take the a b and c variable from the user and find the root of equation 
            (a*x*x + b*x + c)

        :return: It returns the 2 root of quadratic equation
        """
        # Delta formula which is use to find roots
        delta = b*b - 4*a*c
        if delta > 0:
            print("Roots are real and different")
            print((-b + math.sqrt(delta)) / (2 * a))
            print((-b - math.sqrt(delta)) / (2 * a))

        elif delta == 0:
            print("Roots are real and same")  # if both delta == 0 then both the roots are real and equal
            print(-b / (2 * a))

        else:
            print("Roots are complex")  # if delta < 0 then roots are complex
            print(-b / (2 * a), "+ i", cmath.sqrt(delta))
            print(-b / (2 * a), "- i", cmath.sqrt(delta))

    # Algorithm Programs

    @staticmethod
    def insertion_sort(list):
        """ Method convert the unsorted list to the sorted list using insertion sort.

            In this the unsorted list is given by this function we a arrange that list
            in ascending order.

        :param list: list containing elements
        :return: It will return the sorted list
        """
        for i in range(1, len(list)):
            current_ele = list[i]
            pos = i

            while current_ele < list[pos-1] and pos > 0:
                list[pos] = list[pos-1]
                pos = pos-1
            list[pos] = current_ele
        return list

    @staticmethod
    def bubble_sort(list):
        """ Method is used to sort the list using bubble sort technique.

            In this the unsorted list is given it will check element wise and gives
            sorted list in ascending order

        :param list:unsorted list is    given which we have to convert in sorted form
        :return: It returns sorted list
        """
        for i in range(len(list)-1, 0, -1):
            for j in range(i):
                if list[j] > list[j+1]:
                    temp = list[j]
                    list[j] = list[j+1]
                    list[j+1] = temp
        return list

    @staticmethod
    def anagram(str1, str2):
        """ Methods shows that character in a string are equal

            this takes two string from user and checks the string is anagram or not

        :param str1: string given by user
        :param str2: string given by user
        :return: It returns that string is anagram or not
        """
        s1 = sorted(str1)  # it sort the string and arrange it in ascending order
        s2 = sorted(str2)
        if s1 == s2:
            return "It is an anagram"
        else:
            return "It is not an anagram"

    @staticmethod
    def is_prime(num):
        temp = 0
        for i in range(1, num+1):
            if num % i == 0:
                temp += 1
        if temp == 2:
            return True
        else:
            return False

    @staticmethod
    def prime_number():
        """Methods gives the prime number between 0 and 1000

        :return:the list of prime number between 0 and 1000
        """
        list = []
        for num in range(0, 1001):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    list.append(num)
        return list

    # Logical Programs

    @staticmethod
    def gambler(stake, goal, trails):

        """ Methods is to play the gambler game
         This takes stake goal and trails from the user and randomly generate
         the wins and loss occurs.

        :param stake: the amount to paid for game
        :param goal: the to wins the game
        :param trails: number of time you play the game
        :return: It returns the win or loss percentage  and wins time
        """
        bets = 0
        wins = 0
        for i in range(trails):
            cash = stake
            while (cash > 0) and (cash < goal):
                bets += 1
                if random.randint(0, 1) == 0:
                    cash += 1
                else:
                    cash -= 1
            if cash == goal:
                wins += 1

        print("wins percentage: " + str(100*wins//trails))
        print(str(bets//trails) + " average of bets")

    @staticmethod
    def simulate_stopwatch():
        """Method is simulate the stop watch

           In this we press any key to start the watch and press any key to stop
           the watch then it calculates the time between end and start

        :return: time between end and start
        """
        input("To start press any key: ")
        start = datetime.datetime.now()
        input("To stop press any key: ")
        end = datetime.datetime.now()

        result = end - start

        return result
