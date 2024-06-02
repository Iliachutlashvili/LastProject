import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Check for invalid category_id references
cursor.execute("SELECT id, category_id FROM book_book WHERE category_id NOT IN (SELECT id FROM book_category)")
invalid_books = cursor.fetchall()

# Print invalid books for verification
print("Invalid books with non-existent category_id:")
for book in invalid_books:
    print(book)

# Remove invalid books
cursor.execute("DELETE FROM book_book WHERE category_id NOT IN (SELECT id FROM book_category)")
conn.commit()

# Close the connection
conn.close()

print("Invalid books removed successfully.")
