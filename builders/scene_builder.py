from core.scene_objects import SceneObjects

from objects.feature_space_3d import FeatureSpace3D
from objects.feature_space_grid import FeatureSpaceGrid
from objects.point_cloud import PointCloud
from objects.activation_plane import ActivationPlane


class SceneBuilder:

    @staticmethod
    def from_representation(
        rep,
        stage_name="input",
    ):

        stage = rep.get(stage_name)

        axes = (
            FeatureSpace3D()
            .create_axes()
            .create_labels()
        )


        grid = FeatureSpaceGrid(
            grid_data=stage.grid
        )

        cloud = PointCloud(
            stage.points,
            colors=rep.dataset["colors"],
            labels=rep.dataset["labels"],
        )

        return SceneObjects(
            axes=axes,
            grid=grid,
            cloud=cloud,
        )