#file = open('sample.txt','w')
#file.write("this is python project ")
#file.close()

import os

#help user to create file
def create_file(filename):
    try: #exception handling
        with open(filename, 'x') as f:     #insted of using close()
            print(f"File Name {filename}: created sucessfully!") #this msg get displayed after file is created
   
    #there can be 2 types of error 1:file already exists 0r 2:unexpected error
    except FileExistsError:    
        print(f"File Name {filename}: already exists!")

    except Exception as E:
        print(f"An unexpected error occurred:")

def view_all_files():   #this function will display all the files in the current directory
    files = os.listdir()  #give all directory list in the current directory
    if not files:
        print("No file found!")   #if no file - not found 
    else:
        print("Files in directory")  #if file found it runs loop and print all files
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)  #it remove specified file
        print(f"{filename} deleted successfully!")

    except FileNotFoundError:
        print("file not found!")

    except Exception as e:
        print("an error occurred")

def read_file(filename):
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(f"content of '{filename}' :\n{content}")
                  
    except FileNotFoundError:
        print("file not found!")

    except Exception as e:
        print("an error occurred")



def edit_file(filename):
    try:
        with open('sample.txt', 'a') as f:
            content = input("enter data to add: ")
            f.write(content + "\n")
            print(f"content added to '{filename}' successfully!")
    except FileNotFoundError:
        print("file not found!")

    except Exception as e:
        print("an error occurred")


def main():
    while True:
        print("FILE MANAGEMENT SYSTEM")
        print("1. Create File")
        print("2. View All Files")
        print("3. Delete File")
        print("4. Read File")
        print("5. Edit File")
        print("6. Exit")

        choice = input("enter your choice(1-6):  ")

        if choice == '1':
            filename = input("enter file name: ")
            create_file(filename)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            filename = input("enter file name to delete: ")
            delete_file(filename)

        elif choice == '4':
            filename = input("enter file name to read: ")
            read_file(filename)

        elif choice == '5':
            filename = input("enter file name to edit: ")
            edit_file(filename)

        elif choice == '6':
            print("exiting the program")
            break  

        else:
            print("invalid choice! please enter a number between 1 and 6")

if __name__ == "__main__":        #this is the entry point of the program
    main()                #it will call the main function when the script is run directly, allowing the user to interact with the file management system
