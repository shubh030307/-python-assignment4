# -python-assignment4
### TASK 1
1. It opens a file(sample.txt) in **read mode** and iterates to print the first two lines.
2. However, in the `print` statement, `"Line {i}:"` is written as a string rather than formatted properly using `f-strings` or `.format()`, meaning `{i}` won't be replaced with the actual line number.
3. If the file doesn’t exist, it gracefully handles the error with a `FileNotFoundError` exception.
4.sample.txt (assuming the file contains):
- This is a sample text file.
- It contain multiple lines.

### TASK 2 
Functionality:
1. Writing to a File:
   - Opens `output.txt` in **write mode** (`"w"`), erasing any previous content.
   - Takes user input (`writing_file`) and writes it to the file.
   - Closes the file to save changes.

2. Appending Data:
   - Reopens the file in **append mode** (`"a"`).
   - Takes additional user input and appends it.
   - Closes the file again to ensure data is stored.

3. Reading and Displaying Content:
   - Opens the file in **read mode** (`"r"`).
   - Reads and prints the file’s content.
   - Closes the file after reading.
