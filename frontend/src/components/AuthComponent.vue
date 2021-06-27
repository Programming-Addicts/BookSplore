<template>
  <div style="width: 0; height: 0;" />
</template>

<script>
export default {
  name: "AuthComponent",
  mounted() {
    fetch(this.$backend_url + "/users/current")
    .then(
        data => {
            if (!data.ok) {
                this.$router.push('/')
            }
        }
    )
  }
}
</script>
