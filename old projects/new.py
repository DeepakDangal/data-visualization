def is_prime_number(param_number):
    return all(param_number % i for i in range(2, param_number))
 
number = 13
is_prime = is_prime_number(number)
print("Is {} prime? {}".format(number, is_prime))
 
number = 11
is_prime = is_prime_number(number)
print("Is {} prime? {}".format(number, is_prime))