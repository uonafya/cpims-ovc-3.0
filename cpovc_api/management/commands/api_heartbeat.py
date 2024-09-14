from django.core.management.base import BaseCommand, CommandError
from utilities.api_heartbeat import APIHeartbeat


class Command(BaseCommand):
    help = "Check health status of the systems integrations"

    def add_arguments(self, parser):
        parser.add_argument("system_id", nargs="+", type=int)

    def handle(self, *args, **options):
        APIHeartbeat().get_status()
        self.stdout.write(
                self.style.SUCCESS('API heartbeat successfully checked')
            )