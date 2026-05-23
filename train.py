# task - M
def getSquareNumbers(data):
    result = []
    for n in data:
        result.append({"number": n, "square": n**2})
    return result


print(getSquareNumbers([1, 2, 3]))


# task - L
# def reverseSentence(data):
#     arr = data.split(" ")
#     new_arr = []
#     for word in arr:
#         new_arr.append(word[::-1])
#     return " ".join(new_arr)


# print(reverseSentence("we like coding!"))
