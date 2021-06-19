<template>
		<router-view />
</template>

<script>
export default {
	name: "App",
  mounted() {
    this.$session.start()
    console.log(this.$session.getAll())
  }
};
</script>

<style scoped>
</style>
