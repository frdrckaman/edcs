$(document).ready(function(){
    
    if($("#chart_activity").length > 0){
        
        var stuff = [], contacts = [];

        for (var i = 0; i < 7; i += 1) {
            stuff.push([i, parseInt(Math.random() * 30)]);
            contacts.push([i, parseInt(Math.random() * 30)]);
        }

        $.plot($("#chart_activity"), [ { data: stuff, label: "stuff"}, { data: contacts, label: "contacts"}], {xaxis: {show: true}, yaxis: { show: true}});
        
    }
    
    if($(".visitsChart-2").length > 0){

        var d1 = [];
        
        for (var i = 1; i <= 30; i += 1)
            d1.push([i, parseInt(Math.random() * 30)]);

        $.plot($(".visitsChart-2"), [ { data: d1 }], {xaxis: {show: true}, yaxis: { show: true}});
    
    }      
    
    
    if($("#chart-1").length > 0){

        /* CHART - 1*/

        var sin1 = [], sin2 = [], cos1 = [], cos2 = [];

        for (var i = 0; i < 14; i += 0.3) {
            sin1.push([i, Math.sin(i)]);
            sin2.push([i, Math.sin(i-1.57)]);
            cos1.push([i, Math.cos(i)]);
            cos2.push([i, Math.cos(i+1.57)]);
        }

        $.plot($("#chart-1"), [ { data: sin1, label: "sin(x)"}, { data: sin2, label: "sin(y)"} , { data: cos1, label: "cos(x)"}, { data: cos2, label: "cos(y)"} ], {
                series: {lines: { show: true }, points: { show: true }},
                grid: { hoverable: true, clickable: true },
                yaxis: { min: -1.1, max: 1.1 }
                });

        /* eof CHART - 1*/
    
    }    

    if($("#chart-2").length > 0){
        

        var d1 = [];
        for (var i = 0; i <= 10; i += 1)
            d1.push([i, parseInt(Math.random() * 30)]);

        var d2 = [];
        for (var i = 0; i <= 10; i += 1)
            d2.push([i, parseInt(Math.random() * 30)]);

        var d3 = [];
        for (var i = 0; i <= 10; i += 1)
            d3.push([i, parseInt(Math.random() * 30)]);

        var stack = 0, bars = true, lines = false, steps = false;


        $.plot($("#chart-2"), [ { data: d1, label: "data 1" }, { data: d2, label: "data 2" }, { data: d3, label: "data 3" } ], {
            series: {
                stack: stack,
                lines: { show: lines, fill: true, steps: steps },
                bars: { show: bars, barWidth: 0.6 }
            }
        });
        
        
    }

    if($("#chart-3").length > 0){
        
        var data = [];
        	        
	for( var i = 0; i < 5; i++)	
		data[i] = { label: "Series"+(i+1), data: Math.floor(Math.random()*100)+1 };
	

        $.plot($("#chart-3"), data, 
	{
            series: {
                pie: { show: true }
            },
            legend: { show: false }
	});

    }

    if($("#chart-4").length > 0){
        
        var data = [], totalPoints = 300;
        
        var updateInterval = 30;

        

        var plot = $.plot($("#chart-4"), [ getRandomData() ], {
            series: { shadowSize: 0 }, 
            yaxis: { min: 0, max: 100 },
            xaxis: { show: false }
        });

        update();
            
    }

    function update() {
        plot.setData([ getRandomData() ]);
        // since the axes don't change, we don't need to call plot.setupGrid()
        plot.draw();

        setTimeout(update, updateInterval);
    }

    function getRandomData() {
        if (data.length > 0)
            data = data.slice(1);

        // do a random walk
        while (data.length < totalPoints) {
            var prev = data.length > 0 ? data[data.length - 1] : 50;
            var y = prev + Math.random() * 10 - 5;
            if (y < 0)
                y = 0;
            if (y > 100)
                y = 100;
            data.push(y);
        }

        // zip the generated y values with the x values
        var res = [];
        for (var i = 0; i < data.length; ++i)
            res.push([i, data[i]])
        return res;
    }

    function showTooltip(x, y, contents) {
        $('<div class="ct">' + contents + '</div>').css( {
            position: 'absolute',
            display: 'none',
            top: y,
            left: x + 10,
            border: '2px solid #333',
            padding: '2px',
            'background-color': '#ffffff',
            'border-radius': '2px',
            color: '#333'            
        }).appendTo("body").fadeIn(200);
    }    

    var previousPoint = null;
    
    $("#chart-1").bind("plothover", function (event, pos, item) {
        
        $("#x").text(pos.x.toFixed(2));
        $("#y").text(pos.y.toFixed(2));

        if (item) {
            if (previousPoint != item.dataIndex) {
                previousPoint = item.dataIndex;

                $(".ct").remove();
                var x = item.datapoint[0].toFixed(2),
                    y = item.datapoint[1].toFixed(2);

                showTooltip(item.pageX, item.pageY,
                            item.series.label + " of " + x + " = " + y);
            }
        }else {
            $(".ct").remove();
            previousPoint = null;            
        }

    });
    
    $('.mChartBar').sparkline('html',{ enableTagOptions: true });
    
    if($("#lineChart").length > 0){       
               
       var lctx = $("#lineChart").get(0).getContext("2d");
       $("#lineChart").attr('width',$("#lineChart").parent('div').width()).attr('height',300);
       
       lineChart = new Chart(lctx).Line({
            labels : ["January","February","March","April","May","June","July"],
            datasets : [
                    {
                            fillColor : "rgba(220,220,220,0.5)",
                            strokeColor : "rgba(220,220,220,1)",
                            pointColor : "rgba(220,220,220,1)",
                            pointStrokeColor : "#fff",
                            data : [65,59,90,81,56,55,40]
                    },
                    {
                            fillColor : "rgba(151,187,205,0.5)",
                            strokeColor : "rgba(151,187,205,1)",
                            pointColor : "rgba(151,187,205,1)",
                            pointStrokeColor : "#fff",
                            data : [28,48,40,19,96,27,100]
                    }
            ]
        });
                
    }

    if($("#barChart").length > 0){       
               
       var bctx = $("#barChart").get(0).getContext("2d");
       $("#barChart").attr('width',$("#barChart").parent('div').width()).attr('height',300);
       
       barChart = new Chart(bctx).Bar({
            labels : ["January","February","March","April","May","June","July"],
            datasets : [
                    {
                            fillColor : "rgba(220,220,220,0.5)",
                            strokeColor : "rgba(220,220,220,1)",
                            data : [65,59,90,81,56,55,40]
                    },
                    {
                            fillColor : "rgba(151,187,205,0.5)",
                            strokeColor : "rgba(151,187,205,1)",
                            data : [28,48,40,19,96,27,100]
                    }
            ]
        });
                
    }

    if($("#pieChart").length > 0){       
               
       var pctx = $("#pieChart").get(0).getContext("2d");
       $("#pieChart").attr('width',$("#pieChart").parent('div').width()).attr('height',300);
       
       barChart = new Chart(pctx).Pie([
                {
                        value: 30,
                        color:"#F38630"
                },
                {
                        value : 50,
                        color : "#E0E4CC"
                },
                {
                        value : 100,
                        color : "#69D2E7"
                }			
        ]);
                
    }

    if($("#radarChart").length > 0){       
               
       var rctx = $("#radarChart").get(0).getContext("2d");
       $("#radarChart").attr('width',$("#radarChart").parent('div').width()).attr('height',300);
       
       radarChart = new Chart(rctx).Radar({
            labels : ["Eating","Drinking","Sleeping","Designing","Coding","Partying","Running"],
            datasets : [
                    {
                            fillColor : "rgba(220,220,220,0.5)",
                            strokeColor : "rgba(220,220,220,1)",
                            pointColor : "rgba(220,220,220,1)",
                            pointStrokeColor : "#fff",
                            data : [65,59,90,81,56,55,40]
                    },
                    {
                            fillColor : "rgba(151,187,205,0.5)",
                            strokeColor : "rgba(151,187,205,1)",
                            pointColor : "rgba(151,187,205,1)",
                            pointStrokeColor : "#fff",
                            data : [28,48,40,19,96,27,100]
                    }
            ]
        });
                
    }
});

