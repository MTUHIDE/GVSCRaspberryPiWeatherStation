map = new OpenLayers.Map("map");
map.addLayer(new OpenLayers.Layer.OSM());



var lonLat = new OpenLayers.LonLat(271.45, 47.1211).transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject());
var zoom=16;
var markers = new OpenLayers.Layer.Markers( "Markers" );
map.addLayer(markers);
var pi = new OpenLayers.LonLat(271.45282, 47.118287).transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject());

markers.addMarker(new OpenLayers.Marker(pi));
map.setCenter (lonLat, zoom);


document.getElementById("pi-finder-button").onclick = function() {piFinderClick()};
document.getElementById("hide-pi-finder").onclick = function() {hidePiClick()};

function piFinderClick() 
{
document.getElementById("pi-finder-button").style.display = "none";
document.getElementById("pi-finder-menu").style.display = "block";
}

function hidePiClick() 
{
document.getElementById("pi-finder-menu").style.display = "none";
document.getElementById("pi-finder-button").style.display = "block";
}