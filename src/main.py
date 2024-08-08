import os
import sys
import asyncio
sys.path.insert(1,os.path.join(sys.path[0],'..'))
from queries.orm import SyncORM
#from queries.orm import async_insert_data,#create_tables
from database import sync_engine
from models import metadata_object


SyncORM.create_tables()
# metadata_object.reflect(bind=sync_engine)
# tables=metadata_object.tables.keys()
# for table in tables:
#     print(table)
