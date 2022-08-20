import sys
import logging

#sys.path.append('../')

from samsungtvws import SamsungTVWS

# Increase debug level
logging.basicConfig(level=logging.INFO)

# Normal constructor
tv_ip = "192.168.1.106"
tv = SamsungTVWS(tv_ip)

# List the art available on the device
info = tv.art().available()
logging.info(info)

# Retrieve information about the currently selected art
info = tv.art().get_current()
logging.info(info)

# Retrieve a thumbnail for a specific piece of art. Returns a JPEG.
thumbnail = tv.art().get_thumbnail('SAM-F0206')

# Determine whether the TV is currently in art mode
info = tv.art().get_artmode()
logging.info(info)

tv.art().select_image('MY_F0003')
