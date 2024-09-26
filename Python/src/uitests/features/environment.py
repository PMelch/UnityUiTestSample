import behave.model
import behave.runner


def before_all(context: behave.runner.Context):
    from alttester import AltDriver
    context.alt_driver = AltDriver()
    context.alt_driver.call_static_method("uitest.UiTestInterface",
                                      "BeforeAll", parameters=[], assembly="Assembly-CSharp")


def after_all(context: behave.runner.Context):
    context.alt_driver.call_static_method("uitest.UiTestInterface",
                                      "AfterAll", parameters=[], assembly="Assembly-CSharp")

    if hasattr(context, 'alt_driver'):
        context.alt_driver.stop()


def before_scenario(context: behave.runner.Context, scenario: behave.model.Scenario):
    """
    Use this hook to reset the state of the app between each test scenario.
    Use this to make sure no side-effect of one scenario is bleeding into the
    next scenario.
    This can affect data models, mocks, loaded scenes, etc.
    :param context:
    :param scenario:
    :return:
    """

    if "skip" in scenario.effective_tags:
        scenario.skip("Test has tag: @skip")
        return
    try:
        pass

    except Exception as e:
        print(f"There's a problem connecting to the AltTester device. Exception: {e}")
