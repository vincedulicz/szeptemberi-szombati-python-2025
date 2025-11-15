import json


class FileReader:
    """ Csak és kizárólag az olvasásért felel!!! """

    @staticmethod
    def read(file_path):
        """ Default reader """
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def read_json(file_path):
        """ JSON reader """
        with open(file_path, 'r') as file:
            return json.load(file)


class FileWriter:
    """ Csak és kizárólag az írásért felel!!! """

    @staticmethod
    def write(file_path, data):
        with open(file_path, 'w') as file:
            file.write(data)

    @staticmethod
    def write_json(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)


class DataProcessor:
    """ Adatfeldolgozásért felel """
    def __init__(self, data):
        self.data = data # property

    def process(self):
        return self.data.upper()

    def filter_by_name(self, name):
        return [item for item in self.data if item["nev"] == name]

    def filter_by_age(self, min_age, max_age):
        return [item for item in self.data if min_age <= item["kor"] <= max_age]

    def filter_by_zip(self, zip_code):
        return [item for item in self.data if item.get("iranyitoszam") == zip_code]


class TestData:
    """ Teszt adatokért felelős, publikus használatra """

    EXAMPLE_DATA = [
        {"nev": "Teszt Elek", "kor": 30, "cim": "Teszt UTca1", "iranyitoszam": 1234},
        {"nev": "Teszt Elek2", "kor": 33, "cim": "Teszt UTca2", "iranyitoszam": 1235},
        {"nev": "Teszt Elek3", "kor": 37, "cim": "Teszt UTca3", "iranyitoszam": 1236},
        {"nev": "Teszt Elek4", "kor": 39, "cim": "Teszt UTca4", "iranyitoszam": 1236},
    ]


def main():
    file = "example.json"
    FileWriter.write_json(file, TestData.EXAMPLE_DATA)
    data = FileReader.read_json(file)
    processor = DataProcessor(data)

    filtered_by_name = processor.filter_by_name("Teszt Elek")

    filtered_by_zip = processor.filter_by_zip(1236)

    print(filtered_by_name, filtered_by_zip)

main()
