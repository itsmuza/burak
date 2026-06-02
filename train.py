# task - O
def calculateSumOfNumbers(data):
    sum = 0
    for i in data:
        if isinstance(i, int) and not isinstance(i, bool):
            sum += i
    return sum


print(calculateSumOfNumbers([10, "10", {"son": 10}, True, 35, False]))


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
