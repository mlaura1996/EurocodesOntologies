from rdflib import Graph, Namespace, Literal, URIRef, BNode
import pandas as pd

# Create a new graph
g = Graph()

#ontology ref specification
base_url = "https://random-url-to-your-data.com/data#"
ref = URIRef(base_url)

# Create a namespaces for the ontology
INST = Namespace(ref)
C = Namespace("https://w3id.org/conprop#")
DOT = Namespace("https://w3id.org/dot#")
CC = Namespace('http://creativecommons.org/ns#')
DCE = Namespace("http://purl.org/dc/elements/1.1/")
VANN = Namespace("http://purl.org/vocab/vann/")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
SEAS = Namespace("http://www.w3id.org/seas/FeatureOfInterestOntology#")
EV = Namespace("https://w3id.org/seas/EvaluationOntology#")
MAT = Namespace("http://bimerr.iot.linkeddata.es/def/material-properties#")
SAREF = Namespace("https://w3id.org/saref#")
MMO = Namespace("https://w3id.org/pmd/materials-mechanics-ontology/")
OM = Namespace("http://www.ontology-of-units-of-measure.org/resource/om-2/")

# Bind your custom prefixes
g.bind("conProp", C)
g.bind("mat", MAT)
g.bind("data", INST)
g.bind('dot', DOT)
g.bind('rdf', RDF)
g.bind('rdfs', RDFS)
g.bind('owl', OWL)
g.bind('vann', VANN)
g.bind('xsd', XSD)
g.bind('cc', CC)
g.bind('dce', DCE)
g.bind("seas", SEAS)
g.bind("saref", SAREF)
g.bind("mmo", MMO)
g.bind("om", OM)

# Read the Excel file
excel_file = "resources/External/data for Concrete Properties Ontology.xlsx"
poc = pd.read_excel(excel_file, header=None, sheet_name="Properties of Components")
cc = pd.read_excel(excel_file, header=None, sheet_name="Concrete Composition")
cmq = pd.read_excel(excel_file, header=None, sheet_name="Concrete Mix Quantity")
cp = pd.read_excel(excel_file, header=None, sheet_name="Concrete Properties")

#Add material properties to general components
material_properties = poc[0]
units = poc[1]

for i in range(2,poc.shape[1]): 
    component = INST[poc[i][1]]
    g.add((component, RDF.type, C[poc[i][0]]))

    for j in range(2,poc.shape[0]):
        if not pd.isna(poc[i][j]):
            material_property = INST[poc[i][1]+'-'+str(material_properties[j])]
            g.add((material_property, RDF.type, MMO[material_properties[j]]))
            g.add((component, C.hasMaterialProperty, material_property))
            g.add((material_property, SAREF.hasValue, Literal(poc[i][j])))
            g.add((material_property, OM.hasUnit , OM[units[j]]))

#Create concrete types instances and link their components components
for i in range(cc.shape[1]):
    concrete_name = cc[i][0]
    g.add((INST[concrete_name], RDF.type, MAT.Concrete))
    for j in range(1,cc.shape[0]):
        g.add((INST[concrete_name], C.isMadeOfComponentMaterial, INST[cc[i][j]]))




# Assign quantities to each  of the components of the concrete instances
quantity_classes =  cmq[0]
units = cmq[3]


for i in range(1,cmq.shape[1]-1):
    concrete_name = cmq[i][0]
    print("-------"+concrete_name+"----------")
    for j in range(1, cmq.shape[0]):
        if not pd.isna(cmq[i][j]):
            print(concrete_name,quantity_classes[j] )
            component_quantity = INST[concrete_name+'-'+quantity_classes[j]]
            print(component_quantity)
            g.add((component_quantity, RDF.type, INST[quantity_classes[j]]))
            g.add((INST[concrete_name], C.hasComponentQuantity, component_quantity))
            g.add((component_quantity, SAREF.hasValue, Literal(cmq[i][j])))
            g.add((component_quantity, OM.hasUnit, OM[units[j]]))      
    for k in range(1,cp.shape[0]):
        property_instance = INST[concrete_name+cp[0][k]]
        g.add((property_instance, RDF.type, MMO[cp[0][k]]))
        g.add((INST[concrete_name], C.hasMaterialProperty, property_instance))
        g.add((property_instance, OM.hasUnit, OM[cp[1][k]]))


path = 'test.ttl'
g.serialize(destination= path , format ='turtle')

