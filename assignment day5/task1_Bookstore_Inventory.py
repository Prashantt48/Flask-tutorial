
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Bookstore:
    # Static variable shared by all objects
    total_books = 0

    def __init__(self, title, author, genre):
        try:
            if not all(isinstance(x, str) and x.strip()
                       for x in (title, author, genre)):
                raise ValueError(
                    "Title, author, and genre cannot be empty."
                )

            self.title = title.strip()
            self.author = author.strip()
            self.genre = genre.strip()

            Bookstore.total_books += 1
            logging.info("Book added: %s", self.title)

        except ValueError as error:
            logging.error("Unable to create book: %s", error)
            raise

    def display_book(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre : {self.genre}")

    @staticmethod
    def get_total_books():
        return Bookstore.total_books


def main():
    inventory = []

    while True:
        print("\n--- Bookstore Inventory Management ---")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Show Total Books")
        print("4. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                genre = input("Enter genre: ")

                book = Bookstore(title, author, genre)
                inventory.append(book)
                print("Book added successfully!")

            elif choice == "2":
                if not inventory:
                    print("Inventory is empty.")
                else:
                    for number, book in enumerate(inventory, 1):
                        print(f"\nBook {number}")
                        book.display_book()

            elif choice == "3":
                print(
                    "Total books:",
                    Bookstore.get_total_books()
                )

            elif choice == "4":
                print("Exiting bookstore system.")
                break

            else:
                print("Invalid choice. Please select 1-4.")

        except (ValueError, EOFError) as error:
            logging.exception("Input or processing error")
            print("Error:", error)

        except Exception:
            logging.exception("Unexpected error occurred")
            print("Something went wrong. Please try again.")


if __name__ == "__main__":
    main()
