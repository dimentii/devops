from logging import getLogger
from time import sleep
from random import randint

import falcon
from falcon.asgi import Request, Response

logger = getLogger(__name__)


class ProductsEndpoint:
    async def on_put(self, req: Request, resp: Response):
        """
        Create product endpoint
        """
        timeout = randint(100, 250)
        # sleep(timeout * 0.001)
        products = await req.get_media()
        logger.info({'message': f'Received {len(products)} products'})
        resp.status = falcon.HTTP_202
        resp.media = {'success': True, 'message': f'Processed {len(products)} products'}
