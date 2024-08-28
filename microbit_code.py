input.set_accelerometer_range(AcceleratorRange.ONE_G)
while True:
    serial.write_line("" + str((input.acceleration(Dimension.Y))))