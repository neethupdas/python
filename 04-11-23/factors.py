def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

num = int(input("Enter a number: "))

if num < 1:
    print("Factors are not defined for numbers less than 1.")
else:
    result = find_factors(num)
    print("Factors of", num, "are:", result)
