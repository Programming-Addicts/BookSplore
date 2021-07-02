<template>
	<table style="width: 100%; height: 100%;">
		<tr>
			<router-view/>
		</tr>
		<tr>
			<Footer v-if="$route.path != '/dashboard'" />
		</tr>
	</table>
</template>

<script>

import Footer from "@/components/Footer.vue"

export default {
	name: "App",
	components: {
		Footer
	},
	methods: {
		getHeight() {
			return {
				width: "100%",
				height: `${window.innerHeight}px`,
			}
		}
	}
};
</script>

<style scoped>
</style>
