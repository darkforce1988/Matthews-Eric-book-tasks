glossary = {
    'list': 'Lists are one of 4 built-in data types in Python '
            'used to store collections of data.',
    'comment': 'Comments used to make the code more readable.',
    'string': 'Strings are arrays of bytes representing unicode characters.',
    'dictionary': 'Dictionaries are used to store data values in key:value'
                  ' pairs.',
    'method': 'A methods in python are somewhat similar to a functions, '
              'except it is associated with object/classes.',
    'bool': 'Python bool() function is used to return or convert a value'
            ' to a Boolean value i.e., True or False, using the standard truth'
            ' testing procedure.',
    'None': 'None keyword is an object, and it is a data type of the class'
            ' NoneType .',
    'title': 'Title() is the Python String Method which is used to convert'
             ' the first character in each word to Uppercase and remaining '
             'characters to Lowercase in the string and returns a new string.',
    'cycle': 'cycle() Iterator is defined as object types which contains'
             ' values that can be accessed or iterated using a loop.',
    'operator': 'Operators are used to perform operations on values and'
                ' variables.',
}
for key, value in glossary.items():
    print(f"{key.title()}: {value.title()}")
