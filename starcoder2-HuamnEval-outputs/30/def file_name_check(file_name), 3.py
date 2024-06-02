
def file_name_check(file_name):
    if file_name.count(".") != 1:
        return "No"
    if file_name.count(".") == 1:
        if file_name.find(".") == 0:
            return "No"
        if file_name.find(".") == len(file_name) - 1:
            return "No"
        if file_name.find(".") > 0:
            if file_name.find(".") < len(file_name) - 1:
                if file_name[0].isalpha() == False:
                    return "No"
                if file_name[file_name.find(".") + 1:].lower() not in ["txt", "exe", "dll"]:
                    return "No"
                if file_name[file_name.find(".") + 1:].lower() in ["txt", "exe", "dll"]:
                    if file_name.count("0") > 3:
                        return "No"
                    if file_name.count("1") > 3:
                        return "No"
                    if file_name.count("2") > 3:
                        return "No"
                    if file_name.count("3") > 3:
                        return "No"
                    if file_name.count("4") > 3:
                        return "No"
                    if file_name.count("5") > 3:
                        return "No"
                    if file_name.count("6") > 3:
                        return "No"
                    if file_name.count("7") > 3:
                        return "No"
                    if file_name.count("8") > 3:
                        return "No"
                    if file_name.count("9") > 3:
                        return "No"
                    return "Yes"
 