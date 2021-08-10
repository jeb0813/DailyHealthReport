#!/usr/bin/python
# -*- coding: UTF-8 -*-
import body
import apscheduler
import time
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
scheduler.add_job(body.start, 'cron', hour=11, minute=29)
scheduler.start()
