<script setup>
import {onMounted, watch, ref} from 'vue';
import {useSinChart} from "../composables/useSinChart.js";
import {useWebsocketPoint} from "../composables/useWebsocketPoint.js";

const chartContainer = ref(null);
const point = useWebsocketPoint();

let chart;
onMounted(() => {
  chart = useSinChart(chartContainer)
});

watch(() => point.value, (newPoint) => {
  if (!(newPoint && chart))
    return;

  const series = chart.series[0];
  const shift = series.data.length > 200;

  series.addPoint(newPoint, true, shift);
}, {deep: true});
</script>

<template>
  <div class="chart-container" ref="chartContainer"></div>
</template>

<style scoped>
.chart-container {
  width: 100vh;
  height: 400px;
}
</style>