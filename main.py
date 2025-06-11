# Computer Science Holiday Homework by Ayush Bhomia

''' 
Ques 1: List contains the following elements: 3, 25, 13, 6, 35, 8, 14, 45. 
        Write a function to swap the content with the next value divisible by 5 so that the resultant List will look like: 25, 3, 13, 35, 6, 8, 45, 14
'''

def ans1() -> int:
    
    """
    ans1() Function gives output in int form.
    lis is the list which contains all numbers, loop runs from 0, 7.
    Condition is checked if the next number is divisible by 5.
    If yes, then nums are swapped.
    """

    lis = [3, 25, 13, 6, 35, 8, 14, 45] # Len of lis = 8
    for i in range(len(lis)-1): # range(0, 7)
        if lis[i+1]%5 == 0:
            lis[i], lis[i+1] = lis[i+1], lis[i]

    print(lis)

# ans1()


'''
Ques 2: Write a program to accept values from a user in a tuple. 
        Add a tuple to it and display its elements one by one. Also display its maximum and minimum value.
'''

def ans2() -> tuple:
    
    """
    ans2() Function accepts a tuple from the user and adds it to a predefined tuple.
    It then displays the elements one by one and the maximum and minimum value.
    Then a loop is used to iterate through the tuple and print each element and add the elements of the tuples.
    """

    user = eval(input("Enter the Tuple (x, y, z): "))
    tup = (34, 56, 2, 67, 54, 77) #  Predefined tuple
    res = [] # Enpty list to store the result
    
    for i in range(len(tup)):
        res.append(user[i] + tup[i])
    res = tuple(res)
    print(res)

    print(f"Maximum value: {max(res)}")
    print(f"Minimum value: {min(res)}")

    for j in res:
        print(f"Element: {j}")

# ans2()


'''
Ques 3: Write a program to input any values for two tuples. Print it, interchange it and then compare them.
'''

def ans3() -> tuple:
    """
    ans3() Function takes two tuples as input from the user.
    It then swaps the tuples and prints them.
    Then it compares the two tuples and prints the results.
    """

    user1 = eval(input("Enter the First Tuple (x, y, z): "))
    user2 = eval(input("Enter the First Tuple (x, y, z): "))
    print(f"First Tuple: {user1} \n Second Tuple: {user2}")

    user1, user2 = user2, user1
    print("---After Exchanging---")
    print(f"First Tuple: {user1} \n Second Tuple: {user2}")

# ans3()


'''
Ques 4: Write a Python program to input 'n' classes and names of their class teachers to store them in a dictionary and display the same.
        Also accept a particular class from the user and display the name of the class teacher of that class.
'''

def ans4() -> dict:
    """
    ans4() Function takes a class and the class teacher's name as key and value respectively.
    It then stores the data in a dictionary and displays the dictionary.
    Then a for loop is used to iterate the values of the keys and prints the class teacher's name.
    """
    dict = {}
    while True:
        class_name = input("Enter the Class (int): ")
        teacher_name = input("Enter the Teacher Name: ")
        dict[class_name] = teacher_name

        choice = input("Do you want to add more classes? [y/n]: ")
        if choice.lower() == 'n':
            break
    print(dict)

    class_name = input("Enter the Class Name to get the teacher's Name: ")
    print(f"Class Teacher Name: {dict.values(class_name)}")

# ans4()


'''
Ques 5: Write a program to store student names and their percentage in a dictionary and delete a particular student name from the dictionary.
        Also display the dictionary after deletion.
'''

def ans5() -> dict:
    """
    ans5() Function takes a Student's name and Percentage and then adds it to a dictionary as key and item respectively.
    It then stores the data in a dictionary and displays the dictionary.
    Finally The students name is removed along with his/her percentage using the pop fucntion.
    """
    dict = {}
    while True:
        student_name = input("Enter the Student's Name: ")
        percentage = input("Enter the Student's Percentage [%]: ")
        dict[student_name] = percentage

        choice = input("Do you want to add more data? [y/n]: ")
        if choice.lower() == "n":
            break
        
    del_name = input("Enter the Student's name which you want to remove: ")
    dict.pop(del_name)

    print(dict)

# ans5()


'''
Ques 6: Write a Python program to capitalize first and last letters of each word of a given string.
'''

def ans6() -> str:
    """
    ans6() Function takes a string as an input and capitalizes the first and last letter.
    The first and last index letters are replaced by the uppercase version of the letters of that index.
    """
    strs = input("Enter the String: ")
    zero = strs[0].upper()
    minus1 = strs[-1].upper()

    strs = strs.replace(strs[-1], minus1)
    strs = strs.replace(strs[0], zero)

    print(strs)

# ans6()


'''
Ques 7: Write a Python program to remove duplicate characters of a given string.
'''

def ans7() -> str:
    """
    ans7() Function Takes a string as an input and removes the duplicate characters.
    The string is simply converted to a set to remove duplicate chars and then converted again to a string.
    """
    strs = input("Enter the string with duplicate characters: ").split()
    sets = set(strs)
    res = str(sets).strip("{}")
    print(type(res), res)

# ans7()


'''
Ques 8: Write a Python program to compute sum of digits of a given string.
'''

def ans8() -> int:
    """
    ans8() Function takes a string and computes the sum of the number of digits in that string.
    """
    strs = input("Enter the String: ")
    count = 0
    for char in strs:
        if char.isdigit():
            count += int(char)

# ans8()


'''
Ques 9: Write a Python program to find the second most repeated word in a given string.
'''

def ans9() -> dict:
    """
    ans9() Function takes string as an input. 
    It then creates a Dictionary with the words and the number of frequencies of those words.
    Finally only those words are printed which have frequencies > 1.
    """
    strs = input("Enter the string: ")
    strs = strs.split()
    print(strs)
    dict = {}
    for i in strs:
        if strs.count(i) > 1:
            dict[i] = strs.count(i)
    print(dict)

# ans9()


'''
Ques 11: Write a Python program to multiply all the items in a list.
'''

def ans11() -> int:
    """
    ans11() Function multiplies all the items in a list and returns the product.
    It uses a variable to keep track of the running product and multiplies each element in the list.
    """
    lis = [1, 2, 3, 4, 5] # Sample List of Numbers
    product = 1
    
    for item in lis:
        product *= item
    
    print(f"List: {lis}")
    print(f"Product of all items: {product}")

# ans11()


'''
Ques 12: Write a Python program to get the smallest number from a list.
'''

def ans12() -> int:
    """
    ans12() Function takes a sample list and prints the minimum value in that list.
    """
    lis = [1, 34, 23, 5, 7, 34]
    print(min(lis))

# ans12()


'''
Ques 13: Write a Python program to append a list to the second list.
'''

def ans13() -> list:
    """
    ans13() Function takes a pre-defined list and extends a seperate list to that list.
    """
    lis1 = [34, 23, "Hello", "Python", True]
    lis1.extend([54, 75, "Ayush", False])
    print(lis1)

# ans13()


'''
Ques 14: Write a Python program to generate and print a list of first and last 5 elements
         where the values are square of numbers between 1 and 30 (both included).
'''

def ans14() -> int:
    """
    ans15() Function generates a list of squares of numbers from 0 to 30 (inclusive).
    It then prints the entire list, followed by printing pairs of elements:
    the first 6 elements and their corresponding elements from the end of the list.
    
    The function creates an empty list, fills it with squares of numbers from 0 to 30,
    and then displays the first 6 elements paired with the last 6 elements in reverse order.
    """
    lis = []
    for i in range(31):
        lis.append(i*i)
        
    print(lis)
    for j in range(6):
        print(lis[j], lis[-j])

# ans14()


'''
Ques 17: Write a Python script to check if a given key already exists in a dictionary. 
'''

def ans17() -> int:
    """
    ans17() Function takes a sample dictionary. 
    User is prompted to enter a key name, if the key is present in the dictionary, it returns the key.
    """
    dict = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
    ask = int(input("Enter the day number: "))
    if ask in dict:
        print(f"Key Exists: {dict.get(ask)}")
    elif ask not in dict:
        print("Key doesn't exists!")

# ans17()


'''
Ques 24: Write a python program to get the largest number from a list. 
'''

def ans24() -> int:
    """
    ans24() Function takes a pre-defined list and prints the max value in thst list'
    """
    lis = [34, 2, 456, 56, 294, 000, 99934, 34589]
    print(max(lis))

# ans24()

def main():
    ask = input("Enter the function name to run: ")
    match ask:
        case "ans1":
            ans1(), print(ans1.__doc__)
        case "ans2":
            ans2(), print(ans2.__doc__)
        case "ans3":
            ans3(), print(ans3.__doc__)
        case "ans4":
            ans4(), print(ans4.__doc__)
        case "ans5":
            ans5(), print(ans5.__doc__)
        case "ans6":
            ans6(), print(ans6.__doc__)
        case "ans7":
            ans7(), print(ans7.__doc__)
        case "ans8":
            ans8(), print(ans8.__doc__)
        case "ans9":
            ans9(), print(ans9.__doc__)
        case "ans11":
            ans11(), print(ans11.__doc__)
        case "ans12":
            ans12(), print(ans12.__doc__)
        case "ans13":
            ans13(), print(ans13.__doc__)
        case "ans14":
            ans14(), print(ans14.__doc__)
        case "ans17":
            ans17(), print(ans17.__doc__)
        case "ans24":
            ans24(), print(ans24.__doc__)

main()