# Unity UiTest Sample Setup
__Version: 1.0.0__

A Unity6 sample project to demonstrate how to write UI tests using Gherkin Syntax.

Tested with Unity version: Unity6 (6000.0.19f1).

Requires Python >= 3.8
![VideoThumbnail](https://github.com/PMelch/UnityUiTestSample/main/UiTestSampleSetup1024.mp4)

## Project Overview
This project showcases a robust approach to UI testing leveraging the Gherkin syntax, Behave framework, and AltTester. It provides a comprehensive solution for automating UI tests in a structured and maintainable manner.

A sample test case writting Gherking could look like this:

```Gherkin
Feature: Account Menu
  With the account menu open, users can manage their data related to their account and log out their user.

  Background:
    Given user Test1 is logged in
    And the lobby page is shown
    And the AccountMenu has been opened

  Scenario: A click on the change password menu entry shows the change-pw dialog
    When the user clicks the "Change Password" button
    Then the "Change Password" page is shown

  Scenario: A click on the logout menu entry will end the user session and forward to the log-in page
    When the user clicks the "Logout" button
    Then no user is logged in
    And the "Login" page is shown
``` 

### Key Components and Workflow

- Gherkin: A human-readable language for describing test scenarios in a natural language format.
- Behave: A Python BDD framework that parses Gherkin features and executes the corresponding test steps.
- AltTester: A cross-platform tool for automating UI testing in Unity applications.

### Test Execution Flow
- Gherkin Feature Files: Test scenarios are defined in Gherkin feature files, using a Given-When-Then structure.
- Behave Framework: Behave reads the feature files and converts them into executable test cases.
- AltTester Driver: The test step implementations within Behave utilize the AltTester driver to establish a connection with the AltTesterDesktop application.
- AltTesterDesktop: This desktop application acts as a bridge between the test scripts and the Unity application.
- Unity Integration: The AltTester package is integrated into the Unity project, enabling communication with AltTesterDesktop.
- Command Execution: AltTesterDesktop receives commands from the test scripts and forwards them to the Unity application for execution.

### Benefits of This Approach
- Readability: Gherkin's natural language syntax makes test cases easy to understand for both technical and non-technical stakeholders.
- Maintainability: The separation of concerns between test scenarios, step definitions, and driver implementation enhances code maintainability.
- Automation: AltTester's automation capabilities enable efficient and reliable testing.
- Flexibility: The AltTesterDesktop acts as a flexible intermediary, allowing for customization and integration with other tools.

## Prerequisites
- Python >= 3.8 installation
- pipenv (Installation instructions: https://pipenv.pypa.io/en/latest/installation.html)
- AltTesterDesktop application (download from https://alttester.com/downloads)

## Get Started
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Change directory to the Python folder
4. run `pipenv install` to install the required packages.
5. Open the AltTesterDesktop application
5. In Unity, open the Scenes/TestingStart scene and hit play - you should see now in the AltTesterDesktop application that the app has connected
6. In the Python folder, run `pipenv run python src/main.py` to execute the test scenarios.
