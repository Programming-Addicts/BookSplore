<template>
  <div :style="getHeight()">
    <nav-bar v-bind:centred="true"/>
    <login-background />
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import LoginBackground from "../components/LoginBackground.vue";

export default {
  name: "SignUp",
	components: {
    NavBar,
    LoginBackground
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
