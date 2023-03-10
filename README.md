# stream2
## A sequence of elements supporting sequential operations.

Example:
```python
from stream2 import Uni

def test01(name: str):
    Uni.CreateItem().item(name) \
        .on_item().transform(lambda x: x[::-1]) \
        .subscribe(lambda x: print(x))

if __name__ == '__main__':
    test01('abc')

# >>> cba 
```
