from owlready2 import *
from rdflib import Graph as rdflibgraph
import os

# ✅ 1️⃣ Ensure Temp Directory is Set for Owlready2
TEMP_DIR = "C:/Users/mlaur/AppData/Local/Temp/Owlready2"
os.makedirs(TEMP_DIR, exist_ok=True)  # Create if it doesn't exist
os.environ["OWLREADY2_TMPDIR"] = TEMP_DIR  # Set for Owlready2

def convert_ttl_to_owl(input_ttl, output_owl):
    """ Converts a TTL ontology to OWL (RDF/XML) format """
    g = rdflibgraph()
    g.parse(input_ttl, format="turtle")
    g.serialize(output_owl, format="xml")
    print(f"✅ Converted: {input_ttl} → {output_owl}")

# ✅ 2️⃣ Convert Ontology and Test Data
convert_ttl_to_owl("workflow-test/Concrete_Properties_OntologyV18_minimal.ttl", 
                   "workflow-test/Concrete_Properties_OntologyV18_minimal.owl")

convert_ttl_to_owl("workflow-test/test-data-cleaned.ttl", 
                   "workflow-test/test-data.owl")

# ✅ 3️⃣ Load Ontologies with Full Path
ontology_path = "file://C:/Users/mlaur/Documents/01.1_PhD/12_Collaborations/Agnieska/EurocodesOntologies/workflow-test/Concrete_Properties_OntologyV18_minimal.owl"
test_data_path = "file://C:/Users/mlaur/Documents/01.1_PhD/12_Collaborations/Agnieska/EurocodesOntologies/workflow-test/test-data.owl"

onto = get_ontology(ontology_path).load()
test_data = get_ontology(test_data_path).load()

# ✅ 4️⃣ Remove any broken imports to avoid missing ontology errors
onto.imported_ontologies = [o for o in onto.imported_ontologies if o.base_iri.startswith("file://")]

# ✅ 5️⃣ Merge test data into the main ontology
onto.imported_ontologies.append(test_data)

# ✅ 6️⃣ Run Pellet Reasoner (without ignore_imports)
try:
    sync_reasoner_pellet(infer_property_values=True)  # Removed "ignore_imports"
    print("✅ Pellet Reasoning Completed Successfully!")
except OwlReadyInconsistentOntologyError:
    print("❌ Ontology is inconsistent! Running Pellet explain...\n")

    # Debug inconsistent classes
    for cls in list(default_world.inconsistent_classes()):
        print(f"Inconsistent Class: {cls}")




