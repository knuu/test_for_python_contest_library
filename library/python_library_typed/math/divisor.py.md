---
layout: default
---

<!-- mathjax config similar to math.stackexchange -->
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    TeX: { equationNumbers: { autoNumber: "AMS" }},
    tex2jax: {
      inlineMath: [ ['$','$'] ],
      processEscapes: true
    },
    "HTML-CSS": { matchFontHeight: false },
    displayAlign: "left",
    displayIndent: "2em"
  });
</script>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/jquery-balloon-js@1.1.2/jquery.balloon.min.js" integrity="sha256-ZEYs9VrgAeNuPvs15E39OsyOJaIkXEEt10fzxJ20+2I=" crossorigin="anonymous"></script>
<script type="text/javascript" src="../../../assets/js/copy-button.js"></script>
<link rel="stylesheet" href="../../../assets/css/copy-button.css" />


# :warning: python_library_typed/math/divisor.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#769bec8a7401b9ea69076e29f833e3d2">python_library_typed/math</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library_typed/math/divisor.py">View this file on GitHub</a>
    - Last commit date: 2020-02-24 15:17:08+00:00




## Code

<a id="unbundled"></a>
{% raw %}
```cpp
from copy import deepcopy
from functools import reduce
from typing import Dict, List


class Divisor:
    """ make divisors list and prime factorization list of n
        complexity: O(n^(1/2))
        used in ProjectEuler No.12, yukicoder No.36
    """
    def __init__(self, n: int) -> None:
        assert(n >= 1)
        number = n
        if number == 1:
            self.primeFactorization = {1: 1}
        else:
            self.primeFactorization = {}
            for i in range(2, int(n**0.5)+1):
                cnt = 0
                while number % i == 0:
                    cnt += 1
                    number //= i
                if cnt > 0:
                    self.primeFactorization[i] = cnt
            if number > 1:
                self.primeFactorization[number] = 1

    def primeFactors(self) -> Dict[int, int]:
        return deepcopy(self.primeFactorization)

    def numDivisors(self) -> int:
        """ the number of divisors """
        if self.primeFactorization.get(1, 0) == 1:
            return 1
        numDiv = 1
        for _, cnt in self.primeFactorization.items():
            numDiv *= cnt+1
        return numDiv

    def sumDivisors(self) -> int:
        return reduce(lambda x, y: x * y, [sum(p**i for i in range(n+1)) for p, n in self.primeFactorization.items()])


def divisorsList(n: int) -> List[int]:
    assert(n >= 1)
    divsList = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divsList.append(i)
            if n // i != i:
                divsList.append(n//i)
    return sorted(divsList)

```
{% endraw %}

<a id="bundled"></a>
{% raw %}
```cpp
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.8.1/x64/lib/python3.8/site-packages/onlinejudge_verify/docs.py", line 348, in write_contents
    bundled_code = language.bundle(self.file_class.file_path, basedir=self.cpp_source_path)
  File "/opt/hostedtoolcache/Python/3.8.1/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/python.py", line 68, in bundle
    raise NotImplementedError
NotImplementedError

```
{% endraw %}

<a href="../../../index.html">Back to top page</a>

