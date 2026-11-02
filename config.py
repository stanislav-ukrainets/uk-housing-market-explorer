from pathlib import Path

# The folder file is in, so paths work whether repo is cloned
REPO_ROOT = Path(__file__).resolve().parent

# API responces saved, untouched and commited as brief requires 
RAW_DATA_DIR = REPO_ROOT / "data" / "raw"

# Base Address of api
HPI_BASE_URL = "https://landregistry.data.gov.uk/data/ukhpi"

# Asking messages for api
USER_AGENT = "uk-housing-market-explorer (github.com/stanislav-ukrainets/uk-housing-market-explorer)"

# Base timeout for api requests,slower server can't hang the script
REQUEST_TIMEOUT_SECONDS = 30

# MAX page size for this api is 200
PAGE_SIZE =200

# Pause between requests to avoid being blocked by the api
PAUSE_SECONDS = 1 

# Project Scope 

START_MONTH = "1995-01"
END_MONTH = "2025-12"

# Tested districts
DISTRICTS = ["camden", "coventry", "cumberland"]