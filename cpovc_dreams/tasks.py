from celery import shared_task

@shared_task()
def get_dreams_services(cpims_id, dreams_id):
	print("Good to go")