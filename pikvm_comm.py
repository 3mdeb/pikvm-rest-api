try:
    import websocket
    import time
    import ssl
    import json
    from websocket import WebSocketBadStatusException
    import requests
    from robot.api.deco import keyword
    ROBOT = False
except Exception:
    ROBOT = False

@keyword("Send Key PiKVM")
def SendKeyPiKVM(key=str, pikvm_ip=str, login="admin", password="admin", press_time=0.2):
    '''
    key - the key to be pressed,\n
    pikvm_ip - IP of the piKVM to send key input,\n
    login - piKVM login\n
    password - piKVM password\n
    press_time - time the key will remain pressed (in seconds)\n
    ---\n
    Possible keys:\n
    'KeyA', 'KeyB', 'KeyC', 'KeyD', 'KeyE', 'KeyF', 'KeyG', 'KeyH',\n
    'KeyI', 'KeyJ', 'KeyK', 'KeyL', 'KeyM', 'KeyN', 'KeyO', 'KeyP', 'KeyQ',\n
    'KeyR', 'KeyS', 'KeyT', 'KeyU', 'KeyV', 'KeyW', 'KeyX', 'KeyY', 'KeyZ',\n
    'Digit1', 'Digit2', 'Digit3', 'Digit4', 'Digit5', 'Digit6', 'Digit7',\n
    'Digit8', 'Digit9', 'Digit0', 'Enter', 'Escape', 'Backspace', 'Tab',\n
    'Space', 'Minus', 'Equal', 'BracketLeft', 'BracketRight', 'Backslash',\n
    'Semicolon', 'Quote', 'Backquote', 'Comma', 'Period', 'Slash', 'CapsLock',\n
    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',\n
    'PrintScreen', 'Insert', 'Home', 'PageUp', 'Delete', 'End', 'PageDown',\n
    'ArrowRight', 'ArrowLeft', 'ArrowDown', 'ArrowUp', 'ControlLeft', 'ShiftLeft',\n
    'AltLeft', 'MetaLeft', 'ControlRight', 'ShiftRight', 'AltRight',\n
    'MetaRight', 'Pause', 'ScrollLock', 'NumLock', 'ContextMenu',\n
    'NumpadDivide', 'NumpadMultiply', 'NumpadSubtract', 'NumpadAdd',\n
    'NumpadEnter', 'Numpad1', 'Numpad2', 'Numpad3', 'Numpad4', 'Numpad5',\n
    'Numpad6', 'Numpad7', 'Numpad8', 'Numpad9', 'Numpad0', 'NumpadDecimal',\n
    'Power', 'IntlBackslash', 'IntlYen'
    '''

    uri = f"wss://{pikvm_ip}/api/ws?stream=0"
    headers = {"X-KVMD-User": login, "X-KVMD-Passwd": password}
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})

    ws.connect(uri, header=headers)
    ws.send('{"event_type": "key", "event": {"key": "' + key + '", "state": true}}')
    time.sleep(float(press_time))
    ws.send('{"event_type": "key", "event": {"key": "' + key + '", "state": false}}')
    ws.close()

@keyword("Send Key Combination PiKVM")
def SendKeyCombinationPiKVM(key_list=list, pikvm_ip=str, login="admin", password="admin", press_time=0.5):
    '''
    key_list - list of keys to be pressed at once,\n
    pikvm_ip - IP of the piKVM to send key input,\n
    login - piKVM login\n
    password - piKVM password\n
    press_time - time the all keys will remain pressed (in seconds)\n
    ---\n
    Possible keys:\n
    'KeyA', 'KeyB', 'KeyC', 'KeyD', 'KeyE', 'KeyF', 'KeyG', 'KeyH',\n
    'KeyI', 'KeyJ', 'KeyK', 'KeyL', 'KeyM', 'KeyN', 'KeyO', 'KeyP', 'KeyQ',\n
    'KeyR', 'KeyS', 'KeyT', 'KeyU', 'KeyV', 'KeyW', 'KeyX', 'KeyY', 'KeyZ',\n
    'Digit1', 'Digit2', 'Digit3', 'Digit4', 'Digit5', 'Digit6', 'Digit7',\n
    'Digit8', 'Digit9', 'Digit0', 'Enter', 'Escape', 'Backspace', 'Tab',\n
    'Space', 'Minus', 'Equal', 'BracketLeft', 'BracketRight', 'Backslash',\n
    'Semicolon', 'Quote', 'Backquote', 'Comma', 'Period', 'Slash', 'CapsLock',\n
    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',\n
    'PrintScreen', 'Insert', 'Home', 'PageUp', 'Delete', 'End', 'PageDown',\n
    'ArrowRight', 'ArrowLeft', 'ArrowDown', 'ArrowUp', 'ControlLeft', 'ShiftLeft',\n
    'AltLeft', 'MetaLeft', 'ControlRight', 'ShiftRight', 'AltRight',\n
    'MetaRight', 'Pause', 'ScrollLock', 'NumLock', 'ContextMenu',\n
    'NumpadDivide', 'NumpadMultiply', 'NumpadSubtract', 'NumpadAdd',\n
    'NumpadEnter', 'Numpad1', 'Numpad2', 'Numpad3', 'Numpad4', 'Numpad5',\n
    'Numpad6', 'Numpad7', 'Numpad8', 'Numpad9', 'Numpad0', 'NumpadDecimal',\n
    'Power', 'IntlBackslash', 'IntlYen'
    '''

    uri = f"wss://{pikvm_ip}/api/ws?stream=0"
    headers = {"X-KVMD-User": login, "X-KVMD-Passwd": password}
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})

    ws.connect(uri, header=headers)
    for key in key_list:
        ws.send('{"event_type": "key", "event": {"key": "' + key + '", "state": true}}')
        time.sleep(float(press_time))

    for key in key_list:
        ws.send('{"event_type": "key", "event": {"key": "' + key + '", "state": false}}')
    ws.close()

@keyword("Send Key Series PiKVM")
def SendKeySeriesPiKVM(key_list=list, pikvm_ip=str, login="admin", password="admin", press_time=0.2):
    '''
    key_list - list of keys to be pressed one after another,\n
    pikvm_ip - IP of the piKVM to send key input,\n
    login - piKVM login\n
    password - piKVM password\n
    press_time - time the every key will remain pressed (in seconds)\n
    ---\n
    Possible keys:\n
    'KeyA', 'KeyB', 'KeyC', 'KeyD', 'KeyE', 'KeyF', 'KeyG', 'KeyH',\n
    'KeyI', 'KeyJ', 'KeyK', 'KeyL', 'KeyM', 'KeyN', 'KeyO', 'KeyP', 'KeyQ',\n
    'KeyR', 'KeyS', 'KeyT', 'KeyU', 'KeyV', 'KeyW', 'KeyX', 'KeyY', 'KeyZ',\n
    'Digit1', 'Digit2', 'Digit3', 'Digit4', 'Digit5', 'Digit6', 'Digit7',\n
    'Digit8', 'Digit9', 'Digit0', 'Enter', 'Escape', 'Backspace', 'Tab',\n
    'Space', 'Minus', 'Equal', 'BracketLeft', 'BracketRight', 'Backslash',\n
    'Semicolon', 'Quote', 'Backquote', 'Comma', 'Period', 'Slash', 'CapsLock',\n
    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12',\n
    'PrintScreen', 'Insert', 'Home', 'PageUp', 'Delete', 'End', 'PageDown',\n
    'ArrowRight', 'ArrowLeft', 'ArrowDown', 'ArrowUp', 'ControlLeft', 'ShiftLeft',\n
    'AltLeft', 'MetaLeft', 'ControlRight', 'ShiftRight', 'AltRight',\n
    'MetaRight', 'Pause', 'ScrollLock', 'NumLock', 'ContextMenu',\n
    'NumpadDivide', 'NumpadMultiply', 'NumpadSubtract', 'NumpadAdd',\n
    'NumpadEnter', 'Numpad1', 'Numpad2', 'Numpad3', 'Numpad4', 'Numpad5',\n
    'Numpad6', 'Numpad7', 'Numpad8', 'Numpad9', 'Numpad0', 'NumpadDecimal',\n
    'Power', 'IntlBackslash', 'IntlYen'
    '''

    uri = f"wss://{pikvm_ip}/api/ws?stream=0"
    headers = {"X-KVMD-User": login, "X-KVMD-Passwd": password}
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})

    ws.connect(uri, header=headers)
    for key in key_list:
        ws.send('{"event_type": "key", "event": {"key": "' + key + '", "state": true}}')
        time.sleep(float(press_time))
        ws.send('{"event_type": "key", "event": {"key": "' + key + '", "state": false}}')
    ws.close()

@keyword("Write Text PiKVM")
def WriteTextPiKVM(text=str, pikvm_ip=str, login="admin", password="admin"):
    '''
    WARNING: Supports only small characters.
    ---\n
    text - text to be written,\n
    pikvm_ip - IP of the piKVM to send key input,\n
    login - piKVM login\n
    password - piKVM password\n
    '''
    keymap = {
        "a": "KeyA",
        "b": "KeyB",
        "c": "KeyC",
        "d": "KeyD",
        "e": "KeyE",
        "f": "KeyF",
        "g": "KeyG",
        "h": "KeyH",
        "i": "KeyI",
        "j": "KeyJ",
        "k": "KeyK",
        "l": "KeyL",
        "m": "KeyM",
        "n": "KeyN",
        "o": "KeyO",
        "p": "KeyP",
        "q": "KeyQ",
        "r": "KeyR",
        "s": "KeyS",
        "t": "KeyT",
        "u": "KeyU",
        "v": "KeyV",
        "w": "KeyW",
        "x": "KeyX",
        "y": "KeyY",
        "z": "KeyZ",
        "1": "Digit1",
        "2": "Digit2",
        "3": "Digit3",
        "4": "Digit4",
        "5": "Digit5",
        "6": "Digit6",
        "7": "Digit7",
        "8": "Digit8",
        "9": "Digit9",
        "0": "Digit0",
        " ": "Space",
        "-": "Minus",
        "=": "Equal",
        "[": "BracketLeft",
        "]": "BracketRight",
        "\\": "Backslash",
        ";": "Semicolon",
        "'": "Quote",
        "`": "Backquote",
        ",": "Comma",
        ".": "Period",
        "/": "Slash",
        "*": "NumpadMultiply",
        "+": "NumpadAdd",
    }

    char_list = list(text.lower())

    uri = f"wss://{pikvm_ip}/api/ws?stream=0"
    headers = {"X-KVMD-User": login, "X-KVMD-Passwd": password}
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})

    ws.connect(uri, header=headers)
    for char in char_list:
        ws.send('{"event_type": "key", "event": {"key": "' + keymap[char] + '", "state": true}}')
        time.sleep(0.2)
        ws.send('{"event_type": "key", "event": {"key": "' + keymap[char] + '", "state": false}}')
    ws.close()

@keyword("Iso image present")
def iso_image_present(image_name, pikvm_ip=str, login="admin", password="admin"):
    """
    image_name - name of the iso image to be found
    pikvm_ip - IP of the piKVM to send key input,\n
    login - piKVM login\n
    password - piKVM password\n
    """
    images = get_all_images(pikvm_ip, login, password)
    return image_name in images

@keyword("Upload image")
def upload_image(image_name, path_to_image, pikvm_ip, login="admin", password="admin"):
    url = f"https://{pikvm_ip}/api/msd/write?image={image_name}"

    with open(path_to_image, "rb") as iso_file:
        binary_data = iso_file.read()

    headers = {"X-KVMD-User": login, "X-KVMD-Passwd": password}

    response = requests.post(url, data=binary_data, headers=headers, verify=False)
    return response

def get_all_images(pikvm_ip, login, password):
    url = f"https://{pikvm_ip}/api/msd"
    headers = {"X-KVMD-User": login, "X-KVMD-Passwd": password}

    response = requests.get(url, headers=headers, verify=False)

    parsed_json = json.loads(response.content)

    return parsed_json["result"]["storage"]["images"].keys()

@keyword("Iso image mount")
def iso_image_mount(image_name, pikvm_ip, login, password):
    url = f"https://{pikvm_ip}/api/msd/set_params?image={image_name}&cdrom=1"

    headers = {"X-KVMD-User": login, "X-KVMD-Passwd": password}

    response = requests.post(url, headers=headers, verify=False)
    return response
