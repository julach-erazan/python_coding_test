#input list
def input_list():
    while True:
        #input string here
        input_string = input("Enter a list nmubers seperated by spaces: ")

        #check user input validity
        try:

            input_list = [int(val) for val in input_string.split()]
            return input_list
        
        except ValueError:
            
            print("Invalid input. Please enter a numbers sparated by spaces.")

#This function returns squre of even numbers in list
def square_evens(input_string):
    square_list = [val ** 2 for val in input_string if val % 2 == 0]
    return square_list

def main():
    output_list = square_evens(input_list())

    #print output
    print("Square values of even numbers in list: ", output_list)


if __name__ == "__main__":
    main()