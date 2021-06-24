<template>
    <div class="timeline-inner">
        <div class="events" v-for="(ev, index) of SubscribedEvents" :key="index">
          <event
          :user="ev.user"
          :eventType="ev.eventType"
          :eventDescription="ev.eventDescription"
          :eventTarget="ev.eventTarget"
          :imageUrl="ev.imageUrl"
          />
        </div>
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

import Event from "./Event.vue";

export default {
    name: "Timeline",
    // props: ["events"],
    components: {
        Event
    },
    data() {
      return {
        SubscribedEvents: [
          new BEvent(
              "Milind",
              "follow",
              "5 books, 32 followers",
              "class PythonAddict",
              require("../assets/ProfilePicture.svg")
          ),
          new BEvent(
              "Milind",
              "follow",
              "5 books, 32 followers",
              "class PythonAddict",
              require("../assets/ProfilePicture.svg")
          ),
          new BEvent(
              "Milind",
              "follow",
              "5 books, 32 followers",
              "class PythonAddict",
              require("../assets/ProfilePicture.svg")
          ),
          new BEvent(
              "Milind",
              "follow",
              "5 books, 32 followers",
              "class PythonAddict",
              require("../assets/ProfilePicture.svg")
          ),
          new BEvent(
              "Milind",
              "follow",
              "5 books, 32 followers",
              "class PythonAddict",
              require("../assets/ProfilePicture.svg")
          ),
          new BEvent(
              "Milind",
              "follow",
              "5 books, 32 followers",
              "class PythonAddict",
              require("../assets/ProfilePicture.svg")
          )
        ]
      }
    }
}
</script>

<style scoped>
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
