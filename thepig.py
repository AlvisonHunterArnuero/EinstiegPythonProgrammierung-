def the_pig(val):
    value = len(val)
    value == sum(int(x) ** len(str(value)) for x in str(value))*3
    print(value)
    return value

the_pig('Eleazar')
