def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)

def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)

def return_book(borrowed_books, book_id):
    if book_id in borrowed_books: 
        borrowed_books.remove(book_id)

def register_member(members, member_id):
    members.add(member_id)

def show_available(catalog, borrowed_books):
    for b_id, (title, author, year) in catalog.items():
        if b_id not in borrowed_books: 
            print(f"{b_id}: {title} by {author} ({year})")

def main():
    catalog, borrowed_books, members = {}, [], set()
    
    add_book(catalog, 101, "The Hobbit", "J.R.R. Tolkien", 1937)
    add_book(catalog, 102, "1984", "George Orwell", 1949)
    add_book(catalog, 103, "Dune", "Frank Herbert", 1965)
    add_book(catalog, 104, "Fahrenheit 451", "Ray Bradbury", 1953)

    for m in [501, 502, 503, 502]: 
        register_member(members, m)
    
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)
    
    return_book(borrowed_books, 101)
    
    print("\nAvailable Books:")
    show_available(catalog, borrowed_books)

if __name__ == "__main__": 
    main()
