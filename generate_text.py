
# Text to be written to the file
sample_text = """Python is a widely used high-level programming language.
Created by Guido van Rossum and first released in 1991.
Python has a design philosophy that emphasizes code readability.
It supports multiple programming paradigms, including object-oriented, imperative, and functional.
Learning Python is a great way to start your coding journey.
Practice makes perfect, especially when dealing with files, lists, and dictionaries!"""

# Create and open a new file in write mode ('w')
with open('generated_text.txt', 'w') as file:
    file.write(sample_text)
print("File 'generated_text.txt' has been created successfully!")