*** Settings ***

Library    pikvm_comm.py

*** Keywords ***

Write PiKVM
    [Documentation]    Keyword for PiKVM writing into Terminal.
    ...                WARNING: Supports only small characters.
    ...                text - text to be written,
    ...                pikvm_ip - IP of the piKVM to send key input,
    ...                login - piKVM login,
    ...                password - piKVM password
    [Arguments]    ${text}    ${login}=admin    ${password}=admin
    Write Text PiKVM    ${text}    ${pikvm_ip}    ${login}    ${password}
    Single Key PiKVM    Enter    ${pikvm_ip}    ${login}    ${password}

Write Bare PiKVM
    [Documentation]    Keyword for PiKVM writing bare into Terminal.
    ...                WARNING: Supports only small characters.
    ...                text - text to be written,
    ...                pikvm_ip - IP of the piKVM to send key input,
    ...                login - piKVM login,
    ...                password - piKVM password
    [Arguments]    ${text}    ${login}=admin    ${password}=admin
    Write Text PiKVM    ${text}    ${pikvm_ip}    ${login}    ${password}

Single Key PiKVM
    [Documentation]    Send single key via PiKVM.
    ...                key - (str) the key to be pressed,
    ...                pikvm_ip - (str) IP of the piKVM to send key input,
    ...                login - (str) piKVM login,
    ...                password - (str) piKVM password,
    ...                press_time - (float) time the key will remain pressed(s),
    ...                possible keys can be found in `lib/pikvm_comm.py`
    [Arguments]    ${key}    ${login}=admin    ${password}=admin    ${press_time}=0.05
    Send Key PiKVM    ${key}    ${pikvm_ip}    ${login}    ${password}    ${press_time}

Multiple Keys PiKVM
    [Documentation]    Send key series via PiKVM.
    ...                key_list - (list) the keys to be pressed one after another,
    ...                pikvm_ip - (str) IP of the piKVM to send key input,
    ...                login - (str) piKVM login
    ...                password - (str) piKVM password
    ...                press_time - (float) time the key will remain pressed(s),
    ...                possible keys can be found in `lib/pikvm_comm.py`
    [Arguments]    ${key_list}    ${login}=admin    ${password}=admin    ${press_time}=0.05
    Send Key Series PiKVM    ${key_list}    ${pikvm_ip}    ${login}    ${password}    ${press_time}

Key Combination PiKVM
    [Documentation]    Send key combination via PiKVM.
    ...                key_list - (list) the key to be pressed simultaneously,
    ...                pikvm_ip - (str) IP of the piKVM to send key input,
    ...                login - (str) piKVM login,
    ...                password - (str) piKVM password,
    ...                press_time - (float) time the key will remain pressed(s),
    ...                possible keys can be found in `lib/pikvm_comm.py`
    [Arguments]    ${key}    ${login}=admin    ${password}=admin    ${press_time}=0.05
    Send Key Combination PiKVM    ${key_list}    ${pikvm_ip}    ${login}    ${password}    ${press_time}

Check if iso image is present
    [Documentation]    Checks if image with name ${image_name} exists.
    ...                Returns True/False
    [Arguments]    ${image_name}    ${pikvm_ip}
    ${result}=    Iso image present    ${image_name}    ${pikvm_ip}
    [Return]    ${result}

Upload iso image
    [Documentation]    Uploads given iso image (${path_to_image}) and saves it
    ...                as ${image_name}
    [Arguments]    ${image_name}    ${path_to_image}    ${pikvm_ip}
    ${res}=    Upload image    ${image_name}    ${path_to_image}    ${pikvm_ip}
    [Return]    ${res}

Mount iso image
    [Documentation]    Mounts given iso image to CD-ROM. Assumes that
    ...                ${image_name} is already uploaded.
    [Arguments]    ${image_name}    ${pikvm_ip}    ${login}=admin    ${password}=admin
    Iso image mount    ${image_name}    ${pikvm_ip}    ${login}    ${password}
