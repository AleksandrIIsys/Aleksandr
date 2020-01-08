import json
def f():
    a = 5
    b = 6
    Summa = a+b
    print(Summa)
    with open("Client\data.json", "w") as write_file:
        json.dump(Summa, write_file)