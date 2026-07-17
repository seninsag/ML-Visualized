from objects.representation_sequence import RepresentationSequence

rep = RepresentationSequence("data/representations.json")

print("Stages:", rep.stage_names())
print("Current:", rep.current.name)

rep.next()
print("Next:", rep.current.name)

relu = rep.get("relu")

print("ReLU stage")
print("Input dimension:", relu.input_dimension)
print("Output dimension:", relu.output_dimension)
print("Number of points:", len(relu.points))
print("Grid shape:", relu.grid["shape"])