from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy import MetaData
import pydotplus
from sqlalchemy import create_engine

def create_schema_graph_pydotplus(metadata, engine, **kwargs):
    graph = create_schema_graph(metadata=metadata, engine=engine, **kwargs)
    dot_data = graph.to_string()
    graph = pydotplus.graph_from_dot_data(dot_data)
    return graph

# Create the database engine
engine = create_engine('sqlite:///law.db')

# Create a new metadata instance
metadata = MetaData()

# Reflect your current database into the metadata
metadata.reflect(bind=engine)

# Create the schema graph from the metadata
graph = create_schema_graph_pydotplus(metadata=metadata, engine=engine, show_datatypes=True, show_indexes=True, rankdir='LR')

# Use pydotplus to render the graph to a file
graph.write_png('schema.png')