# SEARCH PROGRAM
## Program that can be used to search for information in a CSV
### Process
<ul>
  <li>Step 1: Create a function that takes a file name as an argument and reads in the contents of the file as a list of dictionaries, with each dictionary representing a book and containing keys for title, author, ISBN, and price</li>
  <li>Step 2: Create a function that takes an author's name as an argument and returns a list of all books written by that author.</li>
  <li>Step 3: Create a function that takes an ISBN as an argument and returns the title and price of the book with that ISBN.</li>
  <li>Step 4: Create a function that takes a minimum and maximum price as arguments and returns a list of all books within that price range.</li>
  <li>Step 5: Use the functions from steps 2-4 in a user interface that allows the user to search for books by author, ISBN, or price range.</li>
</ul>

### Execution
<p>The first logic is file handling to read the contents of the CSV file.</br>
The empty array, <b>books</b>, is initialized to store the Title, Author, ISBN, and Price of the books which will be used in steps 2-4</br>
The <b>get_author_books</b> function takes in the author and books parameters and initializes an empty array, <em>author_books</em>.</br>
It then loops through the books while appending the titles of the books to the array that matches the author that the user has provided.</br>
The <b>get_books_by_ISBN</b> function follows the same logic appending book title and price for books with the provided ISBN.</br>
The <b>get_books_in_price_range</b> function takes in min_price and max_price parameters. The price of the book is changed into a float to allow comparisons.</br>
The CSV is stored in the books variable which is provided as a parameter in all the functions.</p>

### Search
<p>The search functionality begins by initializing a while loop that ensures the search functionality runs as long as the conditions provided are met.<br>
The UI is meant to provide the user with directions on how to input the correct choice that allows the different functions in steps 2-4 to run.</br>
Choosing 1 prompts the user to input the Author name with the results being provided by the <b>get_author_books function</b> while the other choices call the other functions.</br>
</p>
