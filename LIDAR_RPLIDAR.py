import rclpy
from rplidar import RPLidar

class RPLIDARNode(rclpy.Node):
  def __init__(self):
    super().__init__("rplidar_node")

    self.rplidar = RPLidar("/dev/ttyUSB0")  # Ajustar el puerto según su configuración

    try:
      self.rplidar.start()
    except:
      print("Error al iniciar RPLIDAR")
      return

    self.timer_ = self.create_timer(0.1, self.on_scan)

  def on_scan(self):
    # Procesar datos RPLIDAR
    for scan in self.rplidar.iter_scan():
      # Extraer distancia y ángulo
      distance = scan[0]
      angle = scan[1]
      intensity = scan[2]

      # Imprimir o procesar datos
      print(f"Distancia: {distance}")
      print(f"Ángulo: {angle}")
      print(f"Intensidad: {intensity}")

  def destroy(self):
    self.rplidar.stop()
    super().destroy()

if __name__ == "__main__":
  rclpy.init()
  node = RPLIDARNode()
  rclpy.spin(node)
  rclpy.shutdown()
