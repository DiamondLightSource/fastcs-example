import re
import subprocess
import sys

from fastcs_example import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "fastcs_example", "--version"]
    versions = subprocess.check_output(cmd).decode().strip()

    my_version = re.findall("TemperatureController: (.*)", versions)
    assert len(my_version) == 1
    assert my_version[0] == __version__
