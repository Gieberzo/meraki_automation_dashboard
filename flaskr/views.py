from flaskr import app
from flask import render_template
import meraki
import logging
import os

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))


# OPTIONAL CONFIG VALUES
SUPPRESS_MERAKI_LOGGING = True

dashboard = meraki.DashboardAPI(suppress_logging=SUPPRESS_MERAKI_LOGGING)

@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        hiddenLinks=False,
    )


@app.route("/compliance_report", methods=["GET"])
def compliance_report():
    orgs = getMerakiOrgs()
    log.info(f"Querying list of devices for network {orgs}")
    return render_template(
        "compliance_report.html",
        hiddenLinks=False,
        orgs=orgs,
    )

def getMerakiOrgs():
    orgs = dashboard.organizations.getOrganizations()
    return orgs
