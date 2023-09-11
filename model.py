from text import *
from func import *


def start_notion():
    flag = True
    notion_list = 0
    while flag:
        event = input(event_option)
        if event.isdigit() or 0 < int(event) < 6:
            event = int(event)
        else:
            print(input_error)
            continue
        match event:
            case 1:
                notion_list = open_file()
                print(mission_completed)
            case 2:
                if notion_list == 0:
                    print(open_error)
                    continue
                notion = input(new_notion)
                if notion == "":
                    print(input_error)
                    continue
                notion_list.append(notion + ";")
                print(mission_completed)
            case 3:
                pass
            case 4:
                pass
            case 5:
                flag = False
                if notion_list == 0:
                    print(good_bye)
                else:
                    save_file(notion_list)
                    print(good_bye)
