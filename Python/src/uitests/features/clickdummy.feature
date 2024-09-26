# Created by pmelc at 21.09.22
Feature: Clickdummy
  test that the buttons in the Clickdummy scene serve their purpose

  Background:
    Given the scene ClickDummy is loaded

  Scenario: A click on the Val1 button should set the label value to "Val1"
    When the SetVal1Button is clicked
    Then the value of Label should be "Val1"

  Scenario: A click on the Val2 button should set the label value to "Val2"
    When the SetVal2Button is clicked
    Then the value of Label should be "Val2"

  Scenario: A click on the OpenPanel button should show the panel
    When the OpenPanelButton is clicked
    Then the view Panel should be active

  Scenario: A click on the CloseButton in the panel should close the panel
    Given the view Panel is active
    When the CloseButton is clicked
    Then the view Panel should be inactive
