# LinearProductboardSync

**LinearProductboardSync** is a Python-based integration tool designed to synchronize data between [Linear](https://linear.app/) and [Productboard](https://www.productboard.com/). It leverages a Python script and GitHub Actions to ensure that issues, statuses, and feature requests remain consistent across your engineering and product management workflows.

## Features

* **Automated Sync:** Uses GitHub Actions to run synchronization tasks on a schedule or via manual trigger.
* **Custom Logic:** Built on a flexible Python script (`sync_webhooks.py`) that handles API requests and field mappings.
* **Secure:** Uses GitHub Secrets to manage API keys without hardcoding them in the script.

## Prerequisites

* A **Linear** account with an API key.
* A **Productboard** account with an Access Token.
* Python 3.x (for local execution).

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Aqibk1/LinearProductboardSync.git](https://github.com/Aqibk1/LinearProductboardSync.git)
   cd LinearProductboardSync
