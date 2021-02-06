from page_objects.MainPage import MainPage
from page_objects.AuthorizationPage import AuthorizationPage
from page_objects.TaskCreationPage import TaskCreationPage


def test_creation_with_required_fields_other_category(browser, user_name_valid, password_valid):
    MainPage(browser).go_to_authorization_form()
    AuthorizationPage(browser).authorization(user_name_valid, password_valid)
    MainPage(browser).click_all_projects_button()
    MainPage(browser).choose_mantisbt_project_from_drop_down_list()
    MainPage(browser).go_to_task_creation_page()
    TaskCreationPage(browser).choose_category('o')
    TaskCreationPage(browser).input_summary_into_task_creation_form('test')
    TaskCreationPage(browser).input_description_into_task_creation_form('test_description')
    TaskCreationPage(browser).click_task_creation_button()
    TaskCreationPage(browser).waiting_for_title()
    bug_number = TaskCreationPage(browser).get_number_of_created_task()
    # проверка, что созданная задача выводится в результатах поиска
    MainPage(browser).click_logo()
    MainPage(browser).enter_text_into_search_field(bug_number)
    TaskCreationPage(browser).waiting_for_title()
    assert TaskCreationPage(browser).get_number_of_created_task() == bug_number
