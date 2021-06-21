def sol1(numbers):
    n = len(numbers)
    if n < 3:
        raise ValueError('Necesito al menos 3 números')
    i = 0
    result = None

    while i < n:
        j = i + 1
        while j < n:
            k = j + 1
            while k < n:
                total = numbers[i] + numbers[j] + numbers[k]
                if result is None or total > result:
                    result = total
                k += 1
            j += 1
        i += 1

    return result

def sol2(numbers):
    if len(numbers) < 3:
        raise ValueError('Necesito al menos 3 números')

    a = b = c = None

    for n in numbers:
        if a is None or n > a:
            c = b
            b = a
            a = n
        elif b is None or n > b:
            c = b
            b = n
        elif c is None or n > c:
            c = n
    return a + b + c


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sol1(numbers))
    print(sol2(numbers))
