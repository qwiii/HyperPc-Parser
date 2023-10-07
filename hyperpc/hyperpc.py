from bs4 import BeautifulSoup
from ujson import loads, dump
from requests import get, Response


class HyperPc:
    def __init__(self) -> None:
        self.api: str = "https://hyperpc.ru"

    def __parse__(self, html: str, file_name: str) -> None:
        data: list[dict] = []
        soup: BeautifulSoup = BeautifulSoup(markup=html, features="html.parser")

        for elements in soup.find_all(name="script", attrs={
            "type": "application/ld+json"
        }):
            data.append(loads(elements.string))

        data.pop()

        with open(file_name, "w") as file:
            dump(data, file, indent=2)

    def parse_computers_catalog(self) -> None:
        response: Response = get(url=f"{self.api}/catalog/computers")
        if response.status_code != 200:
            raise Exception("Unable to get information!")

        self.__parse__(html=response.text, file_name="catalog.json")

    def parse_optimal_pc(self) -> None:
        response: Response = get(url=f"{self.api}/gaming-pc/optimal")
        if response.status_code != 200:
            raise Exception("Unable to get information")

        self.__parse__(html=response.text, file_name="optimal.json")

    def parse_powerful_pc(self) -> None:
        response: Response = get(url=f"{self.api}/gaming-pc/powerful")
        if response.status_code != 200:
            raise Exception("Unable to get information")

        self.__parse__(html=response.text, file_name="powerful.json")

    def parse_custom_pc(self) -> None:
        response: Response = get(url=f"{self.api}/gaming-pc/custom")
        if response.status_code != 200:
            raise Exception("Unable to get information")

        self.__parse__(html=response.text, file_name="custom.json")

    def parse_hardware(self, url: str) -> list[str]:
        result: list[str] = []
        response: Response = get(url)
        if response.status_code != 200:
            raise Exception("Unable to get information")

        soup: BeautifulSoup = BeautifulSoup(markup=response.text, features="html.parser")

        for elements in soup.find_all(name="div", attrs={
            "class": "uk-text-center"
        }):
            data = elements.find("img", alt=True)
            if data is not None:
                result.append(data["alt"])

        return result
