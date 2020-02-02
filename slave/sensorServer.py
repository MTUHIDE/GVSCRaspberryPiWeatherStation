from flask import Flask
from flask_restful import Api, Resource, reqparse
import smbus

DEVICE_BUS = 1
DEVICE_ADDR = 0x17

TEMP_REG = 0x01
LIGHT_REG_L = 0x02
LIGHT_REG_H = 0x03
STATUS_REG = 0x04
ON_BOARD_TEMP_REG = 0x05
ON_BOARD_HUMIDITY_REG = 0x06
ON_BOARD_SENSOR_ERROR = 0x07
BMP280_TEMP_REG = 0x08
BMP280_PRESSURE_REG_L = 0x09
BMP280_PRESSURE_REG_M = 0x0A
BMP280_PRESSURE_REG_H = 0x0B
BMP280_STATUS = 0x0C
HUMAN_DETECT = 0x0D

bus = smbus.SMBus(DEVICE_BUS)

app = Flask(__name__)
api = Api(app)

class Weather(Resource):
    def get(self):
        data = {}
        # Read data into buffer
        buffer = [0x00]
        for i in range(TEMP_REG, HUMAN_DETECT + 1):
            buffer.append(bus.read_byte_data(DEVICE_ADDR, i))

        # Read Ground Temp °C
        if buffer[STATUS_REG] & 0x01: # Over range
            data["gnd_tmp"] = None
        elif buffer[STATUS_REG] & 0x02: # Not connected
            data["gnd_tmp"] = None
        else:
            data["gnd_tmp"] = buffer[TEMP_REG]

        # Read Brightness Lux
        if buffer[STATUS_REG] & 0x04: # Over range
            data["light"] = None
        elif buffer[STATUS_REG] & 0x08: # Sensor Failure
            data["light"] = None
        else:
            data["light"] = buffer[LIGHT_REG_H] << 8 | buffer[LIGHT_REG_L]

        # IR Temp °C
        data["ir_temp"] = buffer[ON_BOARD_TEMP_REG]

        # Humidity %
        data["humidity"] = buffer[ON_BOARD_HUMIDITY_REG]

        # Barometer
        if buffer[BMP280_STATUS] == 0:
            # Temp °C
            data["bar_temp"] = buffer[BMP280_TEMP_REG]
            # Pressure (pascal)
            data["pressure"] = buffer[BMP280_PRESSURE_REG_L] | buffer[BMP280_PRESSURE_REG_M] << 8 | buffer[BMP280_PRESSURE_REG_H] << 16
        else:
            data["bar_temp"] = None
            data["pressure"] = None

        data["detect_human"] = buffer[HUMAN_DETECT]

        return data, 200

api.add_resource(Weather, "/api/weather")

app.run(host='0.0.0.0', port=80, debug=False)
