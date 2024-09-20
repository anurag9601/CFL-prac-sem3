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
