<template>
	<div class="navbar-container">
		<div class="title-container">
			<div class="logo-container">
				<img src="../assets/BookSploreIcon.svg" />
				<span class="title bold">Book</span>
				<span class="title italic">Splore</span>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "NavBar",
};
</script>

<style scoped>
.navbar-container {
	border-bottom: 1px white solid;
}

.title-container {
	display: flex;
	justify-content: center;
	width: fit-content;
	/*  float: left; */
}

.logo-container {
	display: flex;
	justify-content: center;
	align-self: left;
	padding: 10px;
}

.title {
	height: 100%;
	font-family: "Lato";
	font-size: 37px;
	text-align: center;
}

.bold {
	font-weight: bold;
}

.italic {
	font-style: italic;
}
</style>
