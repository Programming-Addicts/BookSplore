<template>
	<div style="width: 100%; height: 100%;">
	    <router-view/>
		<Footer v-if="$route.path != '/dashboard'" />
	</div>
</template>

<script>

import Footer from "@/components/Footer.vue"

export default {
	name: "App",
	components: {
		Footer
	}
};
</script>

<style scoped>
</style>
