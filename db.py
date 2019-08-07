import peewee

db = peewee.SqliteDatabase('users.db')


class User(peewee.Model):
    chat_id = peewee.IntegerField(unique=True)
    state = peewee.IntegerField(default = 0)
    firstname = peewee.TextField(default = '')
    lastname = peewee.TextField(default = '')
    phonenumber = peewee.TextField(default = '')

    class Meta:
        database = db


def init():
    db.connect()
    db.create_tables([User], safe=True)
    db.close()


def get_state(chat_id):
    user = User.get_or_none(chat_id=chat_id)
    if user is None:
        return None

    return user.state


def set_state(chat_id, state):
    user, created = User.get_or_create(chat_id=chat_id)

    user.state = state
    user.save()

def set_firstname(chat_id, firstname):
    user, created = User.get_or_create(chat_id=chat_id)

    user.firstname = firstname
    user.save()

def set_lastname(chat_id, lastname):
    user, created = User.get_or_create(chat_id=chat_id)

    user.lastname = lastname
    user.save()

def set_phonenumber(chat_id, number):
    user, created = User.get_or_create(chat_id=chat_id)

    user.phonenumber = number
    user.save()


init()
