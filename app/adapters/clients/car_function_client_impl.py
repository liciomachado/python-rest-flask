import requests
from app.domain.ports.car_function_client import ICarFunctionClient
import os

class CarFunctionClient(ICarFunctionClient):
    def __init__(self, api_key: str):
        self.base_url = "https://api.agrotools.com.br/functions/car/consulting_by_code"
        self.api_key = api_key

    def consultar_por_codigo(self, codigo: str) -> dict:
        url = f"{self.base_url}/{codigo}?IAMKEY={self.api_key}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
