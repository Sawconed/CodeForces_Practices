import math


def sort_by_even(a: list[int]) -> list[int]:
    evens = [num for num in a if num % 2 == 0]
    odds = [num for num in a if num % 2 != 0]

    return evens + odds


def count_pair(a: list[int]) -> int:
    count = 0

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            count += 1 if math.gcd(a[i], 2 * a[j]) > 1 else 0

    return count


def main() -> None:
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = []
        for i in input().split(' '):
            a.append(int(i))

        a = sort_by_even(a)
        print(count_pair(a))


if __name__ == "__main__":
    main()
