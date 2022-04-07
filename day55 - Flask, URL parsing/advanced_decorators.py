
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if kwargs['user'].is_logged_in:
            function(kwargs['user'])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s blog post.")


michal = User('michal')
michal.is_logged_in = True
create_blog_post(user=michal)
