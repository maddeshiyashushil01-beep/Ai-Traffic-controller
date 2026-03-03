import math

class AccidentDetector:
    def __init__(self, distance_threshold=50):
        self.distance_threshold = distance_threshold

    def check_collision(self, vehicles):
        accident_detected = False

        for i in range(len(vehicles)):
            for j in range(i+1, len(vehicles)):
                x1, y1, x2, y2 = vehicles[i]
                a1, b1, a2, b2 = vehicles[j]

                center1 = ((x1+x2)//2, (y1+y2)//2)
                center2 = ((a1+a2)//2, (b1+b2)//2)

                distance = math.sqrt(
                    (center1[0]-center2[0])**2 +
                    (center1[1]-center2[1])**2
                )

                if distance < self.distance_threshold:
                    accident_detected = True

        return accident_detected