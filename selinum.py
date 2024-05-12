import pyperclip
pyperclip.copy('text to be copied')

data = pyperclip.paste()
print(data)
print(type(data))
