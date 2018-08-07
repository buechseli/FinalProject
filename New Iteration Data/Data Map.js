


​



d3.json("https://gist.githubusercontent.com/tdreyno/4278655/raw/7b0762c09b519f40397e4c3e100b097d861f5588/airports.json", createMarkers);



​



function createMarkers(response) {



​



 // pull the airports off of response.data



 var airport = response.data.name



 



​



 // initialize an array to hold airport markers



 var airportMarkers = [];



​



 // loop through the airport array



 for (var index = 0; index < airport.length; index++) {



  var airport = airport[index];



​



  // for each airport, create a marker and bind a popup with the airport's name



  var airportMarker = L.marker([airport.lat, airport.lon])



   .bindPopup("<h3>" + airport.name);



​



  // add the marker to the airportMarkers array



  airportMarkers.push(airportMarker);



 }



​



 // create a layer group made from the airport markers array, pass it into the createMap function



 createMap(L.layerGroup(airportMarkers));



}



​



function createMap(worldAirports) {



​



 // create the tile layer that will be the background of our map



 var lightmap = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {



 	accessToken: 'pk.eyJ1IjoibmFrcmFtMTE1IiwiYSI6ImNqaWR2Ym5peDAyNmgzcG1xeDVwcnIxYXcifQ.FaKZzXQlmEbjQs7q_Md-vA',



 	id: 'mapbox.streets',



 	maxZoom: 1,



 	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',



 });



​



 // create a baseMaps object to hold the lightmap layer



 var baseMaps = {



  "Light Map": lightmap



 };



​



 // create an overlayMaps object to hold the airports layer



 var overlayMaps = {



  "Airports": worldAirports



 };



​



 // Create the map object with options



 var map = L.map("map-id", {



  center: [0, -180.00],



  zoom: 1,



  layers: [lightmap, airportMarkers]



 });



​



 // create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map



 L.control.layers(baseMaps, overlayMaps, {



  collapsed: false



 }).addTo(map);



}



Noreen Malik [7:16 PM]

https://gist.githubusercontent.com/tdreyno/4278655/raw/7b0762c09b519f40397e4c3e100b097d861f5588/airports.json

Message Input





Message Grace C., Noreen Malik