import os
from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup


def kezdet_req():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    if response.status_code == 200:
        print("sikeres kérés: ", response.json())
    else:
        print(f'{response.status_code}')


# kezdet_req()


def prookt_img():
    url = "https://prooktatas.hu/assets/img/prooktatas-programozo-kepzes-online.png"
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open("letoltott_kep.jpg", "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
            print("kép sikeresen letöltve")
    else:
        print(f"hiba: {response.status_code}")


# prookt_img()


def bs4_metodus():
    url = "https://telex.hu"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').text
        print(f'oldal címe: {title}')
    else:
        print("nem elérhető")


# bs4_metodus()


def telex_kep_letolto():
    url = "https://telex.hu/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        os.makedirs('telex_images', exist_ok=True)
        for img in images:
            src = img.get('src')
            if src:
                img_url = src if src.startswith("http") else url + src
                img_response = requests.get(img_url, stream=True)
                if img_response.status_code == 200:
                    file_name = os.path.join("telex_images", os.path.basename(img_url))
                    with open(file_name, "wb") as file:
                        for chunk in img_response.iter_content(4096):
                            file.write(chunk)
        print("minden kép letöltve")
    else:
        print("valami hiba")


# telex_kep_letolto()


def github_api():
    url = "https://api.github.com/search/repositories"
    params = {"q": "python", "sort": "stars"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(response.json()["items"][0]["full_name"])


# github_api()


def try_except():
    try:
        respone = requests.get("https://prooktatas.hu/", timeout=1)
        respone.raise_for_status()
        print("sikeres kérés")
    except requests.exceptions.Timeout:
        print("időtullépés")
    except requests.exceptions.RequestException as e:
        print(f'hiba történt: {e}')


try_except()

class HTTPClient:
    def get(self):
        pass

    def post(self):
        pass


class JSONApiService:
    def __init__(self, client):
        self.client = client

    def get_resource(self, url):
        res = self.client.get(url)


class Downloader(ABC):
    @abstractmethod
    def download(self, url, save_path):
        pass


class ImageDownloader(Downloader):
    def download(self, url, save_path):
        pass
        # business logic


class Config:
    IMAGE_DIR = "downloads/images"


class App:
    def __init__(self, downloader: Downloader, config: Config):
        self.downloader = downloader
        self.config = config

    def download(self, url):
        self.downloader.download(url, "file-path")


def main():
    downloader = ImageDownloader()
    config = Config()
    app = ImageDownloader(downloader, config)

    url = "foo.org"
    path = "/data"
    app.download(url, path)

