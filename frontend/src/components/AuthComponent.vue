<template>
  <div style="width: 0; height: 0;" />
</template>

<script>
export default {
  name: "AuthComponent",
  mounted() {
    fetch("http://localhost:8000/current-user")
      .catch(_ => {
          console.log(_)
          this.$router.push("/")
        }
      )
  }
}
</script>
