from dataclasses import dataclass

from objects.feature_space_3d import FeatureSpace3D
from objects.feature_space_grid import FeatureSpaceGrid
from objects.point_cloud import PointCloud
from objects.activation_plane import ActivationPlane


@dataclass
class SceneObjects:

    axes: FeatureSpace3D
    grid: FeatureSpaceGrid
    cloud: PointCloud