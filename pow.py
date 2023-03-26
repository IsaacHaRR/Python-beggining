def pow(base, pow_number):
    result = 1
    for index in range(pow_number):
        result = result * base
    return result

print(pow(3,2))