def in_range(a, b, k):
    result = []
    count_a = count_b = 0

    for i in a:
        if (1 <= i and i <= k):
            result.append(i)
            count_a += 1

    for i in b:
        if (count_a == int(k/2) and count_b == int(k/2)):
            break

        if (1 <= i and i <= k):
            if (i in result):
                if (count_a <= int(k/2)):
                    continue
                else:
                    count_a -= 1
            else:
                result.append(i)

            count_b += 1

    #     print(count_a, count_b)
    #
    # print(result)

    return len(result) == k and count_a == count_b


def main() -> None:
    # t = int(input())
    #
    # for _ in range(t):
    #     n, m, k = (int(x) for x in input().split(' '))
    #
    #     a = (int(x) for x in input().split(' '))
    #
    #     b = (int(x) for x in input().split(' '))
    #
    #     print('YES' if in_range(set(a), set(b), k) else 'NO')
    a = [2, 3, 8, 5, 6, 5]
    b = [1, 3, 4, 10, 5]
    cnt = [0] * 7
    for e in a:
        if (e <= 6):
            cnt[e] |= 1
    for e in b:
        if (e <= 6):
            cnt[e] |= 2

    print(cnt)
    print(6 | 1)


if __name__ == "__main__":
    main()
