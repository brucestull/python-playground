# Python Playground

## Modules/Packages

## Concepts

### `@property`

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

obj = MyClass(42)
print(obj.value)  # Output: 42
```

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

obj = MyClass(42)
print(obj.value)  # Output: 42
obj.value = 23
print(obj.value)  # Output: 23
```

## Thirsty Cat

### Commands

- `python table.py`
