"""Contains the connection class for communicating with a Postgres Database using psycopg2."""

import psycopg2
import psycopg2.extras
from conf.env_setup import EnvSetup


class Postgres(object):

    def __init__(self):
        self.connection = psycopg2.connect(EnvSetup.DATA_WAREHOUSE)
        self.cursor = None

    def send_committed_query(self, query, params=None):
        connection = self.connection
        self.cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        if params:
            self.cursor.execute(query, (params))
        else:
            self.cursor.execute(query)
        connection.commit()
        return self.cursor.fetchall()

    def close_connection(self):
        connection = self.connection
        self.cursor.close()
        connection.close()
