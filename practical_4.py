#Simple way of code

def find_word():
    file_name = input("Enter proper file name: ")
    try:
        file = open(file_name)
    except:
        return "File not found"

    word_to_find = input("Enter proper the word: ")

    file_words = file.read()

    if(word_to_find in file_words):
        return f"{word_to_find} found in the file"
    else:
        return f"{word_to_find} not found in the file"

print(find_word())

#Code with quite complications

def word_crawler():
    file_name = input("Enter the txt filename: ")

    try:
        file = open(file_name, "r")
    except:
        return "File not found"

    find_word = input("Enter the word: ")

    words = file.readlines()

    word_lst = []


    for i in words:
        i = i.split(" ")
        for j in i:
            if("\n" in j):
                j = j[0:len(j)-1]
                word_lst.append(j)
            else:
                word_lst.append(j)

    for word in word_lst:
        if(word == find_word):
            return f"word {find_word} exist in the file"
    else:
        return f"word {find_word} not found in the file"

print(word_crawler())
