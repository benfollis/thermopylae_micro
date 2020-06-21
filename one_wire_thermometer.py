from machine import Pin
import onewire
import time, ds18x20

def init(config):
    therm_config = config['onewire']
    pin = therm_config['pin']
    ow = onewire.OneWire(Pin(pin))
    ds = ds18x20.DS18X20(ow)
    rom = ds.scan()
    # only handles 1 thermometer right now
    return ds, rom[0]
