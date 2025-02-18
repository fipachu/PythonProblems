# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, please
marks = OrderedDict(json.loads(input()))

# your code here
marks = {'Max': 100} | marks
print(marks)
