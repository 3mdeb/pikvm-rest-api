import logging
import ssl
import time
import warnings

import requests
import websocket
from robot.api.deco import keyword

warnings.filterwarnings("ignore")

logging.basicConfig(level=logging.DEBUG)


class PiKVMClient:
    VALID_KEYS = [
        "KeyA",
        "KeyB",
        "KeyC",
        "KeyD",
        "KeyE",
        "KeyF",
        "KeyG",
        "KeyH",
        "KeyI",
        "KeyJ",
        "KeyK",
        "KeyL",
        "KeyM",
        "KeyN",
        "KeyO",
        "KeyP",
        "KeyQ",
        "KeyR",
        "KeyS",
        "KeyT",
        "KeyU",
        "KeyV",
        "KeyW",
        "KeyX",
        "KeyY",
        "KeyZ",
        "Digit1",
        "Digit2",
        "Digit3",
        "Digit4",
        "Digit5",
        "Digit6",
        "Digit7",
        "Digit8",
        "Digit9",
        "Digit0",
        "Enter",
        "Escape",
        "Backspace",
        "Tab",
        "Space",
        "Minus",
        "Equal",
        "BracketLeft",
        "BracketRight",
        "Backslash",
        "Semicolon",
        "Quote",
        "Backquote",
        "Comma",
        "Period",
        "Slash",
        "CapsLock",
        "F1",
        "F2",
        "F3",
        "F4",
        "F5",
        "F6",
        "F7",
        "F8",
        "F9",
        "F10",
        "F11",
        "F12",
        "PrintScreen",
        "Insert",
        "Home",
        "PageUp",
        "Delete",
        "End",
        "PageDown",
        "ArrowRight",
        "ArrowLeft",
        "ArrowDown",
        "ArrowUp",
        "ControlLeft",
        "ShiftLeft",
        "AltLeft",
        "MetaLeft",
        "ControlRight",
        "ShiftRight",
        "AltRight",
        "MetaRight",
        "Pause",
        "ScrollLock",
        "NumLock",
        "ContextMenu",
        "NumpadDivide",
        "NumpadMultiply",
        "NumpadSubtract",
        "NumpadAdd",
        "NumpadEnter",
        "Numpad1",
        "Numpad2",
        "Numpad3",
        "Numpad4",
        "Numpad5",
        "Numpad6",
        "Numpad7",
        "Numpad8",
        "Numpad9",
        "Numpad0",
        "NumpadDecimal",
        "Power",
        "IntlBackslash",
        "IntlYen",
    ]

    def __init__(self, pikvm_ip, login="admin", password="admin"):
        self.pikvm_ip = pikvm_ip
        self.login = login
        self.password = password
        self.ws_uri = f"wss://{self.pikvm_ip}/api/ws?stream=0"
        self.http_headers = {"X-KVMD-User": self.login, "X-KVMD-Passwd": self.password}

    def _connect_websocket(self):
        try:
            logging.debug(f"Connecting to WebSocket at {self.ws_uri}")
            ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
            ws.connect(self.ws_uri, header=self.http_headers)
            return ws
        except Exception as e:
            logging.error(f"Error connecting to WebSocket: {e}")
            raise

    def _validate_key(self, key):
        """Common internal validation function for checking if the key is valid."""
        if key not in self.VALID_KEYS:
            logging.warning(f"Invalid key: {key}")
            return False
        return True

    @keyword("Single Key PiKVM")
    def send_key(self, key, press_time=0.2):
        """
        key - the key to be pressed,
        press_time - time the key will remain pressed (in seconds)
        """
        if not self._validate_key(key):
            logging.warning(f"Invalid key: {key}")
            return False
        ws = self._connect_websocket()
        ws.send(f'{{"event_type": "key", "event": {{"key": "{key}", "state": true}}}}')
        time.sleep(press_time)
        ws.send(f'{{"event_type": "key", "event": {{"key": "{key}", "state": false}}}}')
        time.sleep(press_time)
        ws.close()

    @keyword("Key Combination PiKVM")
    def send_key_combination(self, key_list, press_time=0.5):
        """
        key_list - list of keys to be pressed at once,
        press_time - time the all keys will remain pressed (in seconds)
        """

        for key in key_list:
            if not self._validate_key(key):
                logging.warning(f"Invalid key: {key}")
                return False

        ws = self._connect_websocket()
        for key in key_list:
            ws.send(
                f'{{"event_type": "key", "event": {{"key": "{key}", "state": true}}}}'
            )

        time.sleep(press_time)

        for key in key_list:
            ws.send(
                f'{{"event_type": "key", "event": {{"key": "{key}", "state": false}}}}'
            )
        ws.close()

    @keyword("Multiple Keys PiKVM")
    def send_key_series(self, key_list, press_time=0.2):
        """
        key_list - list of keys to be pressed one after another,
        press_time - time the every key will remain pressed (in seconds)
        """

        for key in key_list:
            if not self._validate_key(key):
                logging.warning(f"Invalid key: {key}")
                return False

        ws = self._connect_websocket()
        for key in key_list:
            ws.send(
                f'{{"event_type": "key", "event": {{"key": "{key}", "state": true}}}}'
            )
            time.sleep(press_time)
            ws.send(
                f'{{"event_type": "key", "event": {{"key": "{key}", "state": false}}}}'
            )
            time.sleep(press_time)
        ws.close()

    @keyword("Write Bare PiKVM")
    def write_text(self, text, press_time=0.2):
        """
        WARNING: Supports only small characters.
        ---\n
        text - text to be written,\n
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
            "{": "BracketLeft",
            "}": "BracketRight",
            "|": "Backslash",
            ":": "Semicolon",
            '"': "Quote",
            "~": "Backquote",
            "<": "Comma",
            ">": "Period",
            "?": "Slash",
        }

        ws = self._connect_websocket()
        for char in text:
            if char in shift_keymap:
                logging.debug("Using shift_keymap")
                ws.send(
                    '{"event_type": "key", "event": {"key": "ShiftRight", "state": true}}'
                )
                time.sleep(press_time)
                ws.send(
                    f'{{"event_type": "key", "event": {{"key": "{shift_keymap[char]}", "state": true}}}}'
                )
                time.sleep(press_time)
                ws.send(
                    f'{{"event_type": "key", "event": {{"key": "{shift_keymap[char]}", "state": false}}}}'
                )
                ws.send(
                    '{"event_type": "key", "event": {"key": "ShiftRight", "state": false}}'
                )
            else:
                logging.debug("Using regular keymap")
                ws.send(
                    f'{{"event_type": "key", "event": {{"key": "{keymap[char]}", "state": true}}}}'
                )
                time.sleep(press_time)
                ws.send(
                    f'{{"event_type": "key", "event": {{"key": "{keymap[char]}", "state": false}}}}'
                )
        ws.close()

    @keyword("Write PiKVM")
    def write_pikvm(self, text, press_time=0.1):
        self.write_text(text, press_time)
        self.send_key("Enter", press_time)

    @keyword("Mount Image On PiKVM")
    def mount_image(self, img_name):
        """
        pikvm_ip - IP of the piKVM to send key input,
        img_name - name of the image to be mounted,
        """
        requests.post(
            f"https://{self.pikvm_ip}/api/msd/set_connected?connected=0",
            headers=self.http_headers,
            verify=False,
        )
        requests.post(
            f"https://{self.pikvm_ip}/api/msd/set_params?image={img_name}&cdrom=0",
            headers=self.http_headers,
            verify=False,
        )
        requests.post(
            f"https://{self.pikvm_ip}/api/msd/set_connected?connected=1",
            headers=self.http_headers,
            verify=False,
        )

    @keyword("Upload Image To PiKVM")
    def upload_image(self, img_source, img_name, upload_type="url"):
        """
        Upload an image to piKVM, either from a URL or a local file path.

        Parameters:
        - pikvm_ip: IP of the PiKVM
        - img_source: URL of the image or file path of the image to be uploaded
        - img_name: Name of the image to be used on piKVM
        - upload_type: Specify "url" to upload from a URL or "file" to upload from
          a local path (defaults to "url")
        """
        requests.post(
            f"https://{self.pikvm_ip}/api/msd/set_connected?connected=0",
            headers=self.http_headers,
            verify=False,
        )
        requests.post(
            f"https://{self.pikvm_ip}/api/msd/remove?image={img_name}",
            headers=self.http_headers,
            verify=False,
        )

        if upload_type.lower() == "file":
            uri = f"https://{self.pikvm_ip}/api/msd/write?image={img_name}"
            with open(img_source, "rb") as img_file:
                requests.post(
                    uri, headers=self.http_headers, data=img_file, verify=False
                )
        else:
            uri = f"https://{self.pikvm_ip}/api/msd/write_remote?url={img_source}&image={img_name}"
            requests.post(uri, headers=self.http_headers, verify=False)
