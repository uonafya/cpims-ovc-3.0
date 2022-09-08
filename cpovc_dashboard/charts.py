from .parameters import colors

dcolors = ["#377eb8", "#984ea3", "#7cb5ec", "#e41a1c",
           "#434348", "#E80C7A", "#E80C7A"]


def combo_chart(request, params, data):
    """Method to get timeline."""
    try:
        categories = str(data['items'])
        html = '''
                <script>
                $(document).ready(function() {
                    var colors = ["#377eb8", "#984ea3", "#7cb5ec", "#e41a1c", "#434348", "#E80C7A", "#E80C7A"];
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            zoomType: 'xy'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: ''
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
                        }, { // Primary yAxis
                            labels: {
                                format: '{value} %',
                                style: {
                                    color: '#e41a1c'
                                }
                            },
                            title: {
                                text: 'Cascade',
                                style: {
                                    color: '#e41a1c'
                                }
                            },
                            opposite: true
                        }],
                        tooltip: {
                            shared: true
                        },
                        plotOptions: {
                            column: {
                                stacking: 'normal',
                                dataLabels: {
                                    enabled: true
                                }
                            },
                            spline:{
                               colors: colors
                            }
                        },
                        legend: {
                               backgroundColor:
                                Highcharts.defaultOptions.legend.backgroundColor || // theme
                                'rgba(255,255,255,0.25)'
                        },
                        credits: {
                            enabled: false
                        },
                        colors: colors,
                        series: [{
                            name: '# of OVC',
                            type: 'column',
                            data: [{mdata}],
                            tooltip: {
                                valueSuffix: ''
                            },

                        }, {
                            name: 'Cascade',
                            type: 'spline',
                            lineWidth: 0,
                            yAxis: 1,
                            data: [{fdata}],
                            tooltip: {
                                valueSuffix: ' %'
                            },
                            states: {
                                hover: {
                                    lineWidthPlus: 0
                                }
                            }
                        }]
                    });
                });
            </script>'''
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
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
                    var colors = {colors};
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'bar'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        subtitle: {
                            text: ''
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
                            valueSuffix: ' OVC/HH'
                        },
                        plotOptions: {
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
                            enabled: false
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
                            name: '# OVC / HH',
                            data: [{mdata}]
                        }]
                    });
                 });
            </script>'''
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else dcolors
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
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
                            text: ''
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
                            enabled: false
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
                                    enabled: true,
                                    formatter: function() {
                                        return Highcharts.numberFormat(this.y, 0, '', ',') {xtras};
                                    }
                                }
                            }
                        },
                        credits: {
                            enabled: false
                        },
                        colors: colors,
                        legend: { enabled: {legend} },
                        series: [{series}]
                    });
                 });
            </script>'''
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else dcolors
        if params['xAxis']:
            series = "{name: 'Male', data: [{mdata}] }, { name: 'Female', data: [{fdata}] }"
            xtras = "+ '<br/>' + Highcharts.numberFormat(this.percentage, 0, '', ',') + '%'"
        else:
            series = "{name: '# OVC', data: [{mdata}] }"
            xtras = ""
        legend = 'true' if params['legend'] else 'false'
        result = str(html).replace('{series}', series)
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{legend}', legend)
        result = result.replace('{xtras}', xtras)
        result = result.replace('{mdata}', data['mdata'])
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
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
                    var colors = ["#377eb8", "#984ea3", "#7cb5ec", "#e41a1c", "#434348", "#E80C7A", "#E80C7A"];
                    Highcharts.chart('container-{cont}', {
                        chart: {
                            type: 'column'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
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
                                    enabled: true,
                                    formatter: function() {
                                        return Highcharts.numberFormat(this.y, 0, '', ',');
                                    }
                                }
                            }
                        },
                        credits: {
                            enabled: false
                        },
                        colors: colors,
                        legend: { enabled: {legend} },
                        series: [{series}]
                    });
                 });
            </script>'''
        if params['xAxis']:
            series = "{name: 'Male', data: [{mdata}] }, { name: 'Female', data: [{fdata}] }"
        else:
            series = "{name: '# OVC / HH', data: [{mdata}] }"
        legend = 'true' if params['legend'] else 'false'
        result = str(html).replace('{series}', series)
        result = result.replace('{legend}', legend)
        result = result.replace('{mdata}', data['mdata'])
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
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
                            enabled: false
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
                            type: "bar"
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
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
                            reversed: true
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
                            width: '45%'
                        }],
                        plotOptions: {
                            series: {
                                stacking: "normal",
                                groupPadding: 0,
                                pointPadding: 0,
                                dataLabels: {
                                    enabled: true,
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
        sel_color = request.session.get('sel_color', 0)
        ucolors = colors[sel_color] if sel_color else dcolors
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{categories}', categories)
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
                <table id="table-sparkline" class="table">
                <thead>
                    <tr>
                        <th>Agency</th>
                        <th>IP</th>
                        <th>-</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody id="tbody-sparkline">
                    {tables}
                </tbody>
            </table>
        <script>
        var colors = ["#377eb8", "#984ea3", "#7cb5ec", "#e41a1c",
                      "#434348", "#E80C7A", "#E80C7A"];
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
                  width: 120,
                  height: 20,
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
                exporting: {
                  enabled: false
                },
                xAxis: {
                  labels: {
                    enabled: false
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
                  labels: {
                    enabled: false
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
                  shared: true
                },
                colors: colors,
                plotOptions: {
                  series: {
                    stacking: 'normal',
                    animation: false,
                    lineWidth: 1,
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
              tooltip: {
                headerFormat: '<span style="font-size: 10px">' + $td.parent().find('th').html() + ', IP {point.x}:</span><br/>',
                pointFormat: '<b>{point.y}</b> '
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
        tbl0 = '<tr><td %s>%s</td><td>%s</td>'
        tbl0 += '<td>-</td><td data-sparkline="%s "/></tr>'
        tbl = '<tr><td>%s</td>'
        tbl += '<td>-</td><td data-sparkline="%s "/></tr>'
        for dt in data['raw']:
            itm = dt['agency']
            dtm = dt['mechanism']
            dts = dt['schoollevel']
            dct = dt['dcount']
            if dts not in dips:
                dips.append(dts)
            if dtm not in ips:
                ips.append(dtm)
                if itm not in ags:
                    ags[itm] = {'count': 1, 'items': [{dtm: dct}]}
                else:
                    ags[itm]['count'] += 1
                    ags[itm]['items'].append({dtm: dct})
        for ag in ags:
            cnt = 0
            print('AG', ag)
            rsp = ags[ag]['count']
            for itms in ags[ag]['items']:
                cnt += 1
                for itm in itms:
                    dtm = itms[itm]
                    tb0 = 'rowspan="%s"' % rsp if cnt == 1 else ''
                    if cnt == 1:
                        tbls += tbl0 % (tb0, ag, itm, dtm)
                    else:
                        tbls += tbl % (itm, dtm)
        print('ags', ags)
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{tables}', tbls)
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
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
                        xAxis: {
                            categories: {categories},
                            crosshair: false
                        },
                        yAxis: {
                            min: 0,
                            title: {
                                text: '# of OVC'
                            }
                        },
                        tooltip: {
                            pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
                            shared: false
                        },
                        plotOptions: {
                            bar: {
                                stacking: '{stacking}'
                            }
                        },
                        colors: colors,
                        series: {series}
                    });
                });
            </script>'''
        stacking = params['stacking'] if 'stacking' in params else 'percent'
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{categories}', str(data['categories']))
        result = result.replace('{series}', str(data['series']))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{categories}', categories)
        result = result.replace('{stacking}', stacking)
    except Exception as e:
        print('error with kpi data - %s' % (str(e)))
        raise e
    else:
        return result


def stacked_column_chart(request, params, data):
    """Method to get bar chart."""
    try:
        categories = str(data['items'])
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
                            type: 'column'
                        },
                        title: {
                            text: '{title}',
                            align: 'left'
                        },
                        xAxis: {
                            categories: {categories},
                            crosshair: false
                        },
                        yAxis: {
                            min: 0,
                            title: {
                                text: '# of OVC'
                            }
                        },
                        tooltip: {
                            pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
                            shared: false
                        },
                        plotOptions: {
                            column: {
                                stacking: '{stacking}'
                            }
                        },
                        colors: colors,
                        series: {series}
                    });
                });
            </script>'''
        art, nart = 0, 0
        for dt in data['series']:
            if dt['name'] == 'ART':
                art = dt['data'][4]
            if dt['name'] == 'NART':
                nart = dt['data'][4]
        ddts = {'type': 'pie', 'name': 'ART Status',
                'data': [{'name': 'On ART', 'y': art, 'color': '#fee0d2'},
                         {'name': 'Not on ART', 'y': nart,
                          'color': '#de2d26'}],
                'center': [700, 70],
                'size': 100, 'innerSize': '40%',
                'showInLegend': 'false',
                'dataLabels': {'enabled': 'false'}}
        if params['cont'] == '5A':
            data['series'].append(ddts)
        stacking = params['stacking'] if 'stacking' in params else 'normal'
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{categories}', str(data['categories']))
        result = result.replace('{series}', str(data['series']))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
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
                            text: '{title}'
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
        ucolors = colors[sel_color] if sel_color else dcolors
        # Other
        result = str(html).replace('{mdata}', data['mdata'])
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{categories}', str(data['items']))
        result = result.replace('{fdata}', data['fdata'])
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
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
                            text: 'OVC Population : {population}'
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
        ucolors = colors[sel_color] if sel_color else dcolors
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
        result = str(html).replace('{mdata}', str(mdata))
        result = result.replace('{colors}', str(ucolors))
        result = result.replace('{fdata}', str(fdata))
        result = result.replace('{population}', str(pops))
        result = result.replace('{cont}', params['cont'])
        result = result.replace('{title}', params['title'])
        result = result.replace('{categories}', categories)
    except Exception as e:
        print('error with kpi data - %s' % (str(e)))
        raise e
    else:
        return result
