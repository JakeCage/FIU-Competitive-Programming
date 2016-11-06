def isRotation(word, wordRotated):#O(n)
    if len(word) == len(wordRotated):
        for i in range(len(word)):
            if wordRotated[i:] + wordRotated[:i] == word:
                return True

    return False

print(isRotation("waterbottle","erbottlewat"))