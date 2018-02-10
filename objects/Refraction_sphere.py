import objects.Refraction_surface as Refraction_surface
import math_obj.Vector3 as Vector3
import objects.Light as Light

class RefractionSphere(Refraction_surface):
    def __init__(self, center : Vector3, rad):
        """
        :type center: Vector3
        :type rad: float
        :param center:
        """
        super().__init__()
        self.center = center
        self.radius = rad


    def intersect_with_light(self,light: Light):
        """
        This need the center of the the sphere on the axis of Z
        :param light:
        :return:
        """