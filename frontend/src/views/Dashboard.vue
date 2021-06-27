<template>
  <div class="dashboard">
    <auth-component />
    <nav-bar :fixed="true" navbar_type="authenticated" />
    <recent-books :books="UserBooks"/>
    <table style="width: 100%;"><tr>
      <td class="recent-books" style="width: 30%;">
      </td>
      <td>
        <timeline />
      </td>
    </tr></table>
  </div>
</template>

<script>
import AuthComponent from "../components/AuthComponent.vue"
import RecentBooks from "../components/RecentBooks.vue";
import NavBar from "../components/NavBar.vue";
import Timeline from "../components/Timeline.vue";

export default {
  name: "Dashboard",
  components: {
    RecentBooks,
    NavBar,
    Timeline,
    AuthComponent
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
        },
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
        },
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

.recent-books {
  width: 25%;
}

</style>
