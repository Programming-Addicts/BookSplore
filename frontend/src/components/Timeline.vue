<template>
    <div class="timeline">
        <div class="events">
        <event />
        <event />
        <event />
        <event />
        <event />
        <div class="empty"></div>
</div>
    </div>
</template>

<script>
import Event from "./Event.vue";
export default {
    name: "Timeline",
    props: ["events"],
    components: {
        Event
    }
}
</script>

<style scoped>
.timeline {
    position: fixed;
    right: 0%;
    margin-bottom: 10%;
    top: 80px;
    width: inherit;
    /* height: 100%; */
}
.events {
    height: inherit;
    overflow: scroll;

    display: flex;
    flex-direction: column;

    padding-bottom: 100px;
}
.events .empty{
    height: 500px;
    position: relative;
}
</style>