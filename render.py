from ovito.io import import_file
from ovito.modifiers import *

node = import_file("C:\\Users\\Marcos\\git\\ss-2019-tp3\\ovito_output.xyz", multiple_frames = True, columns = ['Particle Identifier',
    'Radius', 'Mass', 'Position.X', 'Position.Y', 'Velocity.X', 'Velocity.Y'])
# id:I:1:radius:R:1:mass:R:1:pos:R:2:velo:R:2
node.add_to_scene()

# Periodic Boundary Condition (X,Y,Z)
node.source.cell.pbc = (False, False, False)

# Cell dimensions
# cell_matrix = node.source.cell.matrix
# cell_matrix.setflags(write = 1)
# for i in range(len(cell_matrix)):
#     cell_matrix[i][i] = 0.5
# cell_matrix.setflags(write = 0)

# Cell Transformation (resize)

modifier = AffineTransformationModifier(
    # operate_on = {'cell'}, # in Ovito 3
    transform_particles = False, # in Ovito 2.9
    transform_surface = False, # in Ovito 2.9
    transform_vector_properties = False, # in Ovito 2.9
    transform_box = True, # in Ovito 2.9
    transformation = [[0.5, 0, 0, 0],
                      [0, 0.5, 0, 0],
                      [0, 0, 0.5, 0]]
)

node.modifiers.append(modifier)

color_modifier = ColorCodingModifier(
	particle_property = 'Particle Identifier',
	start_value = 0,
	end_value = node.compute().number_of_particles
)

node.modifiers.append(color_modifier)

node.compute()
