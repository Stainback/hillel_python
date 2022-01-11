# Data input
data = input('Type your data elements for conversion. Use space to divide each element.   ')

# Data conversion to a list, a set, a tuple, a dict
data_list = data.split(' ')
data_tuple = tuple(data_list)
data_set = set(data_list)

keys = []
for key in range(len(data_list)):
    keys.append(key)
print(keys)
data_dict1 = dict(zip(keys, data_list))

data_dict2 = {i: data_list[i] for i in range(len(data_list))}                       # dictionary comprehension

# Data output
print(type(data_list), data_list)
print(type(data_tuple), data_tuple)
print(type(data_set), data_set)
print(type(data_dict1), data_dict1)
print(type(data_dict2), data_dict2)