<template>
    <div class="timeline">
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
.timeline {
    position: fixed;
    right: 0%;
    margin-bottom: 10%;
    top: 80px;
    width: inherit;
    height: min-content;
}
.events {
    height: inherit;
    display: flex;
    flex-direction: column;
}
.events .empty{
    position: relative;
}
</style>
