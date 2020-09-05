from flask import render_template
from folium import Map
from folium.plugins import HeatMap
from app import app

@app.route('/')
@app.route('/index')
def index():
	start_coords = (30.61722222222222, -96.3338888888889)
	hmap = Map(location=start_coords, zoom_start=15)
	hmap_element = HeatMap([(30.615250, -96.335952)],
			min_opacity=1, max_val=5, radius=17, blur=15)
	hmap.add_child(hmap_element)
	return render_template('index.html', hmap=hmap)

