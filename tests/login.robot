*** Settings ***
Library    SeleniumLibrary
Suite Setup       Open Login Page
Suite Teardown    Close All Browsers

*** Variables ***
${URL}       https://www.saucedemo.com/
${BROWSER}   chrome
${USERNAME}  standard_user
${PASSWORD}  secret_sauce

*** Test Cases ***
Valid Login
    Input Text    id=user-name    ${USERNAME}
    Input Text    id=password     ${PASSWORD}
    Click Button  id=login-button
    Wait Until Page Contains    Products
    Page Should Contain    Products

Invalid Login
    Wait Until Page Contains Element    id=user-name   10s
    Input Text    id=user-name    invalid_user
    Wait Until Page Contains Element    id=password    10s
    Input Text    id=password     invalid_password
    Click Button  id=login-button
    Wait Until Page Contains Element    css=.error-message-container
    Element Should Contain    css=.error-message-container    Epic sadface: Username and password do not match any user in this service

*** Keywords ***
Open Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window