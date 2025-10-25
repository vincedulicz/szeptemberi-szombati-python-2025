import json
import os.path

adat = {
    "név": "Anna",
    "kor": 25,
    "város": "Bp"
}

json_string = json.dumps(adat)
print(type(json_string))

adat = json.loads(json_string)
print(type(adat))

print(adat.get("név"))


with open("adat.json", "w", encoding='utf-8') as file:
    json.dump(adat, file, indent=4, ensure_ascii=False)


with open("adat.json", "r", encoding="utf-8") as file:
    adat = json.load(file)
    print(type(adat))
    print(adat.get("kor"))


sample_json = """{
    "company":{
        "employee":{
            "name":"emma",
            "payble":{
                "salary":7000,
                "bonus":800
            }
        }
    }
}"""

data = json.loads(sample_json)
print(type(data))
print(data["company"]["employee"]["payble"]["salary"])

print(data.get("company").get("employee"))


def safe_json_read(filename: str) -> {}:
    try:
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)
        print(f'Sikeres beolvasás {filename}')
        return data
    except FileNotFoundError:
        print("fájl nem található")
    except json.JSONDecodeError:
        print("nem json formátumu objektum")
    except Exception as e:
        print(f'más van: {e}')
    return {}


print(safe_json_read("hibas_adat.json"))


def safe_json_write(filename, data):
    try:
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f'sikeresen mentve {filename}')
    except (IOError, TypeError) as e:
        print(f'hiba történt: {e}')


def json_check_or_create(path, default_data=None):
    if not os.path.exists(path):
        print(f'nem létezik...')
        with open(path, "w", encoding='utf-8') as f:
            json.dump(default_data or {}, f, indent=4, ensure_ascii=False)
    else:
        print(f'{path} már létezik')


json_check_or_create("verygood.json", {"settings": "verysetting", "flag": True})


def update_json_file(filename, new_data):
    try:
        with open(filename, "r", encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data.update(new_data)

    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f'{filename} frissítve')


update_json_file("verygood.json", {"other_settings_for_very_big_fonts": 42})


import shutil
from datetime import datetime


def backup_json(filename):
    if os.path.exists(filename):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f'{filename}.{ts}.bak'
        shutil.copy(filename, backup_name)
        print(f'backup elkszült: {backup_name}')


backup_json("verygood.json")
