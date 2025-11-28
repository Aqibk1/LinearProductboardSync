# LinearProductboardSync

**LinearProductboardSync** is a Python-based integration tool designed to synchronize data between [Linear](https://linear.app/) and [Productboard](https://www.productboard.com/). It leverages a Python script and GitHub Actions to ensure that issues, statuses, and feature requests remain consistent across your engineering and product management workflows.

## Features

* **Automated Sync:** Uses GitHub Actions (`.github/workflows/sync.yml`) to run synchronization tasks automatically (on a schedule or via manual trigger).
* **Custom Logic:** Built on a flexible Python script (`sync_webhooks.py`) that handles the API interactions.
* **Secure:** Configured to use GitHub Secrets for API keys, ensuring credentials are never hardcoded.

## Prerequisites

* A **Linear** account with an API key.
* A **Productboard** account with an Access Token.
* **Python 3.x** (if running locally).

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Aqibk1/LinearProductboardSync.git](https://github.com/Aqibk1/LinearProductboardSync.git)
    cd LinearProductboardSync
    ```

2.  **Install Dependencies (for local run):**
    If a `requirements.txt` file exists, run:
    ```bash
    pip install -r requirements.txt
    ```
    Otherwise, ensure you have `requests` installed:
    ```bash
    pip install requests
    ```

## Usage

### Option 1: Automated Sync (GitHub Actions)
This repository is configured to run automatically using GitHub Actions. To enable this on your own fork:

1.  **Fork** this repository.
2.  Navigate to **Settings > Secrets and variables > Actions**.
3.  Add the following **Repository Secrets** (ensure these match the variables used in `sync_webhooks.py` and `.github/workflows/sync.yml`):
    * `LINEAR_API_KEY`
    * `PRODUCTBOARD_TOKEN`
4.  Go to the **Actions** tab to enable the workflow. It will run based on the schedule defined in `sync.yml` or can be triggered manually.

### Option 2: Manual Execution (Local)
To run the synchronization script locally:

**macOS/Linux:**
```bash
export LINEAR_API_KEY="your_linear_key"
export PRODUCTBOARD_TOKEN="your_productboard_token"
python sync_webhooks.py
```

**Windows (PowerShell):**
```
$env:LINEAR_API_KEY="your_linear_key"
$env:PRODUCTBOARD_TOKEN="your_productboard_token"
python sync_webhooks.py
```


**Configuration**
The core logic is located in sync_webhooks.py. You may need to modify this file to:
- Update status mappings (e.g., mapping Linear "In Progress" to a specific Productboard status).
- Filter specific teams or projects.
- Change the sync direction (Linear → Productboard vs Productboard → Linear).

**Contributing**
Contributions are welcome!
1. Fork the project.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a Pull Request

**License**
Distributed under the MIT License. See ```LICENSE``` for more information.
