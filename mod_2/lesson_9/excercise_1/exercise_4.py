def join_kwargs(**kwargs):
    text = ""
    for key, value in kwargs.items():
        text = text + ("" if text == "" else "\n") + "klucz=" + key + ", wartość= " + str(value)
    return text


b = {"aaa": 1, "bbb": 2}
c = {"ccc": 1, "ddd": 2}

d = {**b, **c}

print(join_kwargs(**d))
