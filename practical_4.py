def word_crawler():
    file_name = input("Enter the txt filename: ")

    try:
        file = open(file_name, "r")
    except:
        return "File not found"

    find_word = input("Enter the proper word want to find: ")

    words = file.readlines()

    word_lst = words[0].split(" ")

    for word in word_lst:
        if(word == find_word):
            return f"word {find_word} exist in the file"
    else:
        return f"word {find_word} not found in the file"

print(word_crawler())
