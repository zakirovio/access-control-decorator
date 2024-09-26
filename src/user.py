from functools import wraps

from custom_exceptions import PermissionDenied
from settings import current_role

class User:
    def __init__(self, username):
        self.username = username

    def access_control(roles=None):
        roles = roles or ["anonim", "user", "moderator", "admin"]
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if current_role in roles:
                    return func(self, *args, **kwargs)
                else:
                    raise PermissionDenied(f"Access denied with {current_role} role")
            return wrapper
        return decorator
    
    @staticmethod
    def set_user_role(role):
        global current_role
        current_role = role

    @access_control(roles=["admin", "moderator", "user"])
    def get_user_data(self):
        return f"{self.username} data"
    
    @access_control(roles=["admin", "moderator"])
    def get_admin_panel(self):
        return f"{self.username} accessed the admin panel"

    @access_control(roles=["admin"])
    def edit_staff(self):
        return f"{self.username} accessed the staff edit panel"

    @access_control()
    def common_data(self):
        return "Common data"
