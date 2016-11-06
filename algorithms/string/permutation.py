def permutations(inStr):
    if len(inStr) <= 1:
        return [inStr]

    perms = permutations(inStr[1:])
    char = inStr[0]
    result = []
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[i:]+char+perm[:i])
            print(result)

    return result

print(permutations("asdf"))
print(len(permutations("asdf")))