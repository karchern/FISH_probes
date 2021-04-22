import sys
import os
import pkg_resources
from fish_probes import UTIL_log

TEST_DATA_PATH = pkg_resources.resource_filename("fish_probes", "test")

def test():
    UTIL_log.print_log("Run test")
    print(TEST_DATA_PATH)
