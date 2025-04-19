# Imports
import json

# Set DO_TEST to True if you wish to try out test data, False otherwise
DO_TEST = False


# Function
def get_filtered_books(database: list[dict], user_filters: list[list[str]]) -> set[str]:
    # Filter-able attributes include: author (list of str), class (str), bib_type (str), subjects(list of str)
    books = set()
    conditions_to_satisfy = len(user_filters)  # If all conditions are satisfied, the book is added to the set.

    for book in database:
        conditions_satisfied = 0

        # Checking to see if the book satisfies all conditions
        for filter_keyword, value in user_filters:
            retrieved_value_from_book = book.get(filter_keyword, None)
            if isinstance(retrieved_value_from_book, str):
                if value == retrieved_value_from_book:
                    conditions_satisfied += 1

            elif isinstance(retrieved_value_from_book, list):
                if value in retrieved_value_from_book:
                    conditions_satisfied += 1

        # Adding book to the books set IF all conditions were checked
        if conditions_satisfied == conditions_to_satisfy:
            books.add(book["title"])

    return books


# Tests
if DO_TEST:
    with open("database.json", "r") as f:
        json_data = json.load(f)

    # Enter test data samples here
    test_data_samples = [
        [["author", "Young, Johnnie"], ["subjects", "School discipline"], ["subjects", "Education"]],
        [["author", "Verne, Jules"]],
        [["subjects", "Fantasy fiction"]]
    ]

    for sample in test_data_samples:
        print(f"Test data sample: {sample}")
        print(get_filtered_books(json_data, sample))
        print()
