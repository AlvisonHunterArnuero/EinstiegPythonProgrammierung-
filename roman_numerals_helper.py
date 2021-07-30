romans_dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
               "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def from_roman(roman_num):
    try:
        numeric_value = 0
        roman_key = ""
        roman_double_key = ""
        for n in range(len(roman_num)):
            roman_key = romans_dict.get(roman_num[n])
            roman_double_key = romans_dict.get(roman_num[n:n+2])
            if(roman_double_key != None):
                print(f"Double: {n} => {roman_double_key} Glyph: {roman_num[n]}")
                numeric_value += roman_double_key
                n += 1

            elif(roman_key != None):
                print(f"One: {roman_double_key} Glyph: {roman_num[n]}")
                numeric_value += roman_key
                n += 1
            else:
                print("Entro al Else")
                pass

        print(f"Number for {roman_num} is : {numeric_value}")
        print("-"*45)
    except KeyError:
        pass


def to_roman(num):
    numbers_dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
                    "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    roman_value = ""
    init_number = num
    while (num > 0):
        for k, val in numbers_dict.items():
            if(val <= num):
                roman_value = roman_value + k
                num -= val
                break
            else:
                pass
    print(f"Number for {init_number} is : {roman_value}")


from_roman('I')  # 1
from_roman('III')  # 3
from_roman('IV')  # 4
from_roman('XXI')  # 21
from_roman('MMVIII')  # 2008
# from_roman('MMVII')  # 2007
# from_roman('MDCLXIX')  # 1669

# to_roman(1000)  # M
# to_roman(1990)  # MCMXC
# to_roman(4)  # 'IV'
# to_roman(1)  # 'I'
# to_roman(1991)  # 'MCMXCI'
# to_roman(2006)  # 'MMVI'
# to_roman(2020)  # 'MMXX'
