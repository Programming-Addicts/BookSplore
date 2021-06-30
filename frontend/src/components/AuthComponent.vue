<template>
  <div style="width: 0; height: 0;" />
</template>

<script>
export default {
  name: "AuthComponent",
  mounted() {
    console.log(window.localStorage.getItem("token"))
  }
}
</script>
