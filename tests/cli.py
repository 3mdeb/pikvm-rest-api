import argparse
import sys

from pikvm.client import PiKVMClient


class PiKVMTests:
    def __init__(self, ip, login, password):
        self.pikvm = PiKVMClient(pikvm_ip=ip, login=login, password=password)

    def send_single_key(self):
        """Send a single key (A)."""
        try:
            self.pikvm.send_key("KeyA")
            print("Successfully sent the key 'A'.")
        except Exception as e:
            print(f"Failed to send the key 'A': {e}")

    def send_key_combination(self):
        """Send a series of keys (ShiftLeft + A)."""
        try:
            keys = ["ShiftLeft", "KeyA"]
            self.pikvm.send_key_combination(keys)
            print("Successfully sent the key combination: ShiftLeft + A.")
        except Exception as e:
            print(f"Failed to send key combination: {e}")

    def send_key_series(self):
        """Send a series of keys (a, b, c)."""
        try:
            keys = ["KeyA", "KeyB", "KeyC"]
            self.pikvm.send_key_series(keys)
            print("Successfully sent the key series: a, b, c.")
        except Exception as e:
            print(f"Failed to send key series: {e}")

    def write_cmd(self):
        """Write cmd('cat /proc/cpuinfo')."""
        try:
            text = "cat /proc/cpuinfo"
            self.pikvm.write_pikvm(text)
            print("Successfully wrote cmd '/cat/proc/cpuinfo'.")
        except Exception as e:
            print(f"Failed to write cmd: {e}")

    def img_upload_url(self):
        """Upload image from URL."""
        try:
            url = "http://tinycorelinux.net/15.x/x86/release/Core-15.0.iso"
            name = "Core-15.0-url.iso"
            self.pikvm.upload_image(url, name)
            print("Successfully uploaded image from URL.")
        except Exception as e:
            print(f"Failed to upload image from URL: {e}")

    def img_upload_file(self):
        """Upload image from local file."""
        try:
            file = "Core-15.0.iso"
            name = "Core-15.0-local.iso"
            self.pikvm.upload_image(file, name, upload_type="file")
            print("Successfully uploaded image from local file.")
        except Exception as e:
            print(f"Failed to upload image from local file: {e}")

    def img_mount(self):
        """Mount file."""
        try:
            name = "Core-15.0-url.iso"
            self.pikvm.mount_image(name)
            print("Successfully mounted image.")
        except Exception as e:
            print(f"Failed to mount image: {e}")


def main():
    parser = argparse.ArgumentParser(description="PiKVM Functional Test Runner")
    parser.add_argument("--ip", required=True, help="IP address of the PiKVM device")
    parser.add_argument(
        "--login", required=True, help="Login username for the PiKVM device"
    )
    parser.add_argument(
        "--password", required=True, help="Password for the PiKVM device"
    )
    parser.add_argument(
        "--test",
        choices=[
            "single-key",
            "key-combination",
            "key-series",
            "write-text",
            "write-cmd",
            "img-upload-url",
            "img-upload-file",
            "img-mount",
        ],
        required=True,
        help="Test to execute",
    )

    args = parser.parse_args()

    # Initialize PiKVMTests with provided credentials
    tester = PiKVMTests(ip=args.ip, login=args.login, password=args.password)

    # Run the requested test
    if args.test == "single-key":
        tester.send_single_key()
    elif args.test == "key-combination":
        tester.send_key_combination()
    elif args.test == "key-series":
        tester.send_key_series()
    elif args.test == "write-cmd":
        tester.write_cmd()
    elif args.test == "write-cmd":
        tester.write_pikvm()
    elif args.test == "img-upload-url":
        tester.img_upload_url()
    elif args.test == "img-upload-file":
        tester.img_upload_file()
    elif args.test == "img-mount":
        tester.img_mount()

    else:
        print("Invalid test selected. Use --help for usage information.")


if __name__ == "__main__":
    main()
