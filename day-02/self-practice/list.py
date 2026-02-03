#  List is used to store mutliple items on a single value.
#  Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:
# example :- my_list=[1,"Selvi",5.68]

# List Items :- List items are ordered changeable and allow duplicate values.List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered :- When we say that lists are ordered, it means that the items have a defined order, and that order will not change. If you add new items to a list, the new items will be placed at the end of the list.

# Mutable:-  The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.


clouds=[]
def user_input():
    for i in range(2):
        platforms=input("Enter the cloud platforms you know: ")
        clouds.append(platforms)
def brief_out():
    for platform in clouds:
        if platform == "aws":
            print(platform,"This is the worlds leading cloud platform and ranks number 1")
        elif platform == "azure" or platform == "gcp" or platform == "alibaba":
            
            print("This are the second popular platforms ")
        else:
            print("This is an Indian Cloud Platform")

user_input()
print("The different cloud platforms are : ", clouds)
brief_out()