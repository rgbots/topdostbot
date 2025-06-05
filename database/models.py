from enum import IntEnum

from tortoise import Model, fields


class Referals(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    count = fields.IntField(default=0)
    clicked = fields.IntField(default=0)
    price = fields.IntField(default=0)

    class Meta:
        table = 'refs'


class Subs(Model):
    id = fields.IntField(pk=True)
    subbed = fields.IntField(default=0)
    channel_name = fields.TextField(null=True)
    channel_id = fields.BigIntField()
    url = fields.CharField(max_length=256)
    token = fields.TextField(null=True)
    type = fields.TextField(default='channel')

    lang = fields.TextField()

    class Meta:
        table = 'subs'


class Views(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    type = fields.TextField(default='simple')
    viewed = fields.IntField(default=0)
    max_viewed = fields.IntField(default=0)
    status = fields.IntField(default=1)
    from_user = fields.BigIntField()
    message_id = fields.BigIntField()
    inline_mode = fields.BigIntField(default=0)
    viewed_users = fields.JSONField(default="[]")
    markup = fields.JSONField(default="[]")
    msg = fields.CharField(max_length=4096)

    class Meta:
        table = 'views'


class Users(Model):
    id = fields.BigIntField(pk=True, generated=False, index=True)

    first_name = fields.TextField(null=True)
    username = fields.CharField(max_length=64, null=True)
    ref = fields.CharField(max_length=128, null=True)
    subbed = fields.IntField(default=0)
    subbed_count = fields.IntField(default=0)
    valid = fields.SmallIntField(default=1)
    reg_time = fields.BigIntField(null=False)
    last_started = fields.BigIntField(null=False)
    last_active = fields.BigIntField(default=0)
    banned = fields.SmallIntField(default=0)

    class Meta:
        table = 'users'


class Groups(Model):
    id = fields.BigIntField(pk=True, generated=False, index=True)
    title = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'groups'


class Tests(Model):
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField(unique=True)
    answers = fields.JSONField()
    name_user = fields.TextField()

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'tests'


class Results(Model):
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField()
    test_creator_id = fields.BigIntField()
    answers = fields.JSONField()
    date = fields.BigIntField()
    percentage = fields.BigIntField()
    name_user = fields.TextField()

    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = 'results'


class Greetings(Model):
    id = fields.IntField(pk=True, index=True)
    text = fields.TextField()
    markup = fields.JSONField(default="[]")

    class Meta:
        table = 'greetings'


class MSType(IntEnum):
    native = 0
    flyer = 1


class GreetingsType(IntEnum):
    native = 0
    hiviews = 1


class ViewsType(IntEnum):
    native = 0
    gramads = 1


class AdminSettings(Model):
    id = fields.IntField(pk=True)
    ms_type = fields.IntEnumField(MSType, default=MSType.native)
    greetings_type = fields.IntEnumField(GreetingsType, default=GreetingsType.native)
    views_type = fields.IntEnumField(ViewsType, default=ViewsType.native)

    class Meta:
        table = 'admin_settings'
