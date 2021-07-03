<template>
	
	<div style="width: 100%;">
		<nav-bar :fixed="false" navbar_type="authenticated" />
		<div class="container">
			
			<div style="display: flex; justify-self: center;" class="previous-page">
				<img src="../assets/submitArrow.svg" @click="movePage(-1)" />
			</div>
			
			<div id="view" :style="containerStyles()" />
			
			<div style="display: flex; justify-self: center;" class="next-page" >
				<img src="../assets/submitArrow.svg" @click="movePage(1)" />
			</div>
		
		</div>
		<div class="note">Note: This webreader is provided by the Google API</div>
	</div>

</template>

<script>

import NavBar from "../components/NavBar.vue"

export default {
	name: "ReadOnline",
	components: {
		NavBar
	},
	mounted() {
		google.books.load();
		google.books.setOnLoadCallback(this.initializeWebReader);
	},
	data() {
		return {
			viewer: null
		}
	},
	methods: {
		initializeWebReader() {
			this.viewer = new google.books.DefaultViewer(document.getElementById("view"))
			this.viewer.load(`ISBN:${this.$route.params.isbn}`, () => this.$router.push('/404'))
		},
		containerStyles() {
			return {
				"margin": "auto",
				"width": `${0.65 * window.innerWidth}px`,
				"height": `${window.innerHeight - 100}px`,
				"padding-top": "30px"
			}
		},
		movePage(num) {
			if (num == 1) {
				this.viewer.nextPage()
			} else {
				this.viewer.previousPage()
			}
		}
	}
}


</script>

<style scoped>

.previous-page img {
	transform: rotate(180deg);
	margin-right: 20px;
}

.next-page img {
	margin-left: 20px;
}

img {
	cursor: pointer;
}

img:active {
	overflow: visible;
}

.container {
	margin-left: 20px;
	display: flex;
	justify-content: center;
}

.note {
	padding-top: 20px;
	padding-bottom: 20px;
	width: 100%;
	text-align: center;

	color: white;
	font-size: 20px;
	font-family: Lato;
}

* {
	overflow: hidden;
}
</style>
