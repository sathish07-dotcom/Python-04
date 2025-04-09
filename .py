text = "python programming"
result = text.upper()
print(result)  # Output: PYTHON PROGRAMMING

text = "   hello world   "
result = text.strip()
print(result)  # Output: hello world

text = "good morning everyone"
result = text.replace("morning", "evening")
print(result)  # Output: good evening everyone

text = "My name is Alice"
print(text.startswith("My"))   # Output: True
print(text.endswith("Bob"))    # Output: False

text = "apple,banana,cherry"
result = text.split(",")
print(result)  # Output: ['apple', 'banana', 'cherry']

words = ['Hi', 'there', 'friend']
result = " ".join(words)
print(result)  # Output: Hi there friend

text = "banana apple mango"
result = text.count("a")
print(result)  # Output: 5


text = "hello world"
result = text.find("o")
print(result)  # Output: 4 (index starts at 0)

text = "hello world"
result = text.title()
print(result)  # Output: Hello World

text = "PYTHON IS FUN"
result = text.lower()
print(result)  # Output: python is fun
