# Mbit-Stwheel
Es un script de Python que utiliza las librerias VGamepad y Pyserial, para obtener los valores en tiempo real del acelerómetro de la micro:bit, luego traduce estos valores en un movimiento del análogo izquierdo de un Joystick emulado para Windows.

## Para utilizar el cliente
1. Instala las dependencias


   ```bash
   pip install -r requirements.txt
   ```
2. Conecta tu micro:bit
3. Luego ejecuta


   ```bash
   python client.py
   ```

4. Se te pedirá que escribas el puerto de comunicación Serial, debes fijarte en administrador de dispositivos (Suele ser COM5 o COM6).
5. (Opcional) Elige el baudrate o presiona n

## Configuracion en micro:bit
Es necesario que la micro:bit este transmitiendo siempre los valores del acelerómetro utilizando el bloque `serial write line`, y este conectada a un puerto USB 2.0.
