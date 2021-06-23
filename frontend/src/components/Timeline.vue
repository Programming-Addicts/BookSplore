<template>
    <div class="timeline">
        <!--div class="events" v-for="(ev, index) of Events" :key="index"-->
        <!--event :user="Events[0].user"/-->
        <!--/div-->
    </div>
</template>

<script>

class BEvent {
  constructor(user, eventType, eventDescription, eventTarget, imageUrl) {
    this.user = user;
    this.eventType = eventType;
    this.eventDescription = eventDescription;
    this.eventTarget = eventTarget;
    this.imageUrl = imageUrl;
  }
}

//import Event from "./Event.vue";

export default {
    name: "Timeline",
    // props: ["events"],
    components: {
        //Event
    },
    data() {
      return {
        "Events": [
          BEvent("Milind", "follow", "5 books, 32 followers, @class PythonAddict", "@/assets/ProfilePicture.svg")
        ]
      }
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
    position: relative;
}
</style>
