try:
    import ssl
    import time

    import websocket
    from robot.api.deco import keyword

    ROBOT = False
except Exception:
    ROBOT = False


@keyword("Send Key PiKVM")
def SendKeyPiKVM(
    key=str, pikvm_ip=str, login="admin", password="admin", press_time=0.2
):
    """
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
    """

    uri = f"wss://{pikvm_ip}/api/ws?stream=0"
    headers = {"X-KVMD-User": login, "X-KVMD-Passwd": password}
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})

    ws.connect(uri, header=headers)
    ws.send('{"event_type": "key", "event": {"key": "' + key + '", "state": true}}')
    time.sleep(float(press_time))
    ws.send('{"event_type": "key", "event": {"key": "' + key + '", "state": false}}')
    time.sleep(float(press_time))
    ws.close()


@keyword("Send Key Combination PiKVM")
def SendKeyCombinationPiKVM(
    key_list=list, pikvm_ip=str, login="admin", password="admin", press_time=0.5
):
    """
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
    """

    uri = f"wss://{pikvm_ip}/api/ws?stream=0"
    headers = {"X-KVMD-User": login, "X-KVMD-Passwd": password}
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})

    ws.connect(uri, header=headers)
    for key in key_list:
        ws.send('{"event_type": "key", "event": {"key": "' + key + '", "state": true}}')
        time.sleep(float(press_time))

    for key in key_list:
        ws.send(
            '{"event_type": "key", "event": {"key": "' + key + '", "state": false}}'
        )
    ws.close()


@keyword("Send Key Series PiKVM")
def SendKeySeriesPiKVM(
    key_list=list, pikvm_ip=str, login="admin", password="admin", press_time=0.2
):
    """
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
    """

    uri = f"wss://{pikvm_ip}/api/ws?stream=0"
    headers = {"X-KVMD-User": login, "X-KVMD-Passwd": password}
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})

    ws.connect(uri, header=headers)
    for key in key_list:
        ws.send('{"event_type": "key", "event": {"key": "' + key + '", "state": true}}')
        time.sleep(float(press_time))
        ws.send(
            '{"event_type": "key", "event": {"key": "' + key + '", "state": false}}'
        )
        time.sleep(float(press_time))
    ws.close()


@keyword("Write Text PiKVM")
def WriteTextPiKVM(
    text=str, pikvm_ip=str, login="admin", password="admin", press_time=0.2
):
    """
    WARNING: Supports only small characters.
    ---\n
    text - text to be written,\n
    pikvm_ip - IP of the piKVM to send key input,\n
    login - piKVM login\n
    password - piKVM password\n
    """
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
        "\n": "Enter",
    }

    shift_keymap = {
        "A": "KeyA",
        "B": "KeyB",
        "C": "KeyC",
        "D": "KeyD",
        "E": "KeyE",
        "F": "KeyF",
        "G": "KeyG",
        "H": "KeyH",
        "I": "KeyI",
        "J": "KeyJ",
        "K": "KeyK",
        "L": "KeyL",
        "M": "KeyM",
        "N": "KeyN",
        "O": "KeyO",
        "P": "KeyP",
        "Q": "KeyQ",
        "R": "KeyR",
        "S": "KeyS",
        "T": "KeyT",
        "U": "KeyU",
        "V": "KeyV",
        "W": "KeyW",
        "X": "KeyX",
        "Y": "KeyY",
        "Z": "KeyZ",
        "!": "Digit1",
        "@": "Digit2",
        "#": "Digit3",
        "$": "Digit4",
        "%": "Digit5",
        "^": "Digit6",
        "&": "Digit7",
        "*": "Digit8",
        "(": "Digit9",
        ")": "Digit0",
        "_": "Minus",
        "+": "Equal",
        "\{": "BracketLeft",
        "\}": "BracketRight",
        "|": "Backslash",
        ":": "Semicolon",
        '"': "Quote",
        "~": "Backquote",
        "<": "Comma",
        ">": "Period",
        "?": "Slash",
    }

    char_list = list(text)

    uri = f"wss://{pikvm_ip}/api/ws?stream=0"
    headers = {"X-KVMD-User": login, "X-KVMD-Passwd": password}
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})

    ws.connect(uri, header=headers)
    for char in char_list:
        if char in shift_keymap:
            ws.send(
                '{"event_type": "key", "event": {"key": "ShiftRight", "state": true} }'
            )
            time.sleep(float(press_time))
            ws.send(
                '{"event_type": "key", "event": {"key": "'
                + shift_keymap[char]
                + '", "state": true} }'
            )
            time.sleep(float(press_time))
            ws.send(
                '{"event_type": "key", "event": {"key": "'
                + shift_keymap[char]
                + '", "state": false} }'
            )
            ws.send(
                '{"event_type": "key", "event": {"key": "ShiftRight", "state": false} }'
            )
        else:
            ws.send(
                '{"event_type": "key", "event": {"key": "'
                + keymap[char]
                + '", "state": true} }'
            )
            time.sleep(float(press_time))
            ws.send(
                '{"event_type": "key", "event": {"key": "'
                + keymap[char]
                + '", "state": false} }'
            )

    ws.close()
