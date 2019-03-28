# String Validators
# https://www.hackerrank.com/challenges/string-validators/problem

def string_validators(string):
    retorno = ''
    validators = ['isalnum()', 'isalpha()', 'isdigit()',
                  'islower()', 'isupper()']
    for validator in validators:
        retorno += str(any(eval('strg.'+validator) for strg in string)) + ' '
    return '\n'.join(retorno.split())


if __name__ == '__main__':
    s = 'qA2'
    print(string_validators(s))
