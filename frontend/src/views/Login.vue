<template>
  <div :style="getHeight()">
    <nav-bar v-bind:centred="true"/>
    <login-background />
    <input-box v-model="email" />
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import LoginBackground from "../components/LoginBackground.vue";
import InputBox from "../components/InputBox.vue"

export default {
  name: "Login",
	components: {
    NavBar,
    LoginBackground,
    InputBox
  },
  data(){
    return {
      email: "youremail@example.com"
    }
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
