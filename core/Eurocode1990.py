from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, OWL, VANN, DCTERMS, XSD, SKOS
import os

# Define the main namespace and save path
ref = URIRef("http://www.w3id.org/Eurocodes/EC1990#")
save_folder = 'ontologies'
save_filename = 'EC1990.ttl'

# Create ontologies folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

save_path = os.path.join(save_folder, save_filename)

# Instantiate empty graph for the ontology
g = Graph()

# Create namespaces
EC1990 = Namespace(ref)
BOT = Namespace('https://w3id.org/bot#')
CC = Namespace('http://creativecommons.org/ns#')
QUDT = Namespace('http://qudt.org/3.1.2/schema/qudt/')
UNIT = Namespace('http://qudt.org/3.1.2/vocab/unit/')
QUANTITYKIND = Namespace('http://qudt.org/3.1.2/vocab/quantitykind/')

# Bind prefixes
g.bind("ec", EC1990)
g.bind('rdf', RDF)
g.bind('rdfs', RDFS)
g.bind('owl', OWL)
g.bind('xsd', XSD)
g.bind('skos', SKOS)
g.bind('bot', BOT)
g.bind('cc', CC)
g.bind('qudt', QUDT)
g.bind('unit', UNIT)
g.bind('quantitykind',QUANTITYKIND)

# Add improved ontology header triples
g.add((ref, RDF.type, OWL.Ontology))
g.add((ref, DCTERMS.creator, Literal('Carlos Ramonell Cazador (carlos.ramonell@upc.edu), Agnieszka Jędrzejewska (agnieszka.jedrzejewska@polsl.pl) and Maria Laura Leonardi (mlauraleonardi@gmail.com)')))
g.add((ref, DCTERMS.date, Literal('2025-06-30', datatype=XSD.date)))
g.add((ref, DCTERMS.modified, Literal('2025-06-30', datatype=XSD.date)))
g.add((ref, DCTERMS.title, Literal('ECO - Eurocode Core Ontology')))
g.add((ref, DCTERMS.description, Literal("Core ontology formalising knowledge from Eurocode 0 for automated structural design and verification")))
g.add((ref, DCTERMS.format, Literal('ttl')))
g.add((ref, DCTERMS.language, Literal('en')))
g.add((ref, OWL.versionInfo, Literal('1.0.0')))
g.add((ref, VANN.preferredNamespacePrefix, Literal('ec')))
g.add((ref, VANN.preferredNamespaceUri, Literal(ref)))
g.add((ref, CC.license, Literal('http://creativecommons.org/licenses/by/3.0/')))
g.add((ref, OWL.imports, URIRef('https://www.w3id.org/bot')))

##########################################################
#                       CORE CLASSES                    #
##########################################################

# Construction Works
g.add((EC1990['ConstructionWork'], RDF.type, OWL.Class))
g.add((EC1990['ConstructionWork'], RDFS.label, Literal('Construction Works', lang='en')))
g.add((EC1990['ConstructionWork'], RDFS.comment, Literal('Everything that is constructed or results from construction operations. The term covers both building and civil engineering works comprising structural, non-structural and geotechnical elements.', lang='en')))
g.add((EC1990['ConstructionWork'], SKOS.definition, Literal('Everything that is constructed or results from construction operations. The term covers both building and civil engineering works comprising structural, non-structural and geotechnical elements.')))
g.add((EC1990['ConstructionWork'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.1')))
g.add((EC1990['ConstructionWork'], SKOS.example, Literal('building, bridge, nuclea power plant')))

g.add((EC1990['Building'], RDF.type, OWL.Class))
g.add((EC1990['Building'], RDFS.subClassOf, EC1990.ConstructionWork))
g.add((EC1990['Building'], OWL.sameAs, BOT.Building))
g.add((EC1990['Building'], RDFS.label, Literal('Building', lang='en')))
g.add((EC1990['Building'], RDFS.comment, Literal('Type of construction work for building purposes such as dwelling houses, office buildings, etc.', lang='en')))
g.add((EC1990['Building'], SKOS.definition, Literal('Type of construction work for building purposes such as dwelling houses, office buildings, etc.')))
g.add((EC1990['Building'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.2')))
g.add((EC1990['Building'], SKOS.example, Literal('dwelling house, office building, industrial building')))

g.add((EC1990['ResidentialBuilding'], RDF.type, OWL.Class))
g.add((EC1990['ResidentialBuilding'], RDFS.subClassOf, EC1990.Building))
g.add((EC1990['ResidentialBuilding'], RDFS.label, Literal('Residential Building', lang='en')))
g.add((EC1990['ResidentialBuilding'], RDFS.comment, Literal('Building intended primarily for the accommodation and permanent or temporary residence of individuals or households.', lang='en')))
g.add((EC1990['ResidentialBuilding'], SKOS.definition, Literal('Building intended primarily for the accommodation and permanent or temporary residence of individuals or households.')))
g.add((EC1990['ResidentialBuilding'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.2')))
g.add((EC1990['ResidentialBuilding'], SKOS.example, Literal('detached house, apartment building, high-rise residential tower')))

g.add((EC1990['CivilEngineeringWork'], RDF.type, OWL.Class))
g.add((EC1990['CivilEngineeringWork'], RDFS.subClassOf, EC1990.ConstructionWork))
g.add((EC1990['CivilEngineeringWork'], RDFS.label, Literal('Civil Engineering Work', lang='en')))
g.add((EC1990['CivilEngineeringWork'], RDFS.comment, Literal('Type of construction work for civil engineering purposes such as bridges, retaining walls, etc.', lang='en')))
g.add((EC1990['CivilEngineeringWork'], SKOS.definition, Literal('Type of construction work for civil engineering purposes such as bridges, retaining walls, etc.')))
g.add((EC1990['CivilEngineeringWork'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.2')))
g.add((EC1990['CivilEngineeringWork'], SKOS.example, Literal('bridge, retaining wall, tunnel')))

g.add((EC1990['StructuralMember'], RDF.type, OWL.Class))
g.add((EC1990['StructuralMember'], RDFS.subClassOf, BOT.Element))
g.add((EC1990['StructuralMember'], RDFS.label, Literal('Structural Member', lang='en')))
g.add((EC1990['StructuralMember'], RDFS.comment, Literal('Physically distinguishable part of a structure, e.g. a column, a beam, a slab, a foundation pile.', lang='en')))
g.add((EC1990['StructuralMember'], SKOS.definition, Literal('Physically distinguishable part of a structure, e.g. a column, a beam, a slab, a foundation pile.')))
g.add((EC1990['StructuralMember'], DCTERMS.source, Literal('EN 1990:200, Section 1.5.1.7')))
g.add((EC1990['StructuralMember'], SKOS.example, Literal('column, beam, slab, foundation pile')))

g.add((EC1990['EurocodeZone'], RDF.type, OWL.Class))
g.add((EC1990['EurocodeZone'], RDFS.subClassOf, BOT.Zone))
g.add((EC1990['EurocodeZone'], RDFS.label, Literal('Eurocode Zone', lang='en')))
g.add((EC1990['EurocodeZone'], RDFS.comment, Literal('A space classified according to EN 1991-1-1 usage categories', lang='en')))
g.add((EC1990['EurocodeZone'], SKOS.definition, Literal('A space classified according to EN 1991-1-1 usage categories')))
g.add((EC1990['EurocodeZone'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))

# Eurocode-specified categories of areas by use
# Category A - Domestic and Residential
g.add((EC1990['Residential'], RDF.type, OWL.Class))
g.add((EC1990['Residential'], RDFS.subClassOf, EC1990['EurocodeZone']))
g.add((EC1990['Residential'], RDFS.label, Literal('Category A - Domestic and Residential', lang='en')))
g.add((EC1990['Residential'], RDFS.comment, Literal('Area for domestic and residential activities', lang='en')))
g.add((EC1990['Residential'], SKOS.definition, Literal('Area for domestic and residential activities')))
g.add((EC1990['Residential'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['Residential'], SKOS.example, Literal('rooms in residential buildings and houses, bedrooms and wards in hospitals, bedrooms in hotels and hostels, kitchens and toilets')))

# Category B - Office Areas
g.add((EC1990['OfficeArea'], RDF.type, OWL.Class))
g.add((EC1990['OfficeArea'], RDFS.subClassOf, EC1990['EurocodeZone']))
g.add((EC1990['OfficeArea'], RDFS.label, Literal('Category B - Office Areas', lang='en')))
g.add((EC1990['OfficeArea'], RDFS.comment, Literal('Office area', lang='en')))
g.add((EC1990['OfficeArea'], SKOS.definition, Literal('Office area')))
g.add((EC1990['OfficeArea'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['OfficeArea'], SKOS.example, Literal('General office spaces')))

# Category C - Congregation Areas (with subcategories)
g.add((EC1990['CongregationArea'], RDF.type, OWL.Class))
g.add((EC1990['CongregationArea'], RDFS.subClassOf, EC1990['EurocodeZone']))
g.add((EC1990['CongregationArea'], RDFS.label, Literal('Category C - Congregation Areas', lang='en')))
g.add((EC1990['CongregationArea'], RDFS.comment, Literal('Area where people may congregate (except areas under category A, B, and D)', lang='en')))
g.add((EC1990['CongregationArea'], SKOS.definition, Literal('Area where people may congregate (except areas under category A, B, and D)')))
g.add((EC1990['CongregationArea'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))

# Category C1
g.add((EC1990['AreaWithTables'], RDF.type, OWL.Class))
g.add((EC1990['AreaWithTables'], RDFS.subClassOf, EC1990['CongregationArea']))
g.add((EC1990['AreaWithTables'], RDFS.label, Literal('Category C1 - Areas with tables', lang='en')))
g.add((EC1990['AreaWithTables'], RDFS.comment, Literal('Area with tables', lang='en')))
g.add((EC1990['AreaWithTables'], SKOS.definition, Literal('Area with tables')))
g.add((EC1990['AreaWithTables'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['AreaWithTables'], SKOS.example, Literal('areas in schools, cafés, restaurants, dining halls, reading rooms, receptions')))

# Category C2
g.add((EC1990['AreasWithFixedSeats'], RDF.type, OWL.Class))
g.add((EC1990['AreasWithFixedSeats'], RDFS.subClassOf, EC1990['CongregationArea']))
g.add((EC1990['AreasWithFixedSeats'], RDFS.label, Literal('Category C2 - Areas with fixed seats', lang='en')))
g.add((EC1990['AreasWithFixedSeats'], RDFS.comment, Literal('Area with fixed seats', lang='en')))
g.add((EC1990['AreasWithFixedSeats'], SKOS.definition, Literal('Area with fixed seats')))
g.add((EC1990['AreasWithFixedSeats'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['AreasWithFixedSeats'], SKOS.example, Literal('areas in churches, theatres or cinemas, conference rooms, lecture halls, assembly halls, waiting rooms, railway waiting rooms')))

# Category C3
g.add((EC1990['AreasWithoutObstacle'], RDF.type, OWL.Class))
g.add((EC1990['AreasWithoutObstacle'], RDFS.subClassOf, EC1990['CongregationArea']))
g.add((EC1990['AreasWithoutObstacle'], RDFS.label, Literal('Category C3 - Areas without obstacles', lang='en')))
g.add((EC1990['AreasWithoutObstacle'], RDFS.comment, Literal('Area without obstacles for moving people', lang='en')))
g.add((EC1990['AreasWithoutObstacle'], SKOS.definition, Literal('Area without obstacles for moving people')))
g.add((EC1990['AreasWithoutObstacle'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['AreasWithoutObstacle'], SKOS.example, Literal('areas in museums, exhibition rooms, etc. and access areas in public and administration buildings, hotels, hospitals, railway station forecourts')))

# Category C4
g.add((EC1990['PhysicalActivitiesAreas'], RDF.type, OWL.Class))
g.add((EC1990['PhysicalActivitiesAreas'], RDFS.subClassOf, EC1990['CongregationArea']))
g.add((EC1990['PhysicalActivitiesAreas'], RDFS.label, Literal('Category C4 - Physical activities areas', lang='en')))
g.add((EC1990['PhysicalActivitiesAreas'], RDFS.comment, Literal('Area with possible physical activities', lang='en')))
g.add((EC1990['PhysicalActivitiesAreas'], SKOS.definition, Literal('Area with possible physical activities')))
g.add((EC1990['PhysicalActivitiesAreas'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['PhysicalActivitiesAreas'], SKOS.example, Literal('dance halls, gymnastic rooms, stages')))

# Category C5
g.add((EC1990['LargeCrowdsAreas'], RDF.type, OWL.Class))
g.add((EC1990['LargeCrowdsAreas'], RDFS.subClassOf, EC1990['CongregationArea']))
g.add((EC1990['LargeCrowdsAreas'], RDFS.label, Literal('Category C5 - Large crowds areas', lang='en')))
g.add((EC1990['LargeCrowdsAreas'], RDFS.comment, Literal('Area susceptible to large crowds', lang='en')))
g.add((EC1990['LargeCrowdsAreas'], SKOS.definition, Literal('Area susceptible to large crowds')))
g.add((EC1990['LargeCrowdsAreas'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['LargeCrowdsAreas'], SKOS.example, Literal('buildings for public events like concert halls, sports halls including stands, terraces and access areas and railway platforms')))

# Category D - Shopping Areas
g.add((EC1990['ShoppingAreas'], RDF.type, OWL.Class))
g.add((EC1990['ShoppingAreas'], RDFS.subClassOf, EC1990['EurocodeZone']))
g.add((EC1990['ShoppingAreas'], RDFS.label, Literal('Category D - Shopping Areas', lang='en')))
g.add((EC1990['ShoppingAreas'], RDFS.comment, Literal('Shopping area', lang='en')))
g.add((EC1990['ShoppingAreas'], SKOS.definition, Literal('Shopping area')))
g.add((EC1990['ShoppingAreas'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))

# Category D1 - General retail shops
g.add((EC1990['GeneralRetailShops'], RDF.type, OWL.Class))
g.add((EC1990['GeneralRetailShops'], RDFS.subClassOf, EC1990['ShoppingAreas']))
g.add((EC1990['GeneralRetailShops'], RDFS.label, Literal('Category D1 - General retail shops', lang='en')))
g.add((EC1990['GeneralRetailShops'], RDFS.comment, Literal('Area in general retail shops', lang='en')))
g.add((EC1990['GeneralRetailShops'], SKOS.definition, Literal('Area in general retail shops')))
g.add((EC1990['GeneralRetailShops'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['GeneralRetailShops'], SKOS.example, Literal('general retail shops')))

# Category D2 - Department stores
g.add((EC1990['DepartmentStore'], RDF.type, OWL.Class))
g.add((EC1990['DepartmentStore'], RDFS.subClassOf, EC1990['ShoppingAreas']))
g.add((EC1990['DepartmentStore'], RDFS.label, Literal('Category D2 - Department stores', lang='en')))
g.add((EC1990['DepartmentStore'], RDFS.comment, Literal('Area in department stores', lang='en')))
g.add((EC1990['DepartmentStore'], SKOS.definition, Literal('Area in department stores')))
g.add((EC1990['DepartmentStore'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['DepartmentStore'], SKOS.example, Literal('department stores')))

# Category E - Storage and Industrial
g.add((EC1990['IndustrialandStorage'], RDF.type, OWL.Class))
g.add((EC1990['IndustrialandStorage'], RDFS.subClassOf, EC1990['EurocodeZone']))
g.add((EC1990['IndustrialandStorage'], RDFS.label, Literal('Category E - Storage and Industrial', lang='en')))
g.add((EC1990['IndustrialandStorage'], RDFS.comment, Literal('Storage and industrial area', lang='en')))
g.add((EC1990['IndustrialandStorage'], SKOS.definition, Literal('Storage and industrial area')))
g.add((EC1990['IndustrialandStorage'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.3')))

# Category E1
g.add((EC1990['StorageAreas'], RDF.type, OWL.Class))
g.add((EC1990['StorageAreas'], RDFS.subClassOf, EC1990['IndustrialandStorage']))
g.add((EC1990['StorageAreas'], RDFS.label, Literal('Category E1 - Storage areas', lang='en')))
g.add((EC1990['StorageAreas'], RDFS.comment, Literal('Area susceptible to accumulation of goods, including access areas', lang='en')))
g.add((EC1990['StorageAreas'], SKOS.definition, Literal('Area susceptible to accumulation of goods, including access areas')))
g.add((EC1990['StorageAreas'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.3')))
g.add((EC1990['StorageAreas'], SKOS.example, Literal('areas for storage use including storage of books and other documents: archives, libraries, stockrooms')))

# Category E2
g.add((EC1990['IndustrialUse'], RDF.type, OWL.Class))
g.add((EC1990['IndustrialUse'], RDFS.subClassOf, EC1990['IndustrialandStorage']))
g.add((EC1990['IndustrialUse'], RDFS.label, Literal('Category E2 - Industrial use', lang='en')))
g.add((EC1990['IndustrialUse'], RDFS.comment, Literal('Industrial use area', lang='en')))
g.add((EC1990['IndustrialUse'], SKOS.definition, Literal('Industrial use area')))
g.add((EC1990['IndustrialUse'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.3')))
g.add((EC1990['IndustrialUse'], SKOS.example, Literal('industrial facilities: plant rooms, workshops')))

# Category F - Light Vehicle Traffic
g.add((EC1990['LightVehicleTraffic'], RDF.type, OWL.Class))
g.add((EC1990['LightVehicleTraffic'], RDFS.subClassOf, EC1990['EurocodeZone']))
g.add((EC1990['LightVehicleTraffic'], RDFS.label, Literal('Category F - Light Vehicle Traffic', lang='en')))
g.add((EC1990['LightVehicleTraffic'], RDFS.comment, Literal('Traffic and parking area for light vehicles (≤ 30 kN gross vehicle weight and ≤ 8 seats not including driver)', lang='en')))
g.add((EC1990['LightVehicleTraffic'], SKOS.definition, Literal('Traffic and parking area for light vehicles (≤ 30 kN gross vehicle weight and ≤ 8 seats not including driver)')))
g.add((EC1990['LightVehicleTraffic'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.7')))
g.add((EC1990['LightVehicleTraffic'], SKOS.example, Literal('garages, parking areas, parking halls')))

# Category G - Medium Vehicle Traffic
g.add((EC1990['MediumVehicleTraffic'], RDF.type, OWL.Class))
g.add((EC1990['MediumVehicleTraffic'], RDFS.subClassOf, EC1990['EurocodeZone']))
g.add((EC1990['MediumVehicleTraffic'], RDFS.label, Literal('Category G - Medium Vehicle Traffic', lang='en')))
g.add((EC1990['MediumVehicleTraffic'], RDFS.comment, Literal('Traffic and parking area for medium vehicles (>30 kN, ≤ 160 kN gross vehicle weight, on 2 axles)', lang='en')))
g.add((EC1990['MediumVehicleTraffic'], SKOS.definition, Literal('Traffic and parking area for medium vehicles (>30 kN, ≤ 160 kN gross vehicle weight, on 2 axles)')))
g.add((EC1990['MediumVehicleTraffic'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.7')))
g.add((EC1990['MediumVehicleTraffic'], SKOS.example, Literal('access routes, delivery zones, zones accessible to fire engines (≤ 160 kN gross vehicle weight)')))

# Category H - Roofs
g.add((EC1990['Roof'], RDF.type, OWL.Class))
g.add((EC1990['Roof'], RDFS.subClassOf, EC1990['EurocodeZone']))
g.add((EC1990['Roof'], RDFS.label, Literal('Category H - Roofs', lang='en')))
g.add((EC1990['Roof'], RDFS.comment, Literal('Roof not accessible except for normal maintenance and repair', lang='en')))
g.add((EC1990['Roof'], SKOS.definition, Literal('Roof not accessible except for normal maintenance and repair')))
g.add((EC1990['Roof'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.9')))
g.add((EC1990['Roof'], SKOS.example, Literal('roofs accessible only for maintenance')))

# Category I - Accessible Roofs
g.add((EC1990['AccessibleRoofs'], RDF.type, OWL.Class))
g.add((EC1990['AccessibleRoofs'], RDFS.subClassOf, EC1990['EurocodeZone']))
g.add((EC1990['AccessibleRoofs'], RDFS.label, Literal('Category I - Accessible Roofs', lang='en')))
g.add((EC1990['AccessibleRoofs'], RDFS.comment, Literal('Roof accessible with occupancy according to categories A to G', lang='en')))
g.add((EC1990['AccessibleRoofs'], SKOS.definition, Literal('Roof accessible with occupancy according to categories A to G')))
g.add((EC1990['AccessibleRoofs'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.9')))
g.add((EC1990['AccessibleRoofs'], SKOS.example, Literal('Roof used as terraces, gardens, or other occupied spaces')))

# Category K - Helicopter Landing Areas
g.add((EC1990['HelicopterLandingAreas'], RDF.type, OWL.Class))
g.add((EC1990['HelicopterLandingAreas'], RDFS.subClassOf, EC1990['EurocodeZone']))
g.add((EC1990['HelicopterLandingAreas'], RDFS.label, Literal('Category K - Helicopter Landing Areas', lang='en')))
g.add((EC1990['HelicopterLandingAreas'], RDFS.comment, Literal('Roof accessible for special services, such as helicopter landing areas', lang='en')))
g.add((EC1990['HelicopterLandingAreas'], SKOS.definition, Literal('Roof accessible for special services, such as helicopter landing areas')))
g.add((EC1990['HelicopterLandingAreas'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.9')))
g.add((EC1990['HelicopterLandingAreas'], SKOS.example, Literal('helicopter landing pads on roofs')))

# Structure-related classes
g.add((EC1990['Structure'], RDF.type, OWL.Class))
g.add((EC1990['Structure'], RDFS.label, Literal('Structure', lang='en')))
g.add((EC1990['Structure'], RDFS.comment, Literal('Organised combination of connected parts designed to carry loads and provide adequate rigidity.', lang='en')))
g.add((EC1990['Structure'], SKOS.definition, Literal('Organised combination of connected parts designed to carry loads and provide adequate rigidity.')))
g.add((EC1990['Structure'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.6')))
g.add((EC1990['Structure'], SKOS.example, Literal('Residential building, reatining wall, suspension bridge, underground tunnel')))

# Classification of structures accordin to the design service life
g.add((EC1990['TemporaryStructure'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['TemporaryStructure'], RDF.type, EC1990.Structure))
g.add((EC1990['TemporaryStructure'], RDFS.label, Literal('Temporary Structure', lang='en')))
g.add((EC1990['TemporaryStructure'], RDFS.comment, Literal('Structre that is intended to be used for a limited period of time, typically to support, protect, or provide access during the execution of permanent works, or to serve a short-term purpose.', lang='en')))
g.add((EC1990['TemporaryStructure'], SKOS.definition, Literal('Structre that is intended to be used for a limited period of time, typically to support, protect, or provide access during the execution of permanent works, or to serve a short-term purpose.')))
g.add((EC1990['TemporaryStructure'], DCTERMS.source, Literal('EN 1990:2002, Table 2.1')))
g.add((EC1990['TemporaryStructure'], SKOS.example, Literal('formwork system, steel scaffolding, temoprary bridge')))

g.add((EC1990['ReplacableStructuralElements'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['ReplacableStructuralElements'], RDF.type, EC1990.Structure))
g.add((EC1990['ReplacableStructuralElements'], RDFS.label, Literal('Structure with replaceable elements', lang='en')))
g.add((EC1990['ReplacableStructuralElements'], RDFS.comment, Literal('structure designed such that certain primary or secondary structural components can be removed, replaced, or upgraded during its service life without compromising the overall stability, integrity, or usability of the structure.', lang='en')))
g.add((EC1990['ReplacableStructuralElements'], SKOS.definition, Literal('structure designed such that certain primary or secondary structural components can be removed, replaced, or upgraded during its service life without compromising the overall stability, integrity, or usability of the structure.')))
g.add((EC1990['ReplacableStructuralElements'], DCTERMS.source, Literal('EN 1990:2002, Table 2.1')))
g.add((EC1990['ReplacableStructuralElements'], SKOS.example, Literal('modular steel bridge with replaceable girders, industrial building with precast concrete roof panels')))

g.add((EC1990['AgriculturalStructure'], RDF.type, OWL.NamedIndividual)) 
g.add((EC1990['AgriculturalStructure'], RDF.type, EC1990.Structure))
g.add((EC1990['AgriculturalStructure'], RDFS.label, Literal('Agricultural Structure', lang='en')))
g.add((EC1990['AgriculturalStructure'], RDFS.comment, Literal('A building or construction primarily designed and used for farming-related activities.', lang='en')))
g.add((EC1990['AgriculturalStructure'], SKOS.definition, Literal('A building or construction primarily designed and used for farming-related activities.')))
g.add((EC1990['AgriculturalStructure'], DCTERMS.source, Literal('EN 1990:2002, Table 2.1')))
g.add((EC1990['AgriculturalStructure'], SKOS.example, Literal('barn, greenhouse, animal shelter')))

g.add((EC1990['BuildingStructure'], RDF.type, OWL.NamedIndividual)) 
g.add((EC1990['BuildingStructure'], RDF.type, EC1990.Structure))
g.add((EC1990['BuildingStructure'], RDFS.label, Literal('Building Structure', lang='en')))
g.add((EC1990['BuildingStructure'], RDFS.comment, Literal('Load-bearing framework or system designed to support and transfer all applied loads safely to the foundation and ultimately to the ground.', lang='en')))
g.add((EC1990['BuildingStructure'], SKOS.definition, Literal('Load-bearing framework or system designed to support and transfer all applied loads safely to the foundation and ultimately to the ground.')))
g.add((EC1990['BuildingStructure'], DCTERMS.source, Literal('EN 1990:2002, Table 2.1')))
g.add((EC1990['BuildingStructure'], SKOS.example, Literal('masonry building, steel frame building, timber-framed house')))

g.add((EC1990['BridgeStructure'], RDF.type, OWL.NamedIndividual)) 
g.add((EC1990['BridgeStructure'], RDF.type, EC1990.Structure))
g.add((EC1990['BridgeStructure'], RDFS.label, Literal('Bridge Structure', lang='en')))
g.add((EC1990['BridgeStructure'], RDFS.comment, Literal('Engineered construction designed to span physical obstacles such as rivers, valleys, roads, or railways, providing a safe passage for vehicles, pedestrians, or utilities.', lang='en')))
g.add((EC1990['BridgeStructure'], SKOS.definition, Literal('Engineered construction designed to span physical obstacles such as rivers, valleys, roads, or railways, providing a safe passage for vehicles, pedestrians, or utilities.')))
g.add((EC1990['BridgeStructure'], DCTERMS.source, Literal('EN 1990:2002, Table 2.1')))
g.add((EC1990['BridgeStructure'], SKOS.example, Literal('beam bridge, arch bridge, suspension bridge')))

g.add((EC1990['MonumentalBuldingStructure'], RDF.type, OWL.NamedIndividual)) 
g.add((EC1990['MonumentalBuldingStructure'], RDF.type, EC1990.Structure))
g.add((EC1990['MonumentalBuldingStructure'], RDFS.label, Literal('Monumental Building Structure', lang='en')))
g.add((EC1990['MonumentalBuldingStructure'], RDFS.comment, Literal('Large-scale, architecturally significant structure designed to serve as a landmark, memorial, or symbol of cultural, historical, or civic importance.', lang='en')))
g.add((EC1990['MonumentalBuldingStructure'], SKOS.definition, Literal('Large-scale, architecturally significant structure designed to serve as a landmark, memorial, or symbol of cultural, historical, or civic importance.')))
g.add((EC1990['MonumentalBuldingStructure'], DCTERMS.source, Literal('EN 1990:2002, Table 2.1')))
g.add((EC1990['MonumentalBuldingStructure'], SKOS.example, Literal('national parliment building, museum of significant importance, major cathedral')))

g.add((EC1990['CivilEngineeringStructure'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['CivilEngineeringStructure'], RDF.type, EC1990.Structure))
g.add((EC1990['CivilEngineeringStructure'], RDFS.label, Literal('Civil Engineering Structure', lang='en')))
g.add((EC1990['CivilEngineeringStructure'], RDFS.comment, Literal('Constructed system composed of interconnected physical elements designed, analyzed, and built to withstand environmental and operational loads, enabling the provision of essential services such as transport, shelter, water management, or energy distribution.', lang='en')))
g.add((EC1990['CivilEngineeringStructure'], SKOS.definition, Literal('Constructed system composed of interconnected physical elements designed, analyzed, and built to withstand environmental and operational loads, enabling the provision of essential services such as transport, shelter, water management, or energy distribution.')))
g.add((EC1990['CivilEngineeringStructure'], DCTERMS.source, Literal('EN 1990:2002, Table 2.1')))
g.add((EC1990['CivilEngineeringStructure'], SKOS.example, Literal('dam, tunnel, airport, retaining wall, power station, road')))

g.add((EC1990['StructuralSystem'], RDF.type, OWL.Class))
g.add((EC1990['StructuralSystem'], RDFS.label, Literal('Structural System', lang='en')))
g.add((EC1990['StructuralSystem'], RDFS.comment, Literal('Load-bearing members of a building or civil engineering works and the way in which these members function together.', lang='en')))
g.add((EC1990['StructuralSystem'], SKOS.definition, Literal('Load-bearing members of a building or civil engineering works and the way in which these members function together.')))
g.add((EC1990['StructuralSystem'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.9')))
g.add((EC1990['StructuralSystem'], SKOS.example, Literal('Flat-slab system with drop panels, steel potal frame, cable-stayed bridge system, trussed roof system')))

##########################################################
#                   LIMIT STATES                         #
##########################################################

g.add((EC1990['LimitState'], RDF.type, OWL.Class))
g.add((EC1990['LimitState'], RDFS.label, Literal('Limit State', lang='en')))
g.add((EC1990['LimitState'], RDFS.comment, Literal('State beyond which the structure no longer fulfils the relevant design criteria.', lang='en')))
g.add((EC1990['LimitState'], SKOS.definition, Literal('State beyond which the structure no longer fulfils the relevant design criteria.')))
g.add((EC1990['LimitState'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.12')))

g.add((EC1990['UltimateLimitState'], RDF.type, OWL.Class))
g.add((EC1990['UltimateLimitState'], RDFS.subClassOf, EC1990.LimitState))
g.add((EC1990['UltimateLimitState'], RDFS.label, Literal('Ultimate Limit State', lang='en')))
g.add((EC1990['UltimateLimitState'], RDFS.comment, Literal('State associated with collapse or with other similar forms of structural failure. They generally correspond to the maximum load-carrying resistance of a structure or structural member.', lang='en')))
g.add((EC1990['UltimateLimitState'], SKOS.definition, Literal('State associated with collapse or with other similar forms of structural failure. They generally correspond to the maximum load-carrying resistance of a structure or structural member.')))
g.add((EC1990['UltimateLimitState'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.13')))
g.add((EC1990['UltimateLimitState'], SKOS.altLabel, Literal('ULS')))

g.add((EC1990['ServiceabilityLimitState'], RDF.type, OWL.Class))
g.add((EC1990['ServiceabilityLimitState'], RDFS.subClassOf, EC1990.LimitState))
g.add((EC1990['ServiceabilityLimitState'], RDFS.label, Literal('Serviceability Limit State', lang='en')))
g.add((EC1990['ServiceabilityLimitState'], RDFS.comment, Literal('State that correspond to conditions beyond which specified service requirements for a structure or structural member are no longer met.', lang='en')))
g.add((EC1990['ServiceabilityLimitState'], SKOS.definition, Literal('State that correspond to conditions beyond which specified service requirements for a structure or structural member are no longer met.')))
g.add((EC1990['ServiceabilityLimitState'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.14')))
g.add((EC1990['ServiceabilityLimitState'], SKOS.altLabel, Literal('SLS')))

# Specific ULS types
g.add((EC1990['EQU'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['EQU'], RDF.type, EC1990.UltimateLimitState))
g.add((EC1990['EQU'], RDFS.label, Literal('Static Equilibrium', lang='en')))
g.add((EC1990['EQU'], RDFS.comment, Literal('Loss of static equilibrium of the structure or any part of it considered as a rigid body.', lang='en')))
g.add((EC1990['EQU'], SKOS.definition, Literal('Loss of static equilibrium of the structure or any part of it considered as a rigid body.')))
g.add((EC1990['EQU'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.1(1)P a)')))

g.add((EC1990['STR'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['STR'], RDF.type, EC1990.UltimateLimitState))
g.add((EC1990['STR'], RDFS.label, Literal('Structural Resistance', lang='en')))
g.add((EC1990['STR'], RDFS.comment, Literal('Internal failure or excessive deformation of the structure or structural members where the strength of construction materials governs.', lang='en')))
g.add((EC1990['STR'], SKOS.definition, Literal('Internal failure or excessive deformation of the structure or structural members where the strength of construction materials governs.')))
g.add((EC1990['STR'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.1(1)P b)')))

g.add((EC1990['GEO'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['GEO'], RDF.type, EC1990.UltimateLimitState))
g.add((EC1990['GEO'], RDFS.label, Literal('Geotechnical Failure', lang='en')))
g.add((EC1990['GEO'], RDFS.comment, Literal('Failure or excessive deformation of the ground where the strengths of soil or rock are significant in providing resistance.', lang='en')))
g.add((EC1990['GEO'], SKOS.definition, Literal('Failure or excessive deformation of the ground where the strengths of soil or rock are significant in providing resistance.')))
g.add((EC1990['GEO'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.1(1)P c)')))

g.add((EC1990['FAT'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['FAT'], RDF.type, EC1990.UltimateLimitState))
g.add((EC1990['FAT'], RDFS.label, Literal('Fatigue Failure', lang='en')))
g.add((EC1990['FAT'], RDFS.comment, Literal('Fatigue failure of the structure or structural members.', lang='en')))
g.add((EC1990['FAT'], SKOS.definition, Literal('Fatigue failure of the structure or structural members.')))
g.add((EC1990['FAT'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.1(1)P d)')))

g.add((EC1990['UPL'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['UPL'], RDF.type, EC1990.UltimateLimitState))
g.add((EC1990['UPL'], RDFS.label, Literal('Uplift Failure', lang='en')))
g.add((EC1990['UPL'], RDFS.comment, Literal('Loss of equilibrium of the structure or the ground due to uplift by water pressure (buoyancy) or other vertical actions.', lang='en')))
g.add((EC1990['UPL'], SKOS.definition, Literal('Loss of equilibrium of the structure or the ground due to uplift by water pressure (buoyancy) or other vertical actions.')))
g.add((EC1990['UPL'], DCTERMS.source, Literal('EN 1990:2002/A1:2005, Section 6.4.1(1)P e)')))

g.add((EC1990['HYD'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['HYD'], RDF.type, EC1990.UltimateLimitState))
g.add((EC1990['HYD'], RDFS.label, Literal('Hydraulic Failure', lang='en')))
g.add((EC1990['HYD'], RDFS.comment, Literal('Hydraulic heave, internal erosion and piping in the ground caused by hydraulic gradients.', lang='en')))
g.add((EC1990['HYD'], SKOS.definition, Literal('Hydraulic heave, internal erosion and piping in the ground caused by hydraulic gradients.')))
g.add((EC1990['HYD'], DCTERMS.source, Literal('EN 1990:2002/A1:2005, Section 6.4.1(1)P f)')))

# SLS types
g.add((EC1990['RSLS'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['RSLS'], RDF.type, EC1990.ServiceabilityLimitState))
g.add((EC1990['RSLS'], RDFS.label, Literal('Reversible Serviceability Limit State', lang='en')))
g.add((EC1990['RSLS'], RDFS.comment, Literal('Serviceability limit state where no consequences of actions exceeding the specified service requirements will remain when the actions are removed.', lang='en')))
g.add((EC1990['RSLS'], SKOS.definition, Literal('Serviceability limit state where no consequences of actions exceeding the specified service requirements will remain when the actions are removed.')))
g.add((EC1990['RSLS'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 1.5.2.14.2')))

g.add((EC1990['ISLS'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['ISLS'], RDF.type, EC1990.ServiceabilityLimitState))
g.add((EC1990['ISLS'], RDFS.label, Literal('Irreversible Serviceability Limit State', lang='en')))
g.add((EC1990['ISLS'], RDFS.comment, Literal('Serviceability limit state where some consequences of actions exceeding the specified service requirements will remain when the actions are removed.', lang='en')))
g.add((EC1990['ISLS'], SKOS.definition, Literal('Serviceability limit state where some consequences of actions exceeding the specified service requirements will remain when the actions are removed.')))
g.add((EC1990['ISLS'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 1.5.2.14.1')))

##########################################################
#                 DESIGN SITUATIONS                      #
##########################################################

g.add((EC1990['DesignSituation'], RDF.type, OWL.Class))
g.add((EC1990['DesignSituation'], RDFS.label, Literal('Design Situation', lang='en')))
g.add((EC1990['DesignSituation'], RDFS.comment, Literal('Sets of physical conditions representing the real conditions occurring during a certain time interval for which the design will demonstrate that relevant limit states are not exceeded.', lang='en')))
g.add((EC1990['DesignSituation'], SKOS.definition, Literal('Sets of physical conditions representing the real conditions occurring during a certain time interval for which the design will demonstrate that relevant limit states are not exceeded.')))
g.add((EC1990['DesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.2')))

g.add((EC1990['PersistentDesignSituation'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['PersistentDesignSituation'], RDF.type, EC1990.DesignSituation))
g.add((EC1990['PersistentDesignSituation'], RDFS.label, Literal('Persistent Design Situation', lang='en')))
g.add((EC1990['PersistentDesignSituation'], RDFS.comment, Literal('Design situation that is relevant during a period of the same order as the design working life of the structure. Generally refers to conditions of normal use.', lang='en')))
g.add((EC1990['PersistentDesignSituation'], SKOS.definition, Literal('Design situation that is relevant during a period of the same order as the design working life of the structure. Generally refers to conditions of normal use.')))
g.add((EC1990['PersistentDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.4')))

g.add((EC1990['TransientDesignSituation'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['TransientDesignSituation'], RDF.type, EC1990.DesignSituation))
g.add((EC1990['TransientDesignSituation'], RDFS.label, Literal('Transient Design Situation', lang='en')))
g.add((EC1990['TransientDesignSituation'], RDFS.comment, Literal('Design situation that is relevant during a period much shorter than the design working life of the structure and which has a high probability of occurrence, e.g. during construction or repair.', lang='en')))
g.add((EC1990['TransientDesignSituation'], SKOS.definition, Literal('Design situation that is relevant during a period much shorter than the design working life of the structure and which has a high probability of occurrence, e.g. during construction or repair.')))
g.add((EC1990['TransientDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.3')))
g.add((EC1990['TransientDesignSituation'], SKOS.example, Literal('construction phase, repair operations')))

g.add((EC1990['AccidentalDesignSituation'], RDF.type, OWL.Class))
g.add((EC1990['AccidentalDesignSituation'], RDFS.subClassOf, EC1990.DesignSituation))
g.add((EC1990['AccidentalDesignSituation'], RDFS.label, Literal('Accidental Design Situation', lang='en')))
g.add((EC1990['AccidentalDesignSituation'], RDFS.comment, Literal('Design situation involving exceptional conditions of the structure or its exposure, including fire, explosion, impact or local failure.', lang='en')))
g.add((EC1990['AccidentalDesignSituation'], SKOS.definition, Literal('Design situation involving exceptional conditions of the structure or its exposure, including fire, explosion, impact or local failure.')))
g.add((EC1990['AccidentalDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.5')))
g.add((EC1990['AccidentalDesignSituation'], SKOS.example, Literal('fire, explosion, impact, local failure')))

g.add((EC1990['FireDesignSituation'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['FireDesignSituation'], RDF.type, EC1990.AccidentalDesignSituation))
g.add((EC1990['FireDesignSituation'], RDFS.label, Literal('Fire Design Situation', lang='en')))
g.add((EC1990['FireDesignSituation'], RDFS.comment, Literal('Accidental design situation involving fire conditions requiring specific design considerations.', lang='en')))
g.add((EC1990['FireDesignSituation'], SKOS.definition, Literal('Accidental design situation involving fire conditions requiring specific design considerations.')))
g.add((EC1990['FireDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.5 & 6')))

g.add((EC1990['ExplosionDesignSituation'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['ExplosionDesignSituation'], RDF.type, EC1990.AccidentalDesignSituation))
g.add((EC1990['ExplosionDesignSituation'], RDFS.label, Literal('Explosion Design Situation', lang='en')))
g.add((EC1990['ExplosionDesignSituation'], RDFS.comment, Literal('Accidental design situation involving explosion conditions.', lang='en')))
g.add((EC1990['ExplosionDesignSituation'], SKOS.definition, Literal('Accidental design situation involving explosion conditions.')))
g.add((EC1990['ExplosionDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.5')))

g.add((EC1990['ImpactDesignSituation'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['ImpactDesignSituation'], RDF.type, EC1990.AccidentalDesignSituation))
g.add((EC1990['ImpactDesignSituation'], RDFS.label, Literal('Impact Design Situation', lang='en')))
g.add((EC1990['ImpactDesignSituation'], RDFS.comment, Literal('Accidental design situation involving impact conditions.', lang='en')))
g.add((EC1990['ImpactDesignSituation'], SKOS.definition, Literal('Accidental design situation involving impact conditions.')))
g.add((EC1990['ImpactDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.5')))

g.add((EC1990['LocalizedFailureDesignSituation'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['LocalizedFailureDesignSituation'], RDF.type, EC1990.AccidentalDesignSituation))
g.add((EC1990['LocalizedFailureDesignSituation'], RDFS.label, Literal('Localized Failure Design Situation', lang='en')))
g.add((EC1990['LocalizedFailureDesignSituation'], RDFS.comment, Literal('Accidental design situation involving local failure conditions.', lang='en')))
g.add((EC1990['LocalizedFailureDesignSituation'], SKOS.definition, Literal('Accidental design situation involving local failure conditions.')))
g.add((EC1990['LocalizedFailureDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.5')))

g.add((EC1990['SeismicDesignSituation'], RDF.type, OWL.NamedIndividual))
g.add((EC1990['SeismicDesignSituation'], RDF.type, EC1990.DesignSituation))
g.add((EC1990['SeismicDesignSituation'], RDFS.label, Literal('Seismic Design Situation', lang='en')))
g.add((EC1990['SeismicDesignSituation'], RDFS.comment, Literal('Design situation involving exceptional conditions of the structure when subjected to a seismic event.', lang='en')))
g.add((EC1990['SeismicDesignSituation'], SKOS.definition, Literal('Design situation involving exceptional conditions of the structure when subjected to a seismic event.')))
g.add((EC1990['SeismicDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.7')))

##########################################################
#                       ACTIONS                          #
##########################################################

g.add((EC1990['Action'], RDF.type, OWL.Class))
g.add((EC1990['Action'], RDFS.subClassOf, QUDT.Quantity))
g.add((EC1990['Action'], RDFS.label, Literal('Action', lang='en')))
g.add((EC1990['Action'], RDFS.comment, Literal('Set of forces (loads) applied to the structure (direct action) or set of imposed deformations or accelerations caused for example, by temperature changes, moisture variation, uneven settlement or earthquakes (indirect action).', lang='en')))
g.add((EC1990['Action'], SKOS.definition, Literal('Set of forces (loads) applied to the structure (direct action) or set of imposed deformations or accelerations caused for example, by temperature changes, moisture variation, uneven settlement or earthquakes (indirect action).')))
g.add((EC1990['Action'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.1')))
g.add((EC1990['Action'], SKOS.example, Literal('dead load, imopsed load, wind load, thermal action')))
g.add((EC1990['Action'], SKOS.altLabel, Literal('F')))

# Represetative and Design Actions
g.add((EC1990['RepresentativeAction'], RDF.type, OWL.Class))
g.add((EC1990['RepresentativeAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['RepresentativeAction'], RDFS.label, Literal('Representative Action', lang='en')))
g.add((EC1990['RepresentativeAction'], RDFS.comment, Literal('Value ofan action used for limit state verification. A representative value may be the characteristic value or an accompanying value.', lang='en')))
g.add((EC1990['RepresentativeAction'], SKOS.definition, Literal('Value ofan action used for limit state verification. A representative value may be the characteristic value or an accompanying value.')))
g.add((EC1990['RepresentativeAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.20')))

g.add((EC1990['DesignAction'], RDF.type, OWL.Class))
g.add((EC1990['DesignAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['DesignAction'], RDFS.label, Literal('Design Action', lang='en')))
g.add((EC1990['DesignAction'], RDFS.comment, Literal('Value ofan action used for limit state verification. A design valueo is btained by multiplying the representative value by the partial factor.', lang='en')))
g.add((EC1990['DesignAction'], SKOS.definition, Literal('Value ofan action used for limit state verification. A design valueo is btained by multiplying the representative value by the partial factor.')))
g.add((EC1990['DesignAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.21')))

# Favourable and Unfavourable Actions
g.add((EC1990['FavourableAction'], RDF.type, OWL.Class))
g.add((EC1990['FavourableAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['FavourableAction'], RDFS.label, Literal('Favourable Action', lang='en')))
g.add((EC1990['FavourableAction'], RDFS.comment, Literal('Action that reduces the effect of other actions on a structure, or otherwise contributes to structural safety.', lang='en')))
g.add((EC1990['FavourableAction'], SKOS.definition, Literal('Action that reduces the effect of other actions on a structure, or otherwise contributes to structural safety.')))
g.add((EC1990['FavourableAction'], DCTERMS.source, Literal('EN 1990:2002, Section 6.3.2(3)P')))

g.add((EC1990['UnfavourableAction'], RDF.type, OWL.Class))
g.add((EC1990['UnfavourableAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['UnfavourableAction'], RDFS.label, Literal('UnfavourableAction Action', lang='en')))
g.add((EC1990['UnfavourableAction'], RDFS.comment, Literal('An action that increases the effect of other actions on a structure, or otherwise reduces structural safety.', lang='en')))
g.add((EC1990['UnfavourableAction'], SKOS.definition, Literal('An action that increases the effect of other actions on a structure, or otherwise reduces structural safety.')))
g.add((EC1990['UnfavourableAction'], DCTERMS.source, Literal('EN 1990:2002, Section 6.3.2(3)P')))

# Direct and Indirect Actions
g.add((EC1990['DirectAction'], RDF.type, OWL.Class))
g.add((EC1990['DirectAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['DirectAction'], RDFS.label, Literal('Direct Action', lang='en')))
g.add((EC1990['DirectAction'], RDFS.comment, Literal('Set of forces (loads) applied to the structure.', lang='en')))
g.add((EC1990['DirectAction'], SKOS.definition, Literal('Set of forces (loads) applied to the structure.')))
g.add((EC1990['DirectAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.1 a)')))

g.add((EC1990['IndirectAction'], RDF.type, OWL.Class))
g.add((EC1990['IndirectAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['IndirectAction'], RDFS.label, Literal('Indirect Action', lang='en')))
g.add((EC1990['IndirectAction'], RDFS.comment, Literal('Set of imposed deformations or accelerations caused for example, by temperature changes, moisture variation, uneven settlement or earthquakes.', lang='en')))
g.add((EC1990['IndirectAction'], SKOS.definition, Literal('Set of imposed deformations or accelerations caused for example, by temperature changes, moisture variation, uneven settlement or earthquakes.')))
g.add((EC1990['IndirectAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.1 b)')))

# Action classification by time variation
g.add((EC1990['PermanentAction'], RDF.type, OWL.Class))
g.add((EC1990['PermanentAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['PermanentAction'], RDFS.label, Literal('Permanent Action', lang='en')))
g.add((EC1990['PermanentAction'], RDFS.comment, Literal('Action that is likely to act throughout a given reference period and for which the variation in magnitude with time is negligible, or for which the variation is always in the same direction (monotonic) until the action attains a certain limit value.', lang='en')))
g.add((EC1990['PermanentAction'], SKOS.definition, Literal('Action that is likely to act throughout a given reference period and for which the variation in magnitude with time is negligible, or for which the variation is always in the same direction (monotonic) until the action attains a certain limit value.')))
g.add((EC1990['PermanentAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.3')))
g.add((EC1990['PermanentAction'], SKOS.altLabel, Literal('G')))
g.add((EC1990['PermanentAction'], SKOS.example, Literal('self-weight, fixed equipment')))

g.add((EC1990['VariableAction'], RDF.type, OWL.Class))
g.add((EC1990['VariableAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['VariableAction'], RDFS.label, Literal('Variable Action', lang='en')))
g.add((EC1990['VariableAction'], RDFS.comment, Literal('Action for which the variation in magnitude with time is neither negligible nor monotonic.', lang='en')))
g.add((EC1990['VariableAction'], SKOS.definition, Literal('Action for which the variation in magnitude with time is neither negligible nor monotonic.')))
g.add((EC1990['VariableAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.4')))
g.add((EC1990['VariableAction'], SKOS.altLabel, Literal('Q')))
g.add((EC1990['VariableAction'], SKOS.example, Literal('imposed loads, wind, snow, thermal actions')))

g.add((EC1990['AccidentalAction'], RDF.type, OWL.Class))
g.add((EC1990['AccidentalAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['AccidentalAction'], RDFS.label, Literal('Accidental Action', lang='en')))
g.add((EC1990['AccidentalAction'], RDFS.comment, Literal('Action, usually of short duration but of significant magnitude, that is unlikely to occur on a given structure during the design working life.', lang='en')))
g.add((EC1990['AccidentalAction'], SKOS.definition, Literal('Action, usually of short duration but of significant magnitude, that is unlikely to occur on a given structure during the design working life.')))
g.add((EC1990['AccidentalAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.5')))
g.add((EC1990['AccidentalAction'], SKOS.altLabel, Literal('A')))
g.add((EC1990['AccidentalAction'], SKOS.example, Literal('explosions, impact from vehicles')))

g.add((EC1990['SeismicAction'], RDF.type, OWL.Class))
g.add((EC1990['SeismicAction'], RDFS.subClassOf, EC1990.AccidentalAction))
g.add((EC1990['SeismicAction'], RDFS.label, Literal('Seismic Action', lang='en')))
g.add((EC1990['SeismicAction'], RDFS.comment, Literal('Action that arises due to earthquake ground motions.', lang='en')))
g.add((EC1990['SeismicAction'], SKOS.definition, Literal('Action that arises due to earthquake ground motions.')))
g.add((EC1990['SeismicAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.6')))
g.add((EC1990['SeismicAction'], SKOS.altLabel, Literal('A_E')))

# Action classification by spatial variation
g.add((EC1990['FixedAction'], RDF.type, OWL.Class))
g.add((EC1990['FixedAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['FixedAction'], RDFS.label, Literal('Fixed Action', lang='en')))
g.add((EC1990['FixedAction'], RDFS.comment, Literal('Action that has a fixed distribution and position over the structure or structural member such that the magnitude and direction of the action are determined unambiguously for the whole structure.', lang='en')))
g.add((EC1990['FixedAction'], SKOS.definition, Literal('Action that has a fixed distribution and position over the structure or structural member such that the magnitude and direction of the action are determined unambiguously for the whole structure.')))
g.add((EC1990['FixedAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.8')))
g.add((EC1990['FixedAction'], SKOS.example, Literal('Stored goods in a defined storage area with no alternative placement')))

g.add((EC1990['FreeAction'], RDF.type, OWL.Class))
g.add((EC1990['FreeAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['FreeAction'], RDFS.label, Literal('Free Action', lang='en')))
g.add((EC1990['FreeAction'], RDFS.comment, Literal('Action that may have various spatial distributions over the structure.', lang='en')))
g.add((EC1990['FreeAction'], SKOS.definition, Literal('Action that may have various spatial distributions over the structure.')))
g.add((EC1990['FreeAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.9')))
g.add((EC1990['FreeAction'], SKOS.example, Literal('Imposed floor load on individual rooms of a multi-storey building')))

# Action classification by dynamic response
g.add((EC1990['StaticAction'], RDF.type, OWL.Class))
g.add((EC1990['StaticAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['StaticAction'], RDFS.label, Literal('Static Action', lang='en')))
g.add((EC1990['StaticAction'], RDFS.comment, Literal('Action that does not cause significant acceleration of the structure or structural members.', lang='en')))
g.add((EC1990['StaticAction'], SKOS.definition, Literal('Action that does not cause significant acceleration of the structure or structural members.')))
g.add((EC1990['StaticAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.11')))

g.add((EC1990['DynamicAction'], RDF.type, OWL.Class))
g.add((EC1990['DynamicAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['DynamicAction'], RDFS.label, Literal('Dynamic Action', lang='en')))
g.add((EC1990['DynamicAction'], RDFS.comment, Literal('Action that causes significant acceleration of the structure or structural members.', lang='en')))
g.add((EC1990['DynamicAction'], SKOS.definition, Literal('Action that causes significant acceleration of the structure or structural members.')))
g.add((EC1990['DynamicAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.12')))

g.add((EC1990['QuasiStaticAction'], RDF.type, OWL.Class))
g.add((EC1990['QuasiStaticAction'], RDFS.subClassOf, EC1990.DynamicAction))
g.add((EC1990['QuasiStaticAction'], RDFS.label, Literal('Quasi-Static Action', lang='en')))
g.add((EC1990['QuasiStaticAction'], RDFS.comment, Literal('Dynamic action represented by an equivalent static action in a static model.', lang='en')))
g.add((EC1990['QuasiStaticAction'], SKOS.definition, Literal('Dynamic action represented by an equivalent static action in a static model.')))
g.add((EC1990['QuasiStaticAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.13')))

g.add((EC1990['GeotechnicalAction'], RDF.type, OWL.Class))
g.add((EC1990['GeotechnicalAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['GeotechnicalAction'], RDFS.label, Literal('Geotechnical Action', lang='en')))
g.add((EC1990['GeotechnicalAction'], RDFS.comment, Literal('Action transmitted to the structure by the ground, fill or groundwater.', lang='en')))
g.add((EC1990['GeotechnicalAction'], SKOS.definition, Literal('Action transmitted to the structure by the ground, fill or groundwater.')))
g.add((EC1990['GeotechnicalAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.7')))

g.add((EC1990['FatigueAction'], RDF.type, OWL.Class))
g.add((EC1990['FatigueAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['FatigueAction'], RDFS.label, Literal('Fatigue Action', lang='en')))
g.add((EC1990['FatigueAction'], RDFS.comment, Literal('Repeated or fluctuating mechanical action applied over time, which may cause failure even if the individual stress cycles are below the material\'s static strength.', lang='en')))
g.add((EC1990['FatigueAction'], SKOS.definition, Literal('Repeated or fluctuating mechanical action applied over time, which may cause failure even if the individual stress cycles are below the material\'s static strength.')))
g.add((EC1990['FatigueAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.7')))

# Action classification by nature
g.add((EC1990['SelfWeight'], RDF.type, OWL.Class))
g.add((EC1990['SelfWeight'], RDFS.subClassOf, EC1990.PermanentAction))
g.add((EC1990['SelfWeight'], RDFS.label, Literal('Self-weight', lang='en')))
g.add((EC1990['SelfWeight'], RDFS.comment, Literal('.', lang='en')))
g.add((EC1990['SelfWeight'], SKOS.definition, Literal('.')))
g.add((EC1990['SelfWeight'], DCTERMS.source, Literal('EN 1991-1-1:2002')))

g.add((EC1990['DeadLoad'], RDF.type, OWL.Class))
g.add((EC1990['DeadLoad'], RDFS.subClassOf, EC1990.PermanentAction))
g.add((EC1990['DeadLoad'], RDFS.label, Literal('Dead load', lang='en')))
g.add((EC1990['DeadLoad'], RDFS.comment, Literal('.', lang='en')))
g.add((EC1990['DeadLoad'], SKOS.definition, Literal('.')))
g.add((EC1990['DeadLoad'], DCTERMS.source, Literal('EN 1991-1-1:2002')))

g.add((EC1990['ImposedLoad'], RDF.type, OWL.Class))
g.add((EC1990['ImposedLoad'], RDFS.subClassOf, EC1990.VariableAction))
g.add((EC1990['ImposedLoad'], RDFS.label, Literal('Imposed load', lang='en')))
g.add((EC1990['ImposedLoad'], RDFS.comment, Literal('.', lang='en')))
g.add((EC1990['ImposedLoad'], SKOS.definition, Literal('.')))
g.add((EC1990['ImposedLoad'], DCTERMS.source, Literal('EN 1991-1-1:2002')))

g.add((EC1990['SnowLoad'], RDF.type, OWL.Class))
g.add((EC1990['SnowLoad'], RDFS.subClassOf, EC1990.VariableAction))
g.add((EC1990['SnowLoad'], RDFS.label, Literal('Snow load', lang='en')))
g.add((EC1990['SnowLoad'], RDFS.comment, Literal('.', lang='en')))
g.add((EC1990['SnowLoad'], SKOS.definition, Literal('.')))
g.add((EC1990['SnowLoad'], DCTERMS.source, Literal('EN 1991-1-3:2003')))

g.add((EC1990['WindAction'], RDF.type, OWL.Class))
g.add((EC1990['WindAction'], RDFS.subClassOf, EC1990.VariableAction))
g.add((EC1990['WindAction'], RDFS.label, Literal('Wind action', lang='en')))
g.add((EC1990['WindAction'], RDFS.comment, Literal('.', lang='en')))
g.add((EC1990['WindAction'], SKOS.definition, Literal('.')))
g.add((EC1990['WindAction'], DCTERMS.source, Literal('EN 1991-1-4:2005')))

g.add((EC1990['ThermalAction'], RDF.type, OWL.Class))
g.add((EC1990['ThermalAction'], RDFS.subClassOf, EC1990.VariableAction))
g.add((EC1990['ThermalAction'], RDFS.label, Literal('Thermal action', lang='en')))
g.add((EC1990['ThermalAction'], RDFS.comment, Literal('.', lang='en')))
g.add((EC1990['ThermalAction'], SKOS.definition, Literal('.')))
g.add((EC1990['ThermalAction'], DCTERMS.source, Literal('EN 1991-1-5:2003')))

g.add((EC1990['LeadingVariableAction'], RDF.type, OWL.Class))
g.add((EC1990['LeadingVariableAction'], RDFS.subClassOf, EC1990.VariableAction))
g.add((EC1990['LeadingVariableAction'], RDFS.label, Literal('Leading variable action', lang='en')))
g.add((EC1990['LeadingVariableAction'], RDFS.comment, Literal('.', lang='en')))
g.add((EC1990['LeadingVariableAction'], SKOS.definition, Literal('.')))
g.add((EC1990['LeadingVariableAction'], DCTERMS.source, Literal('EN 1990:2003 Section 6.4.3.2(2)')))

g.add((EC1990['AccompanyingVariableAction'], RDF.type, OWL.Class))
g.add((EC1990['AccompanyingVariableAction'], RDFS.subClassOf, EC1990.VariableAction))
g.add((EC1990['AccompanyingVariableAction'], RDFS.label, Literal('Accompanying variable action', lang='en')))
g.add((EC1990['AccompanyingVariableAction'], RDFS.comment, Literal('.', lang='en')))
g.add((EC1990['AccompanyingVariableAction'], SKOS.definition, Literal('.')))
g.add((EC1990['AccompanyingVariableAction'], DCTERMS.source, Literal('EN 1990:2003 Section 6.4.3.2(2)')))

##########################################################
#                 COMBINATIONS OF ACTIONS                #
##########################################################

g.add((EC1990['CombinationOfActions'], RDF.type, OWL.Class))
g.add((EC1990['CombinationOfActions'], RDFS.label, Literal('Combination of Actions', lang='en')))
g.add((EC1990['CombinationOfActions'], RDFS.comment, Literal('Set of design values used for the verification of the structural reliability for a limit state under the simultaneous influence of different actions.', lang='en')))
g.add((EC1990['CombinationOfActions'], SKOS.definition, Literal('Set of design values used for the verification of the structural reliability for a limit state under the simultaneous influence of different actions.')))
g.add((EC1990['CombinationOfActions'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.22')))

g.add((EC1990['ULSCombination'], RDF.type, OWL.Class))
g.add((EC1990['ULSCombination'], RDFS.subClassOf, EC1990.CombinationOfActions))
g.add((EC1990['ULSCombination'], RDFS.label, Literal('Ultimate Limit State Combination', lang='en')))
g.add((EC1990['ULSCombination'], RDFS.comment, Literal('Combination of actions for verifying ultimate limit states.', lang='en')))
g.add((EC1990['ULSCombination'], SKOS.definition, Literal('Combination of actions for verifying ultimate limit states.')))
g.add((EC1990['ULSCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.3')))

g.add((EC1990['FundamentalCombination'], RDF.type, OWL.Class))
g.add((EC1990['FundamentalCombination'], RDFS.subClassOf, EC1990.ULSCombination))
g.add((EC1990['FundamentalCombination'], RDFS.label, Literal('Fundamental Combination', lang='en')))
g.add((EC1990['FundamentalCombination'], RDFS.comment, Literal('Combination of actions for persistent or transient design situations.', lang='en')))
g.add((EC1990['FundamentalCombination'], SKOS.definition, Literal('Combination of actions for persistent or transient design situations.')))
g.add((EC1990['FundamentalCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.3.2')))

g.add((EC1990['AccidentalCombination'], RDF.type, OWL.Class))
g.add((EC1990['AccidentalCombination'], RDFS.subClassOf, EC1990.ULSCombination))
g.add((EC1990['AccidentalCombination'], RDFS.label, Literal('Accidental Combination', lang='en')))
g.add((EC1990['AccidentalCombination'], RDFS.comment, Literal('Combination of actions for accidental design situations.', lang='en')))
g.add((EC1990['AccidentalCombination'], SKOS.definition, Literal('Combination of actions for accidental design situations.')))
g.add((EC1990['AccidentalCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.3.3')))

g.add((EC1990['SeismicCombination'], RDF.type, OWL.Class))
g.add((EC1990['SeismicCombination'], RDFS.subClassOf, EC1990.ULSCombination))
g.add((EC1990['SeismicCombination'], RDFS.label, Literal('Seismic Combination', lang='en')))
g.add((EC1990['SeismicCombination'], RDFS.comment, Literal('Combination of actions for seismic design situations.', lang='en')))
g.add((EC1990['SeismicCombination'], SKOS.definition, Literal('Combination of actions for seismic design situations.')))
g.add((EC1990['SeismicCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.3.4')))

g.add((EC1990['SLSCombination'], RDF.type, OWL.Class))
g.add((EC1990['SLSCombination'], RDFS.subClassOf, EC1990.CombinationOfActions))
g.add((EC1990['SLSCombination'], RDFS.label, Literal('Serviceability Limit State Combination', lang='en')))
g.add((EC1990['SLSCombination'], RDFS.comment, Literal('Combinations of actions for verifying serviceability limit states.', lang='en')))
g.add((EC1990['SLSCombination'], SKOS.definition, Literal('Combinations of actions for verifying serviceability limit states.')))
g.add((EC1990['SLSCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.5.3')))

g.add((EC1990['CharacteristicCombination'], RDF.type, OWL.Class))
g.add((EC1990['CharacteristicCombination'], RDFS.subClassOf, EC1990.SLSCombination))
g.add((EC1990['CharacteristicCombination'], RDFS.label, Literal('Characteristic Combination', lang='en')))
g.add((EC1990['CharacteristicCombination'], RDFS.comment, Literal('Serviceability combination normally used for irreversible limit states.', lang='en')))
g.add((EC1990['CharacteristicCombination'], SKOS.definition, Literal('Serviceability combination normally used for irreversible limit states.')))
g.add((EC1990['CharacteristicCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.5.3(2)a')))

g.add((EC1990['FrequentCombination'], RDF.type, OWL.Class))
g.add((EC1990['FrequentCombination'], RDFS.subClassOf, EC1990.SLSCombination))
g.add((EC1990['FrequentCombination'], RDFS.label, Literal('Frequent Combination', lang='en')))
g.add((EC1990['FrequentCombination'], RDFS.comment, Literal('Serviceability combination normally used for reversible limit states.', lang='en')))
g.add((EC1990['FrequentCombination'], SKOS.definition, Literal('Serviceability combination normally used for reversible limit states.')))
g.add((EC1990['FrequentCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.5.3(2)b')))

g.add((EC1990['QuasiPermanentCombination'], RDF.type, OWL.Class))
g.add((EC1990['QuasiPermanentCombination'], RDFS.subClassOf, EC1990.SLSCombination))
g.add((EC1990['QuasiPermanentCombination'], RDFS.label, Literal('Quasi-Permanent Combination', lang='en')))
g.add((EC1990['QuasiPermanentCombination'], RDFS.comment, Literal('Serviceability combination normally used for long-term effects and the appearance of the structure.', lang='en')))
g.add((EC1990['QuasiPermanentCombination'], SKOS.definition, Literal('Serviceability combination normally used for long-term effects and the appearance of the structure.')))
g.add((EC1990['QuasiPermanentCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.5.3(2)c')))

##########################################################
#                    EFFECTS OF ACTIONS                  #
##########################################################

g.add((EC1990['EffectOfAction'], RDF.type, OWL.Class))
g.add((EC1990['EffectOfAction'], RDFS.subClassOf, QUDT.Quantity))
g.add((EC1990['EffectOfAction'], RDFS.label, Literal('Effect of Action', lang='en')))
g.add((EC1990['EffectOfAction'], RDFS.comment, Literal('Effect of actions on structural members (e.g. internal force, moment, stress, strain) or on the whole structure (e.g. deflection, rotation).', lang='en')))
g.add((EC1990['EffectOfAction'], SKOS.definition, Literal('Effect of actions on structural members (e.g. internal force, moment, stress, strain) or on the whole structure (e.g. deflection, rotation).')))
g.add((EC1990['EffectOfAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))
g.add((EC1990['EffectOfAction'], SKOS.example, Literal('internal force, moment, stress, strain, deflection, rotation')))
g.add((EC1990['EffectOfAction'], SKOS.altLabel, Literal('E')))

# Major effect categories
g.add((EC1990['MechanicalEffect'], RDF.type, OWL.Class))
g.add((EC1990['MechanicalEffect'], RDFS.subClassOf, EC1990.EffectOfAction))
g.add((EC1990['MechanicalEffect'], RDFS.label, Literal('Mechanical Effect', lang='en')))
g.add((EC1990['MechanicalEffect'], RDFS.comment, Literal('Effect of actions in the form of forces, stresses, or strains in structural members.', lang='en')))
g.add((EC1990['MechanicalEffect'], SKOS.definition, Literal('Effect of actions in the form of forces, stresses, or strains in structural members.')))

g.add((EC1990['DeformationEffect'], RDF.type, OWL.Class))
g.add((EC1990['DeformationEffect'], RDFS.subClassOf, EC1990.EffectOfAction))
g.add((EC1990['DeformationEffect'], RDFS.label, Literal('Deformation Effect', lang='en')))
g.add((EC1990['DeformationEffect'], RDFS.comment, Literal('Effect of actions in the form of deformations of the structure or structural members.', lang='en')))
g.add((EC1990['DeformationEffect'], SKOS.definition, Literal('Effect of actions in the form of deformations of the structure or structural members.')))

g.add((EC1990['DynamicEffect'], RDF.type, OWL.Class))
g.add((EC1990['DynamicEffect'], RDFS.subClassOf, EC1990.EffectOfAction))
g.add((EC1990['DynamicEffect'], RDFS.label, Literal('Dynamic Effect', lang='en')))
g.add((EC1990['DynamicEffect'], RDFS.comment, Literal('Effect of actions involving dynamic response, acceleration, or vibration.', lang='en')))
g.add((EC1990['DynamicEffect'], SKOS.definition, Literal('Effect of actions involving dynamic response, acceleration, or vibration.')))

g.add((EC1990['TimeDependentEffect'], RDF.type, OWL.Class))
g.add((EC1990['TimeDependentEffect'], RDFS.subClassOf, EC1990.EffectOfAction))
g.add((EC1990['TimeDependentEffect'], RDFS.label, Literal('Time-Dependent Effect', lang='en')))
g.add((EC1990['TimeDependentEffect'], RDFS.comment, Literal('Effect of actions that varies with time due to material behavior or other time-related factors.', lang='en')))
g.add((EC1990['TimeDependentEffect'], SKOS.definition, Literal('Effect of actions that varies with time due to material behavior or other time-related factors.')))
g.add((EC1990['TimeDependentEffect'], DCTERMS.source, Literal('EN 1990:2002, Section 3.1(5)')))

# Mechanical Effects
g.add((EC1990['InternalForce'], RDF.type, OWL.Class))
g.add((EC1990['InternalForce'], RDFS.subClassOf, EC1990.MechanicalEffect))
g.add((EC1990['InternalForce'], RDFS.label, Literal('Internal Force', lang='en')))
g.add((EC1990['InternalForce'], RDFS.comment, Literal('Effect of actions in the form of internal forces in structural members.', lang='en')))
g.add((EC1990['InternalForce'], SKOS.definition, Literal('Effect of actions in the form of internal forces in structural members.')))
g.add((EC1990['InternalForce'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

g.add((EC1990['BendingMoment'], RDF.type, OWL.Class))
g.add((EC1990['BendingMoment'], RDFS.subClassOf, EC1990.InternalForce))
g.add((EC1990['BendingMoment'], RDFS.label, Literal('Bending Moment', lang='en')))
g.add((EC1990['BendingMoment'], RDFS.comment, Literal('Internal moment causing bending in structural members.', lang='en')))
g.add((EC1990['BendingMoment'], SKOS.definition, Literal('Internal moment causing bending in structural members.')))
g.add((EC1990['BendingMoment'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))
g.add((EC1990['BendingMoment'], SKOS.altLabel, Literal('M')))

g.add((EC1990['AxialForce'], RDF.type, OWL.Class))
g.add((EC1990['AxialForce'], RDFS.subClassOf, EC1990.InternalForce))
g.add((EC1990['AxialForce'], RDFS.label, Literal('Axial Force', lang='en')))
g.add((EC1990['AxialForce'], RDFS.comment, Literal('Internal force acting along the axis of structural members.', lang='en')))
g.add((EC1990['AxialForce'], SKOS.definition, Literal('Internal force acting along the axis of structural members.')))
g.add((EC1990['AxialForce'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))
g.add((EC1990['AxialForce'], SKOS.altLabel, Literal('N')))

g.add((EC1990['ShearForce'], RDF.type, OWL.Class))
g.add((EC1990['ShearForce'], RDFS.subClassOf, EC1990.InternalForce))
g.add((EC1990['ShearForce'], RDFS.label, Literal('Shear Force', lang='en')))
g.add((EC1990['ShearForce'], RDFS.comment, Literal('Internal force acting perpendicular to the axis of structural members.', lang='en')))
g.add((EC1990['ShearForce'], SKOS.definition, Literal('Internal force acting perpendicular to the axis of structural members.')))
g.add((EC1990['ShearForce'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))
g.add((EC1990['ShearForce'], SKOS.altLabel, Literal('V')))

g.add((EC1990['TorsionalMoment'], RDF.type, OWL.Class))
g.add((EC1990['TorsionalMoment'], RDFS.subClassOf, EC1990.InternalForce))
g.add((EC1990['TorsionalMoment'], RDFS.label, Literal('Torsional Moment', lang='en')))
g.add((EC1990['TorsionalMoment'], RDFS.comment, Literal('Internal moment causing twisting in structural members.', lang='en')))
g.add((EC1990['TorsionalMoment'], SKOS.definition, Literal('Internal moment causing twisting in structural members.')))
g.add((EC1990['TorsionalMoment'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))
g.add((EC1990['TorsionalMoment'], SKOS.altLabel, Literal('T')))

g.add((EC1990['Stress'], RDF.type, OWL.Class))
g.add((EC1990['Stress'], RDFS.subClassOf, EC1990.MechanicalEffect))
g.add((EC1990['Stress'], RDFS.label, Literal('Stress', lang='en')))
g.add((EC1990['Stress'], RDFS.comment, Literal('Internal stress in structural members due to actions.', lang='en')))
g.add((EC1990['Stress'], SKOS.definition, Literal('Internal stress in structural members due to actions.')))
g.add((EC1990['Stress'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

g.add((EC1990['NormalStress'], RDF.type, OWL.Class))
g.add((EC1990['NormalStress'], RDFS.subClassOf, EC1990.Stress))
g.add((EC1990['NormalStress'], RDFS.label, Literal('Normal Stress', lang='en')))
g.add((EC1990['NormalStress'], RDFS.comment, Literal('Stress acting in the direction normal to a surface.', lang='en')))
g.add((EC1990['NormalStress'], SKOS.definition, Literal('Stress acting in the direction normal to a surface.')))

g.add((EC1990['ShearStress'], RDF.type, OWL.Class))
g.add((EC1990['ShearStress'], RDFS.subClassOf, EC1990.Stress))
g.add((EC1990['ShearStress'], RDFS.label, Literal('Shear Stress', lang='en')))
g.add((EC1990['ShearStress'], RDFS.comment, Literal('Stress acting in the direction parallel (tangential) to a surface.', lang='en')))
g.add((EC1990['ShearStress'], SKOS.definition, Literal('Stress acting in the direction parallel (tangential) to a surface.')))

g.add((EC1990['PrincipalStress'], RDF.type, OWL.Class))
g.add((EC1990['PrincipalStress'], RDFS.subClassOf, EC1990.Stress))
g.add((EC1990['PrincipalStress'], RDFS.label, Literal('Principal Stress', lang='en')))
g.add((EC1990['PrincipalStress'], RDFS.comment, Literal('Maximum or minimum normal stress at a point.', lang='en')))
g.add((EC1990['PrincipalStress'], SKOS.definition, Literal('Maximum or minimum normal stress at a point.')))

g.add((EC1990['Strain'], RDF.type, OWL.Class))
g.add((EC1990['Strain'], RDFS.subClassOf, EC1990.MechanicalEffect))
g.add((EC1990['Strain'], RDFS.label, Literal('Strain', lang='en')))
g.add((EC1990['Strain'], RDFS.comment, Literal('Deformation per unit length in structural members.', lang='en')))
g.add((EC1990['Strain'], SKOS.definition, Literal('Deformation per unit length in structural members.')))
g.add((EC1990['Strain'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

# Deformation Effects
g.add((EC1990['Deformation'], RDF.type, OWL.Class))
g.add((EC1990['Deformation'], RDFS.subClassOf, EC1990.DeformationEffect))
g.add((EC1990['Deformation'], RDFS.label, Literal('Deformation', lang='en')))
g.add((EC1990['Deformation'], RDFS.comment, Literal('Change in shape or size of a structure or structural member due to actions.', lang='en')))
g.add((EC1990['Deformation'], SKOS.definition, Literal('Change in shape or size of a structure or structural member due to actions.')))
g.add((EC1990['Deformation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

g.add((EC1990['LinearDeformation'], RDF.type, OWL.Class))
g.add((EC1990['LinearDeformation'], RDFS.subClassOf, EC1990.Deformation))
g.add((EC1990['LinearDeformation'], RDFS.label, Literal('Linear Deformation', lang='en')))
g.add((EC1990['LinearDeformation'], RDFS.comment, Literal('Deformation involving linear displacement of points in the structure.', lang='en')))
g.add((EC1990['LinearDeformation'], SKOS.definition, Literal('Deformation involving linear displacement of points in the structure.')))

g.add((EC1990['Deflection'], RDF.type, OWL.Class))
g.add((EC1990['Deflection'], RDFS.subClassOf, EC1990.LinearDeformation))
g.add((EC1990['Deflection'], RDFS.label, Literal('Deflection', lang='en')))
g.add((EC1990['Deflection'], RDFS.comment, Literal('Vertical deflction of a structural member.', lang='en')))
g.add((EC1990['Deflection'], SKOS.definition, Literal('Vertical deflction of a structural member.')))
g.add((EC1990['Deflection'], DCTERMS.source, Literal('EN 1990:2002, Section 1.6')))
g.add((EC1990['Deflection'], SKOS.altLabel, Literal('w')))

g.add((EC1990['Displacement'], RDF.type, OWL.Class))
g.add((EC1990['Displacement'], RDFS.subClassOf, EC1990.LinearDeformation))
g.add((EC1990['Displacement'], RDFS.label, Literal('Displacement', lang='en')))
g.add((EC1990['Displacement'], RDFS.comment, Literal('Horizontal displacement of a structure or structural member.', lang='en')))
g.add((EC1990['Displacement'], SKOS.definition, Literal('Horizontal displacement of a structure or structural member.')))
g.add((EC1990['Displacement'], DCTERMS.source, Literal('EN 1990:2002, Section 1.6')))
g.add((EC1990['Displacement'], SKOS.altLabel, Literal('u')))

g.add((EC1990['AngularDeformation'], RDF.type, OWL.Class))
g.add((EC1990['AngularDeformation'], RDFS.subClassOf, EC1990.Deformation))
g.add((EC1990['AngularDeformation'], RDFS.label, Literal('Angular Deformation', lang='en')))
g.add((EC1990['AngularDeformation'], RDFS.comment, Literal('Deformation involving rotation or angular change in the structure.', lang='en')))
g.add((EC1990['AngularDeformation'], SKOS.definition, Literal('Deformation involving rotation or angular change in the structure.')))
g.add((EC1990['AngularDeformation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

g.add((EC1990['Rotation'], RDF.type, OWL.Class))
g.add((EC1990['Rotation'], RDFS.subClassOf, EC1990.AngularDeformation))
g.add((EC1990['Rotation'], RDFS.label, Literal('Rotation', lang='en')))
g.add((EC1990['Rotation'], RDFS.comment, Literal('Angular rotation of a structure or structural member.', lang='en')))
g.add((EC1990['Rotation'], SKOS.definition, Literal('Angular rotation of a structure or structural member.')))
g.add((EC1990['Rotation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

g.add((EC1990['Twist'], RDF.type, OWL.Class))
g.add((EC1990['Twist'], RDFS.subClassOf, EC1990.AngularDeformation))
g.add((EC1990['Twist'], RDFS.label, Literal('Twist', lang='en')))
g.add((EC1990['Twist'], RDFS.comment, Literal('Angular deformation about the longitudinal axis.', lang='en')))
g.add((EC1990['Twist'], SKOS.definition, Literal('Angular deformation about the longitudinal axis.')))

g.add((EC1990['VolumetricDeformation'], RDF.type, OWL.Class))
g.add((EC1990['VolumetricDeformation'], RDFS.subClassOf, EC1990.Deformation))
g.add((EC1990['VolumetricDeformation'], RDFS.label, Literal('Volumetric Deformation', lang='en')))
g.add((EC1990['VolumetricDeformation'], RDFS.comment, Literal('Deformation involving change in volume of structural elements.', lang='en')))
g.add((EC1990['VolumetricDeformation'], SKOS.definition, Literal('Deformation involving change in volume of structural elements.')))

# Dynamic Effects
g.add((EC1990['AccelerationEffect'], RDF.type, OWL.Class))
g.add((EC1990['AccelerationEffect'], RDFS.subClassOf, EC1990.DynamicEffect))
g.add((EC1990['AccelerationEffect'], RDFS.label, Literal('Acceleration Effect', lang='en')))
g.add((EC1990['AccelerationEffect'], RDFS.comment, Literal('Effect involving acceleration of the structure or structural members.', lang='en')))
g.add((EC1990['AccelerationEffect'], SKOS.definition, Literal('Effect involving acceleration of the structure or structural members.')))
g.add((EC1990['AccelerationEffect'], DCTERMS.source, Literal('EN 1990:2002, Section 4.1.5(2)')))

g.add((EC1990['VibrationResponse'], RDF.type, OWL.Class))
g.add((EC1990['VibrationResponse'], RDFS.subClassOf, EC1990.DynamicEffect))
g.add((EC1990['VibrationResponse'], RDFS.label, Literal('Vibration Response', lang='en')))
g.add((EC1990['VibrationResponse'], RDFS.comment, Literal('Dynamic response of structures to oscillatory actions, important for serviceability considerations.', lang='en')))
g.add((EC1990['VibrationResponse'], SKOS.definition, Literal('Dynamic response of structures to oscillatory actions, important for serviceability considerations.')))

# Time-Dependent Effects
g.add((EC1990['CreepEffect'], RDF.type, OWL.Class))
g.add((EC1990['CreepEffect'], RDFS.subClassOf, EC1990.TimeDependentEffect))
g.add((EC1990['CreepEffect'], RDFS.label, Literal('Creep Effect', lang='en')))
g.add((EC1990['CreepEffect'], RDFS.comment, Literal('Long-term deformation effect due to sustained loading.', lang='en')))
g.add((EC1990['CreepEffect'], SKOS.definition, Literal('Long-term deformation effect due to sustained loading.')))

g.add((EC1990['ShrinkageEffect'], RDF.type, OWL.Class))
g.add((EC1990['ShrinkageEffect'], RDFS.subClassOf, EC1990.TimeDependentEffect))
g.add((EC1990['ShrinkageEffect'], RDFS.label, Literal('Shrinkage Effect', lang='en')))
g.add((EC1990['ShrinkageEffect'], RDFS.comment, Literal('Deformation effect due to material shrinkage over time.', lang='en')))
g.add((EC1990['ShrinkageEffect'], SKOS.definition, Literal('Deformation effect due to material shrinkage over time.')))

g.add((EC1990['FatigueEffect'], RDF.type, OWL.Class))
g.add((EC1990['FatigueEffect'], RDFS.subClassOf, EC1990.TimeDependentEffect))
g.add((EC1990['FatigueEffect'], RDFS.label, Literal('Fatigue Effect', lang='en')))
g.add((EC1990['FatigueEffect'], RDFS.comment, Literal('Progressive damage effect due to repeated loading cycles.', lang='en')))
g.add((EC1990['FatigueEffect'], SKOS.definition, Literal('Progressive damage effect due to repeated loading cycles.')))
g.add((EC1990['FatigueEffect'], DCTERMS.source, Literal('EN 1990:2002, Section 3.1(5)')))

g.add((EC1990['Reaction'], RDF.type, OWL.Class))
g.add((EC1990['Reaction'], RDFS.subClassOf, EC1990.EffectOfAction))
g.add((EC1990['Reaction'], RDFS.label, Literal('Reaction', lang='en')))
g.add((EC1990['Reaction'], RDFS.comment, Literal('Support reaction force or moment at structural supports.', lang='en')))
g.add((EC1990['Reaction'], SKOS.definition, Literal('Support reaction force or moment at structural supports.')))
g.add((EC1990['Reaction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

##########################################################
#                MATERIAL AND RESISTANCE                 #
##########################################################

g.add((EC1990['Material'], RDF.type, OWL.Class))
g.add((EC1990['Material'], RDFS.label, Literal('Material', lang='en')))
g.add((EC1990['Material'], RDFS.comment, Literal('Indication of the principal structural material.', lang='en')))
g.add((EC1990['Material'], SKOS.definition, Literal('Indication of the principal structural material.')))
g.add((EC1990['Material'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.3')))

g.add((EC1990['Concrete'], RDF.type, OWL.Class))
g.add((EC1990['Concrete'], RDFS.subClassOf, EC1990.Material))
g.add((EC1990['Concrete'], RDFS.label, Literal('Concrete', lang='en')))
g.add((EC1990['Concrete'], RDFS.comment, Literal('A composite material consisting of a mixture of cement, water, aggregates (coarse and fine), and, where appropriate, admixtures and additions, which develops its strength by hydration of the cement. ', lang='en')))
g.add((EC1990['Concrete'], SKOS.definition, Literal('A composite material consisting of a mixture of cement, water, aggregates (coarse and fine), and, where appropriate, admixtures and additions, which develops its strength by hydration of the cement. ')))

g.add((EC1990['MaterialProperty'], RDF.type, OWL.Class))
g.add((EC1990['MaterialProperty'], RDFS.subClassOf, QUDT.Quantity))
g.add((EC1990['MaterialProperty'], RDFS.label, Literal('Material Property', lang='en')))
g.add((EC1990['MaterialProperty'], RDFS.comment, Literal('Physical or mechanical property of construction materials.', lang='en')))
g.add((EC1990['MaterialProperty'], SKOS.definition, Literal('Physical or mechanical property of construction materials.')))
g.add((EC1990['MaterialProperty'], DCTERMS.source, Literal('EN 1990:2002, Section 4.2')))

g.add((EC1990['Density'], RDF.type, OWL.Class))
g.add((EC1990['Density'], RDFS.subClassOf, EC1990.MaterialProperty))
g.add((EC1990['Density'], RDFS.label, Literal('Density', lang='en')))
g.add((EC1990['Density'], RDFS.comment, Literal('Mass per unit volume of a material.', lang='en')))
g.add((EC1990['Density'], SKOS.definition, Literal('Mass per unit volume of a material.')))

g.add((EC1990['CompressiveStrength'], RDF.type, OWL.Class))
g.add((EC1990['CompressiveStrength'], RDFS.subClassOf, EC1990.MaterialProperty))
g.add((EC1990['CompressiveStrength'], RDFS.label, Literal('Compressive Strength', lang='en')))
g.add((EC1990['CompressiveStrength'], RDFS.comment, Literal('Compressive strenght of a material.', lang='en')))
g.add((EC1990['CompressiveStrength'], SKOS.definition, Literal('Compressive Strength of a material.')))

g.add((EC1990['GeometricalProperty'], RDF.type, OWL.Class))
g.add((EC1990['GeometricalProperty'], RDFS.subClassOf, QUDT.Quantity))
g.add((EC1990['GeometricalProperty'], RDFS.label, Literal('Geometrical Data', lang='en')))
g.add((EC1990['GeometricalProperty'], RDFS.comment, Literal('Geometrical properties and dimensions of structural elements.', lang='en')))
g.add((EC1990['GeometricalProperty'], SKOS.definition, Literal('Geometrical properties and dimensions of structural elements.')))
g.add((EC1990['GeometricalProperty'], DCTERMS.source, Literal('EN 1990:2002, Section 4.3')))

g.add((EC1990['Thickness'], RDF.type, OWL.Class))
g.add((EC1990['Thickness'], RDFS.subClassOf, EC1990.GeometricalProperty))
g.add((EC1990['Thickness'], RDFS.label, Literal('Thickness', lang='en')))
g.add((EC1990['Thickness'], RDFS.comment, Literal('Dimension of a structural element measured perpendicular to its plane or surface.', lang='en')))
g.add((EC1990['Thickness'], SKOS.definition, Literal('Dimension of a structural element measured perpendicular to its plane or surface.')))

g.add((EC1990['LimitStateValue'], RDF.type, OWL.Class))
g.add((EC1990['LimitStateValue'], RDFS.subClassOf, QUDT.Quantity))
g.add((EC1990['LimitStateValue'], RDFS.label, Literal('Limit State Value', lang='en')))
g.add((EC1990['LimitStateValue'], RDFS.comment, Literal('Design resistance or serviceability criterion used for verificatinon of a limit state.', lang='en')))
g.add((EC1990['LimitStateValue'], SKOS.definition, Literal('Design resistance or serviceability criterion used for verificatinon of a limit state.')))

g.add((EC1990['Resistance'], RDF.type, OWL.Class))
g.add((EC1990['Resistance'], RDFS.subClassOf, EC1990.LimitStateValue))
g.add((EC1990['Resistance'], RDFS.label, Literal('Resistance', lang='en')))
g.add((EC1990['Resistance'], RDFS.comment, Literal('Capacity of a member or component, or a cross-section of a member or component of a structure, to withstand actions without mechanical failure.', lang='en')))
g.add((EC1990['Resistance'], SKOS.definition, Literal('Capacity of a member or component, or a cross-section of a member or component of a structure, to withstand actions without mechanical failure.')))
g.add((EC1990['Resistance'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.15')))
g.add((EC1990['Resistance'], SKOS.example, Literal('bending resistance, buckling resistance, tension resistance')))
g.add((EC1990['Resistance'], SKOS.altLabel, Literal('R')))

g.add((EC1990['BendingMomentResistance'], RDF.type, OWL.Class))
g.add((EC1990['BendingMomentResistance'], RDFS.subClassOf, EC1990.Resistance))
g.add((EC1990['BendingMomentResistance'], RDFS.label, Literal('Bending Moment Resistance', lang='en')))
g.add((EC1990['BendingMomentResistance'], RDFS.comment, Literal('Design value of the maximum bending moment that a structural cross-section can safely resist without failure.', lang='en')))
g.add((EC1990['BendingMomentResistance'], SKOS.definition, Literal('Design value of the maximum bending moment that a structural cross-section can safely resist without failure.')))
g.add((EC1990['BendingMomentResistance'], SKOS.altLabel, Literal('M_Rd')))

g.add((EC1990['LimitingServicabilityCriterion'], RDF.type, OWL.Class))
g.add((EC1990['LimitingServicabilityCriterion'], RDFS.subClassOf, EC1990.LimitStateValue))
g.add((EC1990['LimitingServicabilityCriterion'], RDFS.label, Literal('Limiting Serviceability Criterion', lang='en')))
g.add((EC1990['LimitingServicabilityCriterion'], RDFS.comment, Literal('Limiting design value of the relevant serviceability criterion.', lang='en')))
g.add((EC1990['LimitingServicabilityCriterion'], SKOS.definition, Literal('Limiting design value of the relevant serviceability criterion.')))
g.add((EC1990['LimitingServicabilityCriterion'], DCTERMS.source, Literal('EN 1990:2002, Section 6.5.1')))
g.add((EC1990['LimitingServicabilityCriterion'], SKOS.example, Literal('allowable deflection, allowable crack width')))

##########################################################
#                        VALUES                          #
##########################################################

g.add((EC1990['RepresentativeValue'], RDF.type, OWL.Class))
g.add((EC1990['RepresentativeValue'], RDFS.subClassOf, QUDT.QuantityValue))

g.add((EC1990['NominalValue'], RDF.type, OWL.Class))
g.add((EC1990['NominalValue'], RDFS.subClassOf, QUDT.QuantityValue))

g.add((EC1990['CharacteristicValue'], RDF.type, OWL.Class))
g.add((EC1990['CharacteristicValue'], RDFS.subClassOf, QUDT.QuantityValue))

g.add((EC1990['DesignValue'], RDF.type, OWL.Class))
g.add((EC1990['DesignValue'], RDFS.subClassOf, QUDT.QuantityValue))

g.add((EC1990['MeanValue'], RDF.type, OWL.Class))
g.add((EC1990['MeanValue'], RDFS.subClassOf, QUDT.QuantityValue))

g.add((EC1990['LowerValue'], RDF.type, OWL.Class))
g.add((EC1990['LowerValue'], RDFS.subClassOf, QUDT.QuantityValue))

g.add((EC1990['UpperValue'], RDF.type, OWL.Class))
g.add((EC1990['UpperValue'], RDFS.subClassOf, QUDT.QuantityValue))

##########################################################
#                 OBJECT PROPERTIES                      #
##########################################################

g.add((EC1990['representativeValue'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['representativeValue'], RDFS.subPropertyOf, QUDT.quantityValue))
g.add((EC1990['representativeValue'], RDFS.label, Literal('representative value', lang='en')))
g.add((EC1990['representativeValue'], RDFS.comment, Literal('Relates a Quantity  with its Representative Value.', lang='en')))
g.add((EC1990['representativeValue'], SKOS.definition, Literal('Relates a Quantity  with its Representative Value.')))
g.add((EC1990['representativeValue'], RDFS.domain, QUDT.Quantity))
g.add((EC1990['representativeValue'], RDFS.range, EC1990.RepresentativeValue))

g.add((EC1990['nominalValue'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['nominalValue'], RDFS.subPropertyOf, QUDT.quantityValue))
g.add((EC1990['nominalValue'], RDFS.label, Literal('nominal value', lang='en')))
g.add((EC1990['nominalValue'], RDFS.comment, Literal('Relates a Quantity  with its Nominal Value.', lang='en')))
g.add((EC1990['nominalValue'], SKOS.definition, Literal('Relates a Quantity  with its Nominal Value.')))
g.add((EC1990['nominalValue'], RDFS.domain, QUDT.Quantity))
g.add((EC1990['nominalValue'], RDFS.range, EC1990.NominalValue))

g.add((EC1990['designValue'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['designValue'], RDFS.subPropertyOf, QUDT.quantityValue))
g.add((EC1990['designValue'], RDFS.label, Literal('design value', lang='en')))
g.add((EC1990['designValue'], RDFS.comment, Literal('Relates a Quantity  with its Design Value.', lang='en')))
g.add((EC1990['designValue'], SKOS.definition, Literal('Relates a Quantity  with its Design Value.')))
g.add((EC1990['designValue'], RDFS.domain, QUDT.Quantity))
g.add((EC1990['designValue'], RDFS.range, EC1990.DesignValue))

g.add((EC1990['characteristicValue'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['characteristicValue'], RDFS.subPropertyOf, QUDT.quantityValue))
g.add((EC1990['characteristicValue'], RDFS.label, Literal('characteristic value', lang='en')))
g.add((EC1990['characteristicValue'], RDFS.comment, Literal('Relates a Quantity  with its Characteristic Value.', lang='en')))
g.add((EC1990['characteristicValue'], SKOS.definition, Literal('Relates a Quantity  with its Characteristic Value.')))
g.add((EC1990['characteristicValue'], RDFS.domain, QUDT.Quantity))
g.add((EC1990['characteristicValue'], RDFS.range, EC1990.CharacteristicValue))

g.add((EC1990['meanValue'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['meanValue'], RDFS.subPropertyOf, QUDT.quantityValue))
g.add((EC1990['meanValue'], RDFS.label, Literal('mean value', lang='en')))
g.add((EC1990['meanValue'], RDFS.comment, Literal('Relates a Quantity  with its Mean Value.', lang='en')))
g.add((EC1990['meanValue'], SKOS.definition, Literal('Relates a Quantity  with its Mean Value.')))
g.add((EC1990['meanValue'], RDFS.domain, QUDT.Quantity))
g.add((EC1990['meanValue'], RDFS.range, EC1990.MeanValue))

g.add((EC1990['lowerValue'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['lowerValue'], RDFS.subPropertyOf, QUDT.quantityValue))
g.add((EC1990['lowerValue'], RDFS.label, Literal('lower value', lang='en')))
g.add((EC1990['lowerValue'], RDFS.comment, Literal('Relates a Quantity  with its Lower Value.', lang='en')))
g.add((EC1990['lowerValue'], SKOS.definition, Literal('Relates a Quantity  with its Lower Value.')))
g.add((EC1990['lowerValue'], RDFS.domain, QUDT.Quantity))
g.add((EC1990['lowerValue'], RDFS.range, EC1990.LowerValue))

g.add((EC1990['upperValue'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['upperValue'], RDFS.subPropertyOf, QUDT.quantityValue))
g.add((EC1990['upperValue'], RDFS.label, Literal('upper value', lang='en')))
g.add((EC1990['upperValue'], RDFS.comment, Literal('Relates a Quantity  with its Upper Value.', lang='en')))
g.add((EC1990['upperValue'], SKOS.definition, Literal('Relates a Quantity  with its Upper Value.')))
g.add((EC1990['upperValue'], RDFS.domain, QUDT.Quantity))
g.add((EC1990['upperValue'], RDFS.range, EC1990.UpperValue))

g.add((EC1990['containsAction'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['containsAction'], RDFS.label, Literal('contains action', lang='en')))
g.add((EC1990['containsAction'], RDFS.comment, Literal('Relates a combination of actions to the individual actions it contains.', lang='en')))
g.add((EC1990['containsAction'], SKOS.definition, Literal('Relates a combination of actions to the individual actions it contains.')))
g.add((EC1990['containsAction'], RDFS.domain, EC1990.CombinationOfActions))
g.add((EC1990['containsAction'], RDFS.range, EC1990.Action))

g.add((EC1990['causesEffect'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['causesEffect'], RDFS.label, Literal('causes effect', lang='en')))
g.add((EC1990['causesEffect'], RDFS.comment, Literal('Relates a combination of actions to the effects it causes in the structure.', lang='en')))
g.add((EC1990['causesEffect'], SKOS.definition, Literal('Relates a combination of actions to the effects it causes in the structure.')))
g.add((EC1990['causesEffect'], RDFS.domain, EC1990.CombinationOfActions))
g.add((EC1990['causesEffect'], RDFS.range, EC1990.EffectOfAction))

g.add((EC1990['appliesTo'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['appliesTo'], RDFS.label, Literal('applies to', lang='en')))
g.add((EC1990['appliesTo'], RDFS.comment, Literal('Relates an action to the structural member or structure it acts upon.', lang='en')))
g.add((EC1990['appliesTo'], SKOS.definition, Literal('Relates an action to the structural member or structure it acts upon.')))
g.add((EC1990['appliesTo'], RDFS.domain, EC1990.Action))
g.add((EC1990['appliesTo'], RDFS.range, EC1990.StructuralMember))

g.add((EC1990['isDesignedFor'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['isDesignedFor'], RDFS.label, Literal('is designed for', lang='en')))
g.add((EC1990['isDesignedFor'], RDFS.comment, Literal('Relates a structural memeber with the design situation it is designed for.', lang='en')))
g.add((EC1990['isDesignedFor'], SKOS.definition, Literal('Relates a structural memeber with the design situation it is designed for.')))
g.add((EC1990['isDesignedFor'], RDFS.domain, EC1990.StructuralMember))
g.add((EC1990['isDesignedFor'], RDFS.range, EC1990.DesignSituation))

g.add((EC1990['requiresVerficationOf'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['requiresVerficationOf'], RDFS.label, Literal('requires verification of', lang='en')))
g.add((EC1990['requiresVerficationOf'], RDFS.comment, Literal('Relates a limit state to the combination of actions used for its verification.', lang='en')))
g.add((EC1990['requiresVerficationOf'], SKOS.definition, Literal('Relates a limit state to the combination of actions used for its verification.')))
g.add((EC1990['requiresVerficationOf'], RDFS.domain, EC1990.DesignSituation))
g.add((EC1990['requiresVerficationOf'], RDFS.range, EC1990.LimitState))

g.add((EC1990['verifiedFor'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['verifiedFor'], RDFS.label, Literal('verified for', lang='en')))
g.add((EC1990['verifiedFor'], RDFS.comment, Literal('Relates a limit state to the combination of actions used for its verification.', lang='en')))
g.add((EC1990['verifiedFor'], SKOS.definition, Literal('Relates a limit state to the combination of actions used for its verification.')))
g.add((EC1990['verifiedFor'], RDFS.domain, EC1990.LimitState))
g.add((EC1990['verifiedFor'], RDFS.range, EC1990.CombinationOfActions))

g.add((EC1990['imposesCombination'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['imposesCombination'], RDFS.label, Literal('imposes combination', lang='en')))
g.add((EC1990['imposesCombination'], RDFS.comment, Literal('Relates a design situation to the relevant combination.', lang='en')))
g.add((EC1990['imposesCombination'], SKOS.definition, Literal('Relates a design situation to the relevant combination.')))
g.add((EC1990['imposesCombination'], RDFS.domain, EC1990.DesignSituation))
g.add((EC1990['imposesCombination'], RDFS.range, EC1990.CombinationOfActions))

g.add((EC1990['hasEffect'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasEffect'], RDFS.label, Literal('has effect', lang='en')))
g.add((EC1990['hasEffect'], RDFS.comment, Literal('Relates a structural member to the effect of action.', lang='en')))
g.add((EC1990['hasEffect'], SKOS.definition, Literal('Relates a structural member to the effect of action.')))
g.add((EC1990['hasEffect'], RDFS.domain, EC1990.StructuralMember))
g.add((EC1990['hasEffect'], RDFS.range, EC1990.EffectOfAction))

g.add((EC1990['hasLimitStateValue'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasLimitStateValue'], RDFS.label, Literal('has limit state value', lang='en')))
g.add((EC1990['hasLimitStateValue'], RDFS.comment, Literal('Relates a structural member to its capacity for the effect of action.', lang='en')))
g.add((EC1990['hasLimitStateValue'], SKOS.definition, Literal('Relates a structural member to its capacity for the effect of action.')))
g.add((EC1990['hasLimitStateValue'], RDFS.domain, EC1990.StructuralMember))
g.add((EC1990['hasLimitStateValue'], RDFS.range, EC1990.LimitStateValue))

g.add((EC1990['forLimitState'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['forLimitState'], RDFS.label, Literal('for limit state', lang='en')))
g.add((EC1990['forLimitState'], RDFS.comment, Literal('Relates a limit state value with its corresponding limit state.', lang='en')))
g.add((EC1990['forLimitState'], SKOS.definition, Literal('Relates a limit state value with its corresponding limit state.')))
g.add((EC1990['forLimitState'], RDFS.domain, EC1990.LimitStateValue))
g.add((EC1990['forLimitState'], RDFS.range, EC1990.LimitState))

g.add((EC1990['verifiedAgainstEffect'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['verifiedAgainstEffect'], RDFS.label, Literal('has limit state value', lang='en')))
g.add((EC1990['verifiedAgainstEffect'], RDFS.comment, Literal('Relates a limitstate value with the Action Effect that needs to be verified against.', lang='en')))
g.add((EC1990['verifiedAgainstEffect'], SKOS.definition, Literal('Relates a limitstate value with the Action Effect that needs to be verified against.')))
g.add((EC1990['verifiedAgainstEffect'], RDFS.domain, EC1990.LimitStateValue))
g.add((EC1990['verifiedAgainstEffect'], RDFS.range, EC1990.EffectOfAction))

g.add((EC1990['isMadeOf'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['isMadeOf'], RDFS.label, Literal('is made of', lang='en')))
g.add((EC1990['isMadeOf'], RDFS.comment, Literal('Relates a structural member to the material which it is made of.', lang='en')))
g.add((EC1990['isMadeOf'], SKOS.definition, Literal('Relates a structural member to the material which it is made of.')))
g.add((EC1990['isMadeOf'], RDFS.domain, EC1990.StructuralMember))
g.add((EC1990['isMadeOf'], RDFS.range, EC1990.Material))

g.add((EC1990['hasMaterialProperty'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasMaterialProperty'], RDFS.label, Literal('has Property', lang='en')))
g.add((EC1990['hasMaterialProperty'], RDFS.comment, Literal('Relates a material with its properties.', lang='en')))
g.add((EC1990['hasMaterialProperty'], SKOS.definition, Literal('Relates a material with its properties.')))
g.add((EC1990['hasMaterialProperty'], RDFS.domain, EC1990.Material))
g.add((EC1990['hasMaterialProperty'], RDFS.range, EC1990.MaterialProperty))

g.add((EC1990['hasGeometricalProperty'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasGeometricalProperty'], RDFS.label, Literal('has geometrical property', lang='en')))
g.add((EC1990['hasGeometricalProperty'], RDFS.comment, Literal('Relates a structural member with its geometrical properties.', lang='en')))
g.add((EC1990['hasGeometricalProperty'], SKOS.definition, Literal('Relates a structural member with its geometrical properties.')))
g.add((EC1990['hasGeometricalProperty'], RDFS.domain, EC1990.StructuralMember))
g.add((EC1990['hasGeometricalProperty'], RDFS.range, EC1990.GeometricalProperty))

g.add((EC1990['hasSystem'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasSystem'], RDFS.label, Literal('has system', lang='en')))
g.add((EC1990['hasSystem'], RDFS.comment, Literal('Relates a structure with its structural system.', lang='en')))
g.add((EC1990['hasSystem'], SKOS.definition, Literal('Relates a structure with its structural system.')))
g.add((EC1990['hasSystem'], RDFS.domain, EC1990.Structure))
g.add((EC1990['hasSystem'], RDFS.range, EC1990.StructuralSystem))

g.add((EC1990['hasStructuralMember'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasStructuralMember'], RDFS.subPropertyOf, BOT.hasElement))
g.add((EC1990['hasStructuralMember'], RDFS.label, Literal('has structural member', lang='en')))
g.add((EC1990['hasStructuralMember'], RDFS.comment, Literal('Relates a a structural element with the zone.', lang='en')))
g.add((EC1990['hasStructuralMember'], SKOS.definition, Literal('Relates a a structural element with the zone.')))
g.add((EC1990['hasStructuralMember'], RDFS.domain, BOT.Zone))
g.add((EC1990['hasStructuralMember'], RDFS.range, EC1990.StructuralMember))

g.add((EC1990['containsStructuralMember'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['containsStructuralMember'], RDFS.subPropertyOf, BOT.hasElement))
g.add((EC1990['containsStructuralMember'], RDFS.label, Literal('contains structural member', lang='en')))
g.add((EC1990['containsStructuralMember'], RDFS.comment, Literal('Relates a a structural element with the structural syste.', lang='en')))
g.add((EC1990['containsStructuralMember'], SKOS.definition, Literal('Relates a a structural element with the structural syste.')))
g.add((EC1990['containsStructuralMember'], RDFS.domain, EC1990.StructuralSystem))
g.add((EC1990['containsStructuralMember'], RDFS.range, EC1990.StructuralMember))

g.add((EC1990['hasStructure'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasStructure'], RDFS.subPropertyOf, BOT.hasElement))
g.add((EC1990['hasStructure'], RDFS.label, Literal('has structure', lang='en')))
g.add((EC1990['hasStructure'], RDFS.comment, Literal('Relates a contrution work with the structure.', lang='en')))
g.add((EC1990['hasStructure'], SKOS.definition, Literal('Relates a contrution work with the structure.')))
g.add((EC1990['hasStructure'], RDFS.domain, EC1990.ConstructionWork))
g.add((EC1990['hasStructure'], RDFS.range, EC1990.Structure))

'''g.add((EC1990['belongsTo'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['belongsTo'], RDFS.label, Literal('belongs to', lang='en')))
g.add((EC1990['belongsTo'], RDFS.comment, Literal('Relates a structural element with the zone of which it is a part.', lang='en')))
g.add((EC1990['belongsTo'], SKOS.definition, Literal('Relates a structural element with the zone of which it is a part.')))
g.add((EC1990['belongsTo'], RDFS.domain, EC1990.StructuralMember))
g.add((EC1990['belongsTo'], RDFS.range, BOT.Zone))''' #Not needed. Already defined in BOT 

'''g.add((EC1990['isVerifiedUnder'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['isVerifiedUnder'], RDFS.label, Literal('is verified under', lang='en')))
g.add((EC1990['isVerifiedUnder'], RDFS.comment, Literal('Relates a structural element with the combination of action used for verifcation of elevant Limit State.', lang='en')))
g.add((EC1990['isVerifiedUnder'], SKOS.definition, Literal('Relates a structural element with the combination of action used for verifcation of elevant Limit State.')))
g.add((EC1990['isVerifiedUnder'], RDFS.domain, EC1990.StructuralMember))
g.add((EC1990['isVerifiedUnder'], RDFS.range, EC1990.CombinationOfActions))''' # Redundant

##########################################################
#                 DATA TYPE PROPERTIES                   #
##########################################################

g.add((EC1990['hasDesignWorkingLife'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['hasDesignWorkingLife'], RDFS.label, Literal('has design working life', lang='en')))
g.add((EC1990['hasDesignWorkingLife'], RDFS.comment, Literal('Period during which a structure or structural component is intended to remain functional and to fulfill its performance requirements without major repair or replacement, assuming appropriate maintenance.', lang='en')))
g.add((EC1990['hasDesignWorkingLife'], SKOS.definition, Literal('Period during which a structure or structural component is intended to remain functional and to fulfill its performance requirements without major repair or replacement, assuming appropriate maintenance.')))
g.add((EC1990['hasDesignWorkingLife'], RDFS.domain, EC1990.Structure))
g.add((EC1990['hasDesignWorkingLife'], RDFS.range, XSD.decimal))

#Partial Factors
g.add((EC1990['hasPartialFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['hasPartialFactor'], RDFS.label, Literal('Partial Factor', lang='en')))
g.add((EC1990['hasPartialFactor'], RDFS.comment, Literal('Safety factor applied to actions or material properties to account for uncertainties.', lang='en')))
g.add((EC1990['hasPartialFactor'], SKOS.definition, Literal('Safety factor applied to actions or material properties to account for uncertainties.')))
g.add((EC1990['hasPartialFactor'], DCTERMS.source, Literal('EN 1990:2002, Section 6.3.1')))
g.add((EC1990['hasPartialFactor'], SKOS.altLabel, Literal('γ_f')))
#g.add((EC1990['hasPartialFactor'], RDFS.domain, EC1990.Action))
g.add((EC1990['hasPartialFactor'], RDFS.range, XSD.decimal))

'''g.add((EC1990['hasPermanentActionPartialFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['hasPermanentActionPartialFactor'], RDFS.subPropertyOf, EC1990.hasPartialFactor))
g.add((EC1990['hasPermanentActionPartialFactor'], RDFS.label, Literal('Permanent Action Partial Factor', lang='en')))
g.add((EC1990['hasPermanentActionPartialFactor'], RDFS.comment, Literal('Partial factor applied to permanent actions, also accounting for model uncertainties and dimensional variations.', lang='en')))
g.add((EC1990['hasPermanentActionPartialFactor'], SKOS.definition, Literal('Partial factor applied to permanent actions, also accounting for model uncertainties and dimensional variations.')))
g.add((EC1990['hasPermanentActionPartialFactor'], DCTERMS.source, Literal('EN 1990:2002, Section 6.3.1')))
g.add((EC1990['hasPermanentActionPartialFactor'], RDFS.domain, EC1990.PermanentAction))
g.add((EC1990['hasPermanentActionPartialFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['hasPermanentActionPartialFactor'], SKOS.altLabel, Literal('γ_G')))'''

g.add((EC1990['hasReductionFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['hasReductionFactor'], RDFS.label, Literal('has reduction factor', lang='en')))
g.add((EC1990['hasReductionFactor'], RDFS.comment, Literal('Reduction factor for unfavourable permanent action.', lang='en')))
g.add((EC1990['hasReductionFactor'], SKOS.definition, Literal('Reduction factor for unfavourable permanent action.')))
g.add((EC1990['hasReductionFactor'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.3.2')))
#g.add((EC1990['hasReductionFactor'], RDFS.domain, EC1990.PermanentAction))
g.add((EC1990['hasReductionFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['hasReductionFactor'], SKOS.altLabel, Literal('ξ')))

'''g.add((EC1990['variableActionPartialFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['variableActionPartialFactor'], RDFS.subPropertyOf, EC1990.hasPartialFactor))
g.add((EC1990['variableActionPartialFactor'], RDFS.label, Literal('has variable action partial factor', lang='en')))
g.add((EC1990['variableActionPartialFactor'], RDFS.comment, Literal('Partial factor for variable actions, which takes account of the possibility of unfavourable deviations of the action values from the representative values, also accounting for model uncertainties and dimensional variations.', lang='en')))
g.add((EC1990['variableActionPartialFactor'], SKOS.definition, Literal('Partial factor for variable actions, which takes account of the possibility of unfavourable deviations of the action values from the representative values, also accounting for model uncertainties and dimensional variations.')))
g.add((EC1990['variableActionPartialFactor'], DCTERMS.source, Literal('EN 1990:2002, Section 6.3.1')))
g.add((EC1990['variableActionPartialFactor'], RDFS.domain, EC1990.VariableAction))
g.add((EC1990['variableActionPartialFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['variableActionPartialFactor'], SKOS.altLabel, Literal('γ_Q')))

g.add((EC1990['materialPartialFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['materialPartialFactor'], RDFS.subPropertyOf, EC1990.hasPartialFactor))
g.add((EC1990['materialPartialFactor'], RDFS.label, Literal('has material partial factor', lang='en')))
g.add((EC1990['materialPartialFactor'], RDFS.comment, Literal('Partial factor for material properties taking account of the possibility of an unfavourable deviation of a material property from its characteristic value, also accounting for model uncertainties and dimensional variations.', lang='en')))
g.add((EC1990['materialPartialFactor'], SKOS.definition, Literal('Partial factor for material properties taking account of the possibility of an unfavourable deviation of a material property from its characteristic value, also accounting for model uncertainties and dimensional variations.')))
g.add((EC1990['materialPartialFactor'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 6.3.3')))
g.add((EC1990['materialPartialFactor'], RDFS.domain, EC1990.MaterialProperty))
g.add((EC1990['materialPartialFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['materialPartialFactor'], SKOS.altLabel, Literal('γ_M')))'''

#Combination Factors
g.add((EC1990['combinationFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['combinationFactor'], RDFS.label, Literal('has combination factor', lang='en')))
g.add((EC1990['combinationFactor'], RDFS.comment, Literal('Factor for combination value of a variable action used in ultimate limit state verifications.', lang='en')))
g.add((EC1990['combinationFactor'], SKOS.definition, Literal('Factor for combination value of a variable action used in ultimate limit state verifications.')))
g.add((EC1990['combinationFactor'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.16')))
#g.add((EC1990['hasCombinationFactor'], RDFS.domain, EC1990.VariableAction)) 
g.add((EC1990['combinationFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['combinationFactor'], SKOS.altLabel, Literal('ψ_0')))

g.add((EC1990['hasFrequentFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['hasFrequentFactor'], RDFS.label, Literal('has frequent factor', lang='en')))
g.add((EC1990['hasFrequentFactor'], RDFS.comment, Literal('Factor for frequent value of a variable action, determined so that either the total time within the reference period during which it is exceeded is only a small given part of the reference period, or the frequency of it being exceeded is limited to a given value.', lang='en')))
g.add((EC1990['hasFrequentFactor'], SKOS.definition, Literal('Factor for frequent value of a variable action, determined so that either the total time within the reference period during which it is exceeded is only a small given part of the reference period, or the frequency of it being exceeded is limited to a given value.')))
g.add((EC1990['hasFrequentFactor'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.17')))
#g.add((EC1990['hasFrequentFactor'], RDFS.domain, EC1990.VariableAction))
g.add((EC1990['hasFrequentFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['hasFrequentFactor'], SKOS.altLabel, Literal('ψ_1')))

g.add((EC1990['hasQuasiPermanentFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['hasQuasiPermanentFactor'], RDFS.label, Literal('has quasi-permanent factor', lang='en')))
g.add((EC1990['hasQuasiPermanentFactor'], RDFS.comment, Literal('Factor for quasi-permanent value of a variable action, determined so that the total period of time for which it will be exceeded is a large fraction of the reference period.', lang='en')))
g.add((EC1990['hasQuasiPermanentFactor'], SKOS.definition, Literal('Factor for quasi-permanent value of a variable action, determined so that the total period of time for which it will be exceeded is a large fraction of the reference period.')))
g.add((EC1990['hasQuasiPermanentFactor'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.18')))
#g.add((EC1990['hasQuasiPermanentFactor'], RDFS.domain, EC1990.VariableAction))
g.add((EC1990['hasQuasiPermanentFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['hasQuasiPermanentFactor'], SKOS.altLabel, Literal('ψ_2')))

g.add((EC1990['isSatisfied'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['isSatisfied'], RDFS.label, Literal('is satisfied', lang='en')))
g.add((EC1990['isSatisfied'], RDFS.comment, Literal('Result of verification of the limit state.', lang='en')))
g.add((EC1990['isSatisfied'], SKOS.definition, Literal('Result of verification of the limit state.')))
g.add((EC1990['isSatisfied'], RDFS.domain, EC1990.LimitState))
g.add((EC1990['isSatisfied'], RDFS.range, XSD.boolean))

##########################################################
#                    DISJOINT CLASSES                    #
##########################################################

# Design and Representative actions are mutually exclusive
g.add((EC1990['DesignAction'], OWL.disjointWith, EC1990.RepresentativeAction))

# Variable and Permanent actions are mutually exclusive
g.add((EC1990['VariableAction'], OWL.disjointWith, EC1990.PermanentAction))

# Direct and Indirect actions are mutually exclusive
g.add((EC1990['DirectAction'], OWL.disjointWith, EC1990.IndirectAction))

# Actions by nature are mutually exclusive
g.add((EC1990['WindAction'], OWL.disjointWith, EC1990.SnowLoad))
g.add((EC1990['WindAction'], OWL.disjointWith, EC1990.ImposedLoad))
g.add((EC1990['WindAction'], OWL.disjointWith, EC1990.ThermalAction))
g.add((EC1990['ImposedLoad'], OWL.disjointWith, EC1990.ThermalAction))
g.add((EC1990['ImposedLoad'], OWL.disjointWith, EC1990.SnowLoad))
g.add((EC1990['SnowLoad'], OWL.disjointWith, EC1990.ThermalAction))

# Leading and accompanying actions are mutually exclusive
g.add((EC1990['LeadingVariableAction'], OWL.disjointWith, EC1990.AccompanyingVariableAction))

# Favourable and unfavourble actions are mutually exclusive
g.add((EC1990['FavourableAction'], OWL.disjointWith, EC1990.UnfavourableAction))

# Limit state types are mutually exclusive
g.add((EC1990['UltimateLimitState'], OWL.disjointWith, EC1990.ServiceabilityLimitState))

# Action spatial variation types are mutually exclusive
g.add((EC1990['FixedAction'], OWL.disjointWith, EC1990.FreeAction))

# Action dynamic response types are mutually exclusive
g.add((EC1990['StaticAction'], OWL.disjointWith, EC1990.DynamicAction))

# ULS and SLS combinations are mutually exclusive
g.add((EC1990['ULSCombination'], OWL.disjointWith, EC1990.SLSCombination))

# All ULS combinations are mutually exclusive
g.add((EC1990['FundamentalCombination'], OWL.disjointWith, EC1990.SeismicCombination))
g.add((EC1990['FundamentalCombination'], OWL.disjointWith, EC1990.AccidentalCombination))
g.add((EC1990['SeismicCombination'], OWL.disjointWith, EC1990.AccidentalCombination))

# All SLS combinations are mutually exclusive
g.add((EC1990['CharacteristicCombination'], OWL.disjointWith, EC1990.FrequentCombination))
g.add((EC1990['CharacteristicCombination'], OWL.disjointWith, EC1990.QuasiPermanentCombination))
g.add((EC1990['QuasiPermanentCombination'], OWL.disjointWith, EC1990.FrequentCombination))

# Effect categories are mutually exclusive where appropriate
g.add((EC1990['LinearDeformation'], OWL.disjointWith, EC1990.AngularDeformation))
g.add((EC1990['LinearDeformation'], OWL.disjointWith, EC1990.VolumetricDeformation))
g.add((EC1990['AngularDeformation'], OWL.disjointWith, EC1990.VolumetricDeformation))

##########################################################
#               CONSTRAINTS AND RESTRICTIONS             #
##########################################################

# Value constraints for factors (ψ factors are ≤ 1.0)
# Note: These would be better expressed as SHACL shapes or OWL restrictions

# Add range restrictions for partial factors (typically > 1.0 for safety)

# Add range restrictions for combination factors (typically ≤ 1.0)

##########################################################
#                 ADDITIONAL METADATA                    #
##########################################################

# Add ontology-level metadata for better findability
g.add((ref, SKOS.hasTopConcept, EC1990.Action))
g.add((ref, SKOS.hasTopConcept, EC1990.EffectOfAction))
g.add((ref, SKOS.hasTopConcept, EC1990.LimitState))
g.add((ref, SKOS.hasTopConcept, EC1990.DesignSituation))
g.add((ref, SKOS.hasTopConcept, EC1990.CombinationOfActions))
g.add((ref, SKOS.hasTopConcept, EC1990.ConstructionWork))

# Add provenance information
g.add((ref, DCTERMS.contributor, Literal('Agnieszka Jędrzejewska (Silesian Unviersity of Technology)')))
g.add((ref, DCTERMS.contributor, Literal('Maria Laura Leonardi (University of Minho)')))
g.add((ref, DCTERMS.contributor, Literal('Carlos Ramonell (Politechnic University of Catalonia)')))

##########################################################
#               SEMANTIC RELATIONSHIPS                   #
##########################################################

# Add some semantic relationships that might be useful for reasoning
# These could be expanded based on specific use cases

# Add some usage notes
g.add((EC1990['FundamentalCombination'], SKOS.scopeNote, Literal('Used for persistent and transient design situations in ULS verifications')))
g.add((EC1990['AccidentalCombination'], SKOS.scopeNote, Literal('Used for accidental design situations in ULS verifications')))
g.add((EC1990['SeismicCombination'], SKOS.scopeNote, Literal('Used for seismic design situations in ULS verifications')))
g.add((EC1990['CharacteristicCombination'], SKOS.scopeNote, Literal('Used for irreversible serviceability limit state verifications')))
g.add((EC1990['FrequentCombination'], SKOS.scopeNote, Literal('Used for reversible serviceability limit state verifications')))
g.add((EC1990['QuasiPermanentCombination'], SKOS.scopeNote, Literal('Used for long-term effects and appearance considerations')))

# Add editorial notes for complex concepts
# g.add((EC1990['PartialFactor'], SKOS.editorialNote, Literal('Partial factors account for various sources of uncertainty including statistical uncertainty, model uncertainty, and dimensional variations')))
g.add((EC1990['LimitState'], SKOS.editorialNote, Literal('Limit states define critical conditions that must not be exceeded to ensure structural safety and serviceability')))
g.add((EC1990['EffectOfAction'], SKOS.editorialNote, Literal('Effects of actions can be calculated through structural analysis and must be compared against resistance for verification')))

##########################################################
#                    FINALIZATION                        #
##########################################################

# Save the improved ontology
g.serialize(destination=save_path, format='turtle')

print("✅ Improved EC1990 ontology completed and saved!")
print(f"📁 File saved at: {save_path}")
print(f"🌐 Namespace: {ref}")
print(f"📊 Current triples count: {len(g)}")