"""
Дана функция, она не рабочая. Нужно описать что тут не так текстом, поправить ошибки, словом -
сделать что бы работало.
К примеру:
 - console.log('fff') # в питоне такого нет (меняем но то что есть в питоне) -> print('fff')
"""

# import 'os'
# func readFileId(names=[], mode):
#     _ = ''
#     id = -1
#     for n in names:
#         with os.open(n, 'w') as f:
#             _ += f.read()
#         f.close()
#     print 'default: ' + id + ', actual: ' + _
#     return id ? _ : id

"""
    line 8 - excessive import
    line 9 - PEP recommendations for functions naming, mode param is not used, 
             mutable object cannot be used as a default value, func is not used in Python
    line 10, 11 - default id param is excessive, "result_id" is a more understandable name
    line 13 - unclear logic. instead of os commands better to use built-ins
    line 15 - file doesn't need to be closed due to using of "with" operator
    line 16 - better to use formatted string
    line 17 - wrong ternary operator, unclear logic (should it return result of "default or id" operation?)
"""


def read_file_id(names=None):
    names = names or []
    result_id = ""
    for n in names:
        with open(n, "r") as f:
            result_id += f.read()
    print(f"default: -1, actual: {result_id or -1}")
    return result_id or -1

