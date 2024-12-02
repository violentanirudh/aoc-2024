def main():
    silver()
    gold()

def silver():
    line = open('tests/1-silver.txt')

    left = []
    right = []

    for l in line:
        x, y = l.split()
        left.append(int(x))
        right.append(int(y))

    left.sort()
    right.sort()

    result = sum((abs(x-y) for x, y in zip(left, right)))

    print(f"SILVER : {result}")


def gold():
    line = open('tests/1-gold.txt')

    left = []
    right = {}

    for l in line:
        x, y = l.split()
        y = int(y)
        left.append(int(x))
        if right.get(y) is None:
            right[y] = 0
        right[y] += 1

    result = sum((x * (right.get(x) if right.get(x) else 0) for x in left))

    print(f"GOLD : {result}")

if __name__ == '__main__':
    main()