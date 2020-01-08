import json
def f():
    Summa = 11
    print(Summa)
    with open("data.json", "w") as write_file:
        json.dump(Summa, write_file)