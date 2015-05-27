scripts = """
"""

icon = "bar chart icon"


content = """


<div class="ui segment">
<h3 style="text-align: center"> Our analysis investigates the factors contributing to road crashes with the aim of informing road safety campaigns and policy. </h3>

</div>

<div class="ui segment">
<h3> Hypothesis 1: "Alcohol related crashes happen more on weekends" </h3>
<br>

<p> <b> Reasons: </b> In Victoria, there is a prevalent drinking culture on weekends. Thus we hypothesise that a higher proportion of alcohol related crashes occur on weekends.
<br><br>
<b>What we found: </b> Using our pivot table generator, we counted the number of crashes involving alcohol and not involving alcohol on different days of the week. We chose a bar chart to visualise the percentage of accidents which occured involving alcohol and not involving alcohol throught the week.

<br>
<div style="" id="container" style="min-width: 310px; height: 400px; margin: 0 auto"></div>
<br>

As you can see in the bar chart, the percentage of crashes which occured without alcohol remained relatively constant throughout the week, peaking slightly around Friday and Thursday with 15.6% and 15.9% of non-alcohol-related crashes occuring on these days. However, crashes with alcohol had far more proportional variation throughout the week, with 24.7% and 22.7% of alcohol-related crashes occuring on Saturday and Sunday.
<br><br>
<b>What this means: </b> It would likely be more cost-effective to target weekends in drink-driving campaigns (Booze Buses, patrols, advertising campaigns etc). Non-alcohol related crashes are more constant, and thus the given analysis gives us no reason to target particular days for non-alcohol-related campaigns.
</p>

</div>

<div class="ui segment">
<h3> Hypothesis 2:"Crashes in faster speed limits are more likely to result in death" </h3>
<br>
<h4> Reasons:</h4> <p>Cars travelling in areas with faster speed limits are naturally more likely to be travelling at a higher speed. It was proposed that crashes that happen at these faster speeds was more likely to result in a death due to the greater forces and more dramatic outcomes of a crash at speed</p>
<h4> What we Found:</h4> <p>There is a linear relationship between the percentage of fatal accidents as a proprotion of the total number of accidents and the speed zone for which it occurs. However this relationship becomes more complicated with faster speeds, suggesting a hyperbolic relationship may provide a better fit for these data</p>
<br>
<div style="" id="container2" style="min-width: 310px; height: 400px; margin: 0 auto"></div>
<br>
<h4> The Chart:</h4><p>Linear regression chart of fatialites / crashes</p>
<h4>What this Means</h4> <p>Although frustating to most drivers, a 20km/hr decrease in the speed limit correlates with less than half the chance of being killed if involved in an accident. This highlights the dangers involved in increasing large sections of freeway to 110km/h. Thus councils should be wary of weighing the risks of very high speed limits on certain roads, and ensure to minimize risks where possible. Further analysis could be performed to investigate which factors are correlated with accidents on roads with high speed limits. </p>

</div>

<div class="ui segment">
<h3> Hypothesis 3: "Motorcycling crashes are more likely to be killed than injured in a crash" </h3>
<br>
<h4> Reasons:</h4><p> Despite recent advances in the technology and safety systems relating to motorcyclists and the increase in complexity of jackets and safety equipment, motorcyclists remain extremely vunerable in accidents in part due to the ease in which they are thrown from their vehicle, massively increasing the forces that act on them </h4> <p> </p>
<h4> What we Found:</h4> <p> Motorcyclists are not any more likely than the drivers of other vehicles to be killed in an accident. They have a clearly elevated chance of being seriously injured (44% of accidents compared to 30% in cars) but even then a little more than 50% only sustained injuries that did not require hospitaliziation</p>
<br>
<div style="" id="container3" style="min-width: 310px; height: 400px; margin: 0 auto"></div>

<h4> The Chart:</h4><p></p>
<h4>What this Means</h4><p>Modern advances in Motorcycle systems have been very successful in reducing fatailities compared to modern cars. This lends weight to dispelling the myth that motorcyclists are more likely to be killed then the average motorist. However, motorcyclists are still more likely to be more seriously injured.</p>

</div>

<div class="ui segment">
<h3> Hypothesis 4: "Rural areas will have more accidents which occur in darkness with no street lights" </h3>
<br>
<h4> Reasons:</h4> <p>We hypothesised that a state such as Victoria with considerable wealth and an interest in road safety would have almost all roads well lit, except in rural areas where low traffic would render this cost-ineffective (very low traffic on roads would mean even if they were lit, far less potential crashes would be avoided by better improved lighting).</p>
<h4> What we Found:</h4> <p> This chart displays rural and non-rural crashes which occured in darkness with no streetlights for seven local councils. These had the seven highest numbers of crashes in unlit conditions- each over 100 crashes. As we can see, in Geelong, Melton, Cardinia, Mitchell and Baw Baw, the number of unlit crashes occured mainly in rural areas. This is what we expected - and it seems to reflect more cost-effective lighting. However, the Yarra Ranges and Casey stand out as having by far more unlit crashes in <i>non-rural</i> areas than rural areas. This was not predicted by our hypothesis.</p>
<h4> The Chart:</h4><p></p>
<div style="" id="container4" style="min-width: 310px; height: 400px; margin: 0 auto"></div>
<h4>What this Means</h4> <p>For most of the areas where unlit crashes are greatest, these crashes occur mostly in rural regions, which reflects cost-effective lighting. However, Casey and the Yarra Ranges both have far more unlit crashes in non-rural areas. This means that local councils could spend more money on lighting these areas to improve safety. To do so would be effective - as there are plenty of crashes - and efficient - as these are non-rural areas.</p>


</div>

<div class="ui segment">
<h3> Hypothesis 5: "Cyclists are more at risk at intersections than other road users" </h3>
<br>
<h4> Reasons:</h4> <p> Cyclists can be hard to see, and this could be amplified by both the vision problems and more complicated manouvers associated with intersections </p>
<h4> What we Found:</h4> <p> Looking at cyclists alone, crashes were reasonably uniformly distributed among different types of road geometry, with roughly two thirds of these being at intersections. However, non-cyclists were involved in proportionally far more crashes at non-intersections. Thus we can see that cyclists are comparatively more at risk of crashes at intersections than other road users. This supports our hypothesis. T Intersections are the most dangerous type of intersection, accounting for 34% and 29.5% of crashes for cyclists and non-cyclists respectively. </p>
<br>
<h4> The Charts:</h4><p></p>

<div id="container5_1" style="width:100%; height:400px;"></div>
         
<div id="container5_2" style="width:100%; height:400px;"></div>

<h4>What this Means</h4> <p> Cyclists should take care at intersections. Road users should be wary of this additional risk, and be wary for cyclists in intersections. Council planners should design intersections with cyclist risk in mind, and government policy or advertising could potentially target this issue to help reduce this risk.  </p>

</div>




"""


from template import generate_html

page_title = "Findings"

scripts = """
<script>
$(document).ready(function() {
$(function () {
    $('#container').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Alcohol-related and non-alcohol-related crashes on days of the week'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            categories: [
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday',
                'Sunday',
            ],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Percent of crashes'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f}%</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: 'No Alcohol',
            data: [13.74788238, 14.31661423, 14.99425218, 15.56298403, 15.85037512, 13.30772023, 11.82538722]



        }, {
            name: 'Alcohol',
            data: [9.313338595, 9.0765588, 9.155485399, 10.37884767, 14.52249408, 24.66456196, 22.6519337]


        }]
    });
});

$(function () {
    $('#container2').highcharts({
        xAxis: {
            min: 3,
            title: {
                text: 'Speed Zone (*10^1)'
                    },
        },
        yAxis: {
            min: 0,
            title: {
                text: '% of Accidents which are Fatal'
                    },
        },
        title: {
            text: 'Fatialites as a fraction of all accidents based on Speed Zones'
        },
        series: [{
            type: 'line',
            name: 'Linear Regression Line',
            data: [[4, 0.5], [12, 4]],
            marker: {
                enabled: false
            },
            states: {
                hover: {
                    lineWidth: 0
                }
            },
            enableMouseTracking: false
        }, {
            type: 'scatter',
            name: 'Data Point',
            data: [
            [4, 0.6],[5, 0.86],[6, 1.01],[7, 1.80],[8, 2.29],[9, 2.79],[10, 5.96],[11, 6.89]
            ],
            marker: {
                radius: 4
            }
        }]
    });
});


$(function () {
    $('#container3').highcharts({
        chart: {
            type: 'area',
            spacingBottom: 30
        },
        title: {
            text: 'Injury Severity against Vehicle Type'
        },
        subtitle: {
            text: '',
            floating: true,
            align: 'right',
            verticalAlign: 'bottom',
            y: 15
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            verticalAlign: 'top',
            x: 150,
            y: 100,
            floating: true,
            borderWidth: 1,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
        },
        xAxis: {
            categories: ['Other Injury (non Hospital)', "Serious Injury (Hospital)", "Fatal ( Death <30days)"]
        },
        yAxis: {
            title: {
                text: 'Number of Accidents (Normalized)'
            },
            labels: {
                formatter: function () {
                    return this.value;
                }
            }
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    this.x + ': ' + this.y + '%';
            }
        },
        plotOptions: {
            area: {
                fillOpacity: 0.5
            }
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Non Motorcylist',
            data: [68, 30, 2]
        }, {
            name: 'Motorcyclists',
            data: [54, 44, 2]
        }]
    });
});

$(function () {

    // Radialize the colors
    Highcharts.getOptions().colors = Highcharts.map(Highcharts.getOptions().colors, function (color) {
        return {
            radialGradient: { cx: 0.5, cy: 0.3, r: 0.7 },
            stops: [
                [0, color],
                [1, Highcharts.Color(color).brighten(-0.3).get('rgb')] // darken
            ]
        };
    });

    // Build the chart
    $('#container5_1').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: 'Non-cyling related crashes by road geometry'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    },
                    connectorColor: 'silver'
                }
            }
        },
        series: [{
            type: 'pie',
            name: 'Non-cyling related crashes by road geometry',
            data: [
                ['Cross Intersection',   9364],
                ['T Intersection',       10588],
                {
                    name: 'Not at Intersection',
                    y: 14954,
                    sliced: true,
                    selected: true
                },
                ['Other',   1040]
            ]
        }]
    });
});


$(function () {
    $('#container5_2').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: 'Cyling related crashes by road geometry'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    },
                    connectorColor: 'silver'
                }
            }
        },
        series: [{
            type: 'pie',
            name: 'Cycling related crashes by road geometry',
            data: [
                ['Cross Intersection',   1554],
                ['T Intersection',       1807],
                {
                    name: 'Not at Intersection',
                    y: 1810,
                    sliced: true,
                    selected: true
                },
                ['Other',   138]
            ]
        }]
    });
});                         
 

                 
$(function () {
    $('#container4').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Crashes occuring in darkness without streetlights by local council'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            categories: ['Geelong', 'Yarra Ranges', 'Melton', 'Cardinia', 'Casey', 'Mitchell', 'Baw Baw'],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Crashes',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ' crashes'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -40,
            y: 100,
            floating: true,
            borderWidth: 1,
            backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
            shadow: true
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Rural areas',
            data: [85,93,79,98,30,102,98]
        }, {
            name: 'Non-rural areas',
            data: [44, 110, 34, 32, 108, 23, 12]

        }]
        
    });
});
                 
});

</script>
"""


generate_html(icon, content, page_title, scripts)