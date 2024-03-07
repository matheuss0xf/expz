from sqlalchemy import select

from app.models import User


def test_create_user(session):
    new_user = User(
        username='matheus', password='testpass', email='teste@test'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'matheus'))

    assert user.username == 'matheus'
