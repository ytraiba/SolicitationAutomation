import asyncio
from webScripts.alaska import *
from webScripts.indiana import *
from webScripts.virginia import *

async def main():
    L = await asyncio.gather(
        indiana1(),
        alaska1(),
        virginia1(),
    )
    print('Downloads Are Complete')
