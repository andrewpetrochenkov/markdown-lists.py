<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/markdown-lists.svg?maxAge=3600)](https://pypi.org/project/markdown-lists/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/markdown-lists.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/markdown-lists.py/actions)

### Installation
```bash
$ [sudo] pip install markdown-lists
```

#### Examples
```python
>>> import markdown_lists

>>> lists = ["item1",["subitem11","subitem12"],"item2"]
>>> markdown_lists.render(lists)
+   item1
    +   subitem11
    +   subitem12
+   item2
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>