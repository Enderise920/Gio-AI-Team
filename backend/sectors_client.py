import os
import requests
from dotenv import load_dotenv

load_dotenv()


class SectorsClient:
    BASE_URL = "https://api.sectors.app/v2"

    def __init__(self):
        self.api_key = os.getenv("SECTORS_API_KEY")

        if not self.api_key:
            raise ValueError(
                "SECTORS_API_KEY belum ditemukan di .env"
            )

        self.headers = {
            "Authorization": self.api_key
        }

    def get_companies(
        self,
        where=None,
        order_by="symbol",
        limit=50,
        offset=0
    ):
        url = f"{self.BASE_URL}/companies/"

        params = {
            "order_by": order_by,
            "limit": limit,
            "offset": offset
        }

        if where:
            params["where"] = where

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def get_daily(
        self,
        ticker,
        start=None,
        end=None
    ):
        url = f"{self.BASE_URL}/daily/{ticker}/"

        params = {}

        if start:
            params["start"] = start

        if end:
            params["end"] = end

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()


if __name__ == "__main__":
    client = SectorsClient()

    data = client.get_companies(
        where="symbol='BBRI.JK'",
        order_by="-roe_ttm",
        limit=1
    )

    print(data)

    daily = client.get_daily(
        "BBRI.JK",
        start="2026-09-01"
    )

    print("\nDaily records:", len(daily))