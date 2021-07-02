<template>
	<div>
		<router-view />
		<Footer v-if="$route.path != '/dashboard'" />
	</div>
</template>

<script>

import Footer from "./components/Footer.vue"

export default {
    name: "App",
	components: {
		Footer
	}
};
</script>

<style scoped>
</style>
