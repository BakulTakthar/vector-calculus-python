from manim import *

class BasicVectorField(Scene):
    def func(self, pos):
        x, y, z = pos[:3]
        return np.array([y**2, 2*x*y +z**2, 2*x*y])  # Rotational field

    def construct(self):
        threed_axes = ThreeDAxes(x_range=[-4, 4, 1], y_range=[-3, 3, 1], z_range=[-4, 4, 1])
        self.add(threed_axes)
        field = ArrowVectorField(self.func, x_range=[-4, 4, 1], y_range=[-3, 3, 1], z_range=[-4, 4, 1], length=0.5, color=BLUE)
        self.add(field)

        self.interactive_embed()