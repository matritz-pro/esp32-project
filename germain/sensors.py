import dht

def read_sensor():
  sensor = dht.DHT22(Pin(25))
  #sensor = dht.DHT11(Pin(14))
  try:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      temp = (b'{0:3.1f},'.format(temp))
      hum =  (b'{0:3.1f},'.format(hum))

      # uncomment for Fahrenheit
      #temp = temp * (9/5) + 32.0
      return temp, hum
    else:
      return('Invalid sensor readings.')
  except OSError as e:
    return('Failed to read sensor.')