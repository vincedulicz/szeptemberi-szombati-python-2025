

import os, shutil
import time


def teszter():
    try:
        if not os.path.exists("example_nem_letezik.txt"):
            with open("example_nem_letezik.txt", "w") as f:
                f.write("hello world")
    except FileNotFoundError as e:
        print(e)

    for file in os.listdir("."):
        print(file)

    print(os.getcwd())


# teszter()

# os.mkdir("teszter_elek")

txt_files = [f for f in os.listdir(".") if f.endswith(".txt")]
# print(f'txt files {txt_files}')


file_size = os.path.getsize("example.txt")
# print(file_size)


if os.name == "nt":
    pass
    # os.system("dir")
else:
    os.system("ls")

base_path = os.getcwd()
file_path = os.path.join(base_path, "folder", "file.txt")

print(f'full path: {type(file_path)}')


with open("tempfile.tmp", "w") as temp_file:
    temp_file.write("tmp data")

print("created tmp")

os.remove("tempfile.tmp")


os.environ["NEW_VAR"] = "pyauto"
print("new var: ", os.getenv("NEW_VAR"))



for root, dirs, files in os.walk("."):
    print("Dir: ", root)
    for file in files:
        print(f'File: {file}')




# for key, value in os.environ.items():
#    print(f'k: {key} | v: {value}')



start_time = time.time()
time.sleep(2)
end_time = time.time()
print(f'runtime: {end_time - start_time} sec')

# OOP kezdet

class Nber:
    osztalyvaltozok = 0

    def __init__(self, nev):
        self.nev = nev

    def nev_kiir(self):
        print(self.nev)

    @staticmethod
    def foo():
        print("foo")

    @classmethod
    def set_osztalyvaltozo(cls):
        cls.osztalyvaltozok = 1


nber1 = Nber("Józsi")
print(type(nber1))

nber1.nev_kiir()

nber2 = Nber("Pista")
print(type(nber2))
nber2.nev_kiir()

print(Nber.osztalyvaltozok)
print(nber2.osztalyvaltozok)
Nber.osztalyvaltozok = 1

print(nber2.osztalyvaltozok)