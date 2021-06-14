import asyncpg
import asyncio

class Database(object):
    def __init__(self, app, pool, loop=None, timeout: float = 60.0):
        self.app = app
        self._pool = pool
        self._loop = loop or asyncio
        self.timeout = timeout
        self._rate_limit = asyncio.Semaphore(value=self._pool._maxsize, loop=self._loop)

    @classmethod
    async def create_pool(cls, app, uri=None, *, min_connections=10, max_connections=10,
                          timeout=60.0, loop=None, **kwargs):
        pool = await asyncpg.create_pool(uri, min_size=min_connections, max_size=max_connections, **kwargs)
        self = cls(app=app, pool=pool, loop=loop, timeout=timeout)
        print('Established DataBase pool with {} - {} connections\n'.format(min_connections, max_connections))
        return self

    async def close_connection(self):
        await self._pool.close()

    async def fetch(self, query, *args):
        async with self._rate_limit:
            async with self._pool.acquire() as con:
                return await con.fetch(query, *args, timeout=self.timeout)

    async def fetchrow(self, query, *args):
        async with self._rate_limit:
            async with self._pool.acquire() as con:
                return await con.fetchrow(query, *args, timeout=self.timeout)

    async def execute(self, query: str, *args):
        async with self._rate_limit:
            async with self._pool.acquire() as con:
                return await con.execute(query, *args, timeout=self.timeout)