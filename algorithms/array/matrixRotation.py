def rotate90Degrees(m):
    layers = len(m) // 2
    length = len(m) - 1

    for layer in range(layers): #for each layer
        for i in range(layer, length - layer): # loop through the elements we need to change at each layer
            temp = m[layer][i] #save the top element, it takes just one variable as extra memory
            #Left -> Top
            m[layer][i] = m[length - i][layer]
            #Bottom -> left
            m[length - i][layer] = m[length - layer][length - i]
            #Right -> bottom
            m[length - layer][length - i] = m[i][length - layer]
            #Top -> Right
            m[i][length - layer] = temp
    return m