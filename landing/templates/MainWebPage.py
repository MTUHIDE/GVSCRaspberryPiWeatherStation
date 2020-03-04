import webbrowser
import pathlib

f = open('MainWebPage.html', 'w')

message = """
<html>
<title>TempPi.st</title>
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL">
</script>
    <style>

<style type="text/css">
#back-background 
{
background-color:navy;
}

#outer-border
{
padding:2%;
}

#main-body
{
border-style: solid;
border-width: 5px;
border-color: orange;
border-radius: 10px;
height:95%;
width: 100%;
}

#map
{
height:100%;
width:100%;
position:relative;
}

#main-title-header
{
display:inline;
position: absolute;
width:25%;
padding-top:2%;
text-align:center;

border-radius: 10px;
min-height: 8%;
z-index: 10;
margin-left:37.5%;
}

#pi-finder
{
height: 90%;
width: 10%;
position: absolute;
margin-left:80%;
margin-top:3%;
z-index:10;
}

#pi-finder-button
{
height:70px;
width:70px;
border-radius: 40px;
border-color:orange;
border:2px solid orange;
background-color:lightblue;
outline:none;
}

#pi-finder-button:active 
{
background-color: darkblue;
border: 3px solid red;
box-shadow: 0 5px #666;
}

#pi-finder-menu
{
border-style: solid;
border-width: 5px;
border-color: orange;
border-radius: 10px;
height:70%;
width: 100%;
background-color:darkblue;
display:none;
}

#hide-pi-finder
{
height:20px;
width:20px;
border-radius: 40px;
border-color:orange;
border:2px solid orange;
background-color:lightblue;
outline:none;
}

#hide-pi-finder:active 
{
background-color: darkblue;
border: 3px solid red;
box-shadow: 0 5px #666;
}
</style>

<head>
<script src="http://www.openlayers.org/api/OpenLayers.js"></script>
</head>

<body id="back-background">
<div id="outer-border">
<div id="main-body">

<h1 id="main-title-header"><img src="Logo.png" style="height:100px; margin-left:-20px;"></h1>

<div id="pi-finder">
<button id="pi-finder-button" type="button">Click Me!</button>
<div id="pi-finder-menu">
<button id="hide-pi-finder" type="button">_</button>
</div>
</div>
<div id="map">
<script type="text/javascript">

map = new OpenLayers.Map("map");
map.addLayer(new OpenLayers.Layer.OSM());

var lonLat = new OpenLayers.LonLat(47.118287, -88.544612).transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject());
var zoom=16;
var markers = new OpenLayers.Layer.Markers( "Markers" );
map.addLayer(markers);
var Pi1 = new OpenLayers.LonLat(47.118172, -88.547190).transform(new OpenLayers.Projection("EPSG:4326"), map.getProjectionObject());
markers.addMarker(new OpenLayers.Marker(Pi1));
map.setCenter (lonLat, zoom);
</script>
<script src="LenaTest.js" type="module"></script>
</div>
</div>
</div>
</body>
<script>

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
</script>
</html> """

f.write(message)
f.close()

filename = str(pathlib.Path().absolute())
filename = filename + '\MainWebPage.html'

webbrowser.open_new_tab(filename)
