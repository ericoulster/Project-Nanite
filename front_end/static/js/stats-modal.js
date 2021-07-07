const statsModal_Populate = (data) => {
    statsModal_AddBones();
    statsModal_ProgressBar(data);
    statsModal_WordCountStats(data);
    statsModal_AddSidebar(data);
    statsModal_UpdateGraph(data);

    d3.select("#selDataset").on("change", statsModal_UpdateGraph)
    d3.select("numBars").on("change", statsModal_UpdateGraph)

}

/* ==============================================================================================/
 *  ADDING INITIAL HTML (BONES)
 * =============================================================================================/
 */
const statsModal_AddBones = () => {
    document.getElementById("modal-stats-content").innerHTML = `
    <div id="stats-container" style="width: 100%;">
        <div id="stats-longProgressBar"></div>
        <div id="stats-wordRow">
        <div id="stats-avgWC" class="wcDiv"></div>
        <div id="stats-highestWC" class="wcDiv"></div>
        </div>
        <div id="stats-body">
        <!--STATS BAR CHART START!!-->
        <div id="stats-barChart">
            <div id="userInputRow">
            <select id="selDataset">
                <option value="Daily">Daily</option>
                <option value="Weekly">Weekly</option>
                <option value="Monthly">Monthly</option>
            </select>
        
            <!--Have a div here so that justify-content will slap it onto the right side of the screen-->
            <div class="numBarsContainer Archivo">
                <p>
                Past 
                <input type="text" id="numBars" pattern="[0-9]+" size=1 placeholder=7 />
                <span id="currMeasurement">Measurement</span>
                </p>
            </div>
            </div>
        
            <!--Graph's outside the userInputRow-->
            <div id="wordcounter"></div>          
        </div>
        <!--STATS SIDE BAR START!!! -->
        <div id="stats-sideBar">
            <div id="stats-deadline"></div>
            <div id="stats-currStreak"></div>
            <div id="stats-mostActive"></div>
        </div>
        </div>
    </div>
    `;
}

  /* ================================================================================================/
   *   WORDCOUNT ROW STUFF
   * ===============================================================================================/
   **/
const statsModal_WordCountStats = (data) => {
    let toAdd_avgWC = data.mean_wc ? Math.round(data.mean_wc, 1) : "N/A"
    document.getElementById("stats-avgWC").innerHTML = `<p>Avg daily word count: <span class="emph">${toAdd_avgWC}</span></p>`;

    let toAdd_highWC = data.max_wc ? data.max_wc : "N/A"
    document.getElementById("stats-highestWC").innerHTML = `<p>Highest daily word count: <span class="emph">${toAdd_highWC}</span></p>`;
}
/* ================================================================================================/
   *   PROGRESS BAR STUFF
   * ===============================================================================================/
   **/
const statsModal_ProgressBar = (data) => {

    var barWidth = parseInt(window.getComputedStyle(document.getElementById("stats-container")).width.slice(0, -2) * 1.5);
    // console.log(window.getComputedStyle(document.getElementById("stats-container")).width)
    // console.log(data.current_wc)
    // console.log(barWidth)
    var progress_val = (data.current_wc / data.word_goal_and_deadline.wordgoal)*100;

    if (progress_val < 25) {
        progress_color = "#D0D0D0"
    }
    else if (progress_val < 50) {
        progress_color = "#F6B85C"
    }
    else if (progress_val < 75) {
        progress_color = "#F6D55C"
    }
    else if (progress_val < 100) {
        progress_color = "#CEF65C"
    }
    else if (progress_val < 115) {
        progress_color = "#96F65C"
    }
    else if (progress_val < 200) {
        progress_color = "#5CF6D1"
    }
    else {
        progress_color = "#5CBFF6"
    };

    if (progress_val > 100) {
        progress_val_capped = 100
    }
    else {progress_val_capped = progress_val};

    var svg = d3.select('#stats-longProgressBar')
        .append('svg')
        .attr('height', 57)
        .attr('width', barWidth);

    var bar_width = barWidth * .9;

    var bar_height = 15;


    var bar_x = (bar_width/50);
    var bar_y = (bar_height/3);

    var bar_cap = (bar_width/100);

    if (progress_val < 50) {
        var text_color ='#E3E3E3'
    }
    else {
        var text_color = '#1F2428'}

    svg.append('rect')
        .attr('class', 'bg-rect')
        .attr('rx', 20)
        .attr('ry', 20)
        .attr('fill', 'none')
        // .attr('stroke', '#333A40')
        .attr('stroke', '#22262a')
        .attr('stroke-width', 4)
        .attr('height', bar_height + (bar_height*.9))
        .attr('width', function(){
            return bar_width + (bar_width*0.04);
        })
        .attr('x', bar_x)
        .attr('y', bar_y);




    var progress = svg.append('rect')
                    .attr('class', 'progress-rect')
                    .attr('fill', progress_color)
                    .attr('height', bar_height)
                    .attr('width', 0)
                    .attr('rx', 10)
                    .attr('ry', 10)
                    .attr('x', bar_x + (bar_x*.65))
                    .attr('y', bar_y + (bar_y*1.40));

    progress.transition()
        .duration(1000)
        .attr('width', function(){
            var index = progress_val_capped;
            return index * bar_cap;
        });

    svg.append("text")
        .text(`${data.current_wc}/${data.word_goal_and_deadline.wordgoal} words (${Math.floor(progress_val)}%)`)
        .attr('x', bar_width/2 -50)
        .attr('y', bar_height*1.5)
        .attr('fill', '#333A40')
        .attr('font-family', 'Archivo')
        .attr('font-weight', 200)
        .attr('font-size', '12px')
        .style('fill', text_color)
        .raise()
}

/* ================================================================================================/
   *   MISC SIDELINE STUFF
   * ===============================================================================================/
   **/
const statsModal_AddSidebar = (data) => {
    document.getElementById("stats-deadline").innerHTML = `<p>Current Deadline <br/> <span class="emph">${data.word_goal_and_deadline.deadline}</span></p>`;
    document.getElementById("stats-currStreak").innerHTML = `<p>Current Streak <br/> <span class="emph">${data.current_streak ? data.current_streak : "none"}</span></p>`;
    var sidebarWidth = parseInt(window.getComputedStyle(document.querySelector("#stats-sideBar")).width.slice(0, -2)) * .95;
    var weekData = data.weekBar.weekmeans
    var maxday = data.weekBar.maxday

    // set the dimensions and margins of the graph
    //  var margin = {top: 30, right: 30, bottom: 70, left: 60},
    //       width = sidebarWidth - margin.left - margin.right,
    //       height = (sidebarWidth * .5) - margin.top - margin.bottom;
    var margin = {top: (sidebarWidth * .5), right: (sidebarWidth * .1), bottom: (sidebarWidth * .5), left: (sidebarWidth * .1)},
        width = sidebarWidth,
        height = (sidebarWidth * .5)

    // append the svg object to the body of the page
    var weekSvg = d3.select("#stats-mostActive")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    var x = d3.scaleBand()
    .range([ 0, width ])
    .domain(weekData.map(function(d) { return d.Day; }))
    .padding(0.44);

    weekSvg.append("g")
    .attr("transform", "translate(0," + (height+10) + ")")
    .call(d3.axisBottom(x).tickSize(0))
    .call(g => g.select(".domain").remove())
    .selectAll("text")
    .attr('font-family', 'Archivo')
            .attr('font-weight', 100)
            .attr('font-size', '6px')
            .style("text-anchor", "middle")
            .style('fill', "#E3E3E3");


    // max of Y axis
    var maxY = d3.max(weekData, (d) => {return +d.Wcount})

    //"#F6D55C"
    
    // Y axis
    var y = d3.scaleLinear()
    .domain([0, maxY])
    .range([ height, 0]);

    var bar = weekSvg.selectAll("bar")
    .data(weekData)
    .enter()
    .append("rect")
    .attr("x", function(d) { return x(d.Day); })
    .attr("y", function(d) { return y(d.Wcount); })
    .attr("width", x.bandwidth())
    .attr("height", function(d) { return height - y(d.Wcount); })
    .attr("ry", 8)
    .attr("fill", function(d) {if (d.IsMax === false) {return "#1F2428"} else {return "#F6D55C"}}
    
    );

    weekSvg.append("text")
        .attr("x", (width / 2))             
        .attr("y", 0 - (margin.top / 2))
        .attr("text-anchor", "middle")  
        .attr('font-family', 'Archivo')
        .attr('font-size', '12px')
        .style('fill', "#E3E3E3")
        // .text("You are most active on:" + maxday)
        .text("Most Active: " + maxday);
}

/* ================================================================================================/
 *   WORD COUNT BAR CHART STUFF
 * ===============================================================================================/
 **/

const statsModal_UpdateGraph = (data) => {
    var sel_userInputRow = document.getElementById("userInputRow");
    var sel_numBars = document.getElementById("numBars");
    var barWidth = parseInt(window.getComputedStyle(document.querySelector("#stats-barChart")).width.slice(0, -2));
    // d3.selectAll("wcsvg").remove();
    document.getElementById("wordcounter").innerHTML = "";

    var dropdownMenu = d3.select("#selDataset");
    var granularity = dropdownMenu.property("value");
    var barData, time_name, numBars;

    // Originally takes in numbars value as string
    var rawNumBars = parseInt(sel_numBars.value);
    var numBars; 
    // Making sure user actually did type in a uint
    // Numbars is negative so that (later) the slice will nab the most recent
    if (!isNaN(rawNumBars) && rawNumBars > 0){
        numBars = rawNumBars * -1;
    } else{
        // Sets the default based on what the granularity is
        // Once again, we're using negatives so the slice will nab the most recent
        switch (granularity) {
        case "Daily":
            numBars = -7;
            break;
        case "Weekly":
            numBars = -3;
            break;
        case "Daily":
            numBars = -3;
            break;
        default:
            numBars = -7;
        } 
    }

    if (granularity === 'Daily') {
        barData = data.barData.daily;
        time_name = "Day";
    }
    else if (granularity === 'Weekly') {
        barData = data.barData.weekly;
        time_name = "Week";
    }
    else if (granularity === 'Monthly') {
        barData = data.barData.monthly;
        time_name = "Month";
    }
    else {
        barData = data.barData.daily;
        time_name = "Day;"
    };

    // Actually slicing the data based on user's numBar input
    // First ensuring that the user doesn't break things by inputting a higher numBars
    //   than there is data available for Day / Week / Month.
    // If they input a number that's higher than the available data, we just set it to
    //   the max amount of data available.
    if ((barData.length * -1) > numBars){
        numBars = (barData.length * -1);
    } 
    barData = barData.slice(numBars)

    // Adds the currently selected measurement to the numBars selection input line
    document.getElementById("currMeasurement").innerText = time_name + "s";

    // console.log("===============================");
    // console.log(`Current numBars: ${numBars}`);
    // console.log(`Current TypeOf: ${typeof numBars}`);
    // console.log(`Current granularity: ${granularity}`);


    // set the dimensions and margins of the graph
    // var margin = {top: 30, right: 30, bottom: 70, left: 60},
    //     width = barWidth - margin.left - margin.right,
    //     height = (barWidth * .67) - margin.top - margin.bottom;
    var margin = {top: barWidth * .1, right: barWidth * .05, bottom: barWidth * .2, left: barWidth * .15},
        width = barWidth - margin.left - margin.right,
        height = (barWidth * .67) - margin.top - margin.bottom;
    
    // setting the width and padding of the userInputDiv to match the graph
    sel_userInputRow.style.width = width + margin.left - margin.right; // ㅎㅎㅎ
    sel_userInputRow.style.paddingLeft = margin.right;

    // append the svg object to the body of the page
    var wcsvg = d3.select("#wordcounter")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");

  // The data (which will be separated into another file later on)

  // The current number of values
  var data_length = barData.length;

    // if data_range > data_length then data_range = data_length
    // else data_range = input for html element

    //var data_range = 

    // X axis
  var x = d3.scaleBand()
    .range([ 0, width ])
    .domain(barData.map(function(d) { return d.Wdate; }))
    .padding(0.3);
  
    wcsvg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).tickSize(0))
    .selectAll("text")
      .attr("transform", "translate(-10,0)rotate(-45)")
      .attr('font-family', 'Archivo')
            .attr('font-weight', 100)
            .attr('font-size', '10px')
            .style("text-anchor", "end")
            .style('fill', "#E3E3E3");


  // max of Y axis
  var maxY = d3.max(barData, (wordplot) => {
      if (wordplot.Wcount > wordplot.Wtarget) {
          return wordplot.Wcount;
      }
      else {
          return wordplot.Wtarget;
      }
    });

    
  // Y axis
  var y = d3.scaleLinear()
    .domain([0, maxY])
    .range([ height, 0]);
  
    wcsvg.append("g")
    .call(d3.axisLeft(y).tickSize(0))
    .attr('font-family', 'Archivo')
    .selectAll("text")
      .style('fill', "#E3E3E3").attr('font-size', '10px');

  // add the Y gridlines
  wcsvg.append("g")			
      .attr("class", "grid")
      .call(d3.axisLeft(y)
          .tickSize(-width)
          .tickFormat("")
          .ticks(6)
      );
      
  // Bars
    var bar = wcsvg.selectAll("bar")
        .data(barData)
        .enter()
        .append("rect")
        .attr("x", function(d) { return x(d.Wdate); })
        .attr("y", function(d) { return y(d.Wcount); })
        .attr("width", x.bandwidth())
        .attr("height", function(d) { return height - y(d.Wcount); })
        .attr("ry", 2)
        .attr("fill", "#F6D55C");

    // Line
    wcsvg.append("path")
        .datum(barData)
        .attr("fill", "none")
        .attr("stroke", "#474F56")
        .attr("stroke-width", 2)
        .attr("d", d3.line()
            .x(function(d) { return x(d.Wdate) + (x.bandwidth()/2)}) //Need a better system for this
            .y(function(d) { return y(d.Wtarget) })
        );


    // Line-bubbles
    wcsvg.selectAll("circles")
        .data(barData)
        .enter()
        .append("circle")
        .attr("stroke-width", 2)
        .attr("cx", function(d) { return x(d.Wdate) + (x.bandwidth()/2)})
        .attr("cy", function(d) { return y(d.Wtarget) })
        .attr("fill", "#F6D55C")
        .attr("stroke", "#474F56")
        .attr("r", 4);

    wcsvg.append("text")         // Add the Y Axis
    .attr("x", (width / 2))             
    .attr("y", 0 - (margin.top / 2))
    .attr("text-anchor", "middle")  
    .style("font-size", "13px") 
    .attr('font-family', 'Archivo') 
    .style("fill", "#E3E3E3")
    .text(`Wordcount Per ${time_name}`);

    //Erasing previous values when new ones pop up
    wcsvg.selectAll("g").select(".domain").remove();
}