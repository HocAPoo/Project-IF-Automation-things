import pywemo

devices = pywemo.discover_devices()
print(devices)
devices[0].toggle()
