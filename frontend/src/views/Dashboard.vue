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
        "booooooooooooooooooooooooooooooooooooook",
        "book1",
        "book2",
        "book3",
        "book4",
        "book5",
        "book",
        "book",
        "book",
        "book",
        "book",
      ],
    };
  },
};
</script>


<style scoped>
</style>