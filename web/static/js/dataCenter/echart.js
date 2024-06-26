$(function() {

    ceshis1(data1, legend1);
    ceshi2(yield_data);
    ceshi3();
    ceshi4();
    ceshi5();
    ceshi6(data1,legend1);
    ceshi7(all_yield);

    echart_map(chinaDatas); //还是用的原数据，只是


    function ceshis1(data1, legend1) {
        var myChart = echarts.init(document.getElementById('ceshi'));

        /*var ydata = [{name: '鲤鱼',value: 18},];
        var color = ["#8d7fec", "#5085f2", "#e75fc3", "#f87be2", "#f2719a", "#fca4bb", "#f59a8f", "#fdb301", "#57e7ec", "#cf9ef1"]
        var xdata = ['鲤鱼', "鲫鱼", "鳙鱼", "鲈鱼", '鲳鱼', '鲷鱼', '黑鱼', '草鱼', '黄花鱼', '鳊鱼'];
        */
        //var legend1 = [i.get('name') for i in data1]; 问题在这，这是python
        // console
        console.log(supply);
        option = {
            /*backgroundColor: "rgba(255,255,255,1)",*/
            color:  ["#8d7fec", "#5085f2", "#e75fc3", "#f87be2", "#f2719a", "#fca4bb", "#f59a8f"],
            legend: {  /*图例*/
                orient: "vartical",
                x: "left",
                top: "center",
                left: "53%",
                bottom: "0%",
                //data: xdata,
                data: legend1,
                itemWidth: 8,
                itemHeight: 8,
                textStyle: {
                    color: '#fff'
                },
                formatter: function(name) {
                    return '' + name
                }
            },
            series: [{
                type: 'pie',
                clockwise: false, //饼图的扇区是否是顺时针排布
                minAngle: 2, //最小的扇区角度（0 ~ 360）
                radius: ["20%", "60%"],
                center: ["30%", "45%"],
                avoidLabelOverlap: false,
                itemStyle: { //图形样式
                    normal: {
                        borderColor: '#ffffff',
                        borderWidth: 1,
                    },
                },
                label: {
                    normal: {
                        show: false,
                        position: 'center',
                        formatter: '{text|{b}}\n{c} ({d}%)',
                        rich: {
                            text: {
                                color: "#fff",
                                fontSize: 14,
                                align: 'center',
                                verticalAlign: 'middle',
                                padding: 8
                            },
                            value: {
                                color: "#8693F3",
                                fontSize: 24,
                                align: 'center',
                                verticalAlign: 'middle',
                            },
                        }
                    },
                    emphasis: {
                        show: true,
                        textStyle: {
                            fontSize: 24,
                        }
                    }
                },
                //data: ydata
                data: data1
            }]
        };
        myChart.setOption(option);
        /*myChart.on('click',  function(param) {
            //alert("更多模板，关注公众号【DreamCoders】\n回复'BigDataView'即可获取\n或前往Gitee下载 https://gitee.com/iGaoWei/big-data-view")
            setTimeout(function(){
                location.href = "https://gitee.com/iGaoWei/big-data-view";
            },20000);
        });*/
        setTimeout(function() {
            myChart.on('mouseover', function(params) {
                if (params.name == ydata[0].name) {
                    myChart.dispatchAction({
                        type: 'highlight',
                        seriesIndex: 0,
                        dataIndex: 0
                    });
                } else {
                    myChart.dispatchAction({
                        type: 'downplay',
                        seriesIndex: 0,
                        dataIndex: 0
                    });
                }
            });

            myChart.on('mouseout', function(params) {
                myChart.dispatchAction({
                    type: 'highlight',
                    seriesIndex: 0,
                    dataIndex: 0
                });
            });
            myChart.dispatchAction({
                type: 'highlight',
                seriesIndex: 0,
                dataIndex: 0
            });
        }, 1000);

        myChart.currentIndex = -1;

        setInterval(function() {
            var dataLen = option.series[0].data.length;
            // 取消之前高亮的图形
            myChart.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: myChart.currentIndex
            });
            myChart.currentIndex = (myChart.currentIndex + 1) % dataLen;
            // 高亮当前图形
            myChart.dispatchAction({
                type: 'highlight',
                seriesIndex: 0,
                dataIndex: myChart.currentIndex
            });
        }, 1000);

        // 使用刚指定的配置项和数据显示图表。
        /*myChart.setOption(option);*/
        window.addEventListener("resize", function() {
            myChart.resize();
        });
    }

    function echart_map(chinaDatas) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('ceshi8'));

        var chinaGeoCoordMap = {
            "上海": [121.4648, 31.2891],
            "云南": [102.9199, 25.4663],
            "内蒙古": [110.3467, 41.4899],
            //"北京": [116.4551, 40.2539],
            "吉林": [125.325, 43.8868],
            "四川": [103.9526, 30.7617],
            "天津": [117.4219, 39.4189],
            "安徽": [117.194778, 31.86577],
            "山东": [117.1582, 36.8701],
            "山西": [112.5300, 37.8700],
            "广东": [113.12244, 23.009505],
            "广西": [108.479, 23.1152],
            "江苏": [118.8062, 31.9208],
            "江西": [116.0046, 28.6633],
            "河北": [114.4995, 38.1006],
            "河南": [113.6650, 34.7580],
            "浙江": [119.5313, 29.8773],
            "湖北": [114.2986, 30.5844],
            "湖南": [113.0823, 28.2568],
            "福建": [119.4543, 25.9222],
            "辽宁": [123.1238, 42.1216],
            "重庆": [108.384366, 30.439702],
            "陕西": [108.970163, 34.284398],
            "黑龙江": [127.9688, 45.368]
        };
        
        /*var chinaDatas_ = [
            [{
                name: '黑龙江',
                value: 0
            }],
            [{
                name: '内蒙古',
                value: 0
            }],
            [{
                name: '辽宁',
                value: 0
            }],
            [{
                name: '河北',
                value: 0
            }],
            [{
                name: '天津',
                value: 0
            }],
            [{
                name: '甘肃',
                value: 0
            }],
            [{
                name: '四川',
                value: 0
            }],
            [{
                name: '重庆',
                value: 0
            }],
            [{
                name: '山东',
                value: 0
            }],
            [{
                name: '江苏',
                value: 0
            }],
            [{
                name: '浙江',
                value: 0
            }],
            [{
                name: '福建',
                value: 0
            }],
            [{
                name: '江西',
                value: 0
            }],
            [{
                name: '湖南',
                value: 0
            }],
            [{
                name: '云南',
                value: 0
            }],
            [{
                name: '广东',
                value: 0
            }],
            [{
                name: '广西',
                value: 0
            }],
            [{
                name: '上海',
                value: 1
            }]
        ];*/

        //chinaDatas = [[{'name': item['省份'], 'value': float(item['温度'])}] for item in supply];
        var convertData = function(data) {
            var res = [];
            for (var i = 0; i < data.length; i++) {
                var dataItem = data[i];
                var fromCoord = chinaGeoCoordMap[dataItem[0].name];
                var toCoord = [116.4551, 40.2539];
                if (fromCoord && toCoord) {
                    res.push([{
                        coord: fromCoord,
                        value: dataItem[0].value
                        //value: String(dataItem[0].value)  // 转换为字符串
                    }, {
                        coord: toCoord,
                    }]);
                }
            }
            return res;
        };
        var series = [];
        [
            ['北京', chinaDatas]
        ].forEach(function(item, i) {
            console.log(item)
            series.push({
                    type: 'lines',
                    zlevel: 2,
                    effect: {
                        show: true,
                        period: 4, //箭头指向速度，值越小速度越快
                        trailLength: 0.02, //特效尾迹长度[0,1]值越大，尾迹越长重
                        symbol: 'arrow', //箭头图标
                        symbolSize: 5, //图标大小
                    },
                    lineStyle: {
                        normal: {
                            width: 1, //尾迹线条宽度
                            opacity: 1, //尾迹线条透明度
                            curveness: .3 //尾迹线条曲直度
                        }
                    },
                    data: convertData(item[1])
                }, {
                    type: 'effectScatter',
                    coordinateSystem: 'geo',
                    zlevel: 2,
                    rippleEffect: { //涟漪特效
                        period: 4, //动画时间，值越小速度越快
                        brushType: 'stroke', //波纹绘制方式 stroke, fill
                        scale: 4 //波纹圆环最大限制，值越大波纹越大
                    },
                    label: {
                        normal: {
                            show: true,
                            position: 'right', //显示位置
                            offset: [5, 0], //偏移设置
                            formatter: function(params) { //圆环显示文字
                                return params.data.name;
                            },
                            fontSize: 13
                        },
                        emphasis: {
                            show: true
                        }
                    },
                    symbol: 'circle',
                    symbolSize: function(val) {
                        return 5 + val[2] * 5; //圆环大小
                    },
                    itemStyle: {
                        normal: {
                            show: false,
                            color: '#f00'
                        }
                    },
                    data: item[1].map(function(dataItem) {
                        return {
                            name: dataItem[0].name,
                            value: chinaGeoCoordMap[dataItem[0].name].concat([dataItem[0].value])
                            //value: chinaGeoCoordMap[dataItem[0].name].concat([String(dataItem[0].value)]) // 转换为字符串
                        };
                    }),
                },
                //被攻击点
                {
                    type: 'scatter',
                    coordinateSystem: 'geo',
                    zlevel: 2,
                    rippleEffect: {
                        period: 4,
                        brushType: 'stroke',
                        scale: 4
                    },
                    label: {
                        normal: {
                            show: true,
                            position: 'right',
                            //offset:[5, 0],
                            color: '#0f0',
                            formatter: '{b}',
                            textStyle: {
                                color: "#0f0"
                            }
                        },
                        emphasis: {
                            show: true,
                            color: "#f60"
                        }
                    },
                    symbol: 'pin',
                    symbolSize: 50,
                    data: [{
                        name: item[0],
                        value: chinaGeoCoordMap[item[0]].concat([10]),
                    }],
                }
            );
        });

        option = {
            tooltip: {
                trigger: 'item',
                backgroundColor: 'rgba(166, 200, 76, 0.82)',
                borderColor: '#FFFFCC',
                showDelay: 0,
                hideDelay: 0,
                enterable: true,
                transitionDuration: 0,
                extraCssText: 'z-index:100',
                formatter: function(params, ticket, callback) {
                    //根据业务自己拓展要显示的内容
                    var res = "";
                    var name = params.name;
                    var value = params.value[params.seriesIndex + 1];
                    res = "<span style='color:#fff;'>" + name + "</span><br/>水质：" + value;
                    return res;
                }
            },
            /*backgroundColor:"#013954",*/
            visualMap: { //图例值控制
                min: 0,
                max: 1,
                calculable: true,
                show: false,
                color: ['#f44336', '#fc9700', '#ffde00', '#ffde00', '#00eaff'],
                textStyle: {
                    color: '#fff'
                }
            },
            geo: {
                map: 'china',
                zoom: 1.2,
                label: {
                    emphasis: {
                        show: false
                    }
                },
                roam: true, //是否允许缩放
                itemStyle: {
                    normal: {
                        color: 'rgba(51, 69, 89, .5)', //地图背景色
                        borderColor: '#516a89', //省市边界线00fcff 516a89
                        borderWidth: 1
                    },
                    emphasis: {
                        color: 'rgba(37, 43, 61, .5)' //悬浮背景
                    }
                }
            },
            series: series
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function() {
            myChart.resize();
        });
        /*myChart.on('click',  function(param) {
            alert("更多模板，关注公众号【DreamCoders】\n回复'BigDataView'即可获取\n或前往Gitee下载 https://gitee.com/iGaoWei/big-data-view")
            setTimeout(function(){
                location.href = "https://gitee.com/iGaoWei/big-data-view";
            },20000);
        });*/

    }

    function ceshi2(yield_data) {
        // 初始化 echarts 实例，指定图表容器的 DOM 节点
        var myChart = echarts.init($("#ceshi2")[0]);
    
        // 设置图表的配置项和数据
        option = {
            /*backgroundColor: '#05163B',*/
            // 提示框配置，当鼠标悬停在数据点上时触发
            tooltip: {
                trigger: 'axis'
            },
            // 工具箱配置，包括标记、数据视图、切换图表类型、还原和保存图片等功能
            toolbox: {
                show: true,
                feature: {
                    mark: {
                        show: true
                    },
                    dataView: {
                        show: true,
                        readOnly: false
                    },
                    magicType: {
                        show: true,
                        type: ['line', 'bar']
                    },
                    restore: {
                        show: true
                    },
                    saveAsImage: {
                        show: true
                    }
                }
            },
            // 绘图区域的位置和大小配置
            grid: {
                top: 'middle',
                left: '3%',
                right: '4%',
                bottom: '3%',
                top: '10%',
                containLabel: true
            },
            // 图例配置，包括各个系列数据的名称
            legend: {
                data: ['产量', '养殖面积', '同比增加', '平均产量'],
                textStyle: {
                    color: "#fff"
                }
            },
            // X 轴配置
            xAxis: [{
                type: 'category',
                // X 轴数据
                data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
                axisLabel: {
                    show: true,
                    // X 轴标签文字样式
                    textStyle: {
                        color: "#ebf8ac" //X轴文字颜色
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: '#01FCE3'
                    }
                },
            }],
            // Y 轴配置
            yAxis: [{
                    type: 'value',
                    name: '产量',
                    axisLabel: {
                        formatter: '{value} 吨',
                        textStyle: {
                            color: "#2EC7C9" //X轴文字颜色
                        }
                    },
                    axisLine: {
                        lineStyle: {
                            color: '#01FCE3'
                        }
                    },
                },
                {
                    type: 'value',
                    name: '鱼排面积',
                    axisLabel: {
                        formatter: '{value} 亩',
                        textStyle: {
                            color: "#2EC7C9" //X轴文字颜色
                        }
                    }
                }
            ],
            // 系列数据配置
            series: [{
                    name: '产量',
                    type: 'bar',
                    // 柱状图样式配置
                    itemStyle: {
                        normal: {
                            barBorderRadius: 5,
                            // 渐变色填充
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                        offset: 0,
                                        color: "#00FFE3"
                                    },
                                    {
                                        offset: 1,
                                        color: "#4693EC"
                                    }
                                ])
                        }
                    },
                    // 数据
                    //data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
                    data: yield_data['产量']
                },
                {
                    name: '鱼排面积',
                    type: 'bar',
                    // 柱状图样式配置
                    itemStyle: {
                        normal: {
                            barBorderRadius: 5,
                            // 渐变色填充
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                        offset: 0,
                                        color: "#C1B2EA"
                                    },
                                    {
                                        offset: 1,
                                        color: "#8362C6"
                                    }
                                ])
                        }
                    },
                    // 数据
                    //data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
                    data: yield_data['鱼排面积']
                },
                {
                    name: '同比增加',
                    type: 'line',
                    yAxisIndex: 1,
                    // 数据
                    //data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
                    data: yield_data['同比增加'],
                    // 折线样式配置
                    lineStyle: {
                        normal: {
                            width: 5,
                            color: {
                                type: 'linear',
                                colorStops: [{
                                        offset: 0,
                                        color: '#AAF487' // 0% 处的颜色
                                    },
                                    {
                                        offset: 0.4,
                                        color: '#47D8BE' // 100% 处的颜色
                                    }, {
                                        offset: 1,
                                        color: '#47D8BE' // 100% 处的颜色
                                    }
                                ],
                                globalCoord: false // 缺省为 false
                            },
                            shadowColor: 'rgba(71,216,190, 0.5)',
                            shadowBlur: 10,
                            shadowOffsetY: 7
                        }
                    },
                    // 点样式配置
                    itemStyle: {
                        normal: {
                            color: '#AAF487',
                            borderWidth: 10,
                            borderColor: "#AAF487"
                        }
                    },
                    smooth: true,
                },
                {
                    name: '平均产量',
                    type: 'line',
                    yAxisIndex: 1,
                    // 数据
                    //data: [4.0, 3.2, 2.3, 5.5, 4.3, 11.2, 15.3, 22.4, 21.0, 13.5, 12.0, 10.2],
                    data: yield_data['平均产量'],
                    // 折线样式配置
                    lineStyle: {
                        normal: {
                            width: 5,
                            color: {
                                type: 'linear',
                                colorStops: [{
                                        offset: 0,
                                        color: '#F8B854' // 0% 处的颜色
                                    },
                                    {
                                        offset: 0.4,
                                        color: '#DE801C' // 100% 处的颜色
                                    }, {
                                        offset: 1,
                                        color: '#DE801C' // 100% 处的颜色
                                    }
                                ],
                                globalCoord: false // 缺省为 false
                            },
                            shadowColor: 'rgba(71,216,190, 0.5)',
                            shadowBlur: 10,
                            shadowOffsetY: 7
                        }
                    },
                    // 点样式配置
                    itemStyle: {
                        normal: {
                            color: '#F7AD3E',
                            borderWidth: 10,
                            borderColor: "#F7AD3E"
                        }
                    },
                    smooth: true,
                }
            ]
        };
    
        // 使用刚指定的配置项和数据显示图表
        myChart.setOption(option);
    
        // 监听窗口大小变化事件，调整图表大小
        window.addEventListener('resize', function() {
            myChart.resize();
        })
    
    }
    

    function ceshi3() {
        var myChart = echarts.init($("#ceshi3")[0]);
        /**
         * 图标所需数据
         */
        var data = {
            value: 20.2,
            text: '-',
            color: '#4ac7f5',
            xAxis: ['批发'],
            values: ['76'],
        }

        var seriesData = []
        var titleData = []
        data.values.forEach(function(item, index) {
            titleData.push({
                text: data.xAxis[index],
                left: 50 * (index + 1) - .5 + '%',
                top: '60%',

                textAlign: 'center',
                textStyle: {
                    fontSize: '12',
                    color: '#ffffff',
                    fontWeight: '400',
                },
            })
            seriesData.push({
                type: 'pie',
                radius: ['35', '45'],

                center: [50 * (index + 1) + '%', '30%'],
                hoverAnimation: false,
                label: {
                    normal: {
                        position: 'center'
                    },
                },
                data: [{
                        value: item,
                        name: data.text,
                        itemStyle: {
                            normal: {
                                color: data.color,
                            }
                        },
                        label: {
                            normal: {
                                show: false,
                            }
                        }
                    },
                    {
                        value: 100 - item,
                        name: '占位',
                        tooltip: {
                            show: false
                        },
                        itemStyle: {
                            normal: {
                                color: '#edf1f4',
                            }
                        },
                        label: {
                            normal: {
                                formatter: item + '',
                                textStyle: {
                                    fontSize: 36,
                                    color: data.color
                                }
                            },

                        }
                    }
                ]
            })
        })

        ////////////////////////////////////////

        let value = data.value || 0
        option = {
            /*backgroundColor: '#fff',*/
            title: titleData,
            series: seriesData
        }

        myChart.setOption(option);
        window.addEventListener('resize', function() {
            myChart.resize();
        })

    }

    function ceshi4() {
        var myChart = echarts.init($("#ceshi4")[0]);
        /**
         * 图标所需数据
         */
        var data = {
            value: 20.2,
            text: '-',
            color: '#25f3e6',
            xAxis: ['批发'],
            values: ['46'],
        }

        var seriesData = []
        var titleData = []
        data.values.forEach(function(item, index) {
            titleData.push({
                text: data.xAxis[index],
                left: 50 * (index + 1) - .5 + '%',
                top: '60%',

                textAlign: 'center',
                textStyle: {
                    fontSize: '12',
                    color: '#ffffff',
                    fontWeight: '400',
                },
            })
            seriesData.push({
                type: 'pie',
                radius: ['35', '45'],
                center: [50 * (index + 1) + '%', '30%'],
                hoverAnimation: false,
                label: {
                    normal: {
                        position: 'center'
                    },
                },
                data: [{
                        value: item,
                        name: data.text,
                        itemStyle: {
                            normal: {
                                color: data.color,
                            }
                        },
                        label: {
                            normal: {
                                show: false,
                            }
                        }
                    },
                    {
                        value: 100 - item,
                        name: '占位',
                        tooltip: {
                            show: false
                        },
                        itemStyle: {
                            normal: {
                                color: '#edf1f4',
                            }
                        },
                        label: {
                            normal: {
                                formatter: item + '',
                                textStyle: {
                                    fontSize: 36,
                                    color: data.color
                                }
                            },

                        }
                    }
                ]
            })
        })

        ////////////////////////////////////////

        let value = data.value || 0
        option = {
            /*backgroundColor: '#fff',*/
            title: titleData,
            series: seriesData
        }

        myChart.setOption(option);
        window.addEventListener('resize', function() {
            myChart.resize();
        })

    }

    function ceshi5() {
        var myChart = echarts.init($("#ceshi5")[0]);
        /**
         * 图标所需数据
         */
        var data = {
            value: 20.2,
            text: '-',
            color: '#ffff43',
            xAxis: ['批发'],
            values: ['76'],
        }

        var seriesData = []
        var titleData = []
        data.values.forEach(function(item, index) {
            titleData.push({
                text: data.xAxis[index],
                left: 50 * (index + 1) - .5 + '%',
                top: '60%',

                textAlign: 'center',
                textStyle: {
                    fontSize: '12',
                    color: '#ffffff',
                    fontWeight: '400',
                },
            })
            seriesData.push({
                type: 'pie',
                radius: ['35', '45'],
                center: [50 * (index + 1) + '%', '30%'],
                hoverAnimation: false,
                label: {
                    normal: {
                        position: 'center'
                    },
                },
                data: [{
                        value: item,
                        name: data.text,
                        itemStyle: {
                            normal: {
                                color: data.color,
                            }
                        },
                        label: {
                            normal: {
                                show: false,
                            }
                        }
                    },
                    {
                        value: 100 - item,
                        name: '占位',
                        tooltip: {
                            show: false
                        },
                        itemStyle: {
                            normal: {
                                color: '#edf1f4',
                            }
                        },
                        label: {
                            normal: {
                                formatter: item + '',
                                textStyle: {
                                    fontSize: 36,
                                    color: data.color
                                }
                            },

                        }
                    }
                ]
            })
        })

        ////////////////////////////////////////

        let value = data.value || 0
        option = {
            /*backgroundColor: '#fff',*/
            title: titleData,
            series: seriesData
        }

        myChart.setOption(option);
        window.addEventListener('resize', function() {
            myChart.resize();
        })

    }

    function ceshi6(data1,legend1) {
        var myChart = echarts.init($("#ceshi6")[0]);

        //var data = [110, 20, 36, 10, 50, 80, 100, 60];
        var data = data1.map(item => item.value);
        var sum = 0;
        var percentdata = [];
        for (var i = 0; i < data.length; i++) {
            sum += data[i];
        };
        for (var j = 0; j < data.length; j++) {
            percentdata.push((((data[j] / sum) * 100).toFixed(2)));
        };
        // console.log(percentdata);
        option = {
            color: ['#0035f9', '#f36f8a', '#ffff43', '#25f3e6'],
            grid: {
                left: '8%',
                right: '10%',
                top: '12%',
                bottom: '18%',
                containLabel: true
            },
            yAxis: {
                //data: ['鲤鱼', "鲫鱼", "鳙鱼", "鲈鱼", '鲳鱼', '鲷鱼', '黑鱼', '草鱼'],
                data: legend1,
                axisTick: {
                    show: false
                },
                axisLabel: {
                    formatter: '{value} ',
                    textStyle: {
                        color: "#2EC7C9" //X轴文字颜色
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: '#01FCE3'
                    }
                },

            },

            xAxis: [{
                axisTick: {
                    show: false
                },
                type: 'value',
                // max: 100,
                splitNumber: 5,
                axisLabel: {
                    formatter: '{value}%',
                    show: true,
                    textStyle: {
                        color: "#ebf8ac" //X轴文字颜色
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: '#01FCE3'
                    }
                },
            }],
            series: [{
                name: '销量',
                type: 'bar',
                itemStyle: {
                    normal: {
                        barBorderRadius: 5,
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: "#25f3e6"
                            },
                            {
                                offset: 1,
                                color: "#4693EC"
                            }
                        ])
                    }
                },
                barWidth: '55%',
                label: {
                    normal: {
                        show: true,
                        position: 'right',
                        formatter: '{c}%',
                        textStyle: {
                            color: '#ffffff'
                        }
                    }
                },
                data: percentdata
            }]
        };

        myChart.setOption(option);
        window.addEventListener('resize', function() {
            myChart.resize();
        })
    }

    function ceshi7(all_yield) {
        var myChart = echarts.init($("#ceshi7")[0]);
        option = {
            /*backgroundColor: '#031845',*/
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)",

            },
            graphic: {
                elements: [{
                    type: 'image',
                    style: {
                        /*image: giftImageUrl,*/
                        width: 50,
                        height: 50
                    },
                    left: 'center',
                    top: 'center'
                }]
            },
            /*title: {
                //text: '产量分析',
                //left: 'center',
                right: '10px'
                top: '10%',
                padding: [24, 0],
                textStyle: {
                    color: '#fff',
                    fontSize: 18,
                    align: 'center'
                }
            },*/
            title: {
                text: '产 \n量 \n分 \n析', // 使用换行符来分隔每个字符
                top: 'middle', // 根据需要调整垂直居中
                right: '10px', // 调整标题距离右侧的距离
                textStyle: {
                    color: '#fff',
                    fontSize: 19,
                    align: 'center' // 根据需要调整对齐方式
                },
                rotate: 90, // 旋转角度，使标题竖向显示
            },
            legend: {
                orient: 'horizontal',
                icon: 'circle',
                bottom: 0,
                x: 'center',
                //data: ['一号渔排', '二号渔排', '三号渔排', '四号渔排', '五号渔排', '六号渔排', '七号渔排'],
                data: ['鱼类', '甲壳类', '蟹类', '贝类', '藻类', '其它'],
                textStyle: {
                    color: '#fff'
                }
            },
            series: [{
                name: '产量',
                type: 'pie',
                radius: ['25%', '35%'],
                color: ['#00FFFF', '#44EAB1', '#7BDD43', '#FEBE12', '#EBEC2F', '#FF7C44', '#FA3E5F', '#6635EF'],
                labelLine: {
                    normal: {
                        show: true,
                        length: 10,
                        length2: 10,
                        lineStyle: {
                            width: 1
                        }
                    }
                },
                label: {
                    normal: {
                        formatter: '{c|{c}}\n{hr|}\n{d|{d}%}',
                        rich: {
                            b: {
                                fontSize: 12,
                                color: '#12EABE',
                                align: 'left',
                                padding: 4
                            },
                            hr: {
                                borderColor: '#12EABE',
                                width: '80%',
                                borderWidth: 2,
                                height: 0
                            },
                            d: {
                                fontSize: 12,
                                color: '#fff',
                                align: 'left',
                                padding: 4
                            },
                            c: {
                                fontSize: 12,
                                color: '#fff',
                                align: 'left',
                                padding: 4
                            }
                        }
                    }
                },
                /*data: [{value: 100, name: '一号渔排' }, ]*/
               data: all_yield
            }]
        };
        myChart.currentIndex = -1;
        myChart.setOption(option);
        console.log(option.series[0].data[0]);
        setInterval(function() {
            var dataLen = option.series[0].data.length;
            // 取消之前高亮的图形
            myChart.dispatchAction({
                type: 'downplay',
                seriesIndex: 0,
                dataIndex: myChart.currentIndex
            });
            myChart.currentIndex = (myChart.currentIndex + 1) % dataLen;
            // 高亮当前图形
            myChart.dispatchAction({
                type: 'highlight',
                seriesIndex: 0,
                dataIndex: myChart.currentIndex
            });
        }, 1000);

        window.addEventListener('resize', function() {
            myChart.resize();
        })
    }






})