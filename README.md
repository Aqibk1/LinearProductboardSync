LinearProductboardSync
LinearProductboardSync is a Python-based integration tool designed to synchronize data between Linear and Productboard. It leverages a Python script and GitHub Actions to ensure that issues, statuses, and feature requests remain consistent across your engineering and product management workflows.

Features
Automated Sync: Uses GitHub Actions to run synchronization tasks on a schedule or via manual trigger.

Custom Logic: Built on a flexible Python script (sync_webhooks.py) that can be modified to handle specific field mappings.

Secure: Uses GitHub Secrets to manage API keys without hardcoding them in the script.

Prerequisites
A Linear account with an API key.

A Productboard account with an Access Token.

A GitHub account (if using the automated workflow).

Installation
Clone the repository:

Bash

git clone https://github.com/Aqibk1/LinearProductboardSync.git
cd LinearProductboardSync
Install Dependencies (for local run):

Bash

pip install -r requirements.txt
# Or manually install requests if requirements.txt is missing
pip install requests
Usage
Option 1: Manual Execution (Local)
To run the sync manually from your local machine, set your environment variables and run the script:

Bash

# macOS/Linux
export LINEAR_API_KEY="your_linear_key"
export PRODUCTBOARD_TOKEN="your_productboard_token"

python sync_webhooks.py
Option 2: Automated Sync (GitHub Actions)
This repository includes a workflow file (.github/workflows/sync.yml) that automates the execution. To set this up:

Fork this repository to your own GitHub account.

Go to your repository Settings > Secrets and variables > Actions.

Click New repository secret and add the following secrets (check sync.yml for the exact variable names expected):

LINEAR_API_KEY

PRODUCTBOARD_TOKEN

(Add any other secrets defined in the env section of the workflow file)

The workflow is likely configured to run on a schedule (e.g., every hour) or on workflow_dispatch (manual button click in the Actions tab).

Go to the Actions tab in your repository and ensure the workflow is enabled.

Configuration
The main logic resides in sync_webhooks.py. You can customize the following:

Field Mapping: Modify the script to change how Linear priority/status maps to Productboard importance/status.

Filters: Update the query logic to only sync specific teams or projects.

Contributing
Contributions are welcome!

Fork the project.

Create your feature branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.

License
Distributed under the MIT License. See LICENSE for more information.
