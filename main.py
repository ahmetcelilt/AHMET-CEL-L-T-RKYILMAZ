from database import (
    create_tables,
    add_book,
    list_books,
    add_member,
    list_members,
    borrow_book,
    return_book
)


def show_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add Member")
    print("4. List Members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("0. Exit")


def main():
    create_tables()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Book title: ")
            author = input("Book author: ")
            year = input("Publication year: ")

            try:
                year = int(year)
            except ValueError:
                year = None

            add_book(title, author, year)
            print("Book added successfully.")

        elif choice == "2":
            books = list_books()

            print("\nBooks:")
            if not books:
                print("No books found.")
            else:
                for book in books:
                    print(
                        f"ID: {book[0]} | "
                        f"Title: {book[1]} | "
                        f"Author: {book[2]} | "
                        f"Year: {book[3]} | "
                        f"Status: {book[4]}"
                    )

        elif choice == "3":
            name = input("Member name: ")
            email = input("Member email: ")

            try:
                add_member(name, email)
                print("Member added successfully.")
            except Exception:
                print("Error: This email may already exist.")

        elif choice == "4":
            members = list_members()

            print("\nMembers:")
            if not members:
                print("No members found.")
            else:
                for member in members:
                    print(
                        f"ID: {member[0]} | "
                        f"Name: {member[1]} | "
                        f"Email: {member[2]}"
                    )

        elif choice == "5":
            try:
                book_id = int(input("Book ID: "))
                member_id = int(input("Member ID: "))

                message = borrow_book(book_id, member_id)
                print(message)
            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "6":
            try:
                book_id = int(input("Book ID: "))

                message = return_book(book_id)
                print(message)
            except ValueError:
                print("Please enter a valid book ID.")

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
