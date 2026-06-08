# task - R
def calculate(data):
    sum = 0
    args = data.split("+")
    for n in args:
        sum += int(n)
    return sum

print(calculate("1 + 2 + 10 + 11"))




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
