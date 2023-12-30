from redis import Redis
from connection_options import connection

class redis_connection:
    def __init__(self) -> None:
        self.host = connection['HOST']
        self.port = connection['PORT']
        self.db = connection['DB']
        self.connection = None

    def connect(self) ->Redis:
        self.connection = Redis(
            host = self.host,
            port = self.port,
            db = self.db
        )
        return self.connection

        