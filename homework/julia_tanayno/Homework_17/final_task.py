import argparse
import os

# распознать аргументы, которые ввел пользователь
parser = argparse.ArgumentParser()
parser.add_argument('folder', help='full path to the folder')
parser.add_argument( '-text', help='text to search')
args = parser.parse_args()

# определить, что указал пользователь: файл или папку
source_type = None
if os.path.isdir(args.folder):
    source_type = "folder"

elif os.path.isfile(args.folder):
    source_type = "file"

else:
    source_type = "error"

# получить содержимое файла (файлов)
all_files_content = {}
if source_type == "file":
    file_path = args.folder
    with open(file_path, "r") as file:
        content = file.read()
        all_files_content[file_path] = content

elif source_type == "folder":
    for item in os.listdir(args.folder):
# проверяем, что это файл (а не подпапка)
        if os.path.isfile(os.path.join(args.folder, item)):
            file_path = os.path.join(args.folder, item)
# открываем и читаем каждый файл
            with open(file_path, 'r') as file:
                content = file.read()
            all_files_content[file_path] = content

else:
    print('такого файла/папки не существует')
    exit()

# разбить содержимое на блоки и сохранить блоки в переменной
all_blocks = {}
for file_path, content in all_files_content.items():
    blocks = {}
    current_block = []  # (line_number, line)
    current_time = None
    for line_number, line in enumerate(content.splitlines(), start=1):
        line = line.strip()
        if (
            len(line) > 19
            and line[0].isdigit()
            and line[4] == "-"
            and line[7] == "-"
            and line[10] == " "
            and line[13] == ":"
            and line[16] == ":"
        ):
            if current_block:
                blocks[current_time] = current_block

            current_time = line[:19]
            current_block = []

        else:
            current_block.append((line_number, line))

    if current_block:
        blocks[current_time] = current_block

    all_blocks[file_path] = blocks

# реализовать поиск по тексту
found = False
target = args.text.lower()

for file_path, blocks in all_blocks.items():
    for time, block_lines in blocks.items():

        # объединяем блок в один текст
        block_text = " ".join(line for _, line in block_lines).lower()

        # убираем знаки препинания
        clean_text = (
            block_text.replace(",", " ")
                      .replace(".", " ")
                      .replace(":", " ")
                      .replace(";", " ")
                      .replace("[", " ")
                      .replace("]", " ")
        )

        # проверяем наличие слова/подстроки
        if target in clean_text:
            found = True

            words = clean_text.split()
            target_words = target.split()

            for i, word in enumerate(words):
                if words[i : i + len(target_words)] == target_words:
                    start = max(0, i - 5)
                    end = i + len(target_words) + 5
                    context = words[start:end]

                    # находим номер строки
                    for line_number, line in block_lines:
                        if target in line.lower():
                            found_line = line_number
                            break

                    print(f"Файл: {file_path}, Строка: {found_line}, Время: {time}")
                    print("Контекст:", " ".join(context))
                    print("-" * 60)

# если ничего не нашли
if not found:
    print("По вашему запросу ничего не найдено.")
