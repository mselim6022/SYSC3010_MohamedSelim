from pandas import read_sql_query
import sqlite3
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Connect the database
dbconnect = sqlite3.connect("sensorDB.db")

#Read the database into a DataFrame
df = read_sql_query('''SELECT * from sensordata''', dbconnect, "id", "readTime")

#Make a plot with a secondary y axis. Since the values of temperature and humidity are around the same
#order of magnitude, we will plot them on the same y axis. The values of pressure will be on a separate
#y axis.
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.update_layout(title = "Sensor Data over time")


#Add trace for temperature and humidity values
fig.add_trace(
	go.Scatter(x=df['readTime'], y= df['temperature'], name = "Temperature(\u2103)", mode="markers"),
	secondary_y = False
)
fig.add_trace(
	go.Scatter(x=df['readTime'], y=df['humidity'], name = "Humidity(%)", mode="markers"),
	secondary_y = False
)

#Add trace for pressure
fig.add_trace(
	go.Scatter(x = df['readTime'], y = df['pressure'], name = "Pressure(millibars)", mode= "markers"),
	secondary_y = True
)

fig.write_html('tmp.html', auto_open = True)
