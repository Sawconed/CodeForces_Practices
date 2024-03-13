def is_pangram(s: str) -> bool:
    if (len(s) < 26):
        return False

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    s = s.lower()

    for c in alphabet:
        if c not in s:
            return False

    return True


def main() -> None:
    n = int(input())
    s = input()
    print('YES' if is_pangram(s) else 'NO')


if __name__ == "__main__":
    main()
