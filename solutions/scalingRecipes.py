numTests = int(input())
for recipeIter in range(numTests):
    settings = input()
    settings = settings.split()
    settings = [int(x) for x in settings]
    numIng = settings[0]
    multiplier = settings[2]/settings[1]

    ingList = []
    for ingIter in range(numIng):
        ingredient = input()
        ingredient = ingredient.split()

        if ingredient[2] == "100.0":
            baseWeight = float(ingredient[1])*multiplier

        ingList.append(ingredient)

    print("Recipe # " + str(recipeIter+1))
    for ing in ingList:
        print(ing[0] + " " + str(baseWeight*(float(ing[2])/100)))
    print("----------------------------------------")