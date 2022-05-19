# Meraki - Automation Dashboard

This code repository contains a proof-of-concept Meraki automation dashboard. It is currently under development.

## Contacts
* Matt Giepert(mgiepert@cisco.com)

## Solution Components
* Meraki Dashboard APIs
* Flask

## Installation/Configuration

**Clone repo:**
```bash
git clone <repo_url>
```

**Install required dependancies:**
```bash
pip install -r requirements.txt
```

**Configure required variables:**

Export your Meraki API key using the command.

export MERAKI_DASHBOARD_API_KEY=093b24e85df15a3e66f1fc359f4c48493eaa1b73


## Usage

After all required configuration items are in place, run the application with the following command:

```
python setup.py
```

If running the app locally, browse to `http://127.0.0.1:5000`. 

