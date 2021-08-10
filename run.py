import body
import apscheduler
import time
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
scheduler.add_job(body.start, 'cron', hour=00, minute=1)
scheduler.start()
