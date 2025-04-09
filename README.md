# 📘 String Methods in Python

Python provides a rich set of **built-in string methods** that make text manipulation easy and efficient. These methods are used to perform various operations like formatting, searching, modifying, and analyzing strings.

---

## 🔤 Commonly Used String Methods

| Method | Description |
|--------|-------------|
| `str.upper()` | Converts all characters in the string to uppercase |
| `str.lower()` | Converts all characters to lowercase |
| `str.title()` | Converts the first character of each word to uppercase |
| `str.strip()` | Removes whitespace from both ends of the string |
| `str.lstrip()` | Removes whitespace from the beginning only |
| `str.rstrip()` | Removes whitespace from the end only |
| `str.replace(old, new)` | Replaces all occurrences of a substring |
| `str.find(sub)` | Returns the index of the first occurrence of the substring (-1 if not found) |
| `str.count(sub)` | Returns the number of times a substring appears in the string |
| `str.startswith(sub)` | Checks if the string starts with the given substring |
| `str.endswith(sub)` | Checks if the string ends with the given substring |
| `str.split(sep)` | Splits the string into a list using the separator |
| `str.join(iterable)` | Joins the elements of an iterable with the string as a separator |

---

## 🧠 Examples

```python
text = "  Python Programming  "

print(text.strip())       # 'Python Programming'
print(text.upper())       # '  PYTHON PROGRAMMING  '
print(text.lower())       # '  python programming  '
print(text.title())       # '  Python Programming  '
print(text.replace("Python", "Java"))  # '  Java Programming  '
print(text.find("Prog"))  # 9
print(text.count("m"))    # 2
print(text.startswith(" "))  # True
print(text.endswith(" "))    # True

# Split and Join
fruits = "apple,banana,mango"
print(fruits.split(","))           # ['apple', 'banana', 'mango']
print(" - ".join(["one", "two"]))  # one - two
```

---

## 📌 Notes
- String methods **do not change the original string** (strings are immutable in Python).
- Most methods **return a new string** based on the transformation.
- Always assign the result to a variable or use `print()` to view changes.

---

## ✅ Practice Tip

Try applying these methods in small projects like:
- Text formatters
- Word counters
- Simple password validators
- CSV parsers
