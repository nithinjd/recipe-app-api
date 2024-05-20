
# wait for the database to be available
import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg20pError
class Command(BaseCommand):
    def handle(self,*args,**options):
        self.stdout.write("waiting for database")
        db_up = False
        while db_up is False:
            try:
                self.check(database=['default'])
                db_up= True
            except(Psycopg20pError,OperationalError):
                self.stdout.write("delay for a second")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database Available'))
