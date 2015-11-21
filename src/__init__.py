from LivePlaylist import LivePlaylist

def create_instance(c_instance):
    return LivePlaylist(c_instance)

from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[14], model_name='LivePlaylist'),
     PORTS_KEY: [inport(props=[NOTES_CC, REMOTE, SCRIPT]), outport(props=[NOTES_CC, REMOTE, SCRIPT])]}
