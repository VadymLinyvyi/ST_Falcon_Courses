with open ("text.txt", "w+", encoding="utf-8") as file:
    file.write("first line ")
    file.write("second\n")
    file.writelines("""contains two
    lines""")
    file.seek(0)
    tmp = file.read(5)
    print(tmp)
    print(file.tell())
    print(file.readline(), end=" ")
    tmp = file.read()
    print("tmp")

import pickle

t1 = [1, 2, 3]
s = pickle.dumps(t1)
print(s)

t2 = pickle.loads(s)
print(t2)