from django.core.management.base import BaseCommand
from utilities.update_kmhfr import KMHFLFacilities

class Command(BaseCommand):
	help = 'Update KMHFL facilities'

	def add_arguments(self, parser):
		pass

	def handle(self, *args, **options):
		KMHFLFacilities().get_newest_facilities()
		self.stdout.write('----- Updated KMHFL Facilities -----')