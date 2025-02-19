from owlready2 import *

# Access the ontology
onto = get_ontology("https://w3id.org/hmo#").load()

# Convert the generator to a list
classes_list = list(onto.classes())



# Define a masonry wall instance
with onto:
    wall1 = onto.MasonryWall("Wall_001")
    # Define Representative Volume Elements (RVE) and add them
    rve1 = onto.RepresentativeVolumeElement("RVE_001")
    wall1.hasRepresentativeVolumeElement.append(rve1)

    # Define a pattern and associate it
    pattern1 = onto.Pattern("Pattern_001")
    rve1.hasPattern.append(pattern1)

    # Define joints (mortar, vertical, horizontal)
    mortar_joint = onto.MortarJoints("MortarJoint_001")
    vertical_joint = onto.VerticalJoints("VerticalJoint_001")
    horizontal_joint = onto.HorizontalJoints("HorizontalJoint_001")

    pattern1.hasDominantPatternEntities.extend([mortar_joint, vertical_joint, horizontal_joint])

# **Run Pellet Reasoner** to infer masonry quality
sync_reasoner_pellet(infer_property_values=True)

# Query inferred masonry quality properties
print(f"Masonry Quality Index of Wall_001: {wall1.hasMasonryQualityIndex}")
print(f"Mortar Quality (Out of Plane): {wall1.MQIMortarQualityOutOfPlane}")
print(f"Wall Dimensions Vertical: {wall1.UnitsDimensionsVertical}")

# # Run Pellet reasoner to infer mechanical properties
sync_reasoner_pellet(infer_property_values=True)
print(list(rve1.get_properties()))


#sync_reasoner_pellet(debug=4)
