from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import urequests
import time
import unit

# Set your WIFI SSID
wifi_ssid = ''
# Set your WIFI WPA key (Password)
wifi_wpa = ''
# Set your unique webhooks url
webhooks_url = ''

setScreenColor(0x111111)
light_1 = unit.get(unit.LIGHT, unit.PORTA)
light = None
rectangle0 = M5Rect(94, -69, 1, 20, 0xff0000, 0xff0000)

axp.setLcdBrightness(0)
while True:
  if wifiCfg.wlan_sta.isconnected():
    M5Led.off()
    while True:
      light = light_1.analogValue
      if light > 100:
        try:
          req = urequests.request(method='GET', url=webhooks_url)
          M5Led.on()
          wait_ms(50)
          M5Led.off()
          setScreenColor(0xffff66)
          wait_ms(1000)
          setScreenColor(0x000000)
        except:
          pass
        wait(4)
      wait_ms(2)
  else:
    M5Led.on()
    wifiCfg.doConnect(wifi_ssid, wifi_wpa)
  wait_ms(2)
