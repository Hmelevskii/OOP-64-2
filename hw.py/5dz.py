import time #Модуль к ДЗ 2

# Задание 1
def is_admin(func):
        def wrapper(user):
            if user.role == "admin":
                return func(user)
            else:
                print('У вас нет доступа')
        return wrapper

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

@is_admin
def delete_video(user):
        print('Видео удалено')

admin = User("Ardager", "admin")
user = User("Bek", "user")
delete_video(admin)
delete_video(user)

# задание 2
def timer(func):
    def wrapper():
        start = time.time()
        func()
        stop = time.time()
        print(f'Время выполнения: {round(stop - start, 1)} ceкунд')
    return wrapper
@timer
def download_video():
     time.sleep(2)
     print('Видео загружено')

download_video()

