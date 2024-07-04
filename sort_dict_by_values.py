# Function calling
def sort_dict_by_value():

    # Declaring dictionary
    input_dict = {}

    while True:

        try:

            #Declaring length
            dict_length = int(input("Enter a number of entries you want to add: "))
            
            for i in range(dict_length):
                key = input("Enter a key: ")
                value = input("Enter a value: ")
                input_dict.update({key: value})

            #Sort dictionary
            sorted_dict = sorted(input_dict.items(), key=lambda kv: (kv[1], kv[0]))

            return sorted_dict
        
        except ValueError:
            print("Invalid input. Pleace enter a number.")



def main():
    output_dict = sort_dict_by_value()

    #Print output
    print("Sorted dictionary: ", output_dict)

if __name__ == "__main__":
    main()
