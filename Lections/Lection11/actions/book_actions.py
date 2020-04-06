from models.book import TABLE_NAME as BOOK_TABLE
from models.writer import TABLE_NAME as WRITERS_TABLE
from helpers.output_helper import pretty_print
from services.data_service import (get_data, execute_command)
from actions.writer_actions import add_writer


def books_list():
    query = ("SELECT {0}.id, {0}.name as book, {0}.description,"
             " {1}.name as writer FROM {0}, {1} WHERE {0}.writerId = {1}.id".format(BOOK_TABLE, WRITERS_TABLE))
    books = get_data(query)
    pretty_print(books)


def get_book_info():
    book_name = None
    while True:
        book_name = input("Enter book name, please: ")
        if len(book_name.strip()) > 0:
            break
    query = ("SELECT {0}.name as book, {0}.description, {1}.name as writer FROM {0}, {1}"
             " WHERE {0}.writerId = {1}.id AND {0}.name = '{2}'".format(BOOK_TABLE, WRITERS_TABLE, book_name))
    book_info = get_data(query)
    pretty_print(book_info)


def add_book():
    book_name = None
    book_description = None
    author = None

    while True:
        book_name = input("Enter book name, please: ")
        book_description = input("Enter book description, please: ")
        author = input("Enter author's name, please: ")
        if len(book_name.strip()) > 0 and len(author.strip()) > 0:
            break
    query = ("SELECT id FROM {0} WHERE name = '{1}'".format(WRITERS_TABLE, author))
    author_id = get_data(query)

    if not author_id:
        add_writer(author)
        author_id = get_data(query)
    author_id = author_id[0]['id']

    query = ("INSERT INTO {} (name, description, writerId) VALUES ('{}', '{}', {})"
             .format(BOOK_TABLE, book_name, book_description, author_id))
    execute_command(query)
    print("Saved")