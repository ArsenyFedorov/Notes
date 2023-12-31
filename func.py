FILE_NAME = 'notion.txt'


def open_file() -> list[str]:
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        my_str = f.read()
        notion_list = my_str.split(";")
        for i in range(len(notion_list) - 1):
            notion_list[i] = notion_list[i].strip()
            if notion_list[i] == "":
                notion_list.pop(i)
        return notion_list


def save_file(user_list: list[str]):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for i in range(len(user_list)):
            f.write(user_list[i] + ";" + "\n")


def print_notion(user_list: list[str]):
    for i in range(len(user_list)):
        print(f"{i + 1}." + user_list[i])
