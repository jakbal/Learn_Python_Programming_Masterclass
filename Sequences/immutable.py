result = True
another_result = result
print(id(result))
print(id(another_result))

result = False
print(id(result))

text = "Correct"
another_text = text
print(id(text))
print(id(another_text))

text += "ly"
print(id(text))
print(id(another_text))
