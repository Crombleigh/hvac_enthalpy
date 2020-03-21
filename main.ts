let temperature = 0
forever(function () {
    bme280.setPower(true)
    bme280.setAddress(BME280_I2C_ADDRESS.ADDR_0x76)
    display.showString("Hello world", 1)
    temperature = bme280.temperature()
})
