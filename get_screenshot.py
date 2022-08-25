import utils.helper as helper
import base64

helper.connect_device()
device = helper.get_device()
png_screenshot_data = device.shell("screencap -p | busybox base64")
png_screenshot_data = base64.b64decode(png_screenshot_data)

with open("screen.png", "wb") as fp:
    fp.write(png_screenshot_data)
