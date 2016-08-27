import os


class EnvSetup(object):

    # Environment variable of the Database
    DATA_WAREHOUSE = os.getenv('DATA_WAREHOUSE', 'postgresql://postgres:unified123@localhost:5432/testdb')

