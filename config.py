import os
import logging

APP_NAME = os.getenv("APP_NAME", "insights-puptoo")

logger = logging.getLogger(APP_NAME)

def get_namespace():
    try:
        with open("/var/run/secrets/kubernetes.io/serviceaccount/namespace", "r") as f:
            namespace = f.read()
        return namespace
    except EnvironmentError:
        logger.info("Not running in openshift")


LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()
BUILD_ID = os.getenv("OPENSHIFT_BUILD_COMMIT", "unknown")
DEVMODE = os.getenv("DEVMODE", False)
MAX_WORKERS = int(os.getenv("MAX_WORKERS", 50))
GROUP_ID = os.getenv("GROUP_ID", "advisor-pup")
MQ = os.getenv("KAFKAMQ", "kafka:29092").split(",")
CONSUME_TOPIC = os.getenv("CONSUME_TOPIC", "platform.upload.pup")
AWS_ACCESS_KEY_ID = os.getenv("CW_AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = os.getenv("CW_AWS_SECRET_ACCESS_KEY", None)
AWS_REGION_NAME = os.getenv("CW_AWS_REGION_NAME", "us-east-1")
INVENTORY_TOPIC = os.getenv("INVENTORY_TOPIC", "platform.inventory.host-ingress")
MAX_RECORDS = int(os.getenv("MAX_RECORDS", 1))
FACT_EXTRACT_LOGLEVEL = os.getenv("FACT_EXTRACT_LOGLEVEL", "ERROR")
LOG_GROUP = os.getenv("LOG_GROUP", "platform")
TRACKER_TOPIC = os.getenv("PAYLOAD_TRACKER_TOPIC", "platform.payload-status")
PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT", 8000))
DISABLE_PROMETHEUS = True if os.getenv("DISABLE_PROMETHEUS") == "True" else False
NAMESPACE = get_namespace()