#String reverse function
def reverse_string (input_string):
    
    return input_string[::-1]

def main():
    #Get user input
    input_string = input("Enter a string here: ")

    #Pass the value to function and get output
    output_string = reverse_string(input_string)

    #print output
    print("Reverse string: ", output_string)

if __name__ == "__main__":
    main()