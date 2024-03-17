#variant 1
text = "You better lose yourself in the music, the moment You own it you better never let it go"
print(f"Original text: {text}")
letter = input("Enter one letter for delete: ")

result = text.replace(letter, "")
print(f"Result: {result}")

#variant 2
text_1 = input("Enter your text: ")
letter = input("Enter one letter for delete: ")

result_1 = text_1.replace(letter, "")
print(f"Result: {result_1}")