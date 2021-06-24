<template>
  <div style="width: 0; height: 0;" />
</template>

<script>
export default {
  name: "AuthComponent",
  mounted() {
    fetch("https://booksplore.milind.me/users/current")
      .then(data => data.json())
      .catch(_ => {
          console.log(_)
          this.$router.push("/")
        }
      )
  }
}
</script>
