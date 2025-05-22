# -------------------------------
# Python Assignment 1 Solutions
# -------------------------------

# FUNCTIONS AND LOGIC BUILDING

# 1. Prime Number Generator
def prime_numbers(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

# 2. Number to Words Converter
import inflect
p = inflect.engine()
def number_to_words(n):
    return p.number_to_words(n)

# 3. Tic-Tac-Toe Board Printer
def print_tic_tac_toe(board=None):
    if not board:
        board = [[' ']*3 for _ in range(3)]
    for row in board:
        print('|'.join(row))
        print('-'*5)


# WORKING WITH STRINGS AND LISTS

# 4. Anagram Checker
def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

# 5. Password Strength Checker
import re
def is_strong_password(password):
    return (len(password) >= 8 and
            re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'[0-9]', password) and
            re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

# 6. Longest Word Finder
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# 7. List Flattening
def flatten_list(nested_list):
    result = []
    for i in nested_list:
        if isinstance(i, list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result


# DICTIONARIES AND SETS

# 8. Frequency Counter
def word_frequency(paragraph):
    words = paragraph.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# 9. Character Counter
def char_frequency(s):
    freq = {}
    for char in s.replace(" ", ""):
        freq[char] = freq.get(char, 0) + 1
    return freq

# 10. Student Gradebook
def student_gradebook():
    students = {
        'Alice': 85,
        'Bob': 92,
        'Charlie': 78
    }
    name = input("Enter student name: ")
    print(students.get(name, "Student not found."))


# FILE HANDLING

# 11. Read and Count Words
def read_file_stats(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        words = content.split()
        chars = len(content)
        return len(lines), len(words), chars

# 12. Simple Log Writer
from datetime import datetime
def write_log(filepath):
    with open(filepath, 'a') as f:
        f.write(f"Log at {datetime.now()}\n")

# 13. CSV Reader
import csv
def read_csv_above_75(filepath):
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if float(row['marks']) > 75:
                print(row['name'])


# BASIC OBJECT-ORIENTED PROGRAMMING

# 14. Bank Account Simulation
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance

# 15. Library Management System
class Book:
    def __init__(self, title):
        self.title = title
        self.borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.borrowed:
                book.borrowed = True
                return f"You borrowed {title}"
        return "Book not available."

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.borrowed:
                book.borrowed = False
                return f"You returned {title}"
        return "Invalid return."

# 16. Employee Management
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_department(self, dept):
        for emp in self.employees:
            if emp.department == dept:
                print(emp.name)


# MINI PROJECTS / APPLICATION LOGIC

# 17. Simple Quiz App
def simple_quiz():
    questions = [
        {"q": "What is the capital of France?", "a": "Paris"},
        {"q": "2 + 2?", "a": "4"},
        {"q": "Color of the sky?", "a": "blue"}
    ]
    score = 0
    for q in questions:
        ans = input(q["q"] + " ")
        if ans.lower() == q["a"].lower():
            score += 1
    print(f"Your score: {score}/{len(questions)}")

# 18. Expense Tracker
def expense_tracker():
    expenses = {}
    for i in range(7):
        day = input("Enter day: ")
        amount = float(input(f"Expense for {day}: "))
        expenses[day] = amount
    print("Weekly Summary:")
    for day, amt in expenses.items():
        print(f"{day}: ${amt}")

# 19. To-Do App with File Persistence
def todo_app(filename="todo.txt"):
    while True:
        choice = input("1. Add 2. Remove 3. Mark Done 4. View 5. Exit: ")
        if choice == '1':
            task = input("Enter task: ")
            with open(filename, 'a') as f:
                f.write(f"[ ] {task}\n")
        elif choice == '2':
            with open(filename, 'r') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                print(f"{i + 1}: {line}", end="")
            idx = int(input("Enter line to remove: ")) - 1
            lines.pop(idx)
            with open(filename, 'w') as f:
                f.writelines(lines)
        elif choice == '3':
            with open(filename, 'r') as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                print(f"{i + 1}: {line}", end="")
            idx = int(input("Enter line to mark done: ")) - 1
            if lines[idx].startswith("[ ]"):
                lines[idx] = lines[idx].replace("[ ]", "[x]", 1)
            with open(filename, 'w') as f:
                f.writelines(lines)
        elif choice == '4':
            with open(filename, 'r') as f:
                print(f.read())
        elif choice == '5':
            break

# END OF FILE




