def reverseSentence(data):
    arr = data.split(" ")
    new_arr = []
    for word in arr:
        new_arr.append(word[::-1])
    return " ".join(new_arr)


print(reverseSentence("we like coding!"))
