def flatten(l, new_list):
    try:
        for x in l:
            if isinstance(x, list):
                new_list=flatten(x, new_list)
            elif isinstance(x, str) and not isinstance(x, type(None)):
                print(x)
                new_list.append(x)
                return new_list
        return new_list
    except Exception as e:
        print ("ERROR", e)

input_list=[[[[[[[[[['a'],'b']]],'c']]],'d']],'e']

print ("\nYour new list:", flatten(input_list, []))