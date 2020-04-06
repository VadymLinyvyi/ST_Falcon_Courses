from models.writer import TABLE_NAME
from services.data_service import (get_data, execute_command)
from helpers.output_helper import pretty_print


def view_writers():
    query = ("SELECT * FROM %s" % TABLE_NAME)
    writers = get_data(query)
    pretty_print(writers)


def get_author_name():
    while True:
        author_name = input("Enter Author name, please: ")
        if len(author_name.strip()) > 0:
            return author_name


def add_writer(author_name=None):
    if author_name is None:
        author_name = get_author_name()

    query = ("INSERT INTO {} (name) VALUES ('{}')".format(TABLE_NAME, author_name))
    execute_command(query)
    print("Saved")