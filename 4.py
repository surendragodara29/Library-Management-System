user_ID = "Lib11006"
passw = "Rohan1234"

id_input = input("Enter User ID: ")
password = input("Enter password: ")

if id_input == user_ID and password == passw:
    print("Welcome sir!")

    def Book_Management():
        l = ["General Knowledge", "Political science", "Social science", "Code with harsh"]
        while True:
            print("a = add_book")
            print("b = remove_book")
            print("c = exit")
            choise = input("Enter what you want to edit: ")

            if choise == "a":
                l.append(input("Enter book name: "))
                print("Book added!")

            elif choise == "b":
                book = input("Enter book name: ")
                if book in l:
                    l.remove(book)
                    print("Book is removed!")
                else:
                    print("Book does not exist!!")

            elif choise == "c":
                print("Thank You!")
                break

            else:
                print("Invalid choice!")

            print(l)

    def Student_Management():
        L1 = ["Surendra", "Vashu", "Rutvik", "Harsh", "Rohan"]
        while True:
            print("a = Register new Student")
            print("b = Remove Student")
            print("c = View Student")
            print("d = Exit")
            choise = input("Enter what changes you want to make?: ")

            if choise == "a":
                L1.append(input("Enter the name of the Student: "))
                print("Student added!")

            elif choise == "b":
                name = input("Enter name of student you want to remove: ")
                if name in L1:
                    L1.remove(name)
                    print("Student removed!")
                else:
                    print("Student does not exist!!")

            elif choise == "c":
                name = input("Enter the name of Student: ")
                if name in L1:
                    print("Index:", L1.index(name))
                else:
                    print("Student does not exist!!")

            elif choise == "d":
                print("Thank You!")
                break

            else:
                print("You Do Not Have Authority To Make Change!")

    def Issue_Book():
        l = ["General Knowledge", "Political science", "Social science", "Code with harsh"]
        while True:
            name = input("Enter name of Student (or 'exit' to stop): ")
            if name.lower() == "exit":
                break

            Registration_number = input("Enter Registration number: ")
            Book_name = input("Enter Book name: ")
            Date = input("Enter Date: ")

            if Book_name in l:
                print("Return the Book in Seven Days!!")
            else:
                print("Book is not Available!!")

    def make_changes():
        while True:
            print("a = Book_Management")
            print("b = Student_Management")
            print("c = Issue_Book")
            print("d = Exit Program")
            edit = input("Enter what changes you want to make?: ")

            if edit == "a":
                Book_Management()
            elif edit == "b":
                Student_Management()
            elif edit == "c":
                Issue_Book()
            elif edit == "d":
                print("Goodbye!")
                break
            else:
                print("Invalid option!")

    make_changes()

else:
    print("Incorrect ID or Password")
    