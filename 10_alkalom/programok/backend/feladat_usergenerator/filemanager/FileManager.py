import json


class FileManager:
    @staticmethod
    def save_to_file(file_name, data):
        try:
            with open(file_name, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"mentési hiba: {e}")

    @staticmethod
    def read_from_file(file_name):
        try:
            with open(file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("nem létezik")
        except json.JSONDecodeError:
            print("rossz formátum")
        except Exception as e:
            print(f"Hiba: {e}")
        return None
