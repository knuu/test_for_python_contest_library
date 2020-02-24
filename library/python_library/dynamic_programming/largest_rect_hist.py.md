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


# :heavy_check_mark: python_library/dynamic_programming/largest_rect_hist.py

<a href="../../../index.html">Back to top page</a>

* category: <a href="../../../index.html#aa415874213902fc17e0d0a11c5743d4">python_library/dynamic_programming</a>
* <a href="{{ site.github.repository_url }}/blob/master/python_library/dynamic_programming/largest_rect_hist.py">View this file on GitHub</a>
    - Last commit date: 2020-02-24 15:17:08+00:00




## Verified with

* :heavy_check_mark: <a href="../../../verify/tests/largest_rect_hist.test.py.html">tests/largest_rect_hist.test.py</a>
* :heavy_check_mark: <a href="../../../verify/tests/largest_rect_rect.test.py.html">tests/largest_rect_rect.test.py</a>


## Code

<a id="unbundled"></a>
{% raw %}
```cpp
def calc_largest_rect_in_hist(heights):
    heights.append(0)
    stack = []
    left = [0] * len(heights)
    ans = 0
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] >= height:
            idx = stack.pop()
            ans = max(ans, (i - left[idx] - 1) * heights[idx])
        left[i] = stack[-1] if stack else -1
        stack.append(i)
    heights.pop()
    return ans

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
