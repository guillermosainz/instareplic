import os

MONGODB_JOBS = os.getenv("MONGOLAB_URI")
MONGODB_LOGS = os.getenv("MONGOLAB_URI")
MONGODB_LOGS_SIZE = 10 * 1024 * 1024

REDIS = os.getenv("REDISCLOUD_URL")

if os.getenv("MRQ_DASHBOARD_HTTPAUTH"):
  DASHBOARD_HTTPAUTH = os.getenv("MRQ_DASHBOARD_HTTPAUTH")

TASKS = {
    "mrq.basetasks.utils.JobAction": {"queue": "highpriority"}
}
