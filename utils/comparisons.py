from rdflib import Graph

def compare_graphs(original_file, reasoned_file):
    """
    Compare two RDF graphs and print the triples that exist in the reasoned graph 
    but not in the original graph.

    :param original_file: Filename of the original ontology file (.ttl or .owl)
    :param reasoned_file: Filename of the reasoned ontology file (.ttl or .owl)
    """
    # Load both graphs
    original_graph = Graph()
    reasoned_graph = Graph()

    # Determine file format based on extension
    file_format = "turtle" if original_file.endswith(".ttl") else "xml"

    # Parse both graphs
    original_graph.parse(original_file, format=file_format)
    reasoned_graph.parse(reasoned_file, format=file_format)

    # Compute the difference (inferred triples)
    inferred_triples = reasoned_graph - original_graph

    # Print new inferred triples
    print("\n🔍 New Inferred Triples:")
    if inferred_triples:
        for subj, pred, obj in inferred_triples:
            print(f"➕ {subj} {pred} {obj}")
    else:
        print("✅ No new inferred triples found.")

    return inferred_triples




