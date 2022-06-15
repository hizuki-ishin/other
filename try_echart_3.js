// import { data } from "../data/timeseries.js";

const response = await axios.get("http://localhost:8000/future");
// console.log(response["data"]);
// const dataObj = response["data"];
// console.log(dataObj);
console.log(response["data"]);

const { baseDate, dateSeries, actualSeries, predictSeries, diffSeries } = response["data"];

let option = {
  // Make gradient line here

  title: [
    {
      left: "center",
      text: "Gradient along the y axis",
    },
  ],
  // width: 500,
  // height: 400,
  respoinsive: true,
  tooltip: {
    trigger: "axis",
  },
  xAxis: [
    {
      data: dateSeries,
    },
  ],
  yAxis: [{}],
  grid: [
    {
      bottom: "60%",
    },
  ],
  series: [
    {
      type: "line",
      showSymbol: false,
      data: actualSeries,
    },
    {
      type: "line",
      showSymbol: false,
      data: predictSeries,
    },
    {
      type: "bar",
      showSymbol: false,
      data: diffSeries,
      itemStyle: {
        // Color of the point.
        color: "#aaa",
      },
      emphasis: {
        itemStyle: {
          color: "orange",
        },
      },
    },
  ],
};

var myChart = echarts.init(document.getElementById("main"));

window.onresize = function () {
  myChart.resize();
};

myChart.setOption(option);
