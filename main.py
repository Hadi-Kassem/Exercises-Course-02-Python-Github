# Easy 1
name = input("What is your name? ")
age = input("What is your age? ")
print(f"The user {name} is {age} years old.")

# Easy 2
num = int(input("Enter a number: "))

if num % 4 == 0:
    print("Multiple of 4.")
elif num % 2 == 0:
    print("Even number.")
else:
    print("Odd number.")

num = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))

if num % check == 0:
    print(f"{check} divides evenly into {num}.")
else:
    print(f"{check} does not divide evenly into {num}.")

# Easy 3
def first_and_last(lst):
    return [lst[0], lst[-1]]

# Easy 4
def binary_search(sorted_list, number):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sorted_list[mid] == number:
            return True
        elif sorted_list[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Medium 1
def find_unique_triplets(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in result:
                        result.append(triplet)
    return result

# Medium 2
def count_words(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Medium 3
class Book:
    def __init__(self, title, author, year, is_checked_out=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = is_checked_out

    def checkout(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author} (Checked out: {self.is_checked_out})"

class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book):
        self.collection.append(book)

    def list_books(self):
        for book in self.collection:
            print(f"Title: {book.title}, Checked out: {book.is_checked_out}")

    def find_book(self, title):
        for book in self.collection:
            if book.title.lower() == title.lower():
                return book

    def available_books(self):
        return [book for book in self.collection if not book.is_checked_out]
