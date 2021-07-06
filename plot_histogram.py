import pandas as pd
import plotly.graph_objs as go
from IPython.core.interactiveshell import InteractiveShell # Display all cell outputs
InteractiveShell.ast_node_interactivity = 'last'
pd.options.display.max_columns = 30
import plotly.express as px
df = pd.read_csv('some_data.csv')
df.col0.value_counts()
fig = px.histogram(df.col0)
fig.add_annotation(x=6, y=30,
            text="<b>Bin Intervals:</b><br>[0,5)<br>[5,10)<br>[10,15)<br>[15,20)<br>[20,25)",
            showarrow=False,
            arrowhead=1)

fig.update_layout({
        'title': f'Foo .... over {len(df)} data points',
        'xaxis_title': "Bar ....",
        'yaxis_title': "% of foo over...",
    
    })
