<template>
  <div style="height: 100%;">
    <nav-bar :fixed="false"/>
      <landing-page />
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import LandingPage from "../components/LandingPage.vue";

export default {
  name: "Home",
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
