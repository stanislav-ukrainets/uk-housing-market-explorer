import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config

def fetch_page(district, page):
    url = f"{config.HPI_BASE_URL}.json"
    params = {
        "_pageSize": config.PAGE_SIZE,
        "_page": page,
        "_sort": "refMonth",
        "refRegion": f"http://landregistry.data.gov.uk/id/region/{district}"
    }
    headers = {"User-Agent": config.USER_AGENT}

    response = requests.get(url, params=params, headers=headers, timeout=config.REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response

def main():
    run_timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    files_saved = 0
    for district in config.DISTRICTS:
        page = 0
        while True:
            response = fetch_page(district, page)
            rows = len(response.json()["result"]["items"])
            if rows == 0 and page == 0:
                raise  ValueError(f"No data found for district '{district}'")
            if rows == 0:
                break  # No more data, exit the loop
            file_name = f"hpi_{district}_run-{run_timestamp}_page-{page}.json"
            path = config.RAW_DATA_DIR / file_name
            with open(path, "w", encoding ="utf-8") as f:
                f.write(response.text)

            files_saved += 1 
            print(f"Saved {file_name} ({rows} rows)")

            if rows < config.PAGE_SIZE: 
                break
            page += 1
            time.sleep(config.PAUSE_SECONDS)

        time.sleep(config.PAUSE_SECONDS)
    
    print(f"Done: {files_saved} files saved to {config.RAW_DATA_DIR}")

if __name__ == "__main__":
    main()

        