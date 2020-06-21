import json
import wifi
import server
import one_wire_thermometer

config_fd = open('config.json')
config_json = config_fd.read()
config = json.loads(config_json)

wifi_connection = wifi.join(config)
ds, therm = one_wire_thermometer.init(config)
print(wifi_connection.ifconfig())
server.start(config, ds, therm)
