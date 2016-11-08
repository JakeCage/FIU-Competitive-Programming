import copy


def combinations(data,target=[]):
    for i in range(len(data)):
        print(i)
        new_target = copy.copy(target)#makes copy of array
        new_target.append(data[i])#
        new_data = data[i+1:]
        print(new_target)
        combinations(new_data, new_target)