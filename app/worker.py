from celery import Celery
from time import sleep

import celery

from app.core.settings import settings

celery_app = Celery(broker=settings.redis_url)

celery_app.autodiscover_tasks(["app.modules.research.tasks"])

