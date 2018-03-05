*** Settings ***
Documentation    For an education purposes
Library          FileLib


*** Test Cases ***
Simple Test
    [Tags]  git
    ${files} =  Create List  settings.xml   plotter.ini
    Files Exist  ${files}

