from pymongo import MongoClient
from materi.book import database as db
import csv

def add_book():
    data = open("bestsellers-with-categories.csv",encoding='utf-8')
    books = csv.reader(data, delimiter=',')
    next(books)

    for book in books:
        try:
            data = {
                "nama": book[0],
                "pengarang": book[1],
                "tahunTerbit": book[5],
                "genre": book[6]
            }
            db.insertBook(data)
        except Exception as e:
            print("Kesalahan pada saat memasukan data: {}".format(e))
            break

def search_books(params):
    for book in db.searchBookByName(params):
        print(book)

def show_book() :
    for book in db.showBooks():
        print(book)
    
def show_books_by_id(params):
    for book in db.showBookById(params):
        print(book)

def update_book_by_id(params):
    db.updateBookById(params)
    print("berhasil update")

def delete_book_by_id(params):
    db.deleteBookById(params)
    print("berhasil dihapus")

if __name__ == "__main__":
    db = db()
    add_book()
    # kata_kunci = "harry"
    # search_books(kata_kunci)
    # search_books("10-Day Green Smoothie Cleanse")
    # show_book()
    # delete_book_by_id('60a36da97a229313d8ef20f4')
    show_books_by_id('60a36da97a229313d8ef20f4')

    db.nosql_db.close()


