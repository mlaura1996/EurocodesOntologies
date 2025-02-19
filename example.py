from core.config import os
from utils.converters import convert_ttl_to_owl, convert_owl_to_ttl
from owlready2 import *
from utils.comparisons import compare_graphs

# ✅ 1️⃣ Ensure Temp Directory is Set for Owlready2
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)  # Create if it doesn't exist
os.environ["OWLREADY2_TMPDIR"] = TEMP_DIR  # Set for Owlready2


# ✅ 2️⃣ Convert Ontology and Test Data
convert_ttl_to_owl("resources/Ontologies/ConProp_v01.ttl", 
                   "output/ConProp_v01.owl")

convert_ttl_to_owl("resources/Graph_data/test-data.ttl", 
                   "output/test-data.owl")

convert_ttl_to_owl("resources/Rules/ConProp_SWRLrules.ttl", 
                   "output/test-rules.owl")


# # ✅ 3️⃣ Load Ontologies with Full Path
ontology_path = "output/ConProp_v01.owl"
test_data_path = "output/test-data.owl"
rules_path = "output/test-rules.owl"

onto = get_ontology(ontology_path).load()
test_data = get_ontology(test_data_path).load()
rules = get_ontology(rules_path).load()

# ✅ 4️⃣ Remove any broken imports to avoid missing ontology errors
onto.imported_ontologies = [o for o in onto.imported_ontologies if o.base_iri.startswith("file://")]

# ✅ 5️⃣ Merge test data and rules into the main ontology
#onto.imported_ontologies.append(test_data)
#onto.imported_ontologies.append(rules)

# ✅ 6️⃣ Run Pellet Reasoner (without ignore_imports)
try:
    sync_reasoner_pellet(infer_property_values=True)  # Removed "ignore_imports"
    print("✅ Pellet Reasoning Completed Successfully!")
except OwlReadyInconsistentOntologyError:
    print("❌ Ontology is inconsistent! Running Pellet explain...\n")

    # Debug inconsistent classes
    for cls in list(default_world.inconsistent_classes()):
        print(f"Inconsistent Class: {cls}")

# # 🟢 Save the updated ontology with inferred knowledge
# reasoned_ontology_path = "output/reasoned_ontology.owl"  # Save as OWL file
# onto.save(file=reasoned_ontology_path, format="rdfxml")  # RDF/XML format

# print(f"✅ Reasoned ontology saved to: {reasoned_ontology_path}")

# #Compare graphs 

# compare_graphs("output/test-data.owl", "output/reasoned_ontology.owl")
# convert_owl_to_ttl("output/reasoned_ontology.owl", "output/reasoned_ontology.ttl")


