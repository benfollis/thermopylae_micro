import network
import json
def join(config):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wifi_config = config['wifi']
    ssid=wifi_config['ssid']
    password=wifi_config['password']
    wlan.connect(ssid, password)
    return wlan