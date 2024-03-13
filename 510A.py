def draw_snake(n: int, m: int) -> None:
    switch = 0
    for i in range(n):
        if (i % 2 == 0):
            print('#' * m)
            switch += 1
        else:
            print(f"#{'.' * (m - 1)}" if (switch %
                  2 == 0) else f"{'.' * (m - 1)}#")


def main() -> None:
    n, m = (int(x) for x in input().split(' '))
    draw_snake(n, m)


if __name__ == "__main__":
    main()
