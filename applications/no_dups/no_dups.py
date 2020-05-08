def no_dups(s):
    str_arr = s.split(" ")
    final_list = []
    print("\n")
    for string in str_arr:
        if string not in final_list:
            print(string)
            final_list.append(string)

    # print(str_arr, '\n')
    return "".join(final_list)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))