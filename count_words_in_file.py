#This function counts word in file
def count_words_in_file():
    while True:

        #Input file
        input_file = input("Enter the file name (Ex:- myFile.txt): ")
        try:
        #open file in read method
            with open(input_file, 'r') as file:

                text = file.read()
                word = text.split()
                count = len(word)

                return count
        except:
            
            print("File not fount. Please check and try again.")

def main():
    output_count = count_words_in_file()

    print("Words count in the file: ", output_count)

if __name__ == "__main__":
    main()

