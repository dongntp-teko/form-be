from app.models import User


def get_all():
    users = User.query.all();
    # return [u.to_dict() for u in users]
    return users