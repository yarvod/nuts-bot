from users.models import (
    User,
)


def update_or_create_user(user):
    user_db, created = User.objects.update_or_create(
        id=user.id,
        defaults=dict(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name
        )
    )


