import Highcharts from "highcharts";

export function useSinChart(chartContainer) {
    return Highcharts.chart(chartContainer.value, {
        chart: {
            type: 'line',
            animation: false
        },
        legend: {
            enabled: false,
        },
        title: {
            text: 'Live sin chart'
        },
        xAxis: {
            title: {
                text: 'x'
            }
        },
        yAxis: {
            title: {
                text: 'f(x)'
            }
        },
        series: [{
            name: 'f(x) = sin(x)',
            data: []
        }]
    });
}