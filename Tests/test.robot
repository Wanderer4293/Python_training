*** Settings ***
Documentation    For an education purposes
Library  ../Libraries/FileLib.py
Resource  ../Settings/Variables.robot
Test Timeout  10

*** Test Cases ***
Simple Test
    [Documentation]  Test to check files
    ...  Check file list
    [Tags]  git
    Files Exist  @{Files}

