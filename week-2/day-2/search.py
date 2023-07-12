import csv

def books_reader(file_name):
    books = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            book = {
                'Title': row['name'],
                'Author': row['author'],
                'ISBN': row['isbn'],
                'Price': row['price']
            }
            books.append(book)
    return books

def get_author_books(author, books):
    author_books = []
    author = author.lower()
    for book in books:
        if author in book['Author'].lower():
            author_books.append(book['Title'])
    return author_books


def get_book_by_ISBN(isbn, books):
    ISBN_books = []
    for book in books:
        if book['ISBN'] == isbn:
            ISBN_books.append(book['Title'] + ' ' + book['Price'])
    return ISBN_books

def get_books_in_price_range(min_price, max_price, books):
    books_in_range = []
    for book in books:
        price = float(book['Price'])
        if min_price <= price <= max_price:
            books_in_range.append(book)
    return books_in_range

books = books_reader('main_dataset.csv')

while True:
    print('Search for books by:')
    print('1. Author')
    print('2. ISBN')
    print('3. Price range')
    print('4. Quit')
    choice = input('Enter your choice: ')
    
    if choice == '1':
        author = input('Enter author name: ')
        results = get_author_books(author, books)
        print('Books by', author)
        for book in results:
            print(book)
            
    elif choice == '2':
        isbn = input('Enter ISBN: ')
        results = get_book_by_ISBN(isbn, books)
        print('Book with ISBN', isbn)
        for book in results:
            print(book)
            
    elif choice == '3':
        min_price = float(input('Enter minimum price: '))
        max_price = float(input('Enter maximum price: '))
        results = get_books_in_price_range(min_price, max_price, books)
        print('Books in price range', min_price, 'to', max_price)
        for book in results:
            print(book['Title'], book['Price'])
            
    elif choice == '4':
        break
