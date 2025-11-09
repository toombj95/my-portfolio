def create_catalog():
    
    '''Returns a pre-filled catalog with some example authors and books'''
    
    return {
        ("J.K.", "Rowling"): ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Half-Blood Prince"],
        ("George", "Orwell"): ["1984", "Animal Farm"],
        ("F. Scott", "Fitzgerald"): ["The Great Gatsby"],
        ("Kennedy", "Ryan"): ["The Kingmaker", "The Rebel King", "Queen Move", "Long Shot", "Hook Shot"],
        ("Octavia E.", "Butler"): ["Parable of the Sower", "Kindred", "Fledgling"]
    }

def add_book(catalog):
        
    '''Prompts user to add a book to the catalog.
    Parameters:
        catalog (dict): Existing catalog of authors and their books.

    Returns:
        dict: Updated catalog including the new author/book.'''
        
    first_name = input("Enter author's first name (or press Enter to finish): ")
    last_name = input("Enter author's last name (or press Enter to finish: ")
    book_title = input("Enter book title (or press Enter to finish: ")

    if not first_name or not last_name or not book_title:
        print("No book added.\n")
        return catalog # exit without adding anything
    
    key = (first_name, last_name)

    #Add author to catalog if they don't exist
    if key not in catalog:
        catalog[key] = []

    #Add book title to author's list
    catalog[key].append(book_title)

    print(f"Added '{book_title}' by {first_name} {last_name}.\n")

    return catalog


def checkout(available_books, to_checkout):
    
    '''Attempts to checkout a book from the available_books set.

    Parameters:
        available_books (set of str): set of book titles currently available.
        to_checkout (str): title of the book to checkout.

    Returns:
        tuple:
            -the first element is True if the book was available and successfully checked out,
            or False if the book was not available.
            -the second element is a set representing the updated available_books with the checked
            out book removed if successful, or the original set if unsuccessful.'''

    if to_checkout in available_books:

        updated_books = available_books - {to_checkout}  #Remove the book
        print(f"✅'{to_checkout}' successfully checked out!")
        return updated_books  #gives the updated book list with checked out book removed

    else:
        print(f"❌Sorry, '{to_checkout} is not available for checkout.")
        
        return available_books #gives the original book list if requested book is unavailable
        


from datetime import date, timedelta  #used to call current date and calculate future due dates

def set_due_date(book, tracking_system):
    
    '''Assigns a due date to a book and adds it to a tracking system.

    Parameters:
        book (str): The title of the book to set a due date for.
        tracking_system (dict): A dictionary where keys are book titles (str) and values are due dates as tuples
        (year, month, day) with all integers.

    Returns:
        dict: the updated tracking system dictionary with the due date assigned to the book.'''

   #Dynamic due date, 14 days from today
    today = date.today()
    due = today + timedelta(days=14) #can change the days to set due date as desired
    due_date = (due.year, due.month, due.day)
    tracking_system[book] = due_date

    print(f"Due date for '{book}' set to {due_date[1]}/{due_date[2]}/{due_date[0]}")
    
    return tracking_system


def find_popular_authors(catalog):
    
    '''Identifies authors with multiple books in the catalog.

    Parameters:
        catalog (dict): A dictionary where each key is a tuple (first_name, last_name) representing an author and each
        value is a list of that author's book titles.

    Returns:
        set: A set of author names, as single string, "First Last") for authors who have more than one book listed in the catalog.'''

    popular_authors = set()
    
    #checks if author has multiple books, converts tuple of author name into a single string, and adds them to popular author set
    for author, books in catalog.items():
        if len(books) > 1:
            full_name = f"{author[0]} {author[1]}"
            popular_authors.add(full_name)
    return popular_authors

# ---------- Demo / Menu ----------
def main():
    catalog = create_catalog()
    available_books = {book for books in catalog.values() for book in books}
    tracking_system = {}

    print("Welcome to the Book Catalog Library System!\n")
    print("=== Library System Menu ===")

    while True:
        print("\nOptions:")
        print("1. View full catalog")  
        print("2. Add a book to the catalog")
        print("3. Checkout a book (with due date)")
        print("4. View popular authors")
        print("5. View available books")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")
        print()
        
        if choice == "1":  # view full catalog
            print("Full catalog:")
            for author, books in catalog.items():
                full_name = f"{author[0]} {author[1]}"
                print(f"{full_name}:")
                for book in books:
                    print(f"  - {book}")
                print()
                
        elif choice == "2":
            #Call add_book and update catalog and available_books
            catalog = add_book(catalog)
            available_books = {book for books in catalog.values() for book in books}

        elif choice == "3":
            book_input = input("Enter book(s) to checkout, separated by commas: ")

            # Split input, strip whitespace, remove duplicates while keeping order
            books_to_checkout = list(dict.fromkeys([book.strip() for book in book_input.split(",") if book.strip()]))

            for book in books_to_checkout:
                if book in available_books:
                    
                    # Checkout removes the book from available_books and prints success message
                    available_books = checkout(available_books, book)

                    # Set the due date
                    tracking_system = set_due_date(book, tracking_system)
                else:
                    print(f"❌Sorry, '{book}' is not available for checkout.")

                print()  # blank line between each book

        elif choice == "4":
            popular = find_popular_authors(catalog)
            if popular:
                print("\nPopular authors with multiple books:")
                for author in popular:
                    print(f"- {author}")
            else:
                print("No authors with multiple books.")

        elif choice == "5":
            print("\nAvailable books by author:")
            
            for author, books in catalog.items():
                
                # Filter only books that are still available
                available_by_author = [book for book in books if book in available_books]
                
                if available_by_author:  # Only show authors with at least one available book
                    print(f"{author[0]} {author[1]}:")
                    
                    for book in available_by_author:
                        print(f"  - {book}")
                    print()

        elif choice == "6":
            print("Exiting. Thank you for using the Book Catalog App!")
            break

        else:
            print("Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
