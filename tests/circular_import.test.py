# verify-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb
from python_library.tmp_circular.a import a
from python_library.tmp_circular.b import b


def main() -> None:
    A, B = map(int, input().split())
    print(A + B)


if __name__ == '__main__':
    main()
