from __future__ import print_function
from cobwebiot import client
from cobwebiot import server

try:
    from cobwebiot import beagle
except:
    print("No beaglebone imported")
    pass

try:
    from cobwebiot import rasp
except:
    print("No Raspberry pi imported")
    pass

from cobwebiot import dev
