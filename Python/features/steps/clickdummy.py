from alttester import By
from behave import *

use_step_matcher("re")


@given(r"the scene (?P<scene_name>\w+) is loaded")
def step_impl(context, scene_name: str):
    """
    This will load a scene by name.
    :param context:
    :param scene_name:
    :return:
    """

    context.alt_driver.load_scene(scene_name)


@when(r"the (?P<button_name>\w+) is clicked")
def step_impl(context, button_name: str):
    """
    This will find a button by name and tap it.
    :param context:
    :param button_name:
    :return:
    """

    obj = context.alt_driver.find_object(By.NAME, button_name)
    obj.tap()


@then(r'the value of (?P<label_name>\w+) should be "(?P<value>[^"]+)"')
def step_impl(context, label_name: str, value: str):
    """
    This will find a label by name and check if the text of
    that label matches the expected value.
    :param context:
    :param label_name:
    :param value:
    :return:
    """

    label = context.alt_driver.find_object(By.NAME, label_name)
    label_text = label.get_text()
    assert label_text == value


@then(r"the view (?P<view_name>\w+) should be (?P<state>active|inactive)")
def step_impl(context, view_name: str, state: str):
    """
    This will find a view by name and check if the active state matches the expected value.
    :param context:
    :param view_name:
    :param state:
    :return:
    """

    view = context.alt_driver.find_object(By.NAME, view_name, enabled=False)
    assert (state == "active" and view.enabled) or \
           (state == "inactive" and not view.enabled)


@given(r"the view (?P<view_name>\w+) is active")
def step_impl(context, view_name: str):
    """
    This will find a view by name and call SetActive(true) on it.
    :param context:
    :param view_name:
    :return:
    """

    view = context.alt_driver.find_object(By.NAME, view_name, enabled=False)

    view.call_component_method(
        component_name="UnityEngine.GameObject",
        method_name="SetActive",
        assembly="UnityEngine.CoreModule",
        parameters=["true"],  # Use "false" to deactivate
        type_of_parameters=["System.Boolean"]
    )
