
def sort_phone(phone_list):
    for i in range(len(phone_list)):
        phone_list[i] = phone_list[i].replace("+91", "")
        phone_list[i] = phone_list[i].replace("91", "")
        phone_list[i] = phone_list[i].replace("0", "")
        phone_list[i] = phone_list[i].replace(" ", "")
    phone_list.sort()
    for i in range(len(phone_list)):
        phone_list[i] = "+91 " + phone_list[i][:5] + " " + phone_list[i][5:]
    return phone_list

