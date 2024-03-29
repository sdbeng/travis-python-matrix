import os
import platform

import distro


def test_matrix() -> None:

    python_implementation = platform.python_implementation()
    python_version = platform.python_version()
    system = platform.system()

    if system == "Darwin":
        system = "macOS"
        version = platform.mac_ver()[0]
        if version.startswith("10.14"):
            version = "10.14 (Mojave)"
        elif version.startswith("10.13"):
            version = "10.13 (High Sierra)"
        elif version.startswith("10.12"):
            version = "10.12 (Sierra)"
        else:
            assert False, version
    elif system == "Windows":
        version = platform.win32_ver()[0]
    elif system == "Linux":
        system = distro.name()
        version = distro.version()
        if system == "Ubuntu":
            if version == "16.04":
                version += " (Xenial Xerus)"
            else:
                assert False, version
        else:
            assert False, system
    else:
        assert False, system

    name = "{} {} on {} {}".format(
        platform.python_implementation(),
        platform.python_version(),
        system, version,
    )

    assert name == os.environ["TRAVIS_JOB_NAME"]
