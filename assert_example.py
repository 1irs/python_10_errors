class Rect:

    def __init__(self, a, b):
        assert a > 0 and b > 0
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b) * 2

    def scale(self, factor: float):
        assert factor > 0
        self.a = self.a * factor
        self.b = self.b * factor


#try:
r1 = Rect(2.0, 5.0)
print(f"Perimter r1 = {r1.perimeter()}")

r2 = Rect(0.0, -2.0)
print(f"Perimter r2 = {r2.perimeter()}")
#except AssertionError:
#    print('Увы, какое-то из ограничений assert не выполняется')



def signin_with_user(username, password):
    assert len(username) > 0
    print( f"signed in with {username}")

signin_with_user("vova", "")
#signin_with_user("", "asdf")


def signin_with_user_2(username, password):
    if len(username) == 0:
        raise ValueError('Имя username не может быть пустым')
    print( f"signed in with {username}")


#signin_with_user_2("", "asdf")


def generate_profile_for_user():
    raise NotImplementedError('Пока что вводите данные вручную. Вернусь из отпуска — допишу. :)')
    pass

generate_profile_for_user()