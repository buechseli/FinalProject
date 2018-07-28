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
   console.log(countryData);
   console.log("Total Arrivals :", countryData['ALBANIA'][0]['arrivals_total']);
   console.log("Countries: ", d3.keys(countryData))
  // Step 4: Parse the data

  // Format the data

  //all the countries (there should be 217 countries)
  var country_name=d3.keys(countryData);
  console.log(country_name[1]);
  console.log("Albania Total Arrivals", countryData[country_name[1]][0].arrivals_total);

  //keys for each dictionary in country array (should be 11 keys, per dict)
  var country_keys = d3.keys(countryData[country_name[1]][0]);
  console.log(country_keys);

  //length of array for each country (should be 20, 1995-2014)
  var country_array = countryData[country_name[1]].length;
  console.log(country_array);
  
  //testing for loop
  //for (var i =0; i<country_name.length; i++){
    //console.log("country index"+i);
    //for (var j=0; j<country_array; j++){
      console.log("year index"+j);
      //var total_arrivals_yr_cntry = countryData[country_name[i]][j].arrivals_total;
      //console.log("Country:", country_name[i]);
      //console.log("total arrivals per year :", total_arrivals_yr_cntry);
    //}
  //}  
  
  //actually formatting the data
  for (var i=0; i<country_name.length; i++){
    for(var j=0; j<country_array; j++){
      countryData[country_name[i]][j].arrivals_total = +countryData[country_name[i]][j].arrivals_total;
      countryData[country_name[i]][j].departures_total = +countryData[country_name[i]][j].departures_total;
      countryData[country_name[i]][j].expenditure_in_country = +countryData[country_name[i]][j].expenditure_in_country;
      countryData[country_name[i]][j].expenditure_out_country = +countryData[country_name[i]][j].expenditure_out_country;
      countryData[country_name[i]][j].date = +parseTime(countryData[country_name[i]][j].date);
    }
  }
 
  // Step 5: Create the scales for the chart
  // =================================
  
  //create years_list

  
  for(var j=0; j<country_array; j++){
     var years_list = countryData[country_name[1]][j].date;
     console.log(years_list);
   }
  
  

  var xTimeScale = d3.scaleTime()
    .domain(d3.extent(countryData, d=> d.years))
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