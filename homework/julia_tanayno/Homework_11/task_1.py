class Book:
    is_text = 'да'
    pages_material = 'бумага'

    def __init__(self, title, author, number_of_pages, isbn, is_reserved):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.is_reserved = is_reserved

    def __str__(self):
        return (
            f'Название: {self.title}, '
            f'Автор: {self.author}, '
            f'Страниц: {self.number_of_pages}, '
            f'Материал: {self.pages_material}'
            f'{", зарезервирована" if self.is_reserved else ""}'
        )


class SchoolBook(Book):
    def __init__(
            self,
            title,
            author,
            number_of_pages,
            isbn, is_reserved,
            subject,
            group,
            has_tasks
        ):
        super().__init__(title, author, number_of_pages, isbn, is_reserved)
        self.subject = subject
        self.group = group
        self.has_tasks = has_tasks

    def __str__(self):
        return (
            f'Название: {self.title}, '
            f'Автор: {self.author}, '
            f'Страниц: {self.number_of_pages}, '
            f'Предмет: {self.subject}, '
            f'Класс: {self.group}'
            f'{", зарезервирована" if self.is_reserved else ""}'
        )


book_1 = Book(
    'Идиот', 'Достоевский', 500,
    '978-5-94485-322-6', True
)
book_2 = Book(
    'Братья Карамазовы', 'Достоевский', 550,
    '978-5-94485-333-7', False
)
book_3 = Book(
    'Преступление и наказание', 'Достоевский', 800,
    '999-5-94485-333-7', False
)
book_4 = Book(
    'Война и мир', 'Толстой', 2200,
    '955-5-94485-333-8', False
)
book_5 = Book(
    'Что делать', 'Чернышевский', 1000,
    '777-5-94485-333-8', False
)
school_book_1 = SchoolBook(
    'Алгебра', 'Иванов', 100, '777-5-94485-555-1', False, 'Математика', '9', True
)

school_book_2 = SchoolBook(
    'Оптика', 'Петров', 300, '555-5-94485-555-1', True, 'Физика', '10', True
)

print(book_1)
print(book_2)
print(book_3)
print(book_4)
print(book_5)

print(school_book_1)
print(school_book_2)
