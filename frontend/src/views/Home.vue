<template>
  <div style="height: 100%;">
    <nav-bar/>
      <landing-page :backend_url="backend_url"/>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import LandingPage from "../components/LandingPage.vue";

export default {
  name: "Home",
  data() {
    return {
      backend_url: "https://booksplore.milind.me"
    }
  },
	components: {
    NavBar,
    LandingPage
  },
  methods: {
    getHeight() {
      return {
        "height": `${window.innerHeight}px`
      }
    }
  }
};
</script>

<style>
</style>
