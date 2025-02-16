<template>
    <div class="timeline-inner">
        <div v-if="events.length > 0">
            <div
                class="events"
                v-for="(ev, index) of SubscribedEvents"
                :key="index"
            >
                <event
                    :user="ev.user"
                    :eventType="ev.eventType"
                    :eventDescription="ev.eventDescription"
                    :eventTarget="ev.eventTarget"
                    :imageUrl="ev.imageUrl"
                />
            </div>
        </div>
        <div>
            <img :src="require('../assets/NoData.svg')" />
        </div>
    </div>
</template>

<script>
import Event from "./Event.vue";

export default {
    name: "Timeline",
    components: {
        Event
    },
    data() {
        return {
            events: null
        };
    },
    created() {
        fetch(this.$backend_url + "/users/events", {
            headers: {
                Authorization: window.localStorage.getItem("token")
            }
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            });
    }
};
</script>

<style scoped>
* {
    font-family: Lato;
}

.timeline-inner {
    width: 100%;
    padding: 0;
    margin: 0;
    margin-top: 100px;
}

.events {
    height: inherit;
}
</style>
