factor_list = []
def get_factors(input):
    for x in range(1 , input+1):
        if input % x == 0:
            factor_list.append(x)

prime_numbers = []
prime = False
Ask = True
def isPrime(number):
    get_factors(number)
    if len(factor_list) > 2:
        number += 1
        factor_list.clear()
        prime = True
        return prime
    else:
        prime = False
        factor_list.clear()
        return prime
num = 2

# while Ask:
#     inp = input('next prime?(y/n): ')
#     if inp.lower() == 'y':
#         if isPrime(num) == prime:
#             prime_numbers.append(num)
#             print(num)
#         num += 1
#     else:
#         print(prime_numbers)

while Ask:
    if isPrime(num) == prime:
        inp = input('next prime?(y/n): ')
        if inp.lower() == 'y':
            prime_numbers.append(num)
            print(num)
        else:
            print(prime_numbers)
            print(len(prime_numbers))
            exit()
    num += 1
