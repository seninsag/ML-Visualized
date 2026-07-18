# ml/exporter.py
import json
import torch
import torch.nn as nn
import numpy as np
from pathlib import Path


class XORNet(nn.Module):
    """
    Simple feedforward network for XOR visualization.
    Named modules allow clean extraction without indexing Sequential.
    """

    def __init__(self, hidden_dim=3):
        super().__init__()
        self.linear1 = nn.Linear(2, hidden_dim)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(hidden_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.linear1(x)
        x = self.relu(x)
        x = self.linear2(x)
        x = self.sigmoid(x)
        return x

    @property
    def named_layers(self):
        """Return named layers for iteration."""
        return [
            ("linear1", self.linear1),
            ("relu", self.relu),
            ("linear2", self.linear2),
            ("sigmoid", self.sigmoid),
        ]


class RepresentationExporter:
    """
    Trains a minimal neural network on spread-XOR and exports
    layer-by-layer representations for Manim visualization.
    """

    def __init__(
    self,
    hidden_dim=3,
    grid_size=15,
    grid_range=(-3, 3),
    seed=42,
    mode="trained",
):
        self.hidden_dim = hidden_dim
        self.grid_size = grid_size
        self.grid_range = grid_range
        self.seed = seed
        self.mode = mode
        
        self.model = None
        self.dataset_points = None
        self.dataset_labels = None
        self.grid_points = None
        self.loss_history = []

        if seed is not None:
            torch.manual_seed(seed)
            np.random.seed(seed)

    # ---------------------------------
    # Dataset Generation
    # ---------------------------------

    def generate_spread_xor(self, points_per_center=10, std=0.3):
        centers = [
            (-2, 2),   # Red
            (2, -2),   # Red
            (-2, -2),  # Blue
            (2, 2),    # Blue
        ]
        labels = [0, 0, 1, 1]

        all_points = []
        all_labels = []

        for center, label in zip(centers, labels):
            for _ in range(points_per_center):
                point = np.random.normal(loc=center, scale=std)
                all_points.append(point)
                all_labels.append(label)

        self.dataset_points = torch.tensor(all_points, dtype=torch.float32)
        self.dataset_labels = torch.tensor(all_labels, dtype=torch.long)

        return self
    

    def generate_xor(self):
        """
        Generate the four canonical XOR points.
        """

        self.dataset_points = torch.tensor([
            [-2.0,  2.0],
            [ 2.0, -2.0],
            [-2.0, -2.0],
            [ 2.0,  2.0],
        ], dtype=torch.float32)

        self.dataset_labels = torch.tensor(
            [0, 0, 1, 1],
            dtype=torch.long,
        )

        return self


    def generate_grid(self):
        x_vals = np.linspace(self.grid_range[0], self.grid_range[1], self.grid_size)
        y_vals = np.linspace(self.grid_range[0], self.grid_range[1], self.grid_size)

        grid = []
        for x in x_vals:
            for y in y_vals:
                grid.append([x, y])

        self.grid_points = torch.tensor(grid, dtype=torch.float32)
        return self

    # ---------------------------------
    # Model
    # ---------------------------------

    def build_model(self):
        self.model = XORNet(hidden_dim=self.hidden_dim)

        if self.mode == "educational":
            with torch.no_grad():

                # A clean, interpretable embedding
                self.model.linear1.weight.copy_(torch.tensor([
                    [1.0, 0.0],    # x
                    [0.0, 1.0],    # y
                    [1.0, -1.0],   # x - y
                ]))

                self.model.linear1.bias.zero_()

        return self

    # ---------------------------------
    # Training
    # ---------------------------------

    def train(self, epochs=2000, lr=0.01):
        if self.model is None:
            self.build_model()

        criterion = nn.BCELoss()
        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)

        labels_float = self.dataset_labels.float().unsqueeze(1)

        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = self.model(self.dataset_points)
            loss = criterion(outputs, labels_float)
            loss.backward()
            optimizer.step()

            self.loss_history.append(loss.item())

            if (epoch + 1) % 500 == 0:
                print(f"Epoch {epoch + 1}, Loss: {loss.item():.4f}")

        return self

    # ---------------------------------
    # Extraction
    # ---------------------------------

    def extract_representations(self):
        self.model.eval()

        stages = []

        # Stage 0: Input
        stages.append(self._export_stage(
            name="input",
            stage_type="input",
            index=0,
            representation=self.dataset_points,
            grid=self.grid_points,
            input_dim=2,
            output_dim=2,
        ))

        # Iterate through layers
        prev_representation = self.dataset_points
        prev_grid = self.grid_points

        with torch.no_grad():
            for idx, (name, layer) in enumerate(self.model.named_layers, start=1):
                representation = layer(prev_representation)
                grid_representation = layer(prev_grid)

                stage_type = "activation" if name in ("relu", "sigmoid") else "linear"
                activation = name if stage_type == "activation" else None

                input_dim = prev_representation.shape[1] if prev_representation.dim() > 1 else 1
                output_dim = representation.shape[1] if representation.dim() > 1 else 1

                stages.append(self._export_stage(
                    name=name,
                    stage_type=stage_type,
                    index=idx,
                    representation=representation,
                    grid=grid_representation,
                    input_dim=input_dim,
                    output_dim=output_dim,
                    activation=activation,
                ))

                prev_representation = representation
                prev_grid = grid_representation

        return stages

    def _export_stage(
        self,
        name,
        stage_type,
        index,
        representation,
        grid,
        input_dim,
        output_dim,
        activation=None,
    ):
        # ---------------------------------
        # Convert to 3D
        # ---------------------------------

        points_3d = self._pad_to_3d(representation)
        grid_3d = self._pad_to_3d(grid)

        # ---------------------------------
        # Debug Information
        # ---------------------------------

        print("\n" + "=" * 60)
        print(f"Stage: {name}")
        print("=" * 60)

        print(f"Representation Shape : {tuple(points_3d.shape)}")
        print(f"Grid Shape           : {tuple(grid_3d.shape)}")

        point_min = points_3d.min(dim=0).values
        point_max = points_3d.max(dim=0).values

        grid_min = grid_3d.min(dim=0).values
        grid_max = grid_3d.max(dim=0).values

        print("\nPoint Coordinate Ranges")
        print("-----------------------")
        print(f"X : {point_min[0]:8.3f} -> {point_max[0]:8.3f}")
        print(f"Y : {point_min[1]:8.3f} -> {point_max[1]:8.3f}")
        print(f"Z : {point_min[2]:8.3f} -> {point_max[2]:8.3f}")

        print("\nGrid Coordinate Ranges")
        print("----------------------")
        print(f"X : {grid_min[0]:8.3f} -> {grid_max[0]:8.3f}")
        print(f"Y : {grid_min[1]:8.3f} -> {grid_max[1]:8.3f}")
        print(f"Z : {grid_min[2]:8.3f} -> {grid_max[2]:8.3f}")

        # ---------------------------------
        # Build Stage Dictionary
        # ---------------------------------

        stage = {
            "name": name,
            "type": stage_type,
            "index": index,
            "input_dimension": input_dim,
            "output_dimension": output_dim,
            "points": points_3d.tolist(),
            "grid": {
                "shape": [self.grid_size, self.grid_size],
                "points": grid_3d.tolist(),
            },
        }

        if activation:
            stage["activation"] = activation

        if name == "sigmoid":
            stage["outputs"] = representation.squeeze().tolist()

        return stage

    def _pad_to_3d(self, tensor):
        """Pad 1D or 2D tensors to 3D for consistent visualization."""
        if tensor.dim() == 1:
            return torch.stack([
                tensor,
                torch.zeros_like(tensor),
                torch.zeros_like(tensor),
            ], dim=1)
        elif tensor.shape[1] == 1:
            return torch.cat([tensor, torch.zeros(tensor.shape[0], 2)], dim=1)
        elif tensor.shape[1] == 2:
            return torch.cat([tensor, torch.zeros(tensor.shape[0], 1)], dim=1)
        return tensor

    # ---------------------------------
    # Weights Export
    # ---------------------------------

    def extract_weights(self):
        return {
            "linear1": {
                "weight": self.model.linear1.weight.detach().tolist(),
                "bias": self.model.linear1.bias.detach().tolist(),
            },
            "linear2": {
                "weight": self.model.linear2.weight.detach().tolist(),
                "bias": self.model.linear2.bias.detach().tolist(),
            },
        }

    # ---------------------------------
    # Full Export
    # ---------------------------------

    def export(self, filepath="data/representations.json"):
        stages = self.extract_representations()
        weights = self.extract_weights()

        colors = [
            "#E74C3C" if label == 0 else "#3498DB"
            for label in self.dataset_labels.tolist()
        ]

        data = {
            "metadata": {
                "architecture": [2, self.hidden_dim, 1],
                "activations": ["relu", "sigmoid"],
                "dataset": "spread_xor",
                "points_per_class": len(self.dataset_labels) // 2,
                "grid_size": self.grid_size,
                "grid_range": list(self.grid_range),
                "seed": self.seed,
            },
            "dataset": {
                "labels": self.dataset_labels.tolist(),
                "colors": colors,
            },
            "stages": stages,
            "weights": weights,
            "training": {
                "loss_history": self.loss_history,
            },
            "predictions": {
                "probabilities": stages[-1].get("outputs", []),
                "predicted_labels": [
                    1 if p > 0.5 else 0
                    for p in stages[-1].get("outputs", [])
                ],
            },
        }

        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

        print(f"Exported to {filepath}")
        return self


# ---------------------------------
# CLI
# ---------------------------------

if __name__ == "__main__":

    exporter = RepresentationExporter(
        hidden_dim=3,
        grid_size=15,
        seed=42,
        mode="educational",
    )

    exporter.generate_xor()
    exporter.generate_grid()
    exporter.build_model()

    if exporter.mode == "trained":
        exporter.train(epochs=2000)

    exporter.export("data/representations.json")