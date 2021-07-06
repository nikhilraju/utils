import pandas as pd
import plotly.graph_objs as go
from IPython.core.interactiveshell import InteractiveShell # Display all cell outputs
InteractiveShell.ast_node_interactivity = 'all'
pd.options.display.max_columns = 30
import plotly.express as px
df = pd.read_csv('some_data.csv')
df.col0.value_counts()
px.histogram(df.col0)
