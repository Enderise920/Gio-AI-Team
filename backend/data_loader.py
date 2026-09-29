import json
from pathlib import Path

from sectors_client import SectorsClient


DATA_DIR = Path(__file__).resolve().parent.parent / "data"

COMPANIES_FILE = DATA_DIR / "companies.json"
FUNDAMENTALS_FILE = DATA_DIR / "fundamentals.json"


METRICS = [
    "market_cap",
    "roe_ttm",
    "roa_ttm",
    "pe_ttm",
    "pb_mrq",
    "forward_pe",
    "yield_ttm",
    "dividend_ttm",
    "yoy_quarter_revenue_growth",
    "yoy_quarter_earnings_growth"
]


def load_all_fundamentals(page_size=200):
    """
    Mengambil fundamentals seluruh universe
    menggunakan bulk request Sectors API v2.
    """

    client = SectorsClient()

    order_by = ",".join(METRICS)

    all_companies = []

    offset = 0

    while True:

        print(
            f"Mengambil fundamentals: "
            f"offset={offset}"
        )

        data = client.get_companies(
            order_by=order_by,
            limit=page_size,
            offset=offset,
            include_query_values=True
        )

        results = data.get(
            "results",
            []
        )

        if not results:
            break

        for company in results:

            query_values = company.get(
                "query_values",
                {}
            )

            record = {
                "symbol": company.get(
                    "symbol"
                ),
                "company_name": company.get(
                    "company_name"
                )
            }

            for metric in METRICS:

                record[metric] = query_values.get(
                    metric
                )

            all_companies.append(
                record
            )

        pagination = data.get(
            "pagination",
            {}
        )

        if not pagination.get(
            "has_next",
            False
        ):
            break

        offset = pagination.get(
            "next_offset"
        )

        if offset is None:
            break

    return all_companies


def save_fundamentals(data):
    """
    Menyimpan fundamentals ke JSON lokal.
    """

    DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        FUNDAMENTALS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )

    print(
        f"\nData disimpan ke:"
    )

    print(
        FUNDAMENTALS_FILE
    )


def print_summary(data):
    """
    Menampilkan ringkasan kualitas data.
    """

    print("\n=== DATA QUALITY SUMMARY ===")

    print(
        f"Total perusahaan: {len(data)}"
    )

    print("\nCoverage:")

    for metric in METRICS:

        available = sum(
            1
            for company in data
            if company.get(metric) is not None
        )

        total = len(data)

        percentage = (
            available / total * 100
            if total
            else 0
        )

        print(
            f"{metric:35}"
            f"{available:4}/{total:<4}"
            f"({percentage:5.1f}%)"
        )


if __name__ == "__main__":

    print(
        "=== BAGGER RADAR FUNDAMENTAL INGESTION ==="
    )

    fundamentals = load_all_fundamentals()

    print_summary(
        fundamentals
    )

    save_fundamentals(
        fundamentals
    )