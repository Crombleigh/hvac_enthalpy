temperature = 0
def on_forever():
    bme280.set_power(True)
    bme280.set_address(BME280_I2C_ADDRESS.ADDR_0X76)
    display.show_string("Hello world", 1)
    temperature = bme280.temperature()
forever(on_forever)