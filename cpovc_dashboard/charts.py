import pandas as pd
from .parameters import colors


def combo_chart(request, params, data):
    """Method to get timeline."""
    try:
        print('COMBO', params, data)
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            zoomType: 'xy'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        xAxis: [{
                            categories: {categories},
                            crosshair: true
                        }],
                        yAxis: [{ // Secondary yAxis
                            title: {
                                text: '# of OVC',
                                style: {
                                    color: Highcharts.getOptions().colors[1]
                                }
                            },
                            labels: {
                                format: '{value}',
                                style: {
                                    color: Highcharts.getOptions().colors[1]
                                }
                            }
                        }],
                        tooltip: {
                            shared: true
                        },
                        plotOptions: {
                            column: {
                                stacking: 'normal',
                                colors: {colors},
                                dataLabels: {
                                    enabled: true
                                }
                            },
                            spline:{
                               colors: {colors}
                            }
                        },
                        legend: {
                               backgroundColor:
                                Highcharts.defaultOptions.legend.backgroundColor || // theme
                                'rgba(255,255,255,0.25)'
                        },
                        credits: {
                            enabled: true
                        },
                        series: [{
                            name: '# of OVC',
                            type: 'column',
                            data: [{mdata}],
                            tooltip: {
                                valueSuffix: ''
                            },

                        }]
                    });
                });
            </script>'''
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else colors[1]
        if not params['has_sex']:
            ucolors = colors[sel_color + 10] if sel_color else colors[11]
        if params['colors']:
            ucolors = params['colors']
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
    except Exception as e:
        print('error with combo data - %s' % (str(e)))
        raise e
    else:
        return result


def bar_chart(request, params, data):
    """Method to get bar chart."""
    try:
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'bar'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        xAxis: {
                            categories: {categories},
                            title: {
                                text: null
                            },
                            labels: {
                                useHTML:true, step: 1
                            }
                        },
                        yAxis: {
                            min: 0,
                            title: {
                                text: '{yLabel}'
                            },
                            labels: {
                                overflow: 'justify'
                            }
                        },
                        tooltip: {
                            valueSuffix: ''
                        },
                        plotOptions: {
                            series: {
                              dataSorting: {
                                enabled: true,
                                sortKey: 'y',
                              }
                            },
                            bar: {
                                dataLabels: {
                                    enabled: true
                                },
                                pointWidth: 15
                            }
                        },
                        legend: {
                            enabled: false
                        },
                        credits: {
                            enabled: true
                        },
                        dataLabels: {
                            enabled: true,
                            format: function() {
                                var pcnt = (this.y / this.series.data.map(p => p.y).reduce((a, b) => a + b, 0)) * 100;
                                return Highcharts.numberFormat(pcnt, 0, '', ',') + '%';
                            }
                        },
                        colors: {colors},
                        series: [{                        
                            name: '{yLabel}',
                            data: [{mdata}]
                        }]
                    });
                 });
            </script>'''
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else colors[1]
        if not params['has_sex']:
            ucolors = colors[sel_color + 10] if sel_color else colors[11]
        if params['colors']:
            ucolors = params['colors']
        # Labels
        yLabel = params['yLabel'] if params['yLabel'] else '# of OVC'
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{yLabel}', yLabel)
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
    except Exception as e:
        print('error with kpi data - %s' % (str(e)))
        raise e
    else:
        return result


def bar_chart_stacked(request, params, data):
    """Method to get bar chart."""
    try:
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    var colors = ["#377eb8", "#984ea3", "#7cb5ec", "#e41a1c", "#434348", "#E80C7A", "#E80C7A"];
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'bar'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'right'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        xAxis: {
                            categories: {categories},
                            title: {
                                text: null
                            }
                        },
                        yAxis: {
                            min: 0,
                            title: {
                                text: '# of Beneficiaries / HH',
                                align: 'high'
                            },
                            labels: {
                                overflow: 'justify'
                            }
                        },
                        tooltip: {
                            valueSuffix: ' millions'
                        },
                        plotOptions: {
                            bar: {
                                dataLabels: {
                                    enabled: true
                                },
                                pointWidth: 20,
                                pointPadding: 0,
                                groupPadding: 0.01
                            }
                        },
                        legend: {
                            layout: 'vertical',
                            align: 'right',
                            verticalAlign: 'top',
                            x: -40,
                            y: 80,
                            floating: true,
                            borderWidth: 1,
                            backgroundColor:
                                Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
                            shadow: true
                        },
                        credits: {
                            enabled: true
                        },
                        dataLabels: {
                            enabled: true,
                            format: function() {
                                var pcnt = (this.y / this.series.data.map(p => p.y).reduce((a, b) => a + b, 0)) * 100;
                                return Highcharts.numberFormat(pcnt, 0, '', ',') + '%';
                            }
                        },
                        colors: colors,
                        series: [{
                            name: 'Male',
                            data: [{mdata}]
                        }, {
                            name: 'Female',
                            data: [{fdata}]
                        }]
                    });
                 });
            </script>'''
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
    except Exception as e:
        print('error with kpi data - %s' % (str(e)))
        raise e
    else:
        return result


def column_chart(request, params, data):
    """Method to get bar chart."""
    try:
        categories = str(data['items'])
        items = data['items']
        html = '''
                <script>
                $(document).ready(function() {
                    var colors = {colors};
                    var buttons = Highcharts.getOptions().exporting.buttons.contextButton.menuItems.slice();
                    buttons.push('separator');
                    buttons.push({
                        text: 'Generate SQL',
                        onclick: function () {
                            this.exportChart({
                                width: 250
                            });
                        }
                    });
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'column'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        xAxis: {
                            categories: {categories},
                            title: {
                                text: null
                            }
                        },
                        yAxis: {
                            min: 0,
                            title: {
                                text: '{yLabel}'
                            },
                            stackLabels: {
                                enabled: {slabels},
                                style: {
                                    fontWeight: 'bold',
                                    color: ( // theme
                                        Highcharts.defaultOptions.title.style &&
                                        Highcharts.defaultOptions.title.style.color
                                    ) || 'gray'
                                }
                            }
                        },
                        tooltip: {
                            headerFormat: '<b>{point.x}</b><br/>',
                            pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
                        },
                        plotOptions: {
                            column: {
                                stacking: 'normal',
                                colorByPoint: {colorp},
                                dataLabels: {
                                    enabled: true,
                                    formatter: function() {
                                        return Highcharts.numberFormat(this.y, 0, '', ',') {xtras};
                                    }
                                }
                            }
                        },
                        exporting: {
                          buttons: {
                                contextButton: {
                                    menuItems: buttons
                                }
                            },
                          allowHTML: true,
                          showTable: false
                        },
                        credits: {
                            enabled: true
                        },
                        colors: colors,
                        legend: { enabled: {legend} },
                        series: [{series}]
                    });
                 });
            </script>'''
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else colors[1]
        # Labels
        yLabel = '# of OVC'
        if params['yLabel']:
            yLabel = params['yLabel']
        if not params['has_sex']:
            # del ucolors[0:2]
            ucolors = colors[sel_color + 10] if sel_color else colors[11]
        if params['xAxis']:
            series = "{name: 'Male', data: [{mdata}] }, { name: 'Female', data: [{fdata}] }"
            xtras = "+ '<br/>' + Highcharts.numberFormat(this.percentage, 0, '', ',') + '%'"
            slabels = 'true'
        else:
            series = "{name: '" + yLabel + "', data: [{mdata}] }"
            xtras = ""
            slabels = 'false'
        # Colours
        if params['colors']:
            ucolors = params['colors']
        # Remove the other colors
        ucolors = get_colors(ucolors, params, data)
        legend = 'true' if params['legend'] else 'false'
        colorp = 'false' if params['legend'] else 'true'
        #
        result = str(html).replace('{series}', series)
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{legend}', legend)
        result = result.replace('{yLabel}', yLabel)
        result = result.replace('{colorp}', colorp)
        result = result.replace('{xtras}', xtras)
        result = result.replace('{slabels}', slabels)
        result = result.replace('{mdata}', data['mdata'])
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
    except Exception as e:
        print('error with column chart - %s' % (str(e)))
        raise e
    else:
        return result


def column_chart_2(request, params, data):
    """Method to get bar chart."""
    try:
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'column'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        xAxis: {
                            categories: {categories},
                            title: {
                                text: null
                            }
                        },
                        yAxis: {
                            min: 0,
                            title: {
                                text: '# of OVC'
                            },
                            stackLabels: {
                                enabled: {slabels},
                                style: {
                                    fontWeight: 'bold',
                                    color: ( // theme
                                        Highcharts.defaultOptions.title.style &&
                                        Highcharts.defaultOptions.title.style.color
                                    ) || 'gray'
                                }
                            }
                        },
                        tooltip: {
                            headerFormat: '<b>{point.x}</b><br/>',
                            pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
                        },
                        plotOptions: {
                            series: {
                              dataSorting: {
                                enabled: true,
                                sortKey: 'y',
                              }
                            },
                            column: {
                                stacking: 'normal',
                                colors: {colors},
                                colorByPoint: 'true',
                                dataLabels: {
                                    enabled: true,
                                    formatter: function() {
                                        return Highcharts.numberFormat(this.y, 0, '', ',');
                                    }
                                }
                            }
                        },
                        credits: {
                            enabled: true
                        },
                        legend: { enabled: {legend} },
                        series: [{series}]
                    });
                 });
            </script>'''
        if params['xAxis']:
            series = "{name: 'Male', data: [{mdata}] }, { name: 'Female', data: [{fdata}] }"
            slabels = 'true'
        else:
            series = "{name: '# OVC / HH', data: [{mdata}] }"
            slabels = 'false'
        # Color management
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else colors[1]
        if not params['has_sex']:
            ucolors = colors[sel_color + 10] if sel_color else colors[11]
        # Colours
        if params['colors']:
            ucolors = params['colors']
        # Remove the other colors
        ucolors = get_colors(ucolors, params, data)
        legend = 'true' if params['legend'] else 'false'
        result = str(html).replace('{series}', series)
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{legend}', legend)
        result = result.replace('{slabels}', slabels)
        result = result.replace('{mdata}', data['mdata'])
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
    except Exception as e:
        print('error with column chart - %s' % (str(e)))
        raise e
    else:
        return result


def column_pie_chart(request, params, data):
    """Method to get bar chart."""
    try:
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    var colors = ["#377eb8", "#984ea3", "#7cb5ec", "#e41a1c", "#434348", "#E80C7A", "#E80C7A"];
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'column'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        xAxis: {
                            categories: {categories}
                        },
                        yAxis: {
                            min: 0,
                            title: {
                                text: '# of OVC'
                            },
                            stackLabels: {
                                enabled: true,
                                style: {
                                    fontWeight: 'bold',
                                    color: ( // theme
                                        Highcharts.defaultOptions.title.style &&
                                        Highcharts.defaultOptions.title.style.color
                                    ) || 'gray'
                                }
                            }
                        },
                        tooltip: {
                            headerFormat: '<b>{point.x}</b><br/>',
                            pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
                        },
                        plotOptions: {
                            column: {
                                stacking: 'normal',
                                dataLabels: {
                                    enabled: true
                                }
                            }
                        },
                        credits: {
                            enabled: true
                        },
                        colors: colors,
                        series: [{
                            name: 'Male',
                            type: 'column',
                            data: [{mdata}]
                        }, {
                            name: 'Female',
                            type: 'column',
                            data: [{fdata}]
                        },{
                            type: 'pie',
                            name: 'OVC_HIVSTAT',
                            data: [{
                                name: '+Ve',
                                y: 13,
                                color: Highcharts.getOptions().colors[0]
                            }, {
                                name: '-Ve',
                                y: 23,
                                color: Highcharts.getOptions().colors[1]
                            }],
                            center: [100, 80],
                            size: 100,
                            showInLegend: false,
                            dataLabels: {
                                enabled: false
                            }
                        }]
                    });
                 });
            </script>'''
        result = str(html).replace(',{mdata}', data['mdata'])
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
    except Exception as e:
        print('error with column chart - %s' % (str(e)))
        raise e
    else:
        return result


def population_pyramid_chart(request, params, data):
    """Method to get bar chart."""
    try:
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    var colors = {colors};
                    Highcharts.chart("container-{cont}", {
                        chart: {
                            type: "bar",
                            events: {
                              load: function() {
                                const chart = this,
                                  points = chart.series[0].data,
                                  options = {
                                    dataLabels: {
                                      inside: false,
                                      style: {
                                        color: 'black'
                                      }
                                    }
                                  };

                                points.forEach(function(point) {
                                  if (point.shapeArgs.height < 30) {
                                    point.update(options, false);
                                  }
                                });

                                chart.redraw();
                              }
                            }
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'right'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        accessibility: {
                            point: {
                                valueDescriptionFormat: "{index}. OVC {xDescription}, {value}%."
                            }
                        },
                        xAxis: [
                            {
                                categories: {categories},
                                reversed: false,
                                accessibility: {
                                    description: "OVC (male)"
                                }
                            }
                        ],
                        yAxis: [{
                            title: {
                                text: null
                            },
                            accessibility: {
                                description: "Percentage population",
                                rangeDescription: "Range: 0 to 5%"
                            },
                            width: '50%',
                            reversed: true,
                            max:{yMax}
                        }, {
                            title: {
                                text: null
                            },
                            accessibility: {
                                description: "Percentage population",
                                rangeDescription: "Range: 0 to 5%"
                            },
                            offset: 0,
                            left: '50%',
                            width: '45%',
                            max:{yMax}
                        }],
                        plotOptions: {
                            series: {
                                stacking: "normal",
                                groupPadding: 0,
                                pointPadding: 0,
                                dataLabels: {
                                    enabled: true,
                                    inside: true,
                                    formatter: function() {
                                        return Highcharts.numberFormat(this.y, 0, '', ',');
                                    }
                                }
                            },
                            labels: {
                                formatter: function () {
                                    return this.value;
                                }
                            }
                        },
                        tooltip: {
                            headerFormat: '<b>{series.name}, {point.key}</b><br>',
                            pointFormat: 'OVC: {point.y:.0f}'
                        },
                        colors: colors,
                        series: [
                            {
                                name: "Male",
                                data: [{mdata}]
                            },
                            {
                                name: "Female",
                                data: [{fdata}],
                                yAxis: 1
                            }
                        ]
                    });
                });
            </script>'''
        yMax = 0
        for yVal in data['mdata'].split(','):
            if int(yVal) > yMax:
                yMax = int(yVal)
        for yfVal in data['fdata'].split(','):
            if int(yfVal) > yMax:
                yMax = int(yfVal)
        yPadd = 1000 if yMax > 1000 else 100
        yMax = yMax + yPadd
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else colors[1]
        if not params['has_sex']:
            # del ucolors[0:2]
            ucolors = colors[sel_color + 10] if sel_color else colors[11]
        if params['colors']:
            ucolors = params['colors']
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
        result = result.replace('{yMax}', str(yMax))
    except Exception as e:
        print('error with column chart - %s' % (str(e)))
        raise e
    else:
        return result


def sparkline_chart(request, params, data):
    """Method to get bar chart."""
    try:
        categories = str(data['items'])
        # print('sparkline', data)
        html = '''
                <h4>{title}</h4><br>
                <div id="result"></div>
                <table id="table-sparkline" class="table">
                <thead>
                    <tr>
                        <th>{col1}</th>
                        <th>{col2}</th>
                        <th># of OVC</th>
                        <th>{yLabel}</th>
                    </tr>
                </thead>
                <tbody id="tbody-sparkline">
                    {tables}
                </tbody>
            </table>
            <div id="slegend"><ul style="list-style: none;">{slegend}</ul></div>
        <script>
        var colors = {colors};
        Highcharts.SparkLine = function (a, b, c) {
          var hasRenderToArg = typeof a === 'string' || a.nodeName,
              options = arguments[hasRenderToArg ? 1 : 0],
              defaultOptions = {
                chart: {
                  renderTo: (options.chart && options.chart.renderTo) || this,
                  backgroundColor: null,
                  borderWidth: 0,
                  type: 'bar',
                  margin: [2, 0, 2, 0],
                  width: 280,
                  height: 50,
                  style: {
                    overflow: 'visible'
                  },

                  // small optimalization, saves 1-2 ms each sparkline
                  skipClone: true
                },
                title: {
                  text: ''
                },
                credits: {
                  enabled: false
                },
                dataLabels: {
                    enabled: true,
                    format: function() {
                        var pcnt = (this.y / this.series.data.map(p => p.y).reduce((a, b) => a + b, 0)) * 100;
                        return Highcharts.numberFormat(pcnt, 0, '', ',') + '%';
                    }
                },
                exporting: {
                  enabled: false
                },
                xAxis: {
                  labels: {
                    enabled: true
                  },
                  title: {
                    text: null
                  },
                  startOnTick: false,
                  endOnTick: false,
                  tickPositions: []
                },
                yAxis: {
                  endOnTick: false,
                  startOnTick: false,
                  reversedStacks: false,
                  labels: {
                    enabled: true
                  },
                  title: {
                    text: null
                  },
                  tickPositions: [0]
                },
                legend: {
                  enabled: false
                },
                tooltip: {
                  hideDelay: 0,
                  outside: true,
                  shared: true,
                  pointFormat: '<span>{point.y:.f}</span>'
                },
                colors: colors,
                plotOptions: {
                  series: {
                    stacking: 'normal',
                    dataLabels: { enabled: false },
                    animation: false,
                    lineWidth: 4,
                    shadow: false,
                    states: {
                      hover: {
                        lineWidth: 1
                      }
                    },
                    marker: {
                      radius: 1,
                      states: {
                        hover: {
                          radius: 2
                        }
                      }
                    },
                    fillOpacity: 0.25
                  },
                  column: {
                    negativeColor: '#910000',
                    borderColor: 'silver'
                  }
                }
              };

          options = Highcharts.merge(defaultOptions, options);

          return hasRenderToArg ?
            new Highcharts.Chart(a, options, c) :
          new Highcharts.Chart(options, b);
        };

        var start = +new Date(),
            $tds = $('td[data-sparkline]'),
            fullLen = $tds.length,
            n = 0;

        // Creating 153 sparkline charts is quite fast in modern browsers, but IE8 and mobile
        // can take some seconds, so we split the input into chunks and apply them in timeouts
        // in order avoid locking up the browser process and allow interaction.
        function doChunk() {
          var time = +new Date(),
              i,
              j,
              len = $tds.length,
              $td,
              stringdata,
              arr,
              series,
              chart;
          console.log(series);

          for (i = 0; i < len; i += 1) {
            $td = $($tds[i]);
            stringdata = $td.data('sparkline');
            arr = stringdata.split('; ');
            series = [];
            for(j = 0; j < arr.length; j++) {
              series.push({
                data: $.map(arr[j].split(', '), parseFloat),
                pointStart: 1
              });
            }


            chart = {};

            $td.highcharts('SparkLine', {
              series: series,
              categories: ['ECDE', 'Primary', 'Secondary', 'Tertiary', 'University'],
              tooltip: {
                headerFormat: '<span style="font-size: 10px">' + $td.parent().find('td.ttt').html() + ':</span><br/>',
                pointFormat: '<b>{series.name}:</b>{point.y:.f} '
              },
              chart: chart
            });

            n += 1;

            // If the process takes too much time, run a timeout to allow interaction with the browser
            if (new Date() - time > 500) {
              $tds.splice(0, i + 1);
              setTimeout(doChunk, 0);
              break;
            }

            // Print a feedback on the performance
            if (n === fullLen) {
              $('#result').html('Generated ' + fullLen + ' sparklines in ' + (new Date() - start) + ' ms');
            }
          }
        }
        doChunk();
        </script>
        '''
        tbls = ''
        ags = {}
        ips = []
        dips = []
        dips_dict = {}
        dpps_dict = {}
        tbl0 = '<tr><td %s>%s</td><td class="ttt">%s</td>'
        tbl0 += '<td>%s</td><td data-sparkline="%s "/></tr>\n'
        tbl = '<tr><td class="ttt">%s</td>'
        tbl += '<td valign="right">%s</td><td data-sparkline="%s "/></tr>\n'
        for dt in data['raw']:
            itm = dt['agency']
            dtm = dt['mechanism']
            dts = dt['schoollevel']
            dct = dt['dcount']
            if dts not in dips:
                dips.append(dts)
            if dtm not in ips:
                ips.append(dtm)
                dips_dict[dtm] = [{dts: dct}]
                dpps_dict[dtm] = dct
                if itm not in ags:
                    ags[itm] = {'count': 1, 'items': [{dtm: dct}]}
                else:
                    ags[itm]['count'] += 1
                    ags[itm]['items'].append({dtm: dct})
            else:
                dips_dict[dtm].append({dts: dct})
                dpps_dict[dtm] = dpps_dict[dtm] + dct
        fdips_dict = {}
        for dps in dips_dict:
            dpsds = dips_dict[dps]
            if dps not in fdips_dict:
                fdips_dict[dps] = []
            for dpsd in dpsds:
                for dip in dips:
                    if dip in dpsd:
                        dpd = dpsd[dip]
                        fdips_dict[dps].append(str(dpd))
        print('NTN', fdips_dict)
        for ag in ags:
            cnt = 0
            print('AG', ag, ags[ag])
            rsp = ags[ag]['count']
            for itms in ags[ag]['items']:
                cnt += 1
                for itm in itms:
                    rdtm = fdips_dict[itm]
                    dcnt_f = dpps_dict[itm] if itm in dpps_dict else 0
                    dcnt = '{:,.0f}'.format(dcnt_f)
                    if params['cont'] == '3I':
                        dtm = '  '.join(rdtm)
                    else:
                        dtm = ' ; '.join(rdtm)
                    tb0 = 'rowspan="%s"' % rsp if cnt == 1 else ''
                    if cnt == 1:
                        tbls += tbl0 % (tb0, ag, itm, dcnt, dtm)
                    else:
                        tbls += tbl % (itm, dcnt, dtm)
        # Variables
        spn = '<div style="background: {sclr}; clip-path: circle(50%);'
        spn += ' height: 2em; width: 2em;"></div> '
        # slegend = ' '.join(dips)
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else colors[1]
        if not params['has_sex']:
            ucolors = colors[sel_color + 10] if sel_color else colors[11]
        if params['colors']:
            ucolors = params['colors']
        # Remove the other colors
        data['items'] = dips
        ucolors = get_colors(ucolors, params, data)
        slegend = ''
        flx = '<li style="display: flex; float: left;">'
        for i, dp in enumerate(dips):
            color = ucolors[i]
            sspn = spn.replace('{sclr}', color)
            slegend += '%s %s %s</li>' % (flx, sspn, dp)
        # cols
        col1 = 'Domain' if params['cont'] == '3I' else 'Agency'
        col2 = 'Service' if params['cont'] == '3I' else 'IP'
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{tables}', tbls)
        result = result.replace('{col1}', col1)
        result = result.replace('{col2}', col2)
        result = result.replace('{slegend}', slegend)
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{yLabel}', params['yLabel'])
        result = result.replace('{categories}', categories)
    except Exception as e:
        print('error with column chart - %s' % (str(e)))
        raise e
    else:
        return result


def stacked_bar_chart(request, params, data):
    """Method to get bar chart."""
    try:
        print(params, data)
        categories = str(data['items'])
        dcolors = ["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c",
                   "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00",
                   "#cab2d6", "#6a3d9a", "#ffff99", "#b15928",
                   "#8dd3c7", "#ffffb3", "#bebada", "#fb8072",
                   "#80b1d3", "#fdb462", "#b3de69", "#fccde5"]
        html = '''
                <script>
                $(document).ready(function() {
                    var colors = ["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c",
                                  "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00",
                                  "#cab2d6", "#6a3d9a", "#ffff99", "#b15928",
                                  "#8dd3c7", "#ffffb3", "#bebada", "#fb8072",
                                  "#80b1d3", "#fdb462", "#b3de69", "#fccde5"];
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'bar'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        xAxis: {
                            categories: {categories},
                            crosshair: false
                        },
                        yAxis: {
                            min: 0,
                            reversedStacks: false,
                            title: {
                                text: '{yLabel}'
                            }
                        },
                        tooltip: {
                            pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
                            shared: false
                        },
                        plotOptions: {
                            series: {
                                stacking: '{stacking}',
                                dataLabels: {
                                    enabled: true,
                                    inside: true,
                                    formatter: function () {
                                        var val = this.y;
                                        if (val < 1) {
                                            return '';
                                        }else{
                                            return this.percentage.toFixed(0) + '%';
                                        }
                                    }
                                }
                            },
                            threshold: 1
                        },
                        colors: {colors},
                        series: {series}
                    });
                });
            </script>'''
        yLabel = params['yLabel'] if params['yLabel'] else '# of OVC'
        stacking = params['stacking'] if 'stacking' in params else 'percent'
        # colors
        ucolors = dcolors
        if params['colors']:
            ucolors = params['colors']
        names = []
        for sr in data['series']:
            names.append(sr['name'])
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{categories}', str(data['categories']))
        result = result.replace('{series}', str(data['series']))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        # After
        data['items'] = names
        ucolors = get_colors(ucolors, params, data)
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{categories}', categories)
        result = result.replace('{stacking}', stacking)
        result = result.replace('{yLabel}', yLabel)
    except Exception as e:
        print('error with kpi data - %s' % (str(e)))
        raise e
    else:
        return result


def stacked_column_chart(request, params, data):
    """Method to get bar chart."""
    try:
        categories = str(data['items'])
        ucolors = ["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c",
                   "#fb9a99", "#e31a1c", "#fdbf6f", "#ff7f00",
                   "#cab2d6", "#6a3d9a", "#ffff99", "#b15928",
                   "#8dd3c7", "#ffffb3", "#bebada", "#fb8072",
                   "#80b1d3", "#fdb462", "#b3de69", "#fccde5"]
        html = '''
                <script>
                $(document).ready(function() {
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'column'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        xAxis: {
                            categories: {categories},
                            crosshair: false
                        },
                        yAxis: {
                            min: 0,
                            title: {
                                text: '% of OVC'
                            },
                            labels: {
                                useHTML:true, step: 1
                            }
                        },
                        tooltip: {
                            pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
                            shared: false
                        },
                        plotOptions: {
                            column: {
                                stacking: '{stacking}',
                                dataLabels: {
                                    enabled: true,
                                    inside: true,
                                    formatter: function () {
                                        // return this.percentage.toFixed(0) + '%';
                                        var val = this.y;
                                        if (val < 1) {
                                            return '';
                                        }
                                        // return val;
                                        if ('{stacking}' == 'normal'){
                                           return Highcharts.numberFormat(val, 0, '', ',');
                                        }else{
                                           return this.percentage.toFixed(0) + '%';
                                        }
                                    }
                                }
                            }
                        },
                        colors: {colors},
                        series: {series}
                    });
                });
            </script>'''
        '''
        art, nart = 0, 0
        for dt in data['series']:
            if dt['name'] == 'ART':
                art = dt['data'][4] if len(dt['data']) >= 5 else 0
            if dt['name'] == 'NART':
                nart = dt['data'][4] if len(dt['data']) >= 5 else 0
        ddts = {'type': 'pie', 'name': 'ART Status',
                'data': [{'name': 'On ART', 'y': art, 'color': '#fee0d2'},
                         {'name': 'Not on ART', 'y': nart,
                          'color': '#de2d26'}],
                'center': [700, 70],
                'size': 100, 'innerSize': '40%',
                'showInLegend': 'false',
                'dataLabels': {'enabled': 'false'}}
        if params['cont'] in ['2B', '5B', '7B']:
            data['series'].append(ddts)
        '''
        stacking = params['stacking'] if 'stacking' in params else 'normal'
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{categories}', str(data['categories']))
        # Colours
        if params['colors']:
            ucolors = params['colors']
        ucolors = get_colors(ucolors, params, data, 1)
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{series}', str(data['series']))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
        result = result.replace('{stacking}', stacking)
    except Exception as e:
        print('error with kpi data - %s' % (str(e)))
        raise e
    else:
        return result


def column_compare_chart(request, params, data):
    """Method to get bar chart."""
    try:
        html = '''
                <script>
                $(document).ready(function() {
                    var colors = {colors};
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'column'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        xAxis: {
                            categories: {categories}
                        },
                        yAxis: [{
                            min: 0,
                            title: {
                                text: '# of OVC'
                            }
                        }, {
                            title: {
                                text: ''
                            },
                            opposite: true
                        }],
                        legend: {
                            shadow: false
                        },
                        tooltip: {
                            shared: true
                        },
                        plotOptions: {
                            column: {
                                grouping: false,
                                shadow: false,
                                borderWidth: 0
                            }
                        },
                        colors: colors,
                        series: [{
                            name: 'Case load',
                            color: '#bdbdbd',
                            data: [{mdata}],
                            pointPadding: 0.3,
                            pointPlacement: -0.2
                        }, {
                            name: 'Exit without graduation',
                            data: [{fdata}],
                            pointPadding: 0.4,
                            pointPlacement: -0.2
                        }]
                    });
                });
            </script>'''
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else colors[1]
        if not params['has_sex']:
            # del ucolors[0:2]
            ucolors = colors[sel_color + 10] if sel_color else colors[11]
        # Other
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{categories}', str(data['items']))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
    except Exception as e:
        print('error with kpi data - %s' % (str(e)))
        raise e
    else:
        return result


def pie_chart(request, params, data):
    """Method to get bar chart."""
    try:
        categories = str(data['items'])
        print(params, data)
        html = '''
                <script>
                $(document).ready(function() {
                    var colors = {colors};
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            plotBackgroundColor: null,
                            plotBorderWidth: null,
                            plotShadow: false,
                            type: 'pie'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: 'OVC Population : {population}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        tooltip: {
                            pointFormat: '{series.name}: {point.y} <br><b>{point.percentage:.1f}%</b>'
                        },
                        accessibility: {
                            point: {
                                valueSuffix: '%'
                            }
                        },
                        plotOptions: {
                            pie: {
                                allowPointSelect: true,
                                cursor: 'pointer',
                                dataLabels: {
                                    enabled: true,
                                    format: '<b>{point.name}</b>: {point.percentage:.1f} %'
                                }
                            }
                        },
                        colors: colors,
                        series: [{
                           'name': 'Case Load', 'colorByPoint': 'true', 'innerSize': '40%',
                           'data': [{'name': 'Male', 'y': {mdata} }, {'name': 'Female', 'y': {fdata} }]
                           }]
                    });
                 });
            </script>'''
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else colors[1]
        if not params['has_sex']:
            # del ucolors[0:2]
            ucolors = colors[sel_color + 10] if sel_color else colors[11]
        mdata, fdata = 0, 0
        for dt in data['raw']:
            itm = dt['sex_id']
            dct = dt['dcount']
            if itm == 'Female':
                fdata = dct
            if itm == 'Male':
                mdata = dct
        my_pops = mdata + fdata
        pops = '{:,.0f}'.format(my_pops)
        if params['colors']:
            ucolors = params['colors']
        result = str(html).replace('{mdata}', str(mdata))
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{fdata}', str(fdata))
        result = result.replace('{population}', str(pops))
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
    except Exception as e:
        print('error with kpi data - %s' % (str(e)))
        raise e
    else:
        return result


def basic_bar_chart(request, params, data):
    """Method to get bar chart."""
    try:
        print(params, data)
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'bar'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        xAxis: {
                            categories: {categories},
                            crosshair: false
                        },
                        yAxis: {
                            min: 0,
                            reversedStacks: false,
                            title: {
                                text: '{yLabel}'
                            }
                        },
                        tooltip: {
                            pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
                            shared: false
                        },
                        plotOptions: {
                            series: {
                                stacking: '{stacking}',
                                dataLabels: {
                                    enabled: true,
                                    inside: true,
                                    formatter: function () {
                                        return this.percentage.toFixed(0) + '%';
                                    }
                                }
                            }
                        },
                        colors: {colors},
                        series: {series}
                    });
                });
            </script>'''
        # COLORS
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else colors[1]
        # Colours
        if params['colors']:
            ucolors = params['colors']
        # Remove the other colors
        ucolors = get_colors(ucolors, params, data, 1)
        yLabel = params['yLabel'] if params['yLabel'] else '# of OVC'
        stacking = params['stacking'] if 'stacking' in params else 'percent'
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{categories}', str(data['categories']))
        result = result.replace('{series}', str(data['series']))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
        result = result.replace('{stacking}', stacking)
        result = result.replace('{yLabel}', yLabel)
    except Exception as e:
        print('error with basic bar chart data - %s' % (str(e)))
        raise e
    else:
        return result


def table_chart(request, params, data):
    """Method to get bar chart."""
    try:
        # print('Jinga', params, data)
        df = pd.DataFrame(list(data['raw']))
        df.columns = df.columns.str.title()
        df.rename(columns={'Dcount': '# of OVC'}, inplace=True)
        result = df.to_html(classes='table', index=False)
        html = '<h4>{title}</h4><br>'
        html += result
        stacking = params['stacking'] if 'stacking' in params else 'percent'
        result = str(html)
        result = result.replace('{stacking}', stacking)
        result = result.replace('{title}', params['title'])
    except Exception as e:
        print('error with table chart data - %s' % (str(e)))
        return ''
    else:
        return result


def scatter_chart(request, params, data):
    """Method to get bar chart."""
    try:
        # print(params, data)
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'scatter',
                            zoomType: 'xy'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        xAxis: {
                            title: {
                                enabled: false,
                                text: ''
                            },
                            categories: {categories},
                            startOnTick: true,
                            endOnTick: true,
                            showLastLabel: true
                        },
                        yAxis: {
                            title: {
                                text: '# of OVC'
                            }
                        },
                        plotOptions: {
                            scatter: {
                                marker: {
                                    radius: 5,
                                    states: {
                                        hover: {
                                            enabled: true,
                                            lineColor: 'rgb(100,100,100)'
                                        }
                                    }
                                },
                                states: {
                                    hover: {
                                        marker: {
                                            enabled: false
                                        }
                                    }
                                },
                                tooltip: {
                                    headerFormat: '<b>{series.name}</b><br>',
                                    pointFormat: 'Suppressed: {point.y}'
                                }
                            }
                        },
                        colors: {colors},
                        series: {series}
                    });

                });
            </script>'''
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else colors[1]
        if not params['has_sex']:
            # del ucolors[0:2]
            ucolors = colors[sel_color + 10] if sel_color else colors[11]
        stacking = params['stacking'] if 'stacking' in params else 'percent'
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{categories}', str(data['categories']))
        result = result.replace('{series}', str(data['series']))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
        result = result.replace('{stacking}', stacking)
    except Exception as e:
        print('error with basic scatter chart data - %s' % (str(e)))
        raise e
    else:
        return result


def line_chart(request, params, data):
    """Method to get bar chart."""
    try:
        print(params, data)
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    Highcharts.chart('container-{cont}', {
                        title: {
                            text: '{title}'
                        },

                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        yAxis: {
                            title: {
                                text: '# of OVC'
                            }
                        },

                        xAxis: {
                            accessibility: {
                                rangeDescription: 'Range: 2010 to 2020'
                            }
                        },

                        legend: {
                            layout: 'vertical',
                            align: 'right',
                            verticalAlign: 'middle'
                        },

                        plotOptions: {
                            series: {
                                label: {
                                    connectorAllowed: false
                                },
                                pointStart: 2010
                            }
                        },

                        series: [{
                            name: 'Installation & Developers',
                            data: [43934, 48656, 65165, 81827, 112143, 142383,
                                171533, 165174, 155157, 161454, 154610]
                        }, {
                            name: 'Manufacturing',
                            data: [24916, 37941, 29742, 29851, 32490, 30282,
                                38121, 36885, 33726, 34243, 31050]
                        }, {
                            name: 'Sales & Distribution',
                            data: [11744, 30000, 16005, 19771, 20185, 24377,
                                32147, 30912, 29243, 29213, 25663]
                        }, {
                            name: 'Operations & Maintenance',
                            data: [null, null, null, null, null, null, null,
                                null, 11164, 11218, 10077]
                        }, {
                            name: 'Other',
                            data: [21908, 5548, 8105, 11248, 8989, 11816, 18274,
                                17300, 13053, 11906, 10073]
                        }],

                        responsive: {
                            rules: [{
                                condition: {
                                    maxWidth: 500
                                },
                                chartOptions: {
                                    legend: {
                                        layout: 'horizontal',
                                        align: 'center',
                                        verticalAlign: 'bottom'
                                    }
                                }
                            }]
                        }

                    });

                });
            </script>'''
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else colors[1]
        if not params['has_sex']:
            # del ucolors[0:2]
            ucolors = colors[sel_color + 10] if sel_color else colors[11]
        stacking = params['stacking'] if 'stacking' in params else 'percent'
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{categories}', str(data['categories']))
        result = result.replace('{series}', str(data['series']))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
        result = result.replace('{stacking}', stacking)
    except Exception as e:
        print('error with basic line chart data - %s' % (str(e)))
        raise e
    else:
        return result


def bar_category_chart(request, params, data):
    """Method to get bar chart."""
    try:
        # print('Remove sparklines', params, data)
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'bar'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        colors: {colors},
                        series: {series},
                        xAxis: {
                            categories: {categories},
                            colorByPoint: true
                        },
                        yAxis: {
                            title: {
                                text: '# of OVC'
                            },
                            labels: {
                                overflow: 'justify'
                            }
                        },
                        dataLabels: {
                            enabled: true
                        },
                        plotOptions: {
                            bar: {
                                dataLabels: {
                                    enabled: true
                                },
                                pointWidth: 15
                            }
                        },
                    });

                });
            </script>'''
        ags = {}
        ips = []
        dpps_dict = {}
        for dt in data['raw']:
            itm = dt['agency']
            dtm = dt['mechanism']
            dct = dt['dcount']
            if dtm not in ips:
                ips.append(dtm)
                dpps_dict[dtm] = dct
                if itm not in ags:
                    ags[itm] = {'count': 1, 'items': [{dtm: dct}]}
                else:
                    ags[itm]['count'] += 1
                    ags[itm]['items'].append({dtm: dct})
            else:
                dpps_dict[dtm] = dpps_dict[dtm] + dct
        cats = []
        fvals = []
        pcolors = params['colors']
        dfts = params['defaults']
        # srs = data['series']
        cnt = 0
        for dft in dfts:
            for ag in ags:
                if dft == ag:
                    itms = ags[ag]['items']
                    mct = {"name": ag, "categories": []}
                    for itm in itms:
                        for itmv in itm:
                            itmd = itm[itmv]
                            fval = {'name': itm, 'y': itmd,
                                    'color': pcolors[cnt]}
                            fvals.append(fval)
                            mct['categories'].append(itmv)
                    cats.append(mct)
                    cnt += 1
        fsrs = []
        fcnt = 0
        for dft in dfts:
            fcnt += 1
            itm = {'name': dft, 'data': []}
            if fcnt == 1:
                itm['data'] = fvals
            fsrs.append(itm)

        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(pcolors))
        result = result.replace('{categories}', str(cats))
        result = result.replace('{series}', str(fsrs))
        # result = result.replace('{series}', str(data['series']))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
    except Exception as e:
        print('error with grouped column chart data - %s' % (str(e)))
        raise e
    else:
        return result


def column_comparison_chart(request, params, data):
    """Method to get bar chart."""
    try:
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'column'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        plotOptions: {
                            series: {
                                grouping: false,
                                borderWidth: 0
                            }
                        },
                        legend: {
                            enabled: false
                        },
                        tooltip: {
                            shared: true,
                            headerFormat: '<span style="font-size: 15px">{point.point.name}</span><br/>',
                            pointFormat: '<span style="color:{point.color}">\u25CF</span> {series.name}: <b>{point.y}</b><br/>'
                        },
                        xAxis: {
                            type: 'category',
                            accessibility: {
                                description: 'Countries'
                            },
                            max: 4,
                            labels: {
                                useHTML: true,
                                animate: true,
                                formatter: ctx => {

                                    return '';
                                },
                                style: {
                                    textAlign: 'center'
                                }
                            }
                        },
                        yAxis: [{
                            title: {
                                text: '# of OVC'
                            },
                            showFirstLabel: false
                        }],
                        series: [{
                            color: 'rgba(158, 159, 163, 0.5)',
                            pointPlacement: -0.2,
                            linkedTo: 'main',
                            data: [{
                                    name: 'USAID',
                                    y: 30,
                                    color: "#dd0000"
                                }],
                            name: 'Not Served 2 quarters'
                        }, {
                            name: 'Attrition',
                            id: 'main',
                            dataSorting: {
                                enabled: true,
                                matchByName: true
                            },
                            dataLabels: [{
                                enabled: true,
                                inside: true,
                                style: {
                                    fontSize: '16px'
                                }
                            }],
                            data: [{
                                    name: 'USAID',
                                    y: 50,
                                    color: "#ff0000"
                                }]
                        }],
                        exporting: {
                            allowHTML: true
                        }
                    });

                });
            </script>'''
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(params['colors']))
        # result = result.replace('{categories}', str(data['categories']))
        # result = result.replace('{series}', str(fsrs))
        # result = result.replace('{series}', str(data['series']))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', categories)
    except Exception as e:
        print('error with column comparison chart data - %s' % (str(e)))
        raise e
    else:
        return result


def get_colors(ucolors, params, data, level=0):
    """Get custom colors - TDYs thing. """
    try:
        ctms = data['items']
        itms = params['defaults']
        colors = params['colors']
        if level:
            ctms = []
            for sr in data['series']:
                ctms.append(sr['name'])
        ncolors = []
        if itms and len(colors) >= len(itms):
            '''
            for i, itm in enumerate(itms):
                if itm in ctms:
                    ncolors.append(colors[i])
            '''
            for itm in ctms:
                index = itms.index(itm)
                ncolors.append(colors[index])
        else:
            ncolors = ucolors
    except Exception:
        return ucolors
    else:
        return ncolors


def column_category_chart(request, params, data):
    """Method to get bar chart."""
    try:
        # print('Remove sparklines', params, data)
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'column'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: '{subtitle}',
                            align: 'left'
                        },
                        caption: {
                            text: '{caption}'
                        },
                        colors: {colors},
                        series: {series},
                        xAxis: {
                            categories: {categories}
                        },
                        yAxis: {
                            title: {
                                text: '# of OVC'
                            },
                            labels: {
                                overflow: 'justify'
                            }
                        },
                        dataLabels: {
                            enabled: true
                        },
                        plotOptions: {
                            bar: {
                                dataLabels: {
                                    enabled: true
                                },
                                pointWidth: 15
                            }
                        },
                    });

                });
            </script>'''
        ags = {}
        cats, categories = [], {}
        ips = []
        dpps_dict = {}
        for dt in data['raw']:
            itm = dt['agency']
            dtm = dt['mechanism']
            itv = dt['schoollevel']
            dct = dt['dcount']
            if dtm not in ips:
                ips.append(dtm)
                dpps_dict[dtm] = dct
                itvs = {itv: dct}
                if itm not in ags:
                    ags[itm] = {'count': 1, 'items': {dtm: itvs}}
                else:
                    ags[itm]['count'] += 1
                    ags[itm]['items'][dtm] = itvs
            else:
                dpps_dict[dtm] = dpps_dict[dtm] + dct
                if itv not in ags[itm]['items'][dtm]:
                    ags[itm]['items'][dtm][itv] = dct
            # Generate categories
            if itm not in categories:
                categories[itm] = [dtm]
            else:
                if dtm not in categories[itm]:
                    categories[itm].append(dtm)
        fvals = {}
        pcolors = params['colors']
        dfts = params['defaults']

        cnt = 0
        for dft in dfts:
            for pg in ags:
                itms = ags[pg]['items']
                for fg in itms:
                    ips = itms[fg]
                    for sl in ips:
                        ag = ips[sl]
                        if dft == sl:
                            if dft not in fvals:
                                fvals[dft] = [ag]
                            else:
                                fvals[dft].append(ag)
                            cnt += 1
        fsrs = []
        for dft in dfts:
            if dft in fvals:
                itm = {'name': dft, 'data': fvals[dft]}
                fsrs.append(itm)

        # Categories
        for cat in categories:
            itm = {'name': cat, 'categories': categories[cat]}
            cats.append(itm)

        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(pcolors))
        result = result.replace('{categories}', str(cats))
        result = result.replace('{series}', str(fsrs))
        # result = result.replace('{series}', str(data['series']))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{subtitle}', params['subtitle'])
        result = result.replace('{caption}', params['caption'])
        result = result.replace('{categories}', str(cats))
    except Exception as e:
        print('error with grouped column chart data - %s' % (str(e)))
        raise e
    else:
        return result
