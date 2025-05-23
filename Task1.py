def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for i in range(1, 3):
                print("Line {i}: ", file.readline())
    except FileNotFoundError:
        print("Error: The file", filename,"was not found.")
filename = input("Enter file name: ")
read_file(filename)

