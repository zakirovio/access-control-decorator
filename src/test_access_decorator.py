import pytest

from custom_exceptions import PermissionDenied
from user import User


def test_get_user_data():
    user = User("test_user")
    user.set_user_role("user")
    assert user.get_user_data() == "test_user data"

def test_get_admin_panel_as_admin():
    admin = User("admin_user")
    admin.set_user_role("admin")
    assert admin.get_admin_panel() == "admin_user accessed the admin panel"

def test_get_admin_panel_as_user():
    user = User("test_user")
    user.set_user_role("user")
    with pytest.raises(PermissionDenied):
        user.get_admin_panel()

def test_edit_staff_as_admin():
    admin = User("admin_user")
    admin.set_user_role("admin")
    assert admin.edit_staff() == "admin_user accessed the staff edit panel"

def test_edit_staff_as_moderator():
    moderator = User("moderator_user")
    moderator.set_user_role("moderator")
    with pytest.raises(PermissionDenied):
        moderator.edit_staff()

def test_common_data_for_all():
    user = User("anonim")
    assert user.common_data() == "Common data"
    
    admin = User("admin_user")
    admin.set_user_role("admin")
    assert admin.common_data() == "Common data"

    moderator = User("moderator_user")
    moderator.set_user_role("moderator")
    assert moderator.common_data() == "Common data"

    user = User("test_user")
    user.set_user_role("user")
    assert moderator.common_data() == "Common data"
