from django.core.management.base import BaseCommand
from utilities.update_vl import UpdateVL

class Command(BaseCommand):
	help = 'Updates viral load for each existing and non-existing \
			OVCs'

	def add_arguments(self, parser):
		pass

	def handle(self, *args, **options):
		# UpdateVL().update_tracker()
		UpdateVL().save_data()
		self.stdout.write('----- Updated viral loads -----')
