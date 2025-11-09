📚 Book Catalog System



A Python interactive library program that allows users to manage a book catalog, check out books with due dates, view available books, and identify popular authors. Demonstrates modular design, dictionaries/sets, user input, and date handling.



\*\*Features\*\*



* View full catalog by author and book.
* Add new books interactively.
* Checkout books (single or multiple at once) with automatic due dates.
* View popular authors with multiple books.
* View available books, grouped by author.
* Prevents duplicate checkout attempts and dynamically updates availability.



\*\*How It Works\*\*



1. Catalog Creation: Pre-filled with example authors/books, with option to add more.
2. Adding Books: Enter first name, last name, and book title; new authors added automatically.
3. Checkout: Enter one or multiple books (comma-separated). Checked-out books are removed from available books, and due dates are automatically assigned (14 days from checkout).
4. Popular Authors: Authors with more than one book are dynamically identified.
5. Available Books: Shows books not yet checked out, grouped by author.



🖥 Example Interactive Session

Welcome to the Book Catalog Library System!



Options:

1\. View full catalog

2\. Add a book to the catalog

3\. Checkout a book (with due date)

4\. View popular authors

5\. View available books

6\. Exit



Enter your choice (1-6): 3

Enter book(s) to checkout, separated by commas: Parable of the Sower, Long Shot

✅'Parable of the Sower' successfully checked out!

Due date for 'Parable of the Sower' set to 11/22/2025



✅'Long Shot' successfully checked out!

Due date for 'Long Shot' set to 11/22/2025



\*\*Skills Demonstrated\*\*



* Python fundamentals: variables, loops, conditionals
* Functions with parameters and return values
* Dictionaries, sets, tuples
* Date handling using datetime module
* Modular program design and code reusability
* Input validation and dynamic menus



📸 Screenshots

![Book Catalog Preview](./Book_Catalog/BookCatalogMenu.png)

Option 1: View Full Catalog

Displays all authors and books.

![Book Catalog- Full Catalog Preview → shows full catalog before any changes](./Book_Catalog/Option1.png)



Option 2: Add a Book to the Catalog

User adds a new book or author.

![Book_Catalog- Add a Book Preview → shows new book successfully added](./Book_Catalog/Option2.png)



Option 3: Checkout Book(s) with Due Date

User checks out one or multiple books; due dates displayed.

![Book_Catalog- Checkout w/ Due Date Preview → shows checkout and due dates](./Book_Catalog/Option3.png)



Option 4: View Popular Authors

Lists authors with multiple books in the catalog.

![Book Catalog- Popular Authors Preview → shows authors with multiple books](./Book_Catalog/Option4.png)



Option 5: View Available Books

Displays only books currently available for checkout, grouped by author.

![Book Catalog- Available Books Preview → shows filtered available books](./Book_Catalog/Option5.png)



Option 6: Exit

Clean exit from the program.

![Book Catalog- Exit Preview → shows program exit](./Book_Catalog/Option6.png)


