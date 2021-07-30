# You need to write regex that will validate a password to make sure it meets
# the following criteria:
# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# Valid passwords will only be alphanumeric characters.
# Made with ❤️ in Python 3 by Alvison Hunter - January 21st, 2020
import re
def validate_pwd(pwd):
    p  = re.compile(r'\w')
    x = p.match(pwd)
    print('Matchea ', x)
    if(pwd.isalnum()):
        print('Si es Alpha')
    else:
        print('No es alpha')
    print('Hi', pwd)


# Scenarios
validate_pwd('fjd3IR9')
validate_pwd('ghdfj32')
validate_pwd('DSJKHD23')
validate_pwd('dsF43')
# validate_pwd('4fdg5Fj3')
# validate_pwd('DHSJdhjsU')
# validate_pwd('fjd3IR9.;')
# validate_pwd('fjd3  IR9')
# validate_pwd('djI38D55')
# validate_pwd('a2.d412')
# validate_pwd('JHD5FJ53')
# validate_pwd('!fdjn345')
# validate_pwd('jfkdfj3j')
# validate_pwd('123')
# validate_pwd('abc')
# validate_pwd('123abcABC')
# validate_pwd('ABC123abc')
# validate_pwd('Password123')
