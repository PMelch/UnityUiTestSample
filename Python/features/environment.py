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
        # the BeforeTestScene should reset all necessary mocks and internal states
        # so that each test can run independently of all previous tests.
        # This scene should stop all async operations that were started in previous test cases,
        # reset internal data models and remove other components that could
        # be leftovers from the previous test case.
        context.alt_driver.load_scene('Scenes/BeforeEachTest')

    except Exception as e:
        print(f"There's a problem connecting to the AltTester device. Exception: {e}")
