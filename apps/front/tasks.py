from celery import shared_task


@shared_task
def test_logger():
    """
    Testing celery error logging in prod.
    """
    raise Exception('Celery logger TEST.')
