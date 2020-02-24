# verify-helper: PROBLEM https://judge.yosupo.jp/problem/zalgorithm
import sys
input = sys.stdin.buffer.readline

from python_library.string.z_algorithm import z_algorithm


def main() -> None:
    print(*z_algorithm(input().strip()))


if __name__ == "__main__":
    main()
