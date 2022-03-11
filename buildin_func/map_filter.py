
a = ["a", "b", "c", "d", "e", "f"]
b = [1, 2, 3, 4, 5, 6]


dictionary = {}
j = 0
for i in a:
    print(b[j])
    dictionary[i] = b[j]
    j += 1

print(dictionary)