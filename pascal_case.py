def pascal_case(string):
    if isinstance(string, int):
        return str(string)
    if isinstance(string, float):
        return str(string)
    return ''.join(['_' + letter.lower() if letter.isupper() else letter for letter in string]).lstrip('_')


teste = 1
print(pascal_case(teste))
print(type(pascal_case(teste)))

teste = 0.1
print(pascal_case(teste))
print(type(pascal_case(teste)))

teste = 'PascalCase'
print(pascal_case(teste))
print(type(pascal_case(teste)))
