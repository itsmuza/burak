# Task Z
def sumEvens(arr):
    sum=0
    for n in arr:
        if(n%2==0): sum+=n
    return sum

print(sumEvens([1, 2, 3, 4]))




# task Y
# def findIntersection(arr1, arr2):
#     result = []
#     for n in arr1:
#         if n in arr2: result.append(n)
#     print(result)

# findIntersection([1, 2, 3], [3, 2, 0])




# task X
# def countOccurrences(data, check):
#     count=0
#     for key,value in data.items():
#         if(key == check): count+=1
#         if type(value) == dict:
#             for key1, value1 in value.items():
#                 if key1 == check: count+=1
#     print(count)

# countOccurrences({"model": "A", "s": {"model": "B"}}, "model")



# task W
# def chunkArray(arr, chunk):
#     result_arr = []

#     for i in range(0, len(arr), chunk):
#         temp_arr = []
#         for j in range(chunk):
#             if(i+j < len(arr)):
#                 temp_arr.append(arr[i+j])
#         result_arr.append(temp_arr)
#     return result_arr
   
# print(chunkArray([1, 2, 3, 4, 5,10], 3))


# task V
# def countChars(data):
#     obj={}
#     for key in data:
#         if(key in obj): obj[key] += 1
#         else: obj[key]=1
#     return obj
# print(countChars("hello"))




# task T
# def mergeSortedArrays(arr1, arr2):
#     for n in arr1:
#         arr2.append(n)
#     return sorted(arr2)

# print(mergeSortedArrays([0, 3, 4], [4, 6]))



# task - S
# def missingNumber(data):
#     max1 = max(data)
#     min1 = min(data)
#     for n in range(min1+1, max1):
#         if n not in data:
#             return n

# print(missingNumber([3,0,1]))




# task - R
# def calculate(data):
#     sum = 0
#     args = data.split("+")
#     for n in args:
#         sum += int(n)
#     return sum

# print(calculate("1 + 2 + 10 + 11"))




# task - Q
# def hasProperty(obj, str):
#     return True if str in obj else False
# print(hasProperty({"name": "BMW"}, "name"))




# task - P
# def objectToArray(data):
#     result = []
#     for key, value in data.items():
#         result.append([key, value])
#     return result

# print(objectToArray({"a": 10, "b": 20}))





# task - O
# def calculateSumOfNumbers(data):
#     sum = 0
#     for i in data:
#         if isinstance(i, int) and not isinstance(i, bool):
#             sum += i
#     return sum


# print(calculateSumOfNumbers([10, "10", {"son": 10}, True, 35, False]))


# task - N
# def palindromCheck(data):
#     return data == data[::-1]


# print(palindromCheck("dadadad"))


# task - M
# def getSquareNumbers(data):
#     result = []
#     for n in data:
#         result.append({"number": n, "square": n**2})
#     return result


# print(getSquareNumbers([1, 2, 3]))


# task - L
# def reverseSentence(data):
#     arr = data.split(" ")
#     new_arr = []
#     for word in arr:
#         new_arr.append(word[::-1])
#     return " ".join(new_arr)


# print(reverseSentence("we like coding!"))
