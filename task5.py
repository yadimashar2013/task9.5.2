def is_prime(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        b = 0
        for i in range(2, a // 2 + 1):
            if (a % i == 0):
                b = b + 1
        if (b <= 0):
            print('Простое')
        else:
            print('Составное')

        return a

    return wrapper


@is_prime
def sum_three(num1, num2, num3):
    result = num1 + num2 + num3
    return result


result = sum_three(2, 3, 6)
print(result)
