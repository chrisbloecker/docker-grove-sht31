from http.server                                   import BaseHTTPRequestHandler, HTTPServer
from grove.grove_temperature_humidity_sensor_sht3x import GroveTemperatureHumiditySensorSHT3x

import os
import json


class SHT31Handler(BaseHTTPRequestHandler):
    sensor = GroveTemperatureHumiditySensorSHT3x()

    def do_GET(self):
        temperature, humidity = self.sensor.read()

        res = dict( temperature = round(temperature, 1)
                  , humidity    = round(humidity,    1)
                  )

        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()

        self.wfile.write(json.dumps(res).encode())


def main():
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "80"))

    httpd = HTTPServer((host, port), SHT31Handler)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
