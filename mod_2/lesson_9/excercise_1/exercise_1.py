def join_args(*args):
    text = ""
    for arg in args:
        text = text + ("" if text == "" else "-") + arg
    return text


print(join_args("aaa", "bbb", "ccc", "ddd", "eee"))
print(join_args("fff", "ggg"))
