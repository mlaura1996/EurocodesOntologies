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

# Bind prefixes
g.bind("ec", EC1990)
g.bind('rdf', RDF)
g.bind('rdfs', RDFS)
g.bind('owl', OWL)
g.bind('xsd', XSD)
g.bind('skos', SKOS)
g.bind('bot', BOT)
g.bind('cc', CC)

# Add improved ontology header triples
g.add((ref, RDF.type, OWL.Ontology))
g.add((ref, DCTERMS.creator, Literal('Carlos Ramonell Cazador (carlos.ramonell@upc.edu)')))
g.add((ref, DCTERMS.date, Literal('2024/12/20', datatype=XSD.date)))
g.add((ref, DCTERMS.modified, Literal('2024/12/20', datatype=XSD.date)))
g.add((ref, DCTERMS.title, Literal('EC - Eurocode Ontology')))
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
g.add((EC1990['ConstructionWork'], RDFS.label, Literal('Obras de Construcción', lang='es')))
g.add((EC1990['ConstructionWork'], RDFS.comment, Literal('Everything that is constructed or results from construction operations. The term covers both building and civil engineering works comprising structural, non-structural and geotechnical elements.', lang='en')))
g.add((EC1990['ConstructionWork'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.1')))
g.add((EC1990['ConstructionWork'], SKOS.definition, Literal('Everything that is constructed or results from construction operations. The term covers both building and civil engineering works comprising structural, non-structural and geotechnical elements.')))
g.add((EC1990['ConstructionWork'], SKOS.example, Literal('building, bridge, nuclea power plant')))

g.add((EC1990['Building'], RDF.type, OWL.Class))
g.add((EC1990['Building'], RDFS.subClassOf, EC1990.ConstructionWork))
g.add((EC1990['Building'], OWL.sameAs, BOT.Building))
g.add((EC1990['Building'], RDFS.label, Literal('Building', lang='en')))
g.add((EC1990['Building'], RDFS.label, Literal('Edificio', lang='es')))
g.add((EC1990['Building'], RDFS.comment, Literal('Type of construction works for building purposes such as dwelling houses, office buildings, etc.', lang='en')))
g.add((EC1990['Building'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.2')))
g.add((EC1990['Building'], SKOS.definition, Literal('Type of construction works for building purposes such as dwelling houses, office buildings, etc.')))
g.add((EC1990['Building'], SKOS.example, Literal('dwelling house, office building, industrial building')))

g.add((EC1990['CivilEngineeringWork'], RDF.type, OWL.Class))
g.add((EC1990['CivilEngineeringWork'], RDFS.subClassOf, EC1990.ConstructionWork))
g.add((EC1990['CivilEngineeringWork'], RDFS.label, Literal('Civil Engineering Work', lang='en')))
g.add((EC1990['CivilEngineeringWork'], RDFS.label, Literal('Obra de Ingeniería Civil', lang='es')))
g.add((EC1990['CivilEngineeringWork'], RDFS.comment, Literal('Type of construction works for civil engineering purposes such as bridges, retaining walls, etc.', lang='en')))
g.add((EC1990['CivilEngineeringWork'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.2')))
g.add((EC1990['CivilEngineeringWork'], SKOS.example, Literal('bridge, retaining wall, tunnel')))

g.add((EC1990['StructuralMember'], RDF.type, OWL.Class))
g.add((EC1990['StructuralMember'], RDFS.subClassOf, BOT.Element))
g.add((EC1990['StructuralMember'], RDFS.label, Literal('Structural Member', lang='en')))
g.add((EC1990['StructuralMember'], RDFS.label, Literal('Elemento Estructural', lang='es')))
g.add((EC1990['StructuralMember'], RDFS.comment, Literal('Physically distinguishable part of a structure, e.g. a column, a beam, a slab, a foundation pile.', lang='en')))
g.add((EC1990['StructuralMember'], DCTERMS.source, Literal('EN 1990:200, Section 1.5.1.7')))
g.add((EC1990['StructuralMember'], SKOS.example, Literal('column, beam, slab, foundation pile')))

g.add((EC1990['EurocodeSpace'], RDF.type, OWL.Class))
g.add((EC1990['EurocodeSpace'], RDFS.subClassOf, BOT.Space))
g.add((EC1990['EurocodeSpace'], RDFS.label, Literal('Eurocode Space', lang='en')))
g.add((EC1990['EurocodeSpace'], RDFS.label, Literal('Espacio Eurocódigo', lang='es')))
g.add((EC1990['EurocodeSpace'], RDFS.comment, Literal('A space classified according to EN 1991-1-1 usage categories', lang='en')))
g.add((EC1990['EurocodeSpace'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))

# Category A - Domestic and Residential
g.add((EC1990['Residential'], RDF.type, OWL.Class))
g.add((EC1990['Residential'], RDFS.subClassOf, EC1990['EurocodeSpace']))
g.add((EC1990['Residential'], RDFS.label, Literal('Category A - Domestic and Residential', lang='en')))
g.add((EC1990['Residential'], RDFS.label, Literal('Categoría A - Doméstico y Residencial', lang='es')))
g.add((EC1990['Residential'], RDFS.comment, Literal('Areas for domestic and residential activities', lang='en')))
g.add((EC1990['Residential'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['Residential'], SKOS.example, Literal('Rooms in residential buildings and houses, bedrooms and wards in hospitals, bedrooms in hotels and hostels, kitchens and toilets')))

# Category B - Office Areas
g.add((EC1990['OfficeArea'], RDF.type, OWL.Class))
g.add((EC1990['OfficeArea'], RDFS.subClassOf, EC1990['EurocodeSpace']))
g.add((EC1990['OfficeArea'], RDFS.label, Literal('Category B - Office Areas', lang='en')))
g.add((EC1990['OfficeArea'], RDFS.label, Literal('Categoría B - Áreas de Oficina', lang='es')))
g.add((EC1990['OfficeArea'], RDFS.comment, Literal('Office areas', lang='en')))
g.add((EC1990['OfficeArea'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['OfficeArea'], SKOS.example, Literal('General office spaces')))

# Category C - Congregation Areas (with subcategories)
g.add((EC1990['CongregationArea'], RDF.type, OWL.Class))
g.add((EC1990['CongregationArea'], RDFS.subClassOf, EC1990['EurocodeSpace']))
g.add((EC1990['CongregationArea'], RDFS.label, Literal('Category C - Congregation Areas', lang='en')))
g.add((EC1990['CongregationArea'], RDFS.label, Literal('Categoría C - Áreas de Congregación', lang='es')))
g.add((EC1990['CongregationArea'], RDFS.comment, Literal('Areas where people may congregate (except areas under category A, B, and D)', lang='en')))
g.add((EC1990['CongregationArea'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))

# Category C1
g.add((EC1990['AreaWithTables'], RDF.type, OWL.Class))
g.add((EC1990['AreaWithTables'], RDFS.subClassOf, EC1990['CongregationArea']))
g.add((EC1990['AreaWithTables'], RDFS.label, Literal('Category C1 - Areas with tables', lang='en')))
g.add((EC1990['AreaWithTables'], RDFS.label, Literal('Categoría C1 - Áreas con mesas', lang='es')))
g.add((EC1990['AreaWithTables'], RDFS.comment, Literal('Areas with tables', lang='en')))
g.add((EC1990['AreaWithTables'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['AreaWithTables'], SKOS.example, Literal('Areas in schools, cafés, restaurants, dining halls, reading rooms, receptions')))

# Category C2
g.add((EC1990['AreasWithFixedSeats'], RDF.type, OWL.Class))
g.add((EC1990['AreasWithFixedSeats'], RDFS.subClassOf, EC1990['CongregationArea']))
g.add((EC1990['AreasWithFixedSeats'], RDFS.label, Literal('Category C2 - Areas with fixed seats', lang='en')))
g.add((EC1990['AreasWithFixedSeats'], RDFS.label, Literal('Categoría C2 - Áreas con asientos fijos', lang='es')))
g.add((EC1990['AreasWithFixedSeats'], RDFS.comment, Literal('Areas with fixed seats', lang='en')))
g.add((EC1990['AreasWithFixedSeats'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['AreasWithFixedSeats'], SKOS.example, Literal('Areas in churches, theatres or cinemas, conference rooms, lecture halls, assembly halls, waiting rooms, railway waiting rooms')))

# Category C3
g.add((EC1990['AreasWithoutObstacle'], RDF.type, OWL.Class))
g.add((EC1990['AreasWithoutObstacle'], RDFS.subClassOf, EC1990['CongregationArea']))
g.add((EC1990['AreasWithoutObstacle'], RDFS.label, Literal('Category C3 - Areas without obstacles', lang='en')))
g.add((EC1990['AreasWithoutObstacle'], RDFS.label, Literal('Categoría C3 - Áreas sin obstáculos', lang='es')))
g.add((EC1990['AreasWithoutObstacle'], RDFS.comment, Literal('Areas without obstacles for moving people', lang='en')))
g.add((EC1990['AreasWithoutObstacle'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['AreasWithoutObstacle'], SKOS.example, Literal('Areas in museums, exhibition rooms, etc. and access areas in public and administration buildings, hotels, hospitals, railway station forecourts')))

# Category C4
g.add((EC1990['PhysicalActivitiesAreas'], RDF.type, OWL.Class))
g.add((EC1990['PhysicalActivitiesAreas'], RDFS.subClassOf, EC1990['CongregationArea']))
g.add((EC1990['PhysicalActivitiesAreas'], RDFS.label, Literal('Category C4 - Physical activities areas', lang='en')))
g.add((EC1990['PhysicalActivitiesAreas'], RDFS.label, Literal('Categoría C4 - Áreas de actividades físicas', lang='es')))
g.add((EC1990['PhysicalActivitiesAreas'], RDFS.comment, Literal('Areas with possible physical activities', lang='en')))
g.add((EC1990['PhysicalActivitiesAreas'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['PhysicalActivitiesAreas'], SKOS.example, Literal('Dance halls, gymnastic rooms, stages')))

# Category C5
g.add((EC1990['LargeCrowdsAreas'], RDF.type, OWL.Class))
g.add((EC1990['LargeCrowdsAreas'], RDFS.subClassOf, EC1990['CongregationArea']))
g.add((EC1990['LargeCrowdsAreas'], RDFS.label, Literal('Category C5 - Large crowds areas', lang='en')))
g.add((EC1990['LargeCrowdsAreas'], RDFS.label, Literal('Categoría C5 - Áreas de grandes multitudes', lang='es')))
g.add((EC1990['LargeCrowdsAreas'], RDFS.comment, Literal('Areas susceptible to large crowds', lang='en')))
g.add((EC1990['LargeCrowdsAreas'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['LargeCrowdsAreas'], SKOS.example, Literal('Buildings for public events like concert halls, sports halls including stands, terraces and access areas and railway platforms')))

# Category D - Shopping Areas
g.add((EC1990['ShoppingAreas'], RDF.type, OWL.Class))
g.add((EC1990['ShoppingAreas'], RDFS.subClassOf, EC1990['EurocodeSpace']))
g.add((EC1990['ShoppingAreas'], RDFS.label, Literal('Category D - Shopping Areas', lang='en')))
g.add((EC1990['ShoppingAreas'], RDFS.label, Literal('Categoría D - Áreas Comerciales', lang='es')))
g.add((EC1990['ShoppingAreas'], RDFS.comment, Literal('Shopping areas', lang='en')))
g.add((EC1990['ShoppingAreas'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))

# Category D1
g.add((EC1990['GeneralRetailShops'], RDF.type, OWL.Class))
g.add((EC1990['GeneralRetailShops'], RDFS.subClassOf, EC1990['ShoppingAreas']))
g.add((EC1990['GeneralRetailShops'], RDFS.label, Literal('Category D1 - General retail shops', lang='en')))
g.add((EC1990['GeneralRetailShops'], RDFS.label, Literal('Categoría D1 - Tiendas minoristas generales', lang='es')))
g.add((EC1990['GeneralRetailShops'], RDFS.comment, Literal('Areas in general retail shops', lang='en')))
g.add((EC1990['GeneralRetailShops'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['GeneralRetailShops'], SKOS.example, Literal('General retail shops')))

# Category D2
g.add((EC1990['DepartmentStore'], RDF.type, OWL.Class))
g.add((EC1990['DepartmentStore'], RDFS.subClassOf, EC1990['ShoppingAreas']))
g.add((EC1990['DepartmentStore'], RDFS.label, Literal('Category D2 - Department stores', lang='en')))
g.add((EC1990['DepartmentStore'], RDFS.label, Literal('Categoría D2 - Grandes almacenes', lang='es')))
g.add((EC1990['DepartmentStore'], RDFS.comment, Literal('Areas in department stores', lang='en')))
g.add((EC1990['DepartmentStore'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.1')))
g.add((EC1990['DepartmentStore'], SKOS.example, Literal('Department stores')))

# Category E - Storage and Industrial
g.add((EC1990['IndustrialandStorage'], RDF.type, OWL.Class))
g.add((EC1990['IndustrialandStorage'], RDFS.subClassOf, EC1990['EurocodeSpace']))
g.add((EC1990['IndustrialandStorage'], RDFS.label, Literal('Category E - Storage and Industrial', lang='en')))
g.add((EC1990['IndustrialandStorage'], RDFS.label, Literal('Categoría E - Almacenamiento e Industrial', lang='es')))
g.add((EC1990['IndustrialandStorage'], RDFS.comment, Literal('Storage and industrial areas', lang='en')))
g.add((EC1990['IndustrialandStorage'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.3')))

# Category E1
g.add((EC1990['StorageAreas'], RDF.type, OWL.Class))
g.add((EC1990['StorageAreas'], RDFS.subClassOf, EC1990['IndustrialandStorage']))
g.add((EC1990['StorageAreas'], RDFS.label, Literal('Category E1 - Storage areas', lang='en')))
g.add((EC1990['StorageAreas'], RDFS.label, Literal('Categoría E1 - Áreas de almacenamiento', lang='es')))
g.add((EC1990['StorageAreas'], RDFS.comment, Literal('Areas susceptible to accumulation of goods, including access areas', lang='en')))
g.add((EC1990['StorageAreas'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.3')))
g.add((EC1990['StorageAreas'], SKOS.example, Literal('Areas for storage use including storage of books and other documents')))

# Category E2
g.add((EC1990['IndustrialUse'], RDF.type, OWL.Class))
g.add((EC1990['IndustrialUse'], RDFS.subClassOf, EC1990['IndustrialandStorage']))
g.add((EC1990['IndustrialUse'], RDFS.label, Literal('Category E2 - Industrial use', lang='en')))
g.add((EC1990['IndustrialUse'], RDFS.label, Literal('Categoría E2 - Uso industrial', lang='es')))
g.add((EC1990['IndustrialUse'], RDFS.comment, Literal('Industrial use areas', lang='en')))
g.add((EC1990['IndustrialUse'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.3')))
g.add((EC1990['IndustrialUse'], SKOS.example, Literal('Industrial facilities')))

# Category F - Light Vehicle Traffic
g.add((EC1990['LightVehicleTraffic'], RDF.type, OWL.Class))
g.add((EC1990['LightVehicleTraffic'], RDFS.subClassOf, EC1990['EurocodeSpace']))
g.add((EC1990['LightVehicleTraffic'], RDFS.label, Literal('Category F - Light Vehicle Traffic', lang='en')))
g.add((EC1990['LightVehicleTraffic'], RDFS.label, Literal('Categoría F - Tráfico de Vehículos Ligeros', lang='es')))
g.add((EC1990['LightVehicleTraffic'], RDFS.comment, Literal('Traffic and parking areas for light vehicles (≤ 30 kN gross vehicle weight and ≤ 8 seats not including driver)', lang='en')))
g.add((EC1990['LightVehicleTraffic'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.7')))
g.add((EC1990['LightVehicleTraffic'], SKOS.example, Literal('Garages, parking areas, parking halls')))

# Category G - Medium Vehicle Traffic
g.add((EC1990['MediumVehicleTraffic'], RDF.type, OWL.Class))
g.add((EC1990['MediumVehicleTraffic'], RDFS.subClassOf, EC1990['EurocodeSpace']))
g.add((EC1990['MediumVehicleTraffic'], RDFS.label, Literal('Category G - Medium Vehicle Traffic', lang='en')))
g.add((EC1990['MediumVehicleTraffic'], RDFS.label, Literal('Categoría G - Tráfico de Vehículos Medianos', lang='es')))
g.add((EC1990['MediumVehicleTraffic'], RDFS.comment, Literal('Traffic and parking areas for medium vehicles (>30 kN, ≤ 160 kN gross vehicle weight, on 2 axles)', lang='en')))
g.add((EC1990['MediumVehicleTraffic'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.7')))
g.add((EC1990['MediumVehicleTraffic'], SKOS.example, Literal('Access routes, delivery zones, zones accessible to fire engines (≤ 160 kN gross vehicle weight)')))

# Category H - Roofs
g.add((EC1990['Roof'], RDF.type, OWL.Class))
g.add((EC1990['Roof'], RDFS.subClassOf, EC1990['EurocodeSpace']))
g.add((EC1990['Roof'], RDFS.label, Literal('Category H - Roofs', lang='en')))
g.add((EC1990['Roof'], RDFS.label, Literal('Categoría H - Cubiertas', lang='es')))
g.add((EC1990['Roof'], RDFS.comment, Literal('Roofs not accessible except for normal maintenance and repair', lang='en')))
g.add((EC1990['Roof'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.9')))
g.add((EC1990['Roof'], SKOS.example, Literal('Roofs accessible only for maintenance')))

# Category I - Accessible Roofs
g.add((EC1990['AccessibleRoofs'], RDF.type, OWL.Class))
g.add((EC1990['AccessibleRoofs'], RDFS.subClassOf, EC1990['EurocodeSpace']))
g.add((EC1990['AccessibleRoofs'], RDFS.label, Literal('Category I - Accessible Roofs', lang='en')))
g.add((EC1990['AccessibleRoofs'], RDFS.label, Literal('Categoría I - Cubiertas Accesibles', lang='es')))
g.add((EC1990['AccessibleRoofs'], RDFS.comment, Literal('Roofs accessible with occupancy according to categories A to G', lang='en')))
g.add((EC1990['AccessibleRoofs'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.9')))
g.add((EC1990['AccessibleRoofs'], SKOS.example, Literal('Roofs used as terraces, gardens, or other occupied spaces')))

# Category K - Helicopter Landing Areas
g.add((EC1990['HelicopterLandingAreas'], RDF.type, OWL.Class))
g.add((EC1990['HelicopterLandingAreas'], RDFS.subClassOf, EC1990['EurocodeSpace']))
g.add((EC1990['HelicopterLandingAreas'], RDFS.label, Literal('Category K - Helicopter Landing Areas', lang='en')))
g.add((EC1990['HelicopterLandingAreas'], RDFS.label, Literal('Categoría K - Áreas de Aterrizaje de Helicópteros', lang='es')))
g.add((EC1990['HelicopterLandingAreas'], RDFS.comment, Literal('Roofs accessible for special services, such as helicopter landing areas', lang='en')))
g.add((EC1990['HelicopterLandingAreas'], DCTERMS.source, Literal('EN 1991-1-1:2002 Table 6.9')))
g.add((EC1990['HelicopterLandingAreas'], SKOS.example, Literal('Helicopter landing pads on roofs')))

# Structure-related classes
g.add((EC1990['Structure'], RDF.type, OWL.Class))
g.add((EC1990['Structure'], RDFS.label, Literal('Structure', lang='en')))
g.add((EC1990['Structure'], RDFS.label, Literal('Estructura', lang='es')))
g.add((EC1990['Structure'], RDFS.comment, Literal('Organised combination of connected parts designed to carry loads and provide adequate rigidity.', lang='en')))
g.add((EC1990['Structure'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.6')))
g.add((EC1990['Structure'], SKOS.example, Literal('Residential building, reatining wall, suspension bridge, underground tunnel')))

g.add((EC1990['StructuralSystem'], RDF.type, OWL.Class))
g.add((EC1990['StructuralSystem'], RDFS.label, Literal('Structural System', lang='en')))
g.add((EC1990['StructuralSystem'], RDFS.label, Literal('Sistema Estructural', lang='es')))
g.add((EC1990['StructuralSystem'], RDFS.comment, Literal('Load-bearing members of a building or civil engineering works and the way in which these members function together.', lang='en')))
g.add((EC1990['StructuralSystem'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.9')))
g.add((EC1990['StructuralSystem'], SKOS.example, Literal('Flat-slab system with drop panels, steel potal frame, cable-stayed bridge system, trussed roof system')))

##########################################################
#                   LIMIT STATES                        #
##########################################################

g.add((EC1990['LimitState'], RDF.type, OWL.Class))
g.add((EC1990['LimitState'], RDFS.label, Literal('Limit State', lang='en')))
g.add((EC1990['LimitState'], RDFS.label, Literal('Estado Límite', lang='es')))
g.add((EC1990['LimitState'], RDFS.comment, Literal('State beyond which the structure no longer fulfils the relevant design criteria.', lang='en')))
g.add((EC1990['LimitState'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.12')))
g.add((EC1990['LimitState'], SKOS.definition, Literal('State beyond which the structure no longer fulfils the relevant design criteria.')))

g.add((EC1990['UltimateLimitState'], RDF.type, OWL.Class))
g.add((EC1990['UltimateLimitState'], RDFS.subClassOf, EC1990.LimitState))
g.add((EC1990['UltimateLimitState'], RDFS.label, Literal('Ultimate Limit State', lang='en')))
g.add((EC1990['UltimateLimitState'], RDFS.label, Literal('Estado Límite Último', lang='es')))
g.add((EC1990['UltimateLimitState'], RDFS.comment, Literal('State associated with collapse or with other similar forms of structural failure. They generally correspond to the maximum load-carrying resistance of a structure or structural member.', lang='en')))
g.add((EC1990['UltimateLimitState'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.13')))
g.add((EC1990['UltimateLimitState'], SKOS.altLabel, Literal('ULS')))

g.add((EC1990['ServiceabilityLimitState'], RDF.type, OWL.Class))
g.add((EC1990['ServiceabilityLimitState'], RDFS.subClassOf, EC1990.LimitState))
g.add((EC1990['ServiceabilityLimitState'], RDFS.label, Literal('Serviceability Limit State', lang='en')))
g.add((EC1990['ServiceabilityLimitState'], RDFS.label, Literal('Estado Límite de Servicio', lang='es')))
g.add((EC1990['ServiceabilityLimitState'], RDFS.comment, Literal('State that correspond to conditions beyond which specified service requirements for a structure or structural member are no longer met.', lang='en')))
g.add((EC1990['ServiceabilityLimitState'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.14')))
g.add((EC1990['ServiceabilityLimitState'], SKOS.altLabel, Literal('SLS')))

# Specific ULS types
g.add((EC1990['EQU'], RDF.type, OWL.Class))
g.add((EC1990['EQU'], RDFS.subClassOf, EC1990.UltimateLimitState))
g.add((EC1990['EQU'], RDFS.label, Literal('Static Equilibrium', lang='en')))
g.add((EC1990['EQU'], RDFS.comment, Literal('Loss of static equilibrium of the structure or any part of it considered as a rigid body.', lang='en')))
g.add((EC1990['EQU'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.1(1)P a)')))

g.add((EC1990['STR'], RDF.type, OWL.Class))
g.add((EC1990['STR'], RDFS.subClassOf, EC1990.UltimateLimitState))
g.add((EC1990['STR'], RDFS.label, Literal('Structural Resistance', lang='en')))
g.add((EC1990['STR'], RDFS.comment, Literal('Internal failure or excessive deformation of the structure or structural members where the strength of construction materials governs.', lang='en')))
g.add((EC1990['STR'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.1(1)P b)')))

g.add((EC1990['GEO'], RDF.type, OWL.Class))
g.add((EC1990['GEO'], RDFS.subClassOf, EC1990.UltimateLimitState))
g.add((EC1990['GEO'], RDFS.label, Literal('Geotechnical Failure', lang='en')))
g.add((EC1990['GEO'], RDFS.comment, Literal('Failure or excessive deformation of the ground where the strengths of soil or rock are significant in providing resistance.', lang='en')))
g.add((EC1990['GEO'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.1(1)P c)')))

g.add((EC1990['FAT'], RDF.type, OWL.Class))
g.add((EC1990['FAT'], RDFS.subClassOf, EC1990.UltimateLimitState))
g.add((EC1990['FAT'], RDFS.label, Literal('Fatigue Failure', lang='en')))
g.add((EC1990['FAT'], RDFS.comment, Literal('Fatigue failure of the structure or structural members.', lang='en')))
g.add((EC1990['FAT'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.1(1)P d)')))

g.add((EC1990['UPL'], RDF.type, OWL.Class))
g.add((EC1990['UPL'], RDFS.subClassOf, EC1990.UltimateLimitState))
g.add((EC1990['UPL'], RDFS.label, Literal('Uplift Failure', lang='en')))
g.add((EC1990['UPL'], RDFS.comment, Literal('Loss of equilibrium of the structure or the ground due to uplift by water pressure (buoyancy) or other vertical actions.', lang='en')))
g.add((EC1990['UPL'], DCTERMS.source, Literal('EN 1990:2002/A1:2005, Section 6.4.1(1)P e)')))

g.add((EC1990['HYD'], RDF.type, OWL.Class))
g.add((EC1990['HYD'], RDFS.subClassOf, EC1990.UltimateLimitState))
g.add((EC1990['HYD'], RDFS.label, Literal('Hydraulic Failure', lang='en')))
g.add((EC1990['HYD'], RDFS.comment, Literal('Hydraulic heave, internal erosion and piping in the ground caused by hydraulic gradients.', lang='en')))
g.add((EC1990['HYD'], DCTERMS.source, Literal('EN 1990:2002/A1:2005, Section 6.4.1(1)P f)')))

# SLS types
g.add((EC1990['ReversibleServiceabilityLimitState'], RDF.type, OWL.Class))
g.add((EC1990['ReversibleServiceabilityLimitState'], RDFS.subClassOf, EC1990.ServiceabilityLimitState))
g.add((EC1990['ReversibleServiceabilityLimitState'], RDFS.label, Literal('Reversible Serviceability Limit State', lang='en')))
g.add((EC1990['ReversibleServiceabilityLimitState'], RDFS.comment, Literal('Serviceability limit state where no consequences of actions exceeding the specified service requirements will remain when the actions are removed.', lang='en')))
g.add((EC1990['ReversibleServiceabilityLimitState'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 1.5.2.14.2')))

g.add((EC1990['IrreversibleServiceabilityLimitState'], RDF.type, OWL.Class))
g.add((EC1990['IrreversibleServiceabilityLimitState'], RDFS.subClassOf, EC1990.ServiceabilityLimitState))
g.add((EC1990['IrreversibleServiceabilityLimitState'], RDFS.label, Literal('Irreversible Serviceability Limit State', lang='en')))
g.add((EC1990['IrreversibleServiceabilityLimitState'], RDFS.comment, Literal('Serviceability limit state where some consequences of actions exceeding the specified service requirements will remain when the actions are removed.', lang='en')))
g.add((EC1990['IrreversibleServiceabilityLimitState'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 1.5.2.14.1')))

##########################################################
#                 DESIGN SITUATIONS                     #
##########################################################

g.add((EC1990['DesignSituation'], RDF.type, OWL.Class))
g.add((EC1990['DesignSituation'], RDFS.label, Literal('Design Situation', lang='en')))
g.add((EC1990['DesignSituation'], RDFS.label, Literal('Situación de Proyecto', lang='es')))
g.add((EC1990['DesignSituation'], RDFS.comment, Literal('Sets of physical conditions representing the real conditions occurring during a certain time interval for which the design will demonstrate that relevant limit states are not exceeded.', lang='en')))
g.add((EC1990['DesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.2')))

g.add((EC1990['PersistentDesignSituation'], RDF.type, OWL.Class))
g.add((EC1990['PersistentDesignSituation'], RDFS.subClassOf, EC1990.DesignSituation))
g.add((EC1990['PersistentDesignSituation'], RDFS.label, Literal('Persistent Design Situation', lang='en')))
g.add((EC1990['PersistentDesignSituation'], RDFS.label, Literal('Situación de Proyecto Persistente', lang='es')))
g.add((EC1990['PersistentDesignSituation'], RDFS.comment, Literal('Design situation that is relevant during a period of the same order as the design working life of the structure. Generally refers to conditions of normal use.', lang='en')))
g.add((EC1990['PersistentDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.4')))

g.add((EC1990['TransientDesignSituation'], RDF.type, OWL.Class))
g.add((EC1990['TransientDesignSituation'], RDFS.subClassOf, EC1990.DesignSituation))
g.add((EC1990['TransientDesignSituation'], RDFS.label, Literal('Transient Design Situation', lang='en')))
g.add((EC1990['TransientDesignSituation'], RDFS.label, Literal('Situación de Proyecto Transitoria', lang='es')))
g.add((EC1990['TransientDesignSituation'], RDFS.comment, Literal('Design situation that is relevant during a period much shorter than the design working life of the structure and which has a high probability of occurrence, e.g. during construction or repair.', lang='en')))
g.add((EC1990['TransientDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.3')))
g.add((EC1990['TransientDesignSituation'], SKOS.example, Literal('construction phase, repair operations')))

g.add((EC1990['AccidentalDesignSituation'], RDF.type, OWL.Class))
g.add((EC1990['AccidentalDesignSituation'], RDFS.subClassOf, EC1990.DesignSituation))
g.add((EC1990['AccidentalDesignSituation'], RDFS.label, Literal('Accidental Design Situation', lang='en')))
g.add((EC1990['AccidentalDesignSituation'], RDFS.label, Literal('Situación de Proyecto Accidental', lang='es')))
g.add((EC1990['AccidentalDesignSituation'], RDFS.comment, Literal('Design situation involving exceptional conditions of the structure or its exposure, including fire, explosion, impact or local failure.', lang='en')))
g.add((EC1990['AccidentalDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.5')))
g.add((EC1990['AccidentalDesignSituation'], SKOS.example, Literal('fire, explosion, impact, local failure')))

g.add((EC1990['FireDesignSituation'], RDF.type, OWL.Class))
g.add((EC1990['FireDesignSituation'], RDFS.subClassOf, EC1990.AccidentalDesignSituation))
g.add((EC1990['FireDesignSituation'], RDFS.label, Literal('Fire Design Situation', lang='en')))
g.add((EC1990['FireDesignSituation'], RDFS.comment, Literal('Accidental design situation involving fire conditions requiring specific design considerations.', lang='en')))
g.add((EC1990['FireDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.5 & 6')))

g.add((EC1990['ExplosionDesignSituation'], RDF.type, OWL.Class))
g.add((EC1990['ExplosionDesignSituation'], RDFS.subClassOf, EC1990.AccidentalDesignSituation))
g.add((EC1990['ExplosionDesignSituation'], RDFS.label, Literal('Explosion Design Situation', lang='en')))
g.add((EC1990['ExplosionDesignSituation'], RDFS.comment, Literal('Accidental design situation involving explosion conditions.', lang='en')))
g.add((EC1990['ExplosionDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.5')))

g.add((EC1990['ImpactDesignSituation'], RDF.type, OWL.Class))
g.add((EC1990['ImpactDesignSituation'], RDFS.subClassOf, EC1990.AccidentalDesignSituation))
g.add((EC1990['ImpactDesignSituation'], RDFS.label, Literal('Impact Design Situation', lang='en')))
g.add((EC1990['ImpactDesignSituation'], RDFS.comment, Literal('Accidental design situation involving impact conditions.', lang='en')))
g.add((EC1990['ImpactDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.5')))

g.add((EC1990['LocalizedFailureDesignSituation'], RDF.type, OWL.Class))
g.add((EC1990['LocalizedFailureDesignSituation'], RDFS.subClassOf, EC1990.AccidentalDesignSituation))
g.add((EC1990['LocalizedFailureDesignSituation'], RDFS.label, Literal('Localized Failure Design Situation', lang='en')))
g.add((EC1990['LocalizedFailureDesignSituation'], RDFS.comment, Literal('Accidental design situation involving local failure conditions.', lang='en')))
g.add((EC1990['LocalizedFailureDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.5')))

g.add((EC1990['SeismicDesignSituation'], RDF.type, OWL.Class))
g.add((EC1990['SeismicDesignSituation'], RDFS.subClassOf, EC1990.DesignSituation))
g.add((EC1990['SeismicDesignSituation'], RDFS.label, Literal('Seismic Design Situation', lang='en')))
g.add((EC1990['SeismicDesignSituation'], RDFS.label, Literal('Situación de Proyecto Sísmica', lang='es')))
g.add((EC1990['SeismicDesignSituation'], RDFS.comment, Literal('Design situation involving exceptional conditions of the structure when subjected to a seismic event.', lang='en')))
g.add((EC1990['SeismicDesignSituation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.7')))

##########################################################
#                       ACTIONS                         #
##########################################################

g.add((EC1990['Action'], RDF.type, OWL.Class))
g.add((EC1990['Action'], RDFS.label, Literal('Action', lang='en')))
g.add((EC1990['Action'], RDFS.label, Literal('Acción', lang='es')))
g.add((EC1990['Action'], RDFS.comment, Literal('Set of forces (loads) applied to the structure (direct action) or set of imposed deformations or accelerations caused for example, by temperature changes, moisture variation, uneven settlement or earthquakes (indirect action).', lang='en')))
g.add((EC1990['Action'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.1')))
g.add((EC1990['Action'], SKOS.definition, Literal('Set of forces (loads) applied to the structure (direct action) or set of imposed deformations or accelerations caused for example, by temperature changes, moisture variation, uneven settlement or earthquakes (indirect action).')))
g.add((EC1990['Action'], SKOS.example, Literal('dead load, imopsed load, wind load, thermal action')))
g.add((EC1990['Action'], SKOS.altLabel, Literal('F')))

# Direct and Indirect Actions
g.add((EC1990['DirectAction'], RDF.type, OWL.Class))
g.add((EC1990['DirectAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['DirectAction'], RDFS.label, Literal('Direct Action', lang='en')))
g.add((EC1990['DirectAction'], RDFS.comment, Literal('Set of forces (loads) applied to the structure.', lang='en')))
g.add((EC1990['DirectAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.1 a)')))

g.add((EC1990['IndirectAction'], RDF.type, OWL.Class))
g.add((EC1990['IndirectAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['IndirectAction'], RDFS.label, Literal('Indirect Action', lang='en')))
g.add((EC1990['IndirectAction'], RDFS.comment, Literal('Set of imposed deformations or accelerations caused for example, by temperature changes, moisture variation, uneven settlement or earthquakes.', lang='en')))
g.add((EC1990['IndirectAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.1 b)')))

# Action classification by time variation
g.add((EC1990['PermanentAction'], RDF.type, OWL.Class))
g.add((EC1990['PermanentAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['PermanentAction'], RDFS.label, Literal('Permanent Action', lang='en')))
g.add((EC1990['PermanentAction'], RDFS.label, Literal('Acción Permanente', lang='es')))
g.add((EC1990['PermanentAction'], RDFS.comment, Literal('Action that is likely to act throughout a given reference period and for which the variation in magnitude with time is negligible, or for which the variation is always in the same direction (monotonic) until the action attains a certain limit value.', lang='en')))
g.add((EC1990['PermanentAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.3')))
g.add((EC1990['PermanentAction'], SKOS.altLabel, Literal('G')))
g.add((EC1990['PermanentAction'], SKOS.example, Literal('self-weight, fixed equipment')))

g.add((EC1990['VariableAction'], RDF.type, OWL.Class))
g.add((EC1990['VariableAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['VariableAction'], RDFS.label, Literal('Variable Action', lang='en')))
g.add((EC1990['VariableAction'], RDFS.label, Literal('Acción Variable', lang='es')))
g.add((EC1990['VariableAction'], RDFS.comment, Literal('Action for which the variation in magnitude with time is neither negligible nor monotonic.', lang='en')))
g.add((EC1990['VariableAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.4')))
g.add((EC1990['VariableAction'], SKOS.altLabel, Literal('Q')))
g.add((EC1990['VariableAction'], SKOS.example, Literal('imposed loads, wind, snow, thermal actions')))

g.add((EC1990['AccidentalAction'], RDF.type, OWL.Class))
g.add((EC1990['AccidentalAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['AccidentalAction'], RDFS.label, Literal('Accidental Action', lang='en')))
g.add((EC1990['AccidentalAction'], RDFS.label, Literal('Acción Accidental', lang='es')))
g.add((EC1990['AccidentalAction'], RDFS.comment, Literal('Action, usually of short duration but of significant magnitude, that is unlikely to occur on a given structure during the design working life.', lang='en')))
g.add((EC1990['AccidentalAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.5')))
g.add((EC1990['AccidentalAction'], SKOS.altLabel, Literal('A')))
g.add((EC1990['AccidentalAction'], SKOS.example, Literal('explosions, impact from vehicles')))

g.add((EC1990['SeismicAction'], RDF.type, OWL.Class))
g.add((EC1990['SeismicAction'], RDFS.subClassOf, EC1990.AccidentalAction))
g.add((EC1990['SeismicAction'], RDFS.label, Literal('Seismic Action', lang='en')))
g.add((EC1990['SeismicAction'], RDFS.label, Literal('Acción Sísmica', lang='es')))
g.add((EC1990['SeismicAction'], RDFS.comment, Literal('Action that arises due to earthquake ground motions.', lang='en')))
g.add((EC1990['SeismicAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.6')))
g.add((EC1990['SeismicAction'], SKOS.altLabel, Literal('A_E')))

# Action classification by spatial variation
g.add((EC1990['FixedAction'], RDF.type, OWL.Class))
g.add((EC1990['FixedAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['FixedAction'], RDFS.label, Literal('Fixed Action', lang='en')))
g.add((EC1990['FixedAction'], RDFS.comment, Literal('Action that has a fixed distribution and position over the structure or structural member such that the magnitude and direction of the action are determined unambiguously for the whole structure.', lang='en')))
g.add((EC1990['FixedAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.8')))
g.add((EC1990['FixedAction'], SKOS.example, Literal('Stored goods in a defined storage area with no alternative placement')))

g.add((EC1990['FreeAction'], RDF.type, OWL.Class))
g.add((EC1990['FreeAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['FreeAction'], RDFS.label, Literal('Free Action', lang='en')))
g.add((EC1990['FreeAction'], RDFS.comment, Literal('Action that may have various spatial distributions over the structure.', lang='en')))
g.add((EC1990['FreeAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.9')))
g.add((EC1990['FreeAction'], SKOS.example, Literal('Imposed floor load on individual rooms of a multi-storey building')))

# Action classification by dynamic response
g.add((EC1990['StaticAction'], RDF.type, OWL.Class))
g.add((EC1990['StaticAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['StaticAction'], RDFS.label, Literal('Static Action', lang='en')))
g.add((EC1990['StaticAction'], RDFS.comment, Literal('Action that does not cause significant acceleration of the structure or structural members.', lang='en')))
g.add((EC1990['StaticAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.11')))

g.add((EC1990['DynamicAction'], RDF.type, OWL.Class))
g.add((EC1990['DynamicAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['DynamicAction'], RDFS.label, Literal('Dynamic Action', lang='en')))
g.add((EC1990['DynamicAction'], RDFS.comment, Literal('Action that causes significant acceleration of the structure or structural members.', lang='en')))
g.add((EC1990['DynamicAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.12')))

g.add((EC1990['QuasiStaticAction'], RDF.type, OWL.Class))
g.add((EC1990['QuasiStaticAction'], RDFS.subClassOf, EC1990.DynamicAction))
g.add((EC1990['QuasiStaticAction'], RDFS.label, Literal('Quasi-Static Action', lang='en')))
g.add((EC1990['QuasiStaticAction'], RDFS.comment, Literal('Dynamic action represented by an equivalent static action in a static model.', lang='en')))
g.add((EC1990['QuasiStaticAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.13')))

# Geotechnical Action
g.add((EC1990['GeotechnicalAction'], RDF.type, OWL.Class))
g.add((EC1990['GeotechnicalAction'], RDFS.subClassOf, EC1990.Action))
g.add((EC1990['GeotechnicalAction'], RDFS.label, Literal('Geotechnical Action', lang='en')))
g.add((EC1990['GeotechnicalAction'], RDFS.comment, Literal('Action transmitted to the structure by the ground, fill or groundwater.', lang='en')))
g.add((EC1990['GeotechnicalAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.7')))

##########################################################
#                 COMBINATIONS OF ACTIONS               #
##########################################################

g.add((EC1990['CombinationOfActions'], RDF.type, OWL.Class))
g.add((EC1990['CombinationOfActions'], RDFS.label, Literal('Combination of Actions', lang='en')))
g.add((EC1990['CombinationOfActions'], RDFS.label, Literal('Combinación de Acciones', lang='es')))
g.add((EC1990['CombinationOfActions'], RDFS.comment, Literal('Set of design values used for the verification of the structural reliability for a limit state under the simultaneous influence of different actions.', lang='en')))
g.add((EC1990['CombinationOfActions'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.22')))
g.add((EC1990['CombinationOfActions'], SKOS.definition, Literal('Set of design values used for the verification of the structural reliability for a limit state under the simultaneous influence of different actions.')))

g.add((EC1990['ULSCombination'], RDF.type, OWL.Class))
g.add((EC1990['ULSCombination'], RDFS.subClassOf, EC1990.CombinationOfActions))
g.add((EC1990['ULSCombination'], RDFS.label, Literal('Ultimate Limit State Combination', lang='en')))
g.add((EC1990['ULSCombination'], RDFS.label, Literal('Combinacion ELU', lang='es')))
g.add((EC1990['ULSCombination'], RDFS.comment, Literal('Combination of actions for verifying ultimate limit states.', lang='en')))
g.add((EC1990['ULSCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.3')))

g.add((EC1990['FundamentalCombination'], RDF.type, OWL.Class))
g.add((EC1990['FundamentalCombination'], RDFS.subClassOf, EC1990.ULSCombination))
g.add((EC1990['FundamentalCombination'], RDFS.label, Literal('Fundamental Combination', lang='en')))
g.add((EC1990['FundamentalCombination'], RDFS.label, Literal('Combinación Fundamental', lang='es')))
g.add((EC1990['FundamentalCombination'], RDFS.comment, Literal('Combination of actions for persistent or transient design situations.', lang='en')))
g.add((EC1990['FundamentalCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.3.2')))

g.add((EC1990['AccidentalCombination'], RDF.type, OWL.Class))
g.add((EC1990['AccidentalCombination'], RDFS.subClassOf, EC1990.ULSCombination))
g.add((EC1990['AccidentalCombination'], RDFS.label, Literal('Accidental Combination', lang='en')))
g.add((EC1990['AccidentalCombination'], RDFS.label, Literal('Combinación Accidental', lang='es')))
g.add((EC1990['AccidentalCombination'], RDFS.comment, Literal('Combination of actions for accidental design situations.', lang='en')))
g.add((EC1990['AccidentalCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.3.3')))

g.add((EC1990['SeismicCombination'], RDF.type, OWL.Class))
g.add((EC1990['SeismicCombination'], RDFS.subClassOf, EC1990.ULSCombination))
g.add((EC1990['SeismicCombination'], RDFS.label, Literal('Seismic Combination', lang='en')))
g.add((EC1990['SeismicCombination'], RDFS.label, Literal('Combinación Sísmica', lang='es')))
g.add((EC1990['SeismicCombination'], RDFS.comment, Literal('Combination of actions for seismic design situations.', lang='en')))
g.add((EC1990['SeismicCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.4.3.4')))

g.add((EC1990['SLSCombination'], RDF.type, OWL.Class))
g.add((EC1990['SLSCombination'], RDFS.subClassOf, EC1990.CombinationOfActions))
g.add((EC1990['SLSCombination'], RDFS.label, Literal('Serviceability Limit State Combination', lang='en')))
g.add((EC1990['SLSCombination'], RDFS.label, Literal('Combinaciones ELS', lang='es')))
g.add((EC1990['SLSCombination'], RDFS.comment, Literal('Combinations of actions for verifying serviceability limit states.', lang='en')))
g.add((EC1990['SLSCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.5.3')))

g.add((EC1990['CharacteristicCombination'], RDF.type, OWL.Class))
g.add((EC1990['CharacteristicCombination'], RDFS.subClassOf, EC1990.SLSCombination))
g.add((EC1990['CharacteristicCombination'], RDFS.label, Literal('Characteristic Combination', lang='en')))
g.add((EC1990['CharacteristicCombination'], RDFS.label, Literal('Combinación Característica', lang='es')))
g.add((EC1990['CharacteristicCombination'], RDFS.comment, Literal('Serviceability combination normally used for irreversible limit states.', lang='en')))
g.add((EC1990['CharacteristicCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.5.3(2)a')))

g.add((EC1990['FrequentCombination'], RDF.type, OWL.Class))
g.add((EC1990['FrequentCombination'], RDFS.subClassOf, EC1990.SLSCombination))
g.add((EC1990['FrequentCombination'], RDFS.label, Literal('Frequent Combination', lang='en')))
g.add((EC1990['FrequentCombination'], RDFS.label, Literal('Combinación Frecuente', lang='es')))
g.add((EC1990['FrequentCombination'], RDFS.comment, Literal('Serviceability combination normally used for reversible limit states.', lang='en')))
g.add((EC1990['FrequentCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.5.3(2)b')))

g.add((EC1990['QuasiPermanentCombination'], RDF.type, OWL.Class))
g.add((EC1990['QuasiPermanentCombination'], RDFS.subClassOf, EC1990.SLSCombination))
g.add((EC1990['QuasiPermanentCombination'], RDFS.label, Literal('Quasi-Permanent Combination', lang='en')))
g.add((EC1990['QuasiPermanentCombination'], RDFS.label, Literal('Combinación Cuasi-permanente', lang='es')))
g.add((EC1990['QuasiPermanentCombination'], RDFS.comment, Literal('Serviceability combination normally used for long-term effects and the appearance of the structure.', lang='en')))
g.add((EC1990['QuasiPermanentCombination'], DCTERMS.source, Literal('EN 1990:2002, Section 6.5.3(2)c')))

##########################################################
#                    EFFECTS OF ACTIONS                 #
##########################################################

g.add((EC1990['EffectOfAction'], RDF.type, OWL.Class))
g.add((EC1990['EffectOfAction'], RDFS.label, Literal('Effect of Action', lang='en')))
g.add((EC1990['EffectOfAction'], RDFS.label, Literal('Efecto de las Acciones', lang='es')))
g.add((EC1990['EffectOfAction'], RDFS.comment, Literal('Effect of actions on structural members (e.g. internal force, moment, stress, strain) or on the whole structure (e.g. deflection, rotation).', lang='en')))
g.add((EC1990['EffectOfAction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))
g.add((EC1990['EffectOfAction'], SKOS.definition, Literal('Effect of actions on structural members (e.g. internal force, moment, stress, strain) or on the whole structure (e.g. deflection, rotation).')))
g.add((EC1990['EffectOfAction'], SKOS.example, Literal('internal force, moment, stress, strain, deflection, rotation')))
g.add((EC1990['EffectOfAction'], SKOS.altLabel, Literal('E')))

# Major effect categories
g.add((EC1990['MechanicalEffect'], RDF.type, OWL.Class))
g.add((EC1990['MechanicalEffect'], RDFS.subClassOf, EC1990.EffectOfAction))
g.add((EC1990['MechanicalEffect'], RDFS.label, Literal('Mechanical Effect', lang='en')))
g.add((EC1990['MechanicalEffect'], RDFS.comment, Literal('Effect of actions in the form of forces, stresses, or strains in structural members.', lang='en')))

g.add((EC1990['DeformationEffect'], RDF.type, OWL.Class))
g.add((EC1990['DeformationEffect'], RDFS.subClassOf, EC1990.EffectOfAction))
g.add((EC1990['DeformationEffect'], RDFS.label, Literal('Deformation Effect', lang='en')))
g.add((EC1990['DeformationEffect'], RDFS.comment, Literal('Effect of actions in the form of deformations of the structure or structural members.', lang='en')))

g.add((EC1990['DynamicEffect'], RDF.type, OWL.Class))
g.add((EC1990['DynamicEffect'], RDFS.subClassOf, EC1990.EffectOfAction))
g.add((EC1990['DynamicEffect'], RDFS.label, Literal('Dynamic Effect', lang='en')))
g.add((EC1990['DynamicEffect'], RDFS.comment, Literal('Effect of actions involving dynamic response, acceleration, or vibration.', lang='en')))

g.add((EC1990['TimeDependentEffect'], RDF.type, OWL.Class))
g.add((EC1990['TimeDependentEffect'], RDFS.subClassOf, EC1990.EffectOfAction))
g.add((EC1990['TimeDependentEffect'], RDFS.label, Literal('Time-Dependent Effect', lang='en')))
g.add((EC1990['TimeDependentEffect'], RDFS.comment, Literal('Effect of actions that varies with time due to material behavior or other time-related factors.', lang='en')))
g.add((EC1990['TimeDependentEffect'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 3.1(5)')))

# Mechanical Effects
g.add((EC1990['InternalForce'], RDF.type, OWL.Class))
g.add((EC1990['InternalForce'], RDFS.subClassOf, EC1990.MechanicalEffect))
g.add((EC1990['InternalForce'], RDFS.label, Literal('Internal Force', lang='en')))
g.add((EC1990['InternalForce'], RDFS.label, Literal('Fuerza Interna', lang='es')))
g.add((EC1990['InternalForce'], RDFS.comment, Literal('Effect of actions in the form of internal forces in structural members.', lang='en')))
g.add((EC1990['InternalForce'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

g.add((EC1990['BendingMoment'], RDF.type, OWL.Class))
g.add((EC1990['BendingMoment'], RDFS.subClassOf, EC1990.InternalForce))
g.add((EC1990['BendingMoment'], RDFS.label, Literal('Bending Moment', lang='en')))
g.add((EC1990['BendingMoment'], RDFS.label, Literal('Momento Flector', lang='es')))
g.add((EC1990['BendingMoment'], RDFS.comment, Literal('Internal moment causing bending in structural members.', lang='en')))
g.add((EC1990['BendingMoment'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))
g.add((EC1990['BendingMoment'], SKOS.altLabel, Literal('M')))

g.add((EC1990['AxialForce'], RDF.type, OWL.Class))
g.add((EC1990['AxialForce'], RDFS.subClassOf, EC1990.InternalForce))
g.add((EC1990['AxialForce'], RDFS.label, Literal('Axial Force', lang='en')))
g.add((EC1990['AxialForce'], RDFS.label, Literal('Fuerza Axial', lang='es')))
g.add((EC1990['AxialForce'], RDFS.comment, Literal('Internal force acting along the axis of structural members.', lang='en')))
g.add((EC1990['AxialForce'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))
g.add((EC1990['AxialForce'], SKOS.altLabel, Literal('N')))

g.add((EC1990['ShearForce'], RDF.type, OWL.Class))
g.add((EC1990['ShearForce'], RDFS.subClassOf, EC1990.InternalForce))
g.add((EC1990['ShearForce'], RDFS.label, Literal('Shear Force', lang='en')))
g.add((EC1990['ShearForce'], RDFS.label, Literal('Fuerza Cortante', lang='es')))
g.add((EC1990['ShearForce'], RDFS.comment, Literal('Internal force acting perpendicular to the axis of structural members.', lang='en')))
g.add((EC1990['ShearForce'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))
g.add((EC1990['ShearForce'], SKOS.altLabel, Literal('V')))

g.add((EC1990['TorsionalMoment'], RDF.type, OWL.Class))
g.add((EC1990['TorsionalMoment'], RDFS.subClassOf, EC1990.InternalForce))
g.add((EC1990['TorsionalMoment'], RDFS.label, Literal('Torsional Moment', lang='en')))
g.add((EC1990['TorsionalMoment'], RDFS.label, Literal('Momento Torsor', lang='es')))
g.add((EC1990['TorsionalMoment'], RDFS.comment, Literal('Internal moment causing twisting in structural members.', lang='en')))
g.add((EC1990['TorsionalMoment'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))
g.add((EC1990['TorsionalMoment'], SKOS.altLabel, Literal('T')))

g.add((EC1990['Stress'], RDF.type, OWL.Class))
g.add((EC1990['Stress'], RDFS.subClassOf, EC1990.MechanicalEffect))
g.add((EC1990['Stress'], RDFS.label, Literal('Stress', lang='en')))
g.add((EC1990['Stress'], RDFS.label, Literal('Tensión', lang='es')))
g.add((EC1990['Stress'], RDFS.comment, Literal('Internal stress in structural members due to actions.', lang='en')))
g.add((EC1990['Stress'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

g.add((EC1990['NormalStress'], RDF.type, OWL.Class))
g.add((EC1990['NormalStress'], RDFS.subClassOf, EC1990.Stress))
g.add((EC1990['NormalStress'], RDFS.label, Literal('Normal Stress', lang='en')))
g.add((EC1990['NormalStress'], RDFS.comment, Literal('Stress acting in the direction normal to a surface.', lang='en')))

g.add((EC1990['ShearStress'], RDF.type, OWL.Class))
g.add((EC1990['ShearStress'], RDFS.subClassOf, EC1990.Stress))
g.add((EC1990['ShearStress'], RDFS.label, Literal('Shear Stress', lang='en')))
g.add((EC1990['ShearStress'], RDFS.comment, Literal('Stress acting in the direction parallel (tangential) to a surface.', lang='en')))

g.add((EC1990['PrincipalStress'], RDF.type, OWL.Class))
g.add((EC1990['PrincipalStress'], RDFS.subClassOf, EC1990.Stress))
g.add((EC1990['PrincipalStress'], RDFS.label, Literal('Principal Stress', lang='en')))
g.add((EC1990['PrincipalStress'], RDFS.comment, Literal('Maximum or minimum normal stress at a point.', lang='en')))

g.add((EC1990['Strain'], RDF.type, OWL.Class))
g.add((EC1990['Strain'], RDFS.subClassOf, EC1990.MechanicalEffect))
g.add((EC1990['Strain'], RDFS.label, Literal('Strain', lang='en')))
g.add((EC1990['Strain'], RDFS.label, Literal('Deformación Unitaria', lang='es')))
g.add((EC1990['Strain'], RDFS.comment, Literal('Deformation per unit length in structural members.', lang='en')))
g.add((EC1990['Strain'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

# Deformation Effects
g.add((EC1990['Deformation'], RDF.type, OWL.Class))
g.add((EC1990['Deformation'], RDFS.subClassOf, EC1990.DeformationEffect))
g.add((EC1990['Deformation'], RDFS.label, Literal('Deformation', lang='en')))
g.add((EC1990['Deformation'], RDFS.label, Literal('Deformación', lang='es')))
g.add((EC1990['Deformation'], RDFS.comment, Literal('Change in shape or size of a structure or structural member due to actions.', lang='en')))
g.add((EC1990['Deformation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

g.add((EC1990['LinearDeformation'], RDF.type, OWL.Class))
g.add((EC1990['LinearDeformation'], RDFS.subClassOf, EC1990.Deformation))
g.add((EC1990['LinearDeformation'], RDFS.label, Literal('Linear Deformation', lang='en')))
g.add((EC1990['LinearDeformation'], RDFS.comment, Literal('Deformation involving linear displacement of points in the structure.', lang='en')))

g.add((EC1990['Deflection'], RDF.type, OWL.Class))
g.add((EC1990['Deflection'], RDFS.subClassOf, EC1990.LinearDeformation))
g.add((EC1990['Deflection'], RDFS.label, Literal('Deflection', lang='en')))
g.add((EC1990['Deflection'], RDFS.label, Literal('Flecha', lang='es')))
g.add((EC1990['Deflection'], RDFS.comment, Literal('Vertical deflction of a structural member.', lang='en')))
g.add((EC1990['Deflection'], DCTERMS.source, Literal('EN 1990:2002, Section 1.6')))
g.add((EC1990['Deflection'], SKOS.altLabel, Literal('w')))

g.add((EC1990['Displacement'], RDF.type, OWL.Class))
g.add((EC1990['Displacement'], RDFS.subClassOf, EC1990.LinearDeformation))
g.add((EC1990['Displacement'], RDFS.label, Literal('Displacement', lang='en')))
g.add((EC1990['Displacement'], RDFS.label, Literal('Desplazamiento', lang='es')))
g.add((EC1990['Displacement'], RDFS.comment, Literal('Horizontal displacement of a structure or structural member.', lang='en')))
g.add((EC1990['Displacement'], DCTERMS.source, Literal('EN 1990:2002, Section 1.6')))
g.add((EC1990['Displacement'], SKOS.altLabel, Literal('u')))

g.add((EC1990['AngularDeformation'], RDF.type, OWL.Class))
g.add((EC1990['AngularDeformation'], RDFS.subClassOf, EC1990.Deformation))
g.add((EC1990['AngularDeformation'], RDFS.label, Literal('Angular Deformation', lang='en')))
g.add((EC1990['AngularDeformation'], RDFS.comment, Literal('Deformation involving rotation or angular change in the structure.', lang='en')))
g.add((EC1990['AngularDeformation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

g.add((EC1990['Rotation'], RDF.type, OWL.Class))
g.add((EC1990['Rotation'], RDFS.subClassOf, EC1990.AngularDeformation))
g.add((EC1990['Rotation'], RDFS.label, Literal('Rotation', lang='en')))
g.add((EC1990['Rotation'], RDFS.label, Literal('Rotación', lang='es')))
g.add((EC1990['Rotation'], RDFS.comment, Literal('Angular rotation of a structure or structural member.', lang='en')))
g.add((EC1990['Rotation'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

g.add((EC1990['Twist'], RDF.type, OWL.Class))
g.add((EC1990['Twist'], RDFS.subClassOf, EC1990.AngularDeformation))
g.add((EC1990['Twist'], RDFS.label, Literal('Twist', lang='en')))
g.add((EC1990['Twist'], RDFS.label, Literal('Torsión', lang='es')))
g.add((EC1990['Twist'], RDFS.comment, Literal('Angular deformation about the longitudinal axis.', lang='en')))

g.add((EC1990['VolumetricDeformation'], RDF.type, OWL.Class))
g.add((EC1990['VolumetricDeformation'], RDFS.subClassOf, EC1990.Deformation))
g.add((EC1990['VolumetricDeformation'], RDFS.label, Literal('Volumetric Deformation', lang='en')))
g.add((EC1990['VolumetricDeformation'], RDFS.comment, Literal('Deformation involving change in volume of structural elements.', lang='en')))

# Dynamic Effects
g.add((EC1990['AccelerationEffect'], RDF.type, OWL.Class))
g.add((EC1990['AccelerationEffect'], RDFS.subClassOf, EC1990.DynamicEffect))
g.add((EC1990['AccelerationEffect'], RDFS.label, Literal('Acceleration Effect', lang='en')))
g.add((EC1990['AccelerationEffect'], RDFS.comment, Literal('Effect involving acceleration of the structure or structural members.', lang='en')))
g.add((EC1990['AccelerationEffect'], DCTERMS.source, Literal('EN 1990:2002, Section 4.1.5(2)')))

g.add((EC1990['VibrationResponse'], RDF.type, OWL.Class))
g.add((EC1990['VibrationResponse'], RDFS.subClassOf, EC1990.DynamicEffect))
g.add((EC1990['VibrationResponse'], RDFS.label, Literal('Vibration Response', lang='en')))
g.add((EC1990['VibrationResponse'], RDFS.label, Literal('Respuesta Vibratoria', lang='es')))
g.add((EC1990['VibrationResponse'], RDFS.comment, Literal('Dynamic response of structures to oscillatory actions, important for serviceability considerations.', lang='en')))

# Time-Dependent Effects
g.add((EC1990['CreepEffect'], RDF.type, OWL.Class))
g.add((EC1990['CreepEffect'], RDFS.subClassOf, EC1990.TimeDependentEffect))
g.add((EC1990['CreepEffect'], RDFS.label, Literal('Creep Effect', lang='en')))
g.add((EC1990['CreepEffect'], RDFS.label, Literal('Efecto de Fluencia', lang='es')))
g.add((EC1990['CreepEffect'], RDFS.comment, Literal('Long-term deformation effect due to sustained loading.', lang='en')))

g.add((EC1990['ShrinkageEffect'], RDF.type, OWL.Class))
g.add((EC1990['ShrinkageEffect'], RDFS.subClassOf, EC1990.TimeDependentEffect))
g.add((EC1990['ShrinkageEffect'], RDFS.label, Literal('Shrinkage Effect', lang='en')))
g.add((EC1990['ShrinkageEffect'], RDFS.label, Literal('Efecto de Retracción', lang='es')))
g.add((EC1990['ShrinkageEffect'], RDFS.comment, Literal('Deformation effect due to material shrinkage over time.', lang='en')))

g.add((EC1990['FatigueEffect'], RDF.type, OWL.Class))
g.add((EC1990['FatigueEffect'], RDFS.subClassOf, EC1990.TimeDependentEffect))
g.add((EC1990['FatigueEffect'], RDFS.label, Literal('Fatigue Effect', lang='en')))
g.add((EC1990['FatigueEffect'], RDFS.label, Literal('Efecto de Fatiga', lang='es')))
g.add((EC1990['FatigueEffect'], RDFS.comment, Literal('Progressive damage effect due to repeated loading cycles.', lang='en')))
g.add((EC1990['FatigueEffect'], DCTERMS.source, Literal('EN 1990:2002, Section 3.1(5)')))

g.add((EC1990['Reaction'], RDF.type, OWL.Class))
g.add((EC1990['Reaction'], RDFS.subClassOf, EC1990.EffectOfAction))
g.add((EC1990['Reaction'], RDFS.label, Literal('Reaction', lang='en')))
g.add((EC1990['Reaction'], RDFS.label, Literal('Reacción', lang='es')))
g.add((EC1990['Reaction'], RDFS.comment, Literal('Support reaction force or moment at structural supports.', lang='en')))
g.add((EC1990['Reaction'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.3.2')))

##########################################################
#                MATERIAL AND RESISTANCE                #
##########################################################

g.add((EC1990['Material'], RDF.type, OWL.Class))
g.add((EC1990['Material'], RDFS.label, Literal('Material', lang='en')))
g.add((EC1990['Material'], RDFS.label, Literal('Material', lang='es')))
g.add((EC1990['Material'], RDFS.comment, Literal('Indication of the principal structural material.', lang='en')))
g.add((EC1990['Material'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.1.3')))

g.add((EC1990['MaterialProperty'], RDF.type, OWL.Class))
g.add((EC1990['MaterialProperty'], RDFS.label, Literal('Material Property', lang='en')))
g.add((EC1990['MaterialProperty'], RDFS.label, Literal('Propiedad del Material', lang='es')))
g.add((EC1990['MaterialProperty'], RDFS.comment, Literal('Physical or mechanical property of construction materials.', lang='en')))
g.add((EC1990['MaterialProperty'], DCTERMS.source, Literal('EN 1990:2002, Section 4.2')))

g.add((EC1990['GeometricalProperty'], RDF.type, OWL.Class))
g.add((EC1990['GeometricalProperty'], RDFS.label, Literal('Geometrical Data', lang='en')))
g.add((EC1990['GeometricalProperty'], RDFS.label, Literal('Datos Geométricos', lang='es')))
g.add((EC1990['GeometricalProperty'], RDFS.comment, Literal('Geometrical properties and dimensions of structural elements.', lang='en')))
g.add((EC1990['GeometricalProperty'], DCTERMS.source, Literal('EN 1990:2002, Section 4.3')))

g.add((EC1990['Resistance'], RDF.type, OWL.Class))
g.add((EC1990['Resistance'], RDFS.label, Literal('Resistance', lang='en')))
g.add((EC1990['Resistance'], RDFS.label, Literal('Resistencia', lang='es')))
g.add((EC1990['Resistance'], RDFS.comment, Literal('Capacity of a member or component, or a cross-section of a member or component of a structure, to withstand actions without mechanical failure.', lang='en')))
g.add((EC1990['Resistance'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.15')))
g.add((EC1990['Resistance'], SKOS.example, Literal('bending resistance, buckling resistance, tension resistance')))
g.add((EC1990['Resistance'], SKOS.altLabel, Literal('R')))

g.add((EC1990['DesignWorkingLife'], RDF.type, OWL.Class))
g.add((EC1990['DesignWorkingLife'], RDFS.label, Literal('Design Working Life', lang='en')))
g.add((EC1990['DesignWorkingLife'], RDFS.label, Literal('Vida Útil de Proyecto', lang='es')))
g.add((EC1990['DesignWorkingLife'], RDFS.comment, Literal('Assumed period for which a structure or part of it is to be used for its intended purpose with anticipated maintenance but without major repair being necessary.', lang='en')))
g.add((EC1990['DesignWorkingLife'], DCTERMS.source, Literal('EN 1990:2002, Section 1.5.2.8')))

##########################################################
#                 OBJECT PROPERTIES                     #
##########################################################


g.add((EC1990['containsAction'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['containsAction'], RDFS.label, Literal('contains action', lang='en')))
g.add((EC1990['containsAction'], RDFS.label, Literal('contiene acción', lang='es')))
g.add((EC1990['containsAction'], RDFS.comment, Literal('Relates a combination of actions to the individual actions it contains.', lang='en')))
g.add((EC1990['containsAction'], RDFS.domain, EC1990.CombinationOfActions))
g.add((EC1990['containsAction'], RDFS.range, EC1990.Action))

g.add((EC1990['causesEffect'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['causesEffect'], RDFS.label, Literal('causes effect', lang='en')))
g.add((EC1990['causesEffect'], RDFS.label, Literal('causa efecto', lang='es')))
g.add((EC1990['causesEffect'], RDFS.comment, Literal('Relates a combination of actions to the effects it causes in the structure.', lang='en')))
g.add((EC1990['causesEffect'], RDFS.domain, EC1990.CombinationOfActions))
g.add((EC1990['causesEffect'], RDFS.range, EC1990.EffectOfAction))

g.add((EC1990['appliesTo'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['appliesTo'], RDFS.label, Literal('applies to', lang='en')))
g.add((EC1990['appliesTo'], RDFS.label, Literal('se aplica a', lang='es')))
g.add((EC1990['appliesTo'], RDFS.comment, Literal('Relates an action to the structural member or structure it acts upon.', lang='en')))
g.add((EC1990['appliesTo'], RDFS.domain, EC1990.Action))
g.add((EC1990['appliesTo'], RDFS.range, EC1990.StructuralMember))

g.add((EC1990['isDesignedFor'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['isDesignedFor'], RDFS.label, Literal('is designed for', lang='en')))
g.add((EC1990['isDesignedFor'], RDFS.label, Literal('se aplica a', lang='es')))
g.add((EC1990['isDesignedFor'], RDFS.comment, Literal('Relates a structural memeber with the design situation it is designed for.', lang='en')))
g.add((EC1990['isDesignedFor'], RDFS.domain, EC1990.StructuralMember))
g.add((EC1990['isDesignedFor'], RDFS.range, EC1990.DesignSituation))

g.add((EC1990['requiresVerficationOf'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['requiresVerficationOf'], RDFS.label, Literal('requires verification of', lang='en')))
g.add((EC1990['requiresVerficationOf'], RDFS.label, Literal('requiere verificación de', lang='es')))
g.add((EC1990['requiresVerficationOf'], RDFS.comment, Literal('Relates a limit state to the combination of actions used for its verification.', lang='en')))
g.add((EC1990['requiresVerficationOf'], RDFS.domain, EC1990.DesignSituation))
g.add((EC1990['requiresVerficationOf'], RDFS.range, EC1990.LimitState))

g.add((EC1990['verifiedBy'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['verifiedBy'], RDFS.label, Literal('verified by', lang='en')))
g.add((EC1990['verifiedBy'], RDFS.label, Literal('verificado por', lang='es')))
g.add((EC1990['verifiedBy'], RDFS.comment, Literal('Relates a limit state to the combination of actions used for its verification.', lang='en')))
g.add((EC1990['verifiedBy'], RDFS.domain, EC1990.LimitState))
g.add((EC1990['verifiedBy'], RDFS.range, EC1990.CombinationOfActions))

g.add((EC1990['hasResistance'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasResistance'], RDFS.label, Literal('has resistance', lang='en')))
g.add((EC1990['hasResistance'], RDFS.comment, Literal('Relates a structural member to its resistance capacity.', lang='en')))
g.add((EC1990['hasResistance'], RDFS.domain, EC1990.StructuralMember))
g.add((EC1990['hasResistance'], RDFS.range, EC1990.Resistance))

g.add((EC1990['isMadeOf'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['isMadeOf'], RDFS.label, Literal('is made of', lang='en')))
g.add((EC1990['isMadeOf'], RDFS.comment, Literal('Relates a structural member to the material which it is made of.', lang='en')))
g.add((EC1990['isMadeOf'], RDFS.domain, EC1990.StructuralMember))
g.add((EC1990['isMadeOf'], RDFS.range, EC1990.Material))

g.add((EC1990['hasMaterialProperty'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasMaterialProperty'], RDFS.label, Literal('has Property', lang='en')))
g.add((EC1990['hasMaterialProperty'], RDFS.comment, Literal('Relates a material with its properties.', lang='en')))
g.add((EC1990['hasMaterialProperty'], RDFS.domain, EC1990.Material))
g.add((EC1990['hasMaterialProperty'], RDFS.range, EC1990.MaterialProperty))

g.add((EC1990['hasGeometricalProperty'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasGeometricalProperty'], RDFS.label, Literal('has geometrical property', lang='en')))
g.add((EC1990['hasGeometricalProperty'], RDFS.comment, Literal('Relates a structural member with its geometrical properties.', lang='en')))
g.add((EC1990['hasGeometricalProperty'], RDFS.domain, EC1990.StructuralMember))
g.add((EC1990['hasGeometricalProperty'], RDFS.range, EC1990.GeometricalProperty))

g.add((EC1990['hasSystem'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasSystem'], RDFS.label, Literal('has system', lang='en')))
g.add((EC1990['hasSystem'], RDFS.comment, Literal('Relates a structure with its structural system.', lang='en')))
g.add((EC1990['hasSystem'], RDFS.domain, EC1990.Structure))
g.add((EC1990['hasSystem'], RDFS.range, EC1990.StructuralSystem))

g.add((EC1990['hasDesignWorkingLife'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasDesignWorkingLife'], RDFS.label, Literal('has design working life', lang='en')))
g.add((EC1990['hasDesignWorkingLife'], RDFS.comment, Literal('Relates a structure to its design working life.', lang='en')))
g.add((EC1990['hasDesignWorkingLife'], RDFS.domain, EC1990.Structure))
g.add((EC1990['hasDesignWorkingLife'], RDFS.range, EC1990.DesignWorkingLife))

g.add((EC1990['hasStructuralMember'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasStructuralMember'], RDFS.subPropertyOf, BOT.hasElement))
g.add((EC1990['hasStructuralMember'], RDFS.label, Literal('has structural member', lang='en')))
g.add((EC1990['hasStructuralMember'], RDFS.comment, Literal('Relates a a structural element with the zone.', lang='en')))
g.add((EC1990['hasStructuralMember'], RDFS.domain, BOT.Zone))
g.add((EC1990['hasStructuralMember'], RDFS.range, EC1990.StructuralMember))

g.add((EC1990['containsStructuralMember'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['containsStructuralMember'], RDFS.subPropertyOf, BOT.hasElement))
g.add((EC1990['containsStructuralMember'], RDFS.label, Literal('contains structural member', lang='en')))
g.add((EC1990['containsStructuralMember'], RDFS.comment, Literal('Relates a a structural element with the structural syste.', lang='en')))
g.add((EC1990['containsStructuralMember'], RDFS.domain, EC1990.StructuralSystem))
g.add((EC1990['containsStructuralMember'], RDFS.range, EC1990.StructuralMember))

g.add((EC1990['hasStructure'], RDF.type, OWL.ObjectProperty))
g.add((EC1990['hasStructure'], RDFS.subPropertyOf, BOT.hasElement))
g.add((EC1990['hasStructure'], RDFS.label, Literal('has structure', lang='en')))
g.add((EC1990['hasStructure'], RDFS.comment, Literal('Relates a contrution work with the structure.', lang='en')))
g.add((EC1990['hasStructure'], RDFS.domain, EC1990.ConstructionWork))
g.add((EC1990['hasStructure'], RDFS.range, EC1990.Structure))

##########################################################
#                 DATA PROPERTIES                       #
##########################################################

# Action Values
g.add((EC1990['hasCharacteristicValue'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['hasCharacteristicValue'], RDFS.label, Literal('Characteristic Value', lang='en')))
g.add((EC1990['hasCharacteristicValue'], RDFS.label, Literal('Valor Característico', lang='es')))
g.add((EC1990['hasCharacteristicValue'], RDFS.comment, Literal('Principal representative value of an action. In so far as a characteristic value can be fixed on statistical bases, it is chosen so as to correspond to a prescribed probability of not being exceeded on the unfavourable side during a reference period.', lang='en')))
g.add((EC1990['hasCharacteristicValue'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 1.5.3.14')))
g.add((EC1990['hasCharacteristicValue'], SKOS.altLabel, Literal('Fk')))
g.add((EC1990['hasCharacteristicValue'], RDFS.domain, EC1990.Action))
g.add((EC1990['hasCharacteristicValue'], RDFS.range, XSD.decimal))

g.add((EC1990['hasDesignValue'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['hasDesignValue'], RDFS.label, Literal('Design Value', lang='en')))
g.add((EC1990['hasDesignValue'], RDFS.label, Literal('Valor de Cálculo', lang='es')))
g.add((EC1990['hasDesignValue'], RDFS.comment, Literal('Value obtained by multiplying the representative value by the partial factor γf.', lang='en')))
g.add((EC1990['hasDesignValue'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 1.5.3.21')))
g.add((EC1990['hasDesignValue'], SKOS.altLabel, Literal('Fd')))
g.add((EC1990['hasDesignValue'], RDFS.domain, EC1990.Action))
g.add((EC1990['hasDesignValue'], RDFS.range, XSD.decimal))

g.add((EC1990['hasRepresentativeValue'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['hasRepresentativeValue'], RDFS.label, Literal('Representative Value', lang='en')))
g.add((EC1990['hasRepresentativeValue'], RDFS.label, Literal('Valor Representativo', lang='es')))
g.add((EC1990['hasRepresentativeValue'], RDFS.comment, Literal('Value used for the verification of a limit state. A representative value may be the characteristic value (Fk) or an accompanying value (ψFk).', lang='en')))
g.add((EC1990['hasRepresentativeValue'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 1.5.3.20')))
g.add((EC1990['hasRepresentativeValue'], SKOS.altLabel, Literal('Frep')))
g.add((EC1990['hasRepresentativeValue'], RDFS.domain, EC1990.Action))
g.add((EC1990['hasRepresentativeValue'], RDFS.range, XSD.decimal))

#Partial Factors
g.add((EC1990['PartialFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['PartialFactor'], RDFS.label, Literal('Partial Factor', lang='en')))
g.add((EC1990['PartialFactor'], RDFS.label, Literal('Factor Parcial', lang='es')))
g.add((EC1990['PartialFactor'], RDFS.comment, Literal('Safety factor applied to actions or material properties to account for uncertainties.', lang='en')))
g.add((EC1990['PartialFactor'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 6.3.1')))
g.add((EC1990['PartialFactor'], RDFS.domain, EC1990.Action))
g.add((EC1990['PartialFactor'], RDFS.range, XSD.decimal))

g.add((EC1990['PermanentActionPartialFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['PermanentActionPartialFactor'], RDFS.subPropertyOf, EC1990.PartialFactor))
g.add((EC1990['PermanentActionPartialFactor'], RDFS.label, Literal('Permanent Action Partial Factor', lang='en')))
g.add((EC1990['PermanentActionPartialFactor'], RDFS.label, Literal('Factor Parcial de Acción Permanente', lang='es')))
g.add((EC1990['PermanentActionPartialFactor'], RDFS.comment, Literal('Partial factor γG applied to permanent actions.', lang='en')))
g.add((EC1990['PermanentActionPartialFactor'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 6.3.1')))
g.add((EC1990['PermanentActionPartialFactor'], RDFS.domain, EC1990.PermanentAction))
g.add((EC1990['PermanentActionPartialFactor'], SKOS.altLabel, Literal('γG')))

g.add((EC1990['VariableActionPartialFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['VariableActionPartialFactor'], RDFS.subPropertyOf, EC1990.PartialFactor))
g.add((EC1990['VariableActionPartialFactor'], RDFS.label, Literal('Variable Action Partial Factor', lang='en')))
g.add((EC1990['VariableActionPartialFactor'], RDFS.label, Literal('Factor Parcial de Acción Variable', lang='es')))
g.add((EC1990['VariableActionPartialFactor'], RDFS.comment, Literal('Partial factor γQ applied to variable actions.', lang='en')))
g.add((EC1990['VariableActionPartialFactor'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 6.3.1')))
g.add((EC1990['VariableActionPartialFactor'], RDFS.domain, EC1990.VariableAction))
g.add((EC1990['VariableActionPartialFactor'], SKOS.altLabel, Literal('γQ')))

g.add((EC1990['MaterialPartialFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['MaterialPartialFactor'], RDFS.subPropertyOf, EC1990.PartialFactor))
g.add((EC1990['MaterialPartialFactor'], RDFS.label, Literal('Material Partial Factor', lang='en')))
g.add((EC1990['MaterialPartialFactor'], RDFS.label, Literal('Factor Parcial del Material', lang='es')))
g.add((EC1990['MaterialPartialFactor'], RDFS.comment, Literal('Partial factor γₘ for material properties taking account of the possibility of an unfavourable deviation of a material property from its characteristic value.', lang='en')))
g.add((EC1990['MaterialPartialFactor'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 6.3.3')))
g.add((EC1990['MaterialPartialFactor'], RDFS.domain, EC1990.MaterialProperty))
g.add((EC1990['MaterialPartialFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['MaterialPartialFactor'], SKOS.altLabel, Literal('γₘ')))

g.add((EC1990['MaterialModelPartialFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['MaterialModelPartialFactor'], RDFS.subPropertyOf, EC1990.PartialFactor))
g.add((EC1990['MaterialModelPartialFactor'], RDFS.label, Literal('Material-Model Partial Factor', lang='en')))
g.add((EC1990['MaterialModelPartialFactor'], RDFS.label, Literal('Factor Parcial del Modelo del Material', lang='es')))
g.add((EC1990['MaterialModelPartialFactor'], RDFS.comment, Literal('Partial factor γₘ for material properties also accounting for model uncertainties and dimensional variations.', lang='en')))
g.add((EC1990['MaterialModelPartialFactor'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 6.3.3')))
g.add((EC1990['MaterialModelPartialFactor'], RDFS.domain, EC1990.MaterialProperty))
g.add((EC1990['MaterialModelPartialFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['MaterialModelPartialFactor'], SKOS.altLabel, Literal('γₘ')))

#Combination Factors
g.add((EC1990['CombinationFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['CombinationFactor'], RDFS.label, Literal('Combination Factor', lang='en')))
g.add((EC1990['CombinationFactor'], RDFS.label, Literal('Factor de Combinación', lang='es')))
g.add((EC1990['CombinationFactor'], RDFS.comment, Literal('Factor ψ₀ for combination value of a variable action used in ultimate limit state verifications.', lang='en')))
g.add((EC1990['CombinationFactor'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 1.5.3.16')))
g.add((EC1990['CombinationFactor'], RDFS.domain, EC1990.VariableAction))
g.add((EC1990['CombinationFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['CombinationFactor'], SKOS.altLabel, Literal('ψ₀')))

g.add((EC1990['FrequentFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['FrequentFactor'], RDFS.label, Literal('Frequent Factor', lang='en')))
g.add((EC1990['FrequentFactor'], RDFS.label, Literal('Factor Frecuente', lang='es')))
g.add((EC1990['FrequentFactor'], RDFS.comment, Literal('Factor ψ₁ for frequent value of a variable action, determined so that either the total time within the reference period during which it is exceeded is only a small given part of the reference period, or the frequency of it being exceeded is limited to a given value.', lang='en')))
g.add((EC1990['FrequentFactor'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 1.5.3.17')))
g.add((EC1990['FrequentFactor'], RDFS.domain, EC1990.VariableAction))
g.add((EC1990['FrequentFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['FrequentFactor'], SKOS.altLabel, Literal('ψ₁')))

g.add((EC1990['QuasiPermanentFactor'], RDF.type, OWL.DatatypeProperty))
g.add((EC1990['QuasiPermanentFactor'], RDFS.label, Literal('Quasi-Permanent Factor', lang='en')))
g.add((EC1990['QuasiPermanentFactor'], RDFS.label, Literal('Factor Cuasi-permanente', lang='es')))
g.add((EC1990['QuasiPermanentFactor'], RDFS.comment, Literal('Factor ψ₂ for quasi-permanent value of a variable action, determined so that the total period of time for which it will be exceeded is a large fraction of the reference period.', lang='en')))
g.add((EC1990['QuasiPermanentFactor'], DCTERMS.source, Literal('UNE-EN 1990:2019, Section 1.5.3.18')))
g.add((EC1990['QuasiPermanentFactor'], RDFS.domain, EC1990.VariableAction))
g.add((EC1990['QuasiPermanentFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['QuasiPermanentFactor'], SKOS.altLabel, Literal('ψ₂')))

##########################################################
#                    DISJOINT CLASSES                   #
##########################################################

# Direct and indirect actions are mutually exclusive
g.add((EC1990['DirectAction'], OWL.disjointWith, EC1990.IndirectAction))

# Limit state types are mutually exclusive
g.add((EC1990['UltimateLimitState'], OWL.disjointWith, EC1990.ServiceabilityLimitState))

# SLS subtypes are mutually exclusive
g.add((EC1990['ReversibleServiceabilityLimitState'], OWL.disjointWith, EC1990.IrreversibleServiceabilityLimitState))

# Action spatial variation types are mutually exclusive
g.add((EC1990['FixedAction'], OWL.disjointWith, EC1990.FreeAction))

# Action dynamic response types are mutually exclusive
g.add((EC1990['StaticAction'], OWL.disjointWith, EC1990.DynamicAction))

# Design situation types are mutually exclusive  
g.add((EC1990['PersistentDesignSituation'], OWL.disjointWith, EC1990.TransientDesignSituation))
g.add((EC1990['PersistentDesignSituation'], OWL.disjointWith, EC1990.AccidentalDesignSituation))
g.add((EC1990['PersistentDesignSituation'], OWL.disjointWith, EC1990.SeismicDesignSituation))
g.add((EC1990['TransientDesignSituation'], OWL.disjointWith, EC1990.AccidentalDesignSituation))
g.add((EC1990['TransientDesignSituation'], OWL.disjointWith, EC1990.SeismicDesignSituation))
g.add((EC1990['AccidentalDesignSituation'], OWL.disjointWith, EC1990.SeismicDesignSituation))

# ULS and SLS combinations are mutually exclusive
g.add((EC1990['ULSCombination'], OWL.disjointWith, EC1990.SLSCombination))

# Effect categories are mutually exclusive where appropriate
g.add((EC1990['LinearDeformation'], OWL.disjointWith, EC1990.AngularDeformation))
g.add((EC1990['LinearDeformation'], OWL.disjointWith, EC1990.VolumetricDeformation))
g.add((EC1990['AngularDeformation'], OWL.disjointWith, EC1990.VolumetricDeformation))

##########################################################
#               CONSTRAINTS AND RESTRICTIONS            #
##########################################################

# Value constraints for factors (ψ factors are ≤ 1.0)
# Note: These would be better expressed as SHACL shapes or OWL restrictions

# Add range restrictions for partial factors (typically > 1.0 for safety)
g.add((EC1990['PermanentActionPartialFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['VariableActionPartialFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['MaterialPartialFactor'], RDFS.range, XSD.decimal))

# Add range restrictions for combination factors (typically ≤ 1.0)
g.add((EC1990['CombinationFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['FrequentFactor'], RDFS.range, XSD.decimal))
g.add((EC1990['QuasiPermanentFactor'], RDFS.range, XSD.decimal))

##########################################################
#                 ADDITIONAL METADATA                   #
##########################################################

# Add ontology-level metadata for better findability
g.add((ref, SKOS.hasTopConcept, EC1990.Action))
g.add((ref, SKOS.hasTopConcept, EC1990.EffectOfAction))
g.add((ref, SKOS.hasTopConcept, EC1990.LimitState))
g.add((ref, SKOS.hasTopConcept, EC1990.DesignSituation))
g.add((ref, SKOS.hasTopConcept, EC1990.CombinationOfActions))
g.add((ref, SKOS.hasTopConcept, EC1990.ConstructionWork))

# Add provenance information
g.add((ref, DCTERMS.contributor, Literal('Agnieszka Jedrzejewska (Silesian Unviersity)')))
g.add((ref, DCTERMS.contributor, Literal('Maria Laura Leonardi (University of Minho)')))
g.add((ref, DCTERMS.contributor, Literal('Carlos Ramonell (Politechnical University of Catalonia)')))
g.add((ref, DCTERMS.publisher, Literal('Asociación Española de Normalización (UNE)')))
g.add((ref, DCTERMS.rights, Literal('© UNE 2019 - All rights reserved')))




##########################################################
#               SEMANTIC RELATIONSHIPS                  #
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
g.add((EC1990['PartialFactor'], SKOS.editorialNote, Literal('Partial factors account for various sources of uncertainty including statistical uncertainty, model uncertainty, and dimensional variations')))
g.add((EC1990['LimitState'], SKOS.editorialNote, Literal('Limit states define critical conditions that must not be exceeded to ensure structural safety and serviceability')))
g.add((EC1990['EffectOfAction'], SKOS.editorialNote, Literal('Effects of actions can be calculated through structural analysis and must be compared against resistance for verification')))

##########################################################
#                    FINALIZATION                       #
##########################################################

# Save the improved ontology
g.serialize(destination=save_path, format='turtle')

print("✅ Improved EC1990 ontology completed and saved!")
print(f"📁 File saved at: {save_path}")
print(f"🌐 Namespace: {ref}")
print(f"📊 Current triples count: {len(g)}")
print("\n🔧 Improvements implemented:")
print("   • Complete Limit States framework (ULS/SLS with specific types)")
print("   • Design values and representative values hierarchy")
print("   • Material properties and resistance concepts")
print("   • Enhanced effects taxonomy with better organization")
print("   • Temporal aspects (working life, time-dependent effects)")
print("   • More precise relationships and object properties")
print("   • Multilingual labels (English/Spanish)")
print("   • Comprehensive annotations with document references")
print("   • Disjoint class declarations for logical consistency")
print("   • Improved ontology metadata and provenance")
print("   • SKOS vocabulary for better semantic richness")
print("   • Editorial notes and usage guidance")