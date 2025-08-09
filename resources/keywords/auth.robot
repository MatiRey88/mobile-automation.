*** Settings ***
Library    AppiumLibrary
Library    OperatingSystem
Library    Collections

*** Keywords ***
Open Android App (BS Aware)
    ${cfg}=    Evaluate    __import__('yaml').safe_load(open('configs/appium_android.yaml','r'))
    ${remote}=    Set Variable If    ${cfg['bstack']}==True    https://${BS_USERNAME}:${BS_ACCESS_KEY}@hub.browserstack.com/wd/hub    http://127.0.0.1:4723/wd/hub
    ${caps}=    Evaluate    dict([(k,v) for k,v in ${cfg}.items() if k not in ['bstack','bstack_caps']])
    ${opts}=    Evaluate    dict(**${caps}, **${cfg}.get('bstack_caps', {}))
    Open Application    ${remote}    ${opts}

Login With Credentials
    [Arguments]    ${user}    ${pass}
    Wait Until Element Is Visible    ${USER_FIELD}    15s
    Input Text    ${USER_FIELD}    ${user}
    Input Text    ${PASS_FIELD}    ${pass}
    Click Element    ${LOGIN_BTN}
    Wait Until Element Is Visible    ${HOME_TITLE}    15s
