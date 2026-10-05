def write_report(path, message):
    with open(path, "w", encoding="utf-8") as file:
        file.write(message)
