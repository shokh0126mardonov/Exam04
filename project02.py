from sqlalchemy import (
    select, update, delete, func
)
from database import Base, engine, Session
from models import Task, User

Base.metadata.create_all(engine)

with Session() as session:
    # Faqat ma'lumot yo'q bo'lsa qo'shamiz
    if not session.query(User).first():
        user1 = User(user_name="Ali Valiyev", user_email="ali@gmail.com")
        user2 = User(user_name="Shohjahon Mardonov", user_email="shoh@gmail.com")
        user3 = User(user_name="Abdurauf Nasrullayev", user_email="Abu@gmail.com")

        session.add_all([user1, user2, user3])
        session.commit()

        task1 = Task(task_title="Python loyihasini tugatish", task_status="pending", user_id=user1.user_id)
        task2 = Task(task_title="Presentation tayyorlash", task_status="completed", user_id=user1.user_id)
        task3 = Task(task_title="Django REST API yozish", task_status="pending", user_id=user2.user_id)
        task4 = Task(task_title="SQL darsini takrorlash", task_status="completed", user_id=user3.user_id)

        session.add_all([task1, task2, task3, task4])
        session.commit()

    users = session.query(User).all()
    for u in users:
        print(u.user_name, "→", [t.task_title for t in u.tasks])

    stmt = select(Task).where(Task.task_status == "completed")
    for t in session.scalars(stmt):
        print(t.task_title, t.task_status)

    stmt = (
        update(Task)
        .where(Task.task_title == "Presentation tayyorlash")
        .values(task_status="done")
    )
    session.execute(stmt)
    session.commit()

    tasks = session.execute(select(Task.task_title, Task.task_status)).all()
    for title, status in tasks:
        print(title, status)


    stmt = delete(Task).where(Task.task_title == "SQL darsini takrorlash")
    session.execute(stmt)
    session.commit()


    tasks = session.execute(select(Task.task_title, Task.task_status)).all()
    for title, status in tasks:
        print(title, status)


    stmt = select(Task.task_title, Task.task_status).order_by(Task.task_title.asc())
    for title, status in session.execute(stmt):
        print(title, status)


    stmt = (
        select(User.user_name, func.count(Task.task_id))
        .join(Task, User.user_id == Task.user_id, isouter=True)
        .group_by(User.user_name)
    )
    for name, count in session.execute(stmt):
        print(name, "|", count)
