// Function to determine marker size based on population
function markerSize(population) {
  return population / 40;
}

// An array containing all of the information needed to create city and state markers
var locations = [
  {
    coordinates: [33.6558, -84.4333],
    Airport: {
      name: "'Hartsfield-Jackson Atlanta International Airport'",
      population: 1001200
    },
    city: {
      name: "Atlanta",
      population: 9236586
    }
  },
  {
    coordinates: [34.0522, -118.2437],
    Airport: {
      name: "LAX International Airport",
      population: 900000
    },
    city: {
      name: "Lost Angeles",
      population: 3971883
    }
  },
  {
    coordinates: [41.8781, -87.6298],
    Airport: {
      name: "Chicago O'Hare International Airport",
      population: 992800
    },
    city: {
      name: "Chicago",
      population: 2720546
    }
  },
  {
    coordinates: [29.7604, -95.3698],
    Airport: {
      name: "George Bush Intercontinental Airport",
      population: 696000
    },
    city: {
      name: "Houston",
      population: 2296224
    }
  },
  {
    coordinates: [25.7953, -80.2727],
    Airport: {
      name: "Miami International Airport",
      population: 882000
    },
    city: {
      name: "Miami",
      population: 446599
    }
  }
];

// Define arrays to hold created city and state markers
var cityMarkers = [];
var stateMarkers = [];

// Loop through locations and create city and state markers
for (var i = 0; i < locations.length; i++) {
  // Setting the marker radius for the state by passing population into the markerSize function
  stateMarkers.push(
    L.circle(locations[i].coordinates, {
      stroke: false,
      fillOpacity: 0.75,
      color: "black",
      fillColor: "black",
      radius: markerSize(locations[i].Airport.population)
    })
  );

  // Setting the marker radius for the city by passing population into the markerSize function
  cityMarkers.push(
    L.circle(locations[i].coordinates, {
      stroke: false,
      fillOpacity: 0.75,
      color: "purple",
      fillColor: "purple",
      radius: markerSize(locations[i].city.population)
    })
  );
}

// Define variables for our base layers
var streetmap = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	id: 'mapbox.streets',
	accessToken: 'pk.eyJ1IjoiYnVlY2hzZWxpIiwiYSI6ImNqaWR3ZXNyMzBmenMzcHF2dnZiYzUwdXEifQ.WA83el9zRCPfUnXbV0GEjg',
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
})
var darkmap = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	id: 'mapbox.streets',
	accessToken: 'pk.eyJ1IjoiYnVlY2hzZWxpIiwiYSI6ImNqaWR3ZXNyMzBmenMzcHF2dnZiYzUwdXEifQ.WA83el9zRCPfUnXbV0GEjg',
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
})


// Create two separate layer groups: one for cities and one for states
var Airports = L.layerGroup(stateMarkers);
var cities = L.layerGroup(cityMarkers);

// Create a baseMaps object
var baseMaps = {
  "Street Map": streetmap,
  "Dark Map": darkmap
};

// Create an overlay object
var overlayMaps = {
  "Airport Direct Flights": Airports,
  "Airport Passengers Total": cities
};

// Define a map object
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5,
  layers: [streetmap, Airports, cities]
});

// Pass our map layers into our layer control
// Add the layer control to the map
L.control.layers(baseMaps, overlayMaps, {
  collapsed: false
}).addTo(myMap);
