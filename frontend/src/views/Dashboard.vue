<template>
  <div class="dashboard">
    <!--- auth-component --->
    <nav-bar :fixed="true" navbar_type="authenticated" />
    <recent-books :books="UserBooks" />
  </div>
</template>

<script>
// import AuthComponent from "../components/AuthComponent.vue"
import RecentBooks from "../components/RecentBooks.vue";
import NavBar from "../components/NavBar.vue";

export default {
  name: "Dashboard",
  components: {
    RecentBooks,
    NavBar,
    // AuthComponent
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
