inp = int(input('input number for prime factorization: '))
factor_list = []
def get_factors(input):
    for x in range(1 , input+1):
        if input % x == 0:
            factor_list.append(x)
    print(f'The factors of {inp} are {factor_list}')
get_factors(inp)