import csv
import ipaddress
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
import requests
from testCases import TEST_CASE

TARGET = "http://172.29.221.21:3000"

LOGIN_URL = f"{TARGET}/rest/user/login"

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
CSV_FILE = DATA_DIR / "test_results.csv"

TIMEOUT_SECONDS = 10


def validate(target):
    parsed = urlparse(target)
    
    if parsed.scheme != "http":
        raise ValueError("Invalid URL schema.only http is allowed.")
    if not parsed.hostname or parsed.port != 3000:
        raise ValueError("Target must specify a host and port 3000.")
    
    host = parsed.hostname

    if host == "localhost":
        return

    try:
        address = ipaddress.ip_address(host)
    except ValueError as exc:
        raise ValueError("Use localhost or your verified private IP.") from exc

    if not address.is_private or address.version != 4:
        raise ValueError("Target must be a private IPv4 lab address.")


    
    
def run_test(session, case):
    
    url = f"{TARGET}{case['path']}"
    started = time.perf_counter()
    status_code = ""
    error = ""

    try:
        if case["method"] == "GET":
            response = session.get(
                url,
                timeout=TIMEOUT_SECONDS,
            )
        else:
            response = session.post(
                url,
                json=case["payload"],
                timeout=TIMEOUT_SECONDS,
            )

        status_code = response.status_code
        # print("status:", response.status_code)
        # print("Response:", response.text)
    except requests.RequestException as exc:
        error = str(exc)

    elapsed_ms = round(
        (time.perf_counter() - started) * 1000,
        2,
    )
        
    result = {
        "test_id": case["test_id"],
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "category": case["category"],
        "method": case["method"],
        "path": case["path"],
        "http_status": status_code,
        "response_time_ms": elapsed_ms,
        "error": error,
    }

    print(
        f"{result['test_id']} | "
        f"{result['category']} | "
        f"HTTP {status_code or 'ERROR'} | "
        f"{elapsed_ms} ms"
    )

    if error:
        print(f"  Connection error: {error}")

    return result


def main():
    validate(TARGET)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "test_id",
        "timestamp_utc",
        "category",
        "method",
        "path",
        "http_status",
        "response_time_ms",
        "error",
    ]

    results = []

    with requests.Session() as session:
        for case in TEST_CASE:
            results.append(run_test(session, case))
            time.sleep(1)

    with CSV_FILE.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
        )
        writer.writeheader()
        writer.writerows(results)

    print(f"\nCompleted {len(results)} tests.")
    print(f"CSV saved to: {CSV_FILE}")


if __name__ == "__main__":
    main()