def main():
    unsafe = []
    result_1 = silver(unsafe)
    result_2 = gold(unsafe)

    print(len(unsafe), result_1, result_2, result_1 + result_2)


def silver(unsafe):
    file = open('tests/2-silver.txt')
    counter = 0

    for line in file:
        arr = [int(x) for x in line.split()]
        if not is_safe(arr):
            unsafe.append(arr)
        else:
            counter += 1

    return counter


def gold(unsafe):
    counter = 0
    for arr in unsafe:
        for i in range(len(arr)):
            if is_safe(arr[:i] + arr[i+1:]):
                counter += 1
                break

    return counter

def is_safe(arr):
    sign = True
    safe = True

    if arr[1] - arr[0] < 0:
        sign = False
    else:
        sign = True

    for i in range(1, len(arr)):
        if 1 <= abs(arr[i] - arr[i - 1]) <= 3:
            if sign and arr[i] > arr[i - 1]:
                continue
            elif not sign and (arr[i] < arr[i - 1]):
                continue
            else:
                return False
        else:
            return False

    return True


if __name__ == '__main__':
    main()


