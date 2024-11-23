def main():

    mySimpleList = [1,2,3,4,5,6,7]
    mixedList = [1,"Hello", 'A', True]
    combinedList = mySimpleList + mixedList
    repeatedList = mixedList * 3
    mySimpleList.sort(reverse=True)
    print("Hello" in mySimpleList)
    print(repeatedList)
    print(combinedList)
    
#     #Lists can store elements of different data types, including numbers, strings, Booleans, and even other lists.
#     multiDataList = [1,"yeab", 'a', True, 1.4, [3,6]]
    
#     #accessingElement(mySimpleList,multiDataList)
#     # printingOut(mySimpleList,multiDataList)
#     # slicingList(mySimpleList)
#     addingToList(mySimpleList)

# # Lists are indexed, meaning each element has a unique position, starting from 0 for the first element, 1 for the second, and so on. This in
# def accessingElement(simpleList, multiDataList):
#     index = int(input(f"Enter the index you want to print[simple list] (0,{len(simpleList)}) You can do negative as well: "))
#     print(f"Simple List: {simpleList[index]}")
#     index = int(input(f"Enter the index you want to print[multidata] (0,{len(multiDataList)}):  You can do negative as well: "))
#     print(f"Multi Data: {multiDataList[index]}")

# def printingOut(simpleList, multiDataList):
#     print("The the elements of the simple list are: ")
#     for item in simpleList:
#         print(item, end=" ")
#     print("\n")

#     print("The elements of the multi data list are: ")
#     counter = 0
#     while counter < len(multiDataList):
#         print(multiDataList[counter], end=" ")
#         counter += 1

# # We can separate them into sub lists by using their index
# def slicingList(simpleList):
#     index1,index2 = map(int,input("Enter the index start and end accordingly: Separate them by commas: ").split(','))
#     sublist = simpleList[index1:index2]
#     print(sublist)

# # Adding items to our list
# def addingToList(simpleList):
#     num = int(input("How many items would you like to add: "))
#     while num > 0:
#         position, value = map(int,input("").split(','))
#         simpleList.insert(position,value)
#         num -= 1
#     print(simpleList)
main()

# nestedList = [[1,2,3], [2,3,4],[4,5,6]]

# print(nestedList[2][1])
#print(hash((1, 2, 3)))
# text = input("Enter your text: ")

# newList = list(text.split())
# print(newList)

# del newList[0]
# print(newList)

# newList.clear()
# print(newList)

# # repeatedList = ["Abebe"] * 7

# # print(repeatedList)



