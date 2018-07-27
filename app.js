// Step 1: Set up our chart
//= ================================
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 50
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Step 2: Create an SVG wrapper,
// append an SVG group that will hold our chart,
// and shift the latter by left and top margins.
// =================================
var svg = d3
  .select(".chart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Step 3:
// Import data from the country_info.json file
// =================================

var parseTime = d3.timeParse("%Y");


d3.json("./country_info.json", function(error, countryData) {
   if (error) throw error; 
   console.log(countryData[0]);
   console.log("Country Name :", countryData[0]['country_name']);
   console.log("Total Arrivals :", countryData[0]['arrivals']['total']);
   console.log("Total Departures :", countryData[0]['departures']['total']);
   console.log("Total Inbound Tourism Spend :", countryData[0]['expenditure_in_country']);
   console.log("Total Outbound Tourism Spend :", countryData[0]['expenditure_out_country']);
   console.log("Years :", countryData[0]['years'])

  // Step 4: Parse the data

  // Format the data
  countryData.forEach(function(data) {
    data.arrivals.total = +data.arrivals.total;
    data.departures.total = +data.departures.total;
  });

  // Step 5: Create the scales for the chart
  // =================================
  var xTimeScale = d3.scaleTime()
    .domain(d3.extent(year_axis))
    .range([0, width]);

  var yLinearScale = d3.scaleLinear().range([height, 0]);

  // Step 6: Set up the y-axis domain
  // ==============================================
  // @NEW! determine the max y value
  // find the max of the arrivals data
  var arrivalMax = d3.max(countryData, d => d.arrivals.total);

  // find the max of the evening data
  var departureMax= d3.max(countryData, d => d.departures.total);

  var yMax;
  if (arrivalMax> departureMax) {
    yMax = arrivalMax;
  }
  else {
    yMax = departureMax;
  }

  // var yMax = arrivalMax> departureMax? arrivalMax: departureMax;

  // Use the yMax value to set the yLinearScale domain
  yLinearScale.domain([0, yMax]);


  // Step 7: Create the axes
  // =================================
  var bottomAxis = d3.axisBottom(xTimeScale).tickFormat(d3.timeFormat("%Y"));
  var leftAxis = d3.axisLeft(yLinearScale);

  // Step 8: Append the axes to the chartGroup
  // ==============================================
  // Add x-axis
  chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

  // Add y-axis
  chartGroup.append("g").call(leftAxis);

  // Step 9: Set up two line generators and append two SVG paths
  // ==============================================

  // Line generator for arrivals data
  var line1 = d3.line()
    .x(d => xTimeScale(year_axis))
    .y(d => yLinearScale(d.arrivals.total));

  // Line generator for evening data
  var line2 = d3.line()
    .x(d => xTimeScale(year_axis))
    .y(d => yLinearScale(d.departures.total));

  // Append a path for line1
  chartGroup
    .append("path")
    .attr("d", line1)
    .classed("line green", true);

  // Append a path for line2
  chartGroup
    .data([countryData])
    .append("path")
    .attr("d", line2)
    .classed("line orange", true);

});