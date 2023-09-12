from text import *
from func import *


def start_notion():
    flag = True
    notion_list = 0
    while flag:
        event = input(event_option).strip()
        if event.isdigit() and 0 < int(event) < 7:
            event = int(event)
        else:
            print(input_error)
            continue
        match event:
            case 1:
                notion_list = open_file()
                print(len(notion_list[2]))
                print(mission_completed)
            case 2:
                if notion_list == 0:
                    print(open_error)
                    continue
                notion = input(new_notion).strip()
                if notion == "":
                    print(input_error)
                    continue
                notion_list.append(notion)
                print(mission_completed)
            case 3:
                if notion_list == 0:
                    print(open_error)
                    continue
                elif len(notion_list) == 0:
                    print(empty_error)
                else:
                    print_notion(notion_list)
                    deli = input(del_notion).strip()
                    if deli.isdigit() and 0 < int(deli) < len(notion_list) + 1:
                        notion_list.pop(int(deli) - 1)
                        print(mission_completed)
                    else:
                        print(input_error)
            case 4:
                if notion_list == 0:
                    print(open_error)
                    continue
                elif len(notion_list) == 0:
                    print(empty_error)
                else:
                    print_notion(notion_list)
                    edit = input(edit_notion).strip()
                    if edit.isdigit() and 0 < int(edit) < len(notion_list) + 1:
                        notion = input(new_notion).strip()
                        if notion == "":
                            print(input_error)
                            continue
                        else:
                            notion_list[int(edit) - 1] = notion
                            print(mission_completed)
                    else:
                        print(input_error)
            case 5:
                if notion_list == 0:
                    print(open_error)
                    continue
                elif len(notion_list) == 0:
                    print(empty_error)
                    continue
                else:
                    print_notion(notion_list)
            case 6:
                flag = False
                if notion_list == 0:
                    print(good_bye)
                else:
                    save_file(notion_list)
                    print(good_bye)
