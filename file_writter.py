import os


def file_writer(filename: str, file_content: str):
    cur_dir = os.getcwd()
    path = os.path.join(cur_dir, filename)

    record_exists = False
    if os.path.exists(path):
        with open(path, 'r', encoding='utf8') as f:
            record_content = f.read()
            if file_content in record_content:
                record_exists = True

    if not record_exists:
        with open(path, 'a', encoding='utf8') as f:
            f.write(f"{file_content}\n\n")
