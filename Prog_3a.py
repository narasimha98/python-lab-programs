#Write a function which concatenates all given strings to a single string.
# User can specify sep - default should be comma.
# User can specify first string - default should be 'result: '


def combine(*all, init = "result: ", sep = ','):
    return init + sep.join(all)

print(combine('this', 'is', 'a', 'test'))
print(combine('this', 'is', 'a', 'test', init = 'fool ', sep= ' - '))