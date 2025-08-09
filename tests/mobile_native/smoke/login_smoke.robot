*** Settings ***
Library    AppiumLibrary
Resource   ../../../resources/keywords/auth.robot
Resource   ../../../resources/locators/login_android.robot
Suite Setup     Open Android App (BS Aware)
Suite Teardown  Close Application
Test Teardown   Run Keyword If Test Failed    Log Source

*** Test Cases ***
Login happy path (Android)
    [Tags]    smoke    android    critical
    Login With Credentials    demo@site.com    123456
