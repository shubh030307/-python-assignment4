file=open("output.txt","w")
writing_file=input("Enter text to write to the file: ")
file.write(writIng_file + "\n")
print("Data successfully written to output.txt.")
file.close()

file = open("output.txt", "a")
additional_text = input("Enter additional text to append: ")
file.write(additional_text + "\n")
print("Data successfully appended.")
file.close()

file = open("output.txt", "r")
print("Final content of output.txt:")
print(file.read())
file.close()

