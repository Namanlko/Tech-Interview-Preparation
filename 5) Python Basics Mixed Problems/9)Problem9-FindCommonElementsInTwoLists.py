# Problem 9: Find Common Elements in Two Lists.

def List_Common_Element(list1, list2):
    return list(set(list1) & set(list2))

print(List_Common_Element([1, 2, 3], [2, 3, 4]))        # {2, 3}
print(List_Common_Element([1, 2, 3], [4, 5, 6]))        # set()
print(List_Common_Element([1, 1, 2, 2], [2, 2, 3]))     # {2}
print(List_Common_Element([], [1, 2]))                  # set()
print(List_Common_Element([5, 6, 7], [7, 8, 9]))        # {7}