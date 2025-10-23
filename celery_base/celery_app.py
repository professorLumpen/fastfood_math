from celery import Celery

from celery_base.config import settings


celery_app = Celery(
    main="celery_base.celery_app",
    broker=settings.rabbit_url,
    backend=settings.redis_url,
    broker_connection_retry_on_startup=True,
    include=["celery_base.tasks"],
)
