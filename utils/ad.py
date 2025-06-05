import logging
import aiohttp

from typing import Optional

from config import config

# Call this method wherever you want to show an ad,
# for example your bot just made its job and
# it's a great time to show an ad to a user

log = logging.getLogger('adverts')


async def HiViews(UserId: int, MessageId: int, UserFirstName: str, LanguageCode: Optional[str]):
    if not LanguageCode:
        LanguageCode = 'ru'

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(sock_read=3)) as session:
        try:
            async with session.post(
                'https://hiviews.net/sendMessage',
                headers={
                    'Authorization': config.tg_services.hi_views_token,
                    'Content-Type': 'application/json',
                },
                json={'UserId': UserId, 'MessageId': MessageId, 'UserFirstName': UserFirstName, 'LanguageCode': LanguageCode},
            ) as response:
                resp = await response.text('utf-8')
                if 'No posts' in resp:
                    return False
                else:
                    logging.error(f'[HiViews] - {resp}')
                    return True
        except aiohttp.ServerTimeoutError:
            return True


async def show_advert(user_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            'https://api.gramads.net/ad/SendPost',
            headers={
                'Authorization': 'Bearer ...',
                'Content-Type': 'application/json',
            },
            json={'SendToChatId': user_id},
        ) as response:
            if not response.ok:
                log.error('Gramads: %s' % str(await response.json()))
