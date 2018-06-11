import pyperclip

raw_list = pyperclip.paste()

new_list = raw_list.split()

# check every item in list if is digit
# if all are digits convert to int/float
new_list.sort()

result = str(" ".join(new_list))
pyperclip.copy(result)


