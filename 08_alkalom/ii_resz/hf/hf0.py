import csv
import json
import random
import sys
from datetime import datetime, timedelta


class WeatherGenerator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.weather_conditions = ["szeles", "napos", "esős", "ködös", "semillen"]

    @staticmethod
    def generate_weather_entry(current_date, conditions):
        condition = random.choice(conditions)
        temperature = round(random.uniform(0, 20), 1)
        rain_chance = random.randint(0, 100)

        return (
            f"Dátum: {current_date.strftime('%Y-%m-%d')}\n"
            f"Időjárás: {condition}\n"
            f"Hőmérséklet: {temperature}C\n"
            f"Várható eső: {rain_chance}%\n"
        )

    def generate_weather_data(self, start_date, end_date):
        current_date = start_date
        with open(self.file_name, "w", encoding='utf-8') as file:
            while current_date <= end_date:
                file.write(self.generate_weather_entry(current_date, self.weather_conditions))
                current_date += timedelta(days=1)


class WeatherStorage:
    def __init__(self):
        self.data = {}

    def load_weather_data(self, file_name):
        weather_data = {}

        try:
            with open(file_name, "r", encoding='utf-8') as file:
                current_date = None

                for line in file:
                    if line.startswith("Dátum:"):
                        current_date = line.split(": ")[1].strip()
                        weather_data[current_date] = {}

                    elif line.startswith("Időjárás:"):
                        weather_data[current_date]["condition"] = line.split(": ")[1].strip()

                    elif line.startswith("Hőmérséklet:"):
                        weather_data[current_date]["temperature"] = float(line.split(": ")[1].strip("C\n"))

                    elif line.startswith("Várható eső:"):
                        weather_data[current_date]["rain_chance"] = int(line.split(": ")[1].strip("%\n"))

            self.data = weather_data
            WeatherExporter.save_json(weather_data, "teszterweather.json")
            return weather_data
        except (Exception, FileNotFoundError) as e:
            print(f'Hiba: {e}')
            return {}


class WeatherExporter:
    @staticmethod
    def save_json(data, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print(f"Adat elmentve mint {filename}")
        except IOError as e:
            print(f"Error: Nem lehet elmenteni '{filename}'. {e}")

    @staticmethod
    def export_to_csv(data, output_file):
        is_data_written = False
        try:
            with open(output_file, "w", encoding='utf-8', newline='') as csvfile:
                fieldnames = ["Dátum", "Időjárás", "Hőmérséklet (C)", "Eső valószínűség (%)"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for date, details in data.items():
                    writer.writerow({
                        "Dátum": date,
                        "Időjárás": details["condition"],
                        "Hőmérséklet (C)": details["temperature"],
                        "Eső valószínűség (%)": details["rain_chance"]
                    })
            is_data_written = True
            print(f"\nAz adatok sikeresen exportálva a következő fájlba: {output_file}")
        except (Exception, IOError) as e:
            print(f'Hiba: {e}')
            return is_data_written

        return is_data_written


class WeatherReporter:
    def __init__(self, data):
        self.data = data

    def display_day_report(self, date):
        if date in self.data:
            print(f"\nIdőjárás {date} napján:")
            print(f"Időjárás: {self.data[date]['condition']}")
            print(f"Hőmérséklet: {self.data[date]['temperature']}C")
            print(f"Várható eső: {self.data[date]['rain_chance']}%")
        else:
            print("Nem található adat a megadott dátumra.")

    def display_month_report(self, month):
        print(f"\nIdőjárás jelentés a {month} hónapra:")

        for date, details in self.data.items():
            if date.startswith(month):
                print(f"{date}: {details['condition']}, "
                      f"{details['temperature']}C, "
                      f"eső: {details['rain_chance']}%")

    def analyze_date_range(self, start_date, end_date):
        date_range = [date for date in self.data if start_date <= date <= end_date]
        if not date_range:
            print("Nem található adat a megadott időszakban.")
            return

        total_temp = sum(self.data[date]["temperature"] for date in date_range)
        max_temp = max(self.data[date]["temperature"] for date in date_range)
        rainy_days = sum(1 for date in date_range if self.data[date]["rain_chance"] > 0)
        semillen_days = sum(1 for date in date_range if self.data[date]["condition"] == "semillen")

        print(f"\nStatisztika {start_date} és {end_date} között:")
        print(f"Átlaghőmérséklet: {total_temp / len(date_range):.2f}C")
        print(f"Maximális hőmérséklet: {max_temp}C")
        print(f"Esős napok száma: {rainy_days}")
        print(f"Semillen napok száma: {semillen_days}")


class WeatherApp:
    def __init__(self):
        self.file_name = "weather_data.txt"
        self.storage = WeatherStorage()
        self.exporter = WeatherExporter()
        self.reporter = None

    @staticmethod
    def is_exit_program(choice):
        return choice in ["0", "4", "end", "q", "quit"]

    @staticmethod
    def exit_process():
        sys.exit(1)

    def main_menu(self):
        while True:
            print("\nMenü:")
            print("0. Kilépés")
            print("1. Napi/havi jelentés")
            print("2. Két időpont közötti statisztika")
            print("3. Adatok exportálása CSV-be")
            print("4. Kilépés (end/q/quit)")
            choice = input("Választás: ").strip().lower()

            if self.is_exit_program(choice):
                print("Kilépés...")
                self.exit_process()
            elif choice == "1":
                self.display_daily_or_monthly()
            elif choice == "2":
                self.handle_date_range_analysis()
            elif choice == "3":
                self.exporter.export_to_csv(self.storage.data, "weather_data.csv")
            else:
                print("Érvénytelen választás, próbáld újra!")

    def display_daily_or_monthly(self):
        option = input("Napra vagy hónapra keresel? (D/M): ").strip().lower()

        if self.is_exit_program(option):
            self.exit_process()
        if option == "d":
            date = input("Add meg a dátumot (YYYY-MM-DD): ").strip()
            self.reporter.display_day_report(date)
        elif option == "m":
            month = input("Add meg a hónapot (YYYY-MM): ").strip()
            self.reporter.display_month_report(month)

    def handle_date_range_analysis(self):
        start_date = input("Add meg a kezdő dátumot (YYYY-MM-DD): ").strip()
        if self.is_exit_program(start_date):
            self.exit_process()

        end_date = input("Add meg a végdátumot (YYYY-MM-DD): ").strip()
        if self.is_exit_program(end_date):
            self.exit_process()

        self.reporter.analyze_date_range(start_date, end_date)

    def run(self):
        generator = WeatherGenerator(self.file_name)
        generator.generate_weather_data(datetime(2025, 10, 1), datetime(2025, 12, 12))
        data = self.storage.load_weather_data(self.file_name)
        self.reporter = WeatherReporter(data)
        self.main_menu()


if __name__ == "__main__":
    WeatherApp().run()
