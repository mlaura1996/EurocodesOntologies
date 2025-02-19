from core.config import rdflibgraph

def convert_ttl_to_owl(input_ttl, output_owl):
    """ Converts a TTL ontology to OWL (RDF/XML) format """
    g = rdflibgraph()
    g.parse(input_ttl, format="turtle")
    g.serialize(output_owl, format="xml")
    print(f"✅ Converted: {input_ttl} → {output_owl}")

def convert_owl_to_ttl(input_owl, output_ttl):
    """ Converts a OWL (RDF/XML) ontology to TTL format """
    g = rdflibgraph()
    g.parse(input_owl, format="xml")
    g.serialize(output_ttl, format="turtle")
    print(f"✅ Converted: {input_owl} → {output_ttl}")