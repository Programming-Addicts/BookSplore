<template>
  <div style="width: 0; height: 0;" />
</template>

<script>
export default {
  name: "AuthComponent",
  props: ["backend_url"],
  mounted() {
    fetch("https://localhost:8000/users/current")
      .catch(_ => {
          console.log(_)
          this.$router.push("/")
        }
      )
  }
}
</script>
