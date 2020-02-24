# verify-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_A
import sys
input = sys.stdin.buffer.readline

from python_library.math.divisor import Divisor


def main() -> None:
    N = int(input())
    p = Divisor(N)
    print("{}: ".format(N), end="")
    print(*[d for d, cnt in sorted(p.primeFactors().items()) for i in range(cnt)])


if __name__ == "__main__":
    main()
