import {ref} from "vue";

export function useWebsocketPoint() {
    const socket = new WebSocket("ws://localhost:8080/sin");
    const point = ref([]);

    socket.onopen = () => {
        console.log("WS connection opened");
    };

    socket.onclose = () => {
        console.log("WS connection closed");
    };

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);

        point.value = [data.x, data.y];
    };

    return point;
}