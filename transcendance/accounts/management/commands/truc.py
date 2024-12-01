from django.contrib.auth.models import User
from accounts.models import *
from games.models import *
from relationship.models import *
from tournaments.models import *
# from App2.models import * #etc

import os
from os.path import exists
from pathlib import Path
import shutil

from django.core import management
from django.core.management.commands import migrate
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # args = ‘<foo bar …>’
    # help = ‘our help string comes here’

    def handle(self, *args, **options):
        self._reset_migrations()
        # self._migrate_apps()

        #This works but is not supported for testing so ignore this code if you can
        # self._create_user()
        # self._create_data()

        #For me this fails but it seems nice.
        # self._populate_db_from_fixtures()

    def _reset_migrations(self):
        cwd = os.getcwd()
        # This is the code for sqlite db file deletion. Change for other databases.
        db_file = cwd + '\db.sqlite3'
        if(Path(db_file).is_file() ):
            os.remove(db_file)

        i = 0
        for subdir, dirs, files in os.walk(cwd):
            print(subdir)
            if(os.path.basename(os.path.normpath(subdir)) == "migrations"):
                i = i+1
                shutil.rmtree(subdir)
        print('%i migration folders found and deleted' %(i)) 

    def _migrate_apps(self):
        print('\nmigrate all apps.')
        print('Initial migration for the basics')
        management.call_command('migrate')
