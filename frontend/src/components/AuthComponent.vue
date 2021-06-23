<template>
  <div style="width: 0; height: 0;" />
</template>

<script>
export default {
  name: "AuthComponent",
  mounted() {
    fetch("http://127.0.0.1:8000/current-user")
      .catch(_ => {
          console.log(_)
          this.$router.push("/")
        }
      )
  }
}
</script>
