import json
from mongoengine.errors import (NotUniqueError)
from models import Author, Quote
from mongoengine import connect

if __name__ == '__main__':
    with connect(db='hm', host='mongodb+srv://PythonDB:cud4BUXMwUmTI9A9@cluster0.zv0mgxq.mongodb.net/'):
        with open('authors.json', encoding='utf-8') as fd:
            data = json.load(fd)
            for el in data:
                try:
                    author = Author(fullname=el.get('fullname'), born_date=el.get('born_date'), born_location=el.get('born_location'), description=el.get('description'))
                    author.save()
                except NotUniqueError:
                    print(f"Автор вже існує {el.get('fullname')}")

        with open('quotes.json', encoding='utf-8') as fd:
            data = json.load(fd)
            for el in data:
                author = Author.objects(fullname=el.get('author')).first()
                if author:
                    quote = Quote(quote=el.get('quote'), tags=el.get('tags'), author=author)
                    quote.save()
                else:
                    print(f"Автор з іменем {el.get('author')} не знайдений")

# if __name__ == '__main__':
#     with connect(db='hm', host='mongodb+srv://PythonDB:cud4BUXMwUmTI9A9@cluster0.zv0mgxq.mongodb.net/'):
#         with open('authors.json', encoding='utf-8') as fd:
#             data = json.load(fd)
#             for el in data:
#                 try:
#                     author = Author(fullname=el.get('fullname'), born_date=el.get('born_date'), born_location=el.get('born_location'), description=el.get('description'))
#                     author.save()
#                 except NotUniqueError:
#                     print(f"Автор вже існує {el.get('fullname')}")
#
#         with open('quotes.json', encoding='utf-8') as fd:
#             data = json.load(fd)
#             for el in data:
#                 author = Author.objects(fullname=el.get('author'))
#                 if author:
#                     quote = Quote(quote=el.get('quote'), tags=el.get('tags'), author=author)
#                     quote.save()
#                 else:
#                     print(f"Автор з іменем {el.get('author')} не знайдений")

# if __name__ == '__main__':
#     with open('authors.json', encoding='utf-8') as fd:
#         data = json.load(fd)
#         for el in data:
#             try:
#                 author = Author(fullname=el.get('fullname'), born_date=el.get('born_date'), born_location=el.get('born_location'), description=el.get('description'))
#                 author.save()
#             except NotUniqueError:
#                 print(f"Автор вже існує {el.get('fullname')}")
#
#
#     with open('quotes.json', encoding='utf-8') as fd:
#         data = json.load(fd)
#         for el in data:
#             author, *_ = Author.objects(fullname=el.get('author'))
#             quote = Quote(quote=el.get('quote'), tags=el.get('tags'), author=author)
#             quote.save()