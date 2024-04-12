
import rclpy
from sensor_msgs.msg import LaserScan

class SweepScanseNode(rclpy.Node):
  def __init__(self):
    super().__init__("sweep_scanse_node")

    self.subscription_ = self.create_subscription(
      LaserScan,
      "/scan",
      10,
      self.on_scan)

  def on_scan(self, scan):
    # Imprimir distancia y ángulo
    for i in range(len(scan.ranges)):
      print(f"Distancia: {scan.ranges[i]}")
      print(f"Ángulo: {scan.angle_min + i * scan.angle_increment}")
    

if __name__ == "__main__":
  rclpy.init()
  node = SweepScanseNode()
  rclpy.spin(node)
  rclpy.shutdown()












