import serial

# Configura el puerto serie para comunicarse con el Scanse Sweep
ser = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=0.5)
print("1")

try:
    # Envía el comando para iniciar el escaneo
    ser.write(b'D\n')
    print("2")

    # Lee los datos de escaneo del dispositivo
    while True:
        try:
            line = ser.readline().decode().strip()
            print("Received line:", line)  
            if line.startswith('S'):
                # Si la línea comienza con 'S', es un escaneo válido
                # Separa los datos de escaneo y cuenta las mediciones
                scan_data = line.split()[1:]
                num_measurements = len(scan_data)
                print(f'Got {num_measurements} measurements')
                print("Data:", scan_data)  
            elif line.startswith('E'):
                break
        except KeyboardInterrupt:
            print("Programa interrumpido por el usuario")
            break

except Exception as e:
    print("Error:", e)

finally:
    # Envía el comando para detener el escaneo
    ser.write(b'H\n')
    # Cierra el puerto serie
    ser.close()












