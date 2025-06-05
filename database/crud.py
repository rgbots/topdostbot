import time
import logging
from datetime import datetime

from typing import Optional

from tortoise.expressions import F, Q

from .models import Users, Referals, Subs, Groups, Tests, Results
from .models import Greetings, GreetingsType, AdminSettings, MSType, ViewsType


async def create_or_get_user(
        user_id: int,
        first_name: str,
        username: Optional[str],
        source: Optional[str]
):
    user = await Users.get_or_none(id=user_id)
    if user:
        return user, False
    
    if source:
        ref_checker = await Referals.exists(name=source)
    else:
        ref_checker = None

    if ref_checker or source:
        user = await Users.create(
            id=user_id, first_name=first_name, username=username,
            ref=source, reg_time=int(time.time()),
            last_started=int(time.time())
        )
        await Referals.filter(name=source).update(clicked=F('clicked') + 1, count=F('count') + 1)
    else:
        user = await Users.create(
            id=user_id, first_name=first_name,
            reg_time=int(time.time()),
            last_started=int(time.time()),
        )

    return user, True


async def get_user(user_id: int) -> Optional[Users]:
    return await Users.get_or_none(id=user_id)


async def create_group(chat_id: int, title: str):
    await Groups.update_or_create(id=chat_id, defaults={'title': title})


async def get_test(user_id: int) -> Optional[Tests]:
    return await Tests.get_or_none(user_id=user_id)


async def get_result(
        user_id: int,
        test_creator_id: int
) -> Optional[Results]:
    return await Results.get_or_none(user_id=user_id, test_creator_id=test_creator_id)


async def create_test(
        user_id: int,
        answers: list,
        name_user: str
):
    await Tests.create(user_id=user_id, answers=answers, name_user=name_user, created_at=int(time.time()))


async def delete_test(user_id: int):
    await Tests.filter(user_id=user_id).delete()
    await Results.filter(test_creator_id=user_id).delete()


async def top_results(
        user_id: int
):
    return await Results.filter(test_creator_id=user_id).order_by(
        '-percentage').values_list('percentage', 'name_user')


async def results_count(
        user_id: int
):
    return await Results.filter(test_creator_id=user_id).count()


async def gen_percentage(
        user_id: int
):
    return await Results.filter(test_creator_id=user_id).values_list(
        'percentage', flat=True)


async def creator_answers(
        user_id: int
):
    return await Tests.filter(user_id=user_id).values_list('answers', flat=True)


async def create_result(
        user_id: int,
        test_creator_id: int,
        answers: list,
        date: int,
        percentage: int,
        name_user: str
):
    await Results.create(
        user_id=user_id,
        test_creator_id=test_creator_id,
        answers=answers,
        date=date,
        percentage=percentage,
        name_user=name_user,
        created_at=int(time.time())
    )


async def create_admin_settings() -> None:
    if not await AdminSettings.exists():
        await AdminSettings.create()


async def get_admin_settings_ms_type() -> MSType:
    settings = await AdminSettings.all().first()
    return settings.ms_type


async def update_admin_settings_ms_type(ms_type: MSType) -> None:
    await AdminSettings.all().update(ms_type=ms_type)


async def set_user_unsubscribed(user_id: int) -> None:
    await Users.filter(id=user_id).update(subbed=0, subbed_count=0)


async def update_sub_counter(user_id: int) -> None:
    if (await get_admin_settings_ms_type()) is MSType.native:
        subs_count = await Subs.filter().only("id").count()
    else:
        subs_count = 1

    await Users.filter(id=user_id).update(subbed=1, subbed_count=F('subbed_count') + subs_count)
    await Subs.filter().update(subbed=F('subbed') + 1)


async def get_views_type() -> ViewsType:
    settings = await AdminSettings.all().first()
    return settings.views_type


async def update_views_type(type: ViewsType) -> None:
    await AdminSettings.all().update(views_type=type)


async def get_greetings_type() -> GreetingsType:
    settings = await AdminSettings.all().first()
    return settings.greetings_type


async def update_greetings_type(type: GreetingsType) -> None:
    await AdminSettings.all().update(greetings_type=type)


async def greeting_exists() -> bool:
    greeting = await Greetings.filter().count()
    return bool(greeting)


async def get_greeting() -> Optional[Greetings]:
    return await Greetings.all().first()


async def create_greeting(text: str, markup: list) -> None:
    await Greetings.all().delete()
    await Greetings.create(
        text=text,
        markup=markup
    )


async def delete_greeting() -> None:
    await Greetings.all().delete()


async def get_users_ids_by_ref(ref: str):
    return await Users.filter(ref=ref).values_list('id', flat=True)
