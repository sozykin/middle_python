from pypdf import PdfReader

filename = "zen_of_python.pdf"  

# Читаем файл PDF
reader = PdfReader(filename)

# Получаем количество страниц
number_of_pages = len(reader.pages)

# Получаем первую страницу
page = reader.pages[0]

# Печатаем страницу в PDF
print("Страница в PDF")
print(page) 

# Печатаем текст страницы 
print("Текст страницы")
text = page.extract_text()
print(text)

# Печатаем ссылки в документе 
print("Ссылки в документе")
key = '/Annots'
uri = '/URI'
ank = '/A'

for i, page in enumerate(reader.pages):
    print(f"Страница: {i}")
    pageObject = page.get_object()
    if key in pageObject.keys():
        ann = pageObject[key]
        for a in ann:
            u = a.get_object()
            if uri in u[ank].keys():
                print(u[ank][uri])