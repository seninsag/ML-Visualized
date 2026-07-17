from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Stage:
    """Represents one transformation stage of the neural network."""

    name: str
    type: str
    index: int

    input_dimension: int
    output_dimension: int

    points: list
    grid: dict

    activation: str | None = None
    outputs: list | None = None


class RepresentationSequence:
    """
    Loads exported representations and provides convenient access
    for Manim animations.
    """

    def __init__(self, json_path: str | Path):

        self.json_path = Path(json_path)

        with open(self.json_path, "r") as f:
            self.data = json.load(f)

        self.metadata = self.data["metadata"]
        self.dataset = self.data["dataset"]
        self.weights = self.data["weights"]
        self.training = self.data["training"]
        self.predictions = self.data["predictions"]

        self.stages = [
            Stage(**stage)
            for stage in self.data["stages"]
        ]

        self._current = 0

    # -------------------------------------------------------
    # Properties
    # -------------------------------------------------------

    @property
    def current(self) -> Stage:
        return self.stages[self._current]

    @property
    def num_stages(self):
        return len(self.stages)

    # -------------------------------------------------------
    # Navigation
    # -------------------------------------------------------

    def reset(self):
        self._current = 0
        return self.current

    def next(self):

        if self._current < len(self.stages) - 1:
            self._current += 1

        return self.current

    def previous(self):

        if self._current > 0:
            self._current -= 1

        return self.current

    # -------------------------------------------------------
    # Lookup
    # -------------------------------------------------------

    def get(self, name: str) -> Stage:

        for stage in self.stages:
            if stage.name == name:
                return stage

        raise KeyError(f"Stage '{name}' not found.")

    def by_index(self, index: int) -> Stage:

        return self.stages[index]

    # -------------------------------------------------------
    # Convenience
    # -------------------------------------------------------

    def stage_names(self):

        return [stage.name for stage in self.stages]

    def __len__(self):

        return len(self.stages)

    def __iter__(self):

        return iter(self.stages)