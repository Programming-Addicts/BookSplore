<template>
  <div class="dashboard">
    <nav-bar :fixed="true" navbar_type="authenticated" />
    <div class="recentBooks">
      <recent-books :books="UserBooks" />
    </div>
    <div class="timeline">
      <timeline />
    </div>
  </div>
</template>

<script>
// import AuthComponent from "../components/AuthComponent.vue"
import RecentBooks from "../components/RecentBooks.vue";
import NavBar from "../components/NavBar.vue";
import Timeline from "../components/Timeline.vue";

export default {
  name: "Dashboard",
  components: {
    RecentBooks,
    NavBar,
    Timeline,
    // AuthComponent
  },
  data() {
    return {
      UserBooks: [
        {
          "name": "Writing a Compiler in Go",
          "link": "#"
        },
        {
          "name": "The Hunger Games",
          "link": "#"
        },
        {
          "name": "Immortals of Meluha",
          "link": "#"
        },
        {
          "name": "My Experiences With Truth",
          "link": "#"
        }
      ],
    };
  },
};
</script>

<style scoped>
.recentBooks {
    width: 25%;
}
.timeline {
    width: 75%;
    padding-bottom: 100px;
}
</style>
