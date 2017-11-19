from django.core.management.base import BaseCommand, CommandError
from tenant.models import TmsTenant


class Command(BaseCommand):
    def handle(self, *args, **options):
        tenant = TmsTenant(
            domain_url=input("\tDomain URL: "),
            schema_name=input("\tSchema Name: "),
            name=input("\tName of company: "),
            paid_until=input("\tPaying Date (yyyy-mm-dd) A.D.: "),
            on_trial=input("\tOn Trial(True/False): ")
        )
        tenant.save()

        print("\n\t===========================================================\n")
        print('\n\t\tSchema is created with Domain URL %s. \n\t\tThis schema is valid until %s\n' % (tenant.domain_url, tenant.paid_until))
        print("\n\t===========================================================\n")
