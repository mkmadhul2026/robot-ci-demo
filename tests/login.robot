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

*** Keywords ***
Open Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window