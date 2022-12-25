from pages.settings.groups_page import GroupsPage
from tests.base_test import BaseTest

class TestGroups(BaseTest):
    def test_create_new_group(self):
        groups_obj=GroupsPage(self.driver)
        group_name=groups_obj.get_group_name()
        print(f"group name:{group_name}")
        groups_obj.create_new_group(group_name)
        result=groups_obj.check_if_group_exist(group_name)
        assert result == True

    def test_add_new_user_to_group(self):
        groups_obj=GroupsPage(self.driver)
        user_name, group_name="Ilya test user 1", "ilya3"
        groups_obj.add_new_user_for_group(group_name, user_name)
        result=groups_obj.check_user_in_group(user_name)
        assert result == True


