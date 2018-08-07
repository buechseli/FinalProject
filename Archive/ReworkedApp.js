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

  // Step 4: Parse the data
  // Format the data
  // all the countries (there should be 217 countries)
  var country_name=d3.keys(countryData);
 
  //keys for each dictionary in country array (should be 11 keys, per dict)
  var country_keys = d3.keys(countryData[country_name[1]][0]);

  //length of array for each country (should be 20, 1995-2014)
  var country_array = countryData[country_name[1]].length;
  
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

  console.log(countryData)

  var xTimeScale = d3.scaleTime()
    .domain([1995, 2014])
    .range([0, width]);

  var yLinearScale = d3.scaleLinear()
    .domain([0, 1000])
    .range([height, 0]);

  var bottomAxis = d3.axisBottom(xTimeScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  chartGroup.append("g")
    .classed("axis", true)
    .call(leftAxis)
  chartGroup.append("g")
    .classed("axis", true)
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis)


  var drawLine = d3.line()
   .x(d =>   console.log("d"))
   .y(data => yLinearScale(data.arrivals_total))


    for(var country in countryData){
      obj = countryData[country]
      console.log(country);
      console.log(obj);
     
      for(var year_info in obj){
        year_object = obj[year_info]
        //console.log("year_object", year_object)
      }
      
      chartGroup.append("path")
        //.attr("d", drawLine(obj))
        .classed("line green", true)
        .attr("stroke-width", 3)
      
        //console.log(drawLine(obj));
    }
 
});