<template>
  <div class="dashboard" :style="cssVars">
    <nav-bar :fixed="true" />
    <recent-books :books="UserBooks" />
  </div>
</template>

<script>
import RecentBooks from "../components/RecentBooks.vue";
import NavBar from "../components/NavBar.vue";

export default {
  name: "Dashboard",
  components: {
    RecentBooks,
    NavBar,
  },
  data() {
    return {
      UserBooks: [
        {
          "name": "boooooooooooo0ooooooooooooo oooooook",
          "link": "#"
        },
        {
          "name": "book",
          "link": "#"
        },
        {
          "name": "book",
          "link": "#"
        },
        {
          "name": "book",
          "link": "#"
        },
        {
          "name": "book",
          "link": "#"
        },
        {
          "name": "book",
          "link": "#"
        },
        {
          "name": "book",
          "link": "#"
        },
        {
          "name": "book",
          "link": "#"
        },
        {
          "name": "book",
          "link": "#"
        },
      ],
    };
  },
};
</script>


<style scoped>
</style>