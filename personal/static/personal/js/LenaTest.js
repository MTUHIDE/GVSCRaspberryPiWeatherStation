import 'ol/ol.css';
import Feature from 'ol/Feature';
import Map from 'ol/Map';
import View from 'ol/View';
import Point from 'ol/geom/Point';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import {Fill, RegularShape, Stroke, Style} from 'ol/style';

	
var map = new ol.Map({
	target: 'map',
	layers: [
		new ol.layer.Tile({
			source: new ol.source.OSM()
		})
	],
	view: new ol.View({
		center: ol.proj.fromLonLat([271.44,47.1211]),
		zoom: 14
	})
						
});

var stroke = new Stroke({color: 'black', width: 2});
var fill = new Fill({color: 'red'});
					
var styles = {
  'square': new Style({
    image: new RegularShape({
      fill: fill,
      stroke: stroke,
      points: 4,
      radius: 10,
      angle: Math.PI / 4
    })
  })
};

	var styleKeys = ['square'];

	features[0] new Feature(new Point(271.44,47.1211));
	