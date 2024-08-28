from serial import SerialException
import re
from vgamepad import VX360Gamepad
import time
import serial

class Mbit:
    # Constructor
    def __init__(self, baudrate, port):
        self.baudrate = baudrate
        self.port = port

    # Inicia el proceso de comunicacion mediante conexion Serial:
    def connect(self):
        serial_on = serial.Serial(baudrate=self.baudrate, port=self.port)
        print("Connected succesfully")
        return serial_on

    # Recorre la string, obtiene los numeros y luego retorna un promedio.
    def get_numbers(self, data, number_regex):
        numbers = number_regex.findall(data)
        return (sum(int(number) for number in numbers)) / len(numbers)

    # Obtiene la informacion y la decodifica, devuelve una string.
    def data_decoder(self, serial_base):
        return serial_base.readline().decode().strip()

select_port = str(input("===================================\nSelect serial port to connect: "))
print("Baudrate at 115200 by default. Do you want to change it?")
decision = input("y/n: ")

match decision:
    case "y":
        baudrate = int(input("Select baudrate: "))

    case "n":
        baudrate = 115200

print("Triying to connect: ")
while True:
    try:
        get_serial_data = microbit.Mbit(baudrate, select_port).connect()
        control = VX360Gamepad()
        number_regex = re.compile(r'-?\d+')
        break
    except SerialException:
        print("Connection failed, trying again in: ")
        for i in range(0,2):
            time.sleep(1)
            print(3-i)
    else:
        pass

while True:
    try:
        new_data_string = microbit.Mbit.data_decoder(get_serial_data)

        if new_data_string:
            # Convertir el valor del acelerómetro a un valor entre -32767 y 32767 (rango del joystick)
            joystick_value = int(microbit.Mbit.get_numbers(new_data_string, number_regex) * 32767 / 2048)

            # Actualizar el estado del joystick en el gamepad virtual
            control.left_joystick(x_value=-joystick_value, y_value=0)

            # Envia la actualizacion al sistema
            control.update()
    except SerialException:
        print("Satus: Disconnected")
        time.sleep(1)
        quit("Re-launch again if you want to connect again")