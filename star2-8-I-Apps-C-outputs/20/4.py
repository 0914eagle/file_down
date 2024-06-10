
def rebus(input_str):
    input_str = input_str.replace(" ", "")
    if input_str.count("?") > 100:
        return "Input exceeds limit"
    n = int(input_str.split("=")[-1])
    if n > 1000000:
        return "n exceeds limit"
    input_str = input_str.replace("?", "{}")
    input_list = input_str.split("=")
    input_list = list(map(int, input_list[0].split("+"))) + list(map(int, input_list[1].split("-")))
    output_list = []
    for num in input_list:
        if num < 1 or num > n:
            return "Invalid input"
        output_list.append(str(num))
    output_str = "+".join(output_list[:-1]) + "-" + output_list[-1] + "=" + str(n)
    return output_str

print(rebus("? + ? - ? + ? + ? = 42"))
print(rebus("? - ? = 1"))
print(rebus("? = 1000000"))

