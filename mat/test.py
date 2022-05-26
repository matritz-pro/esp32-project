import sys, dht, esp32, machine, sgp40, time, network
from machine import Pin, PWM, I2C, ADC, RTC
from sgp40 import SGP40

WIFI = {
    "":""
}

def do_connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('connecting to network %s...' % ssid)
        if not wlan.active():
            wlan.active(True)
        wlan.connect(ssid, password)
        start=time.time()
        while not wlan.isconnected() and (time.time() - start) < 5:
            pass
    return wlan.isconnected()
    #print('network config:', wlan.ifconfig())


def get_air_quality():
    return SGP40(I2C(0), 0x59).measure_raw()

def get_dht():
    d = dht.DHT11(Pin(25))
    d.measure()
    return (d.humidity(), d.temperature())

def get_luminosity():
    foto=ADC(Pin(34))
    foto.atten(ADC.ATTN_11DB)
    return foto.read_u16()

# LED
R = Pin(21, Pin.OUT)
G = Pin(23, Pin.OUT)
B = Pin(22, Pin.OUT)

def led(t):
    R.value(t[0])
    G.value(t[1])
    B.value(t[2])

def led_temp(t):
    if t < 10:
        return [0,0,1]
    if t > 30:
        return [1,0,0]
    return [0,0,0]

if __name__ == '__main__':
    connected = False
    while not connected:
        for ssid, password in WIFI.items():
            try:
                connected = do_connect(ssid, password)
            except Exception as e:
                print(str(e))
            else:
                if connected:
                    print('connected to network %s' % ssid)
                    break
                else:
                    print('connection to network %s failed' % ssid)
        if not connected:
            time.sleep(240)
    
    data = {}
    while 1:
        data['air_quality'] = get_air_quality()
        data['humidity'], data['temperature'] = get_ht()
        data['luminosity'] = get_luminosity()
        
        now = RTC().datetime()
        now = [str(x) for x in now]
        
        print('\n', f'{now[0]}-{now[1]}-{now[2]} {now[4]}:{now[5]}:{now[6]}')
        for k, v in data.items():
            print('\t-', f'{k}: {v}', end=';\n')
            
        led(led_temp(data['temperature']))
        
        time.sleep(1)
