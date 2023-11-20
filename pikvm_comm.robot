*** Settings ***
Documentation       This library exposes PiKVM REST API as RF keywords

Library             pikvm_comm.py


*** Keywords ***
Write PiKVM
    [Documentation]    Keyword for PiKVM writing into Terminal.
    ...    WARNING: Supports only small characters.
    ...    text - text to be written,
    ...    pikvm_ip - IP of the piKVM to send key input,
    ...    login - piKVM login,
    ...    password - piKVM password
    [Arguments]    ${text}    ${login}=admin    ${password}=admin    ${press_time}=0.1
    Write Text PiKVM    ${text}    ${PIKVM_IP}    ${login}    ${password}    ${press_time}
    Single Key PiKVM    Enter    ${login}    ${password}    ${press_time}

Write Bare PiKVM
    [Documentation]    Keyword for PiKVM writing bare into Terminal.
    ...    WARNING: Supports only small characters.
    ...    text - text to be written,
    ...    pikvm_ip - IP of the piKVM to send key input,
    ...    login - piKVM login,
    ...    password - piKVM password
    [Arguments]    ${text}    ${login}=admin    ${password}=admin
    Write Text PiKVM    ${text}    ${PIKVM_IP}    ${login}    ${password}

Single Key PiKVM
    [Documentation]    Send single key via PiKVM.
    ...    key - (str) the key to be pressed,
    ...    pikvm_ip - (str) IP of the piKVM to send key input,
    ...    login - (str) piKVM login,
    ...    password - (str) piKVM password,
    ...    press_time - (float) time the key will remain pressed(s),
    ...    possible keys can be found in `lib/pikvm_comm.py`
    [Arguments]    ${key}    ${login}=admin    ${password}=admin    ${press_time}=0.2
    Send Key PiKVM    ${key}    ${PIKVM_IP}    ${login}    ${password}    ${press_time}

Multiple Keys PiKVM
    [Documentation]    Send key series via PiKVM.
    ...    key_list - (list) the keys to be pressed one after another,
    ...    pikvm_ip - (str) IP of the piKVM to send key input,
    ...    login - (str) piKVM login
    ...    password - (str) piKVM password
    ...    press_time - (float) time the key will remain pressed(s),
    ...    possible keys can be found in `lib/pikvm_comm.py`
    [Arguments]    ${key_list}    ${login}=admin    ${password}=admin    ${press_time}=0.1
    Send Key Series PiKVM    ${key_list}    ${PIKVM_IP}    ${login}    ${password}    ${press_time}

Key Combination PiKVM
    [Documentation]    Send key combination via PiKVM.
    ...    key_list - (list) the key to be pressed simultaneously,
    ...    pikvm_ip - (str) IP of the piKVM to send key input,
    ...    login - (str) piKVM login,
    ...    password - (str) piKVM password,
    ...    press_time - (float) time the key will remain pressed(s),
    ...    possible keys can be found in `lib/pikvm_comm.py`
    [Arguments]    ${key_list}    ${login}=admin    ${password}=admin    ${press_time}=0.2
    Send Key Combination PiKVM    ${key_list}    ${PIKVM_IP}    ${login}    ${password}    ${press_time}

Mount Image On PiKVM
    [Documentation]    Mounts the image with the given name on the PiKVM.
    ...    login - (str) piKVM login,
    ...    password - (str) piKVM password,
    ...    pikvm_ip - (str) IP of the piKVM to mount the image on,
    ...    img_name - (str) URL of the image to be mounted
    [Arguments]    ${pikvm_ip}    ${img_name}    ${login}=admin    ${password}=admin
    Mount Image PiKVM    ${pikvm_ip}    ${img_name}    ${login}    ${password}

Upload Image To PiKVM
    [Documentation]    Mounts the image from the given URL on the PiKVM.
    ...    login - (str) piKVM login,
    ...    password - (str) piKVM password,
    ...    pikvm_ip - (str) IP of the piKVM to mount the image on,
    ...    img_url - (str) URL of the image to be mounted
    [Arguments]    ${pikvm_ip}    ${img_url}    ${img_name}    ${login}=admin    ${password}=admin
    Upload Image PiKVM    ${pikvm_ip}    ${img_url}    ${img_name}    ${login}    ${password}
