
#function for adding notes
def add_note(notes, note):
    notes.append(note)

#function for viewing all the notes user created
def view_notes(notes):
    for i, note in enumerate(notes):
        print ( str(i + 1) + "    " + note  )

    

def delete_note(notes, index):
    if 0 <= index < len(notes):
        deleted_note = notes.pop(index)
        print("Note  " + deleted_note + "  has been deleted ")
    else:
        print("Index is incorrect! Try again. ")


#main function
def main():
    #create empty list
    notes = []

    #create while loop for menu 
    while True:
        print("   Menu: Choose one   ")
        print("1. Create note")
        print("2. View notes")
        print("3. Delete notes")
        print("4. Exit \n")
    
        #user input

        choice = input("Enter your choice:  ")
        

        if choice == '1':
            note = input("Enter a note: ")
            #function call
            add_note(notes, note)

        elif choice == '2':
            view_notes(notes)

        elif choice == '3':
            index = int(input("Enter the index of the note to delete: "))
            delete_note(notes, index-1)
        elif choice == '4':
            break
        else:
            print("Invalid")
            continue


if __name__ == "__main__":
    main()   
