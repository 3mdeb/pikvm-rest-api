# PiKVM Client

Python client for a subset of [PiKVM API](https://docs.pikvm.org/api). The
target is to use this class as a library in the
[open-source-firmware-validation repo](https://github.com/Dasharo/open-source-firmware-validation.git).

## Testing

* Start PiKVM with some DUT

* Run test commands one by one

```bash
python3 ./pikvm_test_cli.py --login admin --password admin --ip 192.168.10.45 --test single-key
python3 ./pikvm_test_cli.py --login admin --password admin --ip 192.168.10.45 --test key-series
python3 ./pikvm_test_cli.py --login admin --password admin --ip 192.168.10.45 --test key-combination
python3 ./pikvm_test_cli.py --login admin --password admin --ip 192.168.10.45 --test write-text
python3 ./pikvm_test_cli.py --login admin --password admin --ip 192.168.10.45 --test write-cmd
wget http://tinycorelinux.net/15.x/x86/release/Core-15.0.iso
python3 ./pikvm_test_cli.py --login admin --password admin --ip 192.168.10.45 --test img-upload-url
python3 ./pikvm_test_cli.py --login admin --password admin --ip 192.168.10.45 --test img-upload-file
python3 ./pikvm_test_cli.py --login admin --password admin --ip 192.168.10.45 --test img-mount
```

* Observe the results in PiKVM WEB UI
