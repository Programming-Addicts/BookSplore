<template>
    <div class="main">
		<auth-component />
        <nav-bar navbar_type="authenticated" :fixed="false" />
        <div class="searchBox" :style="scaleFont(50)">
            Explore our wide collection of Books!
            <search-box
			:endpoint="`/search/${(downloadOnly ? 1 : 0)}/#`"
			:height="scale(75)"
			:font_size="scale(35)"
            />
            <p :style="scaleFont(23)">
                <input type="checkbox" v-model="downloadOnly" />
                Only show books which are available for download
            </p>
            <img :src="require(`../assets/searching.svg`)" />
        </div>
    </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import SearchBox from "../components/SearchBox.vue";
import AuthComponent from "../components/AuthComponent.vue"


export default {
    name: "Explore",
    components: {
        NavBar,
        SearchBox,
		AuthComponent
    },
    data() {
        return {
            downloadOnly: false
        };
    },
	methods: {
		scale(num) {
			return `${window.innerHeight * num / 796}px`
		},
		scaleFont(num) {
			return {
				"font-size": `${window.innerHeight * num / 796}px`
			}
		}
	}
};
</script>

<style scoped>

* {
	font-family: Lato;
}

.main {
    height: 100%;
    width: 100%;
    font-family: Lato;
    color: white;
}

.searchBox {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 0%;
    padding: 0%;
    margin-top: 40px;
    align-items: center;
    justify-content: center;
    text-align: center;

    font-weight: 500;
    row-gap: 50px;
}

.searchBox img {
    padding: 30px;
}

.searchBox p {
    font-size: 20px;
    padding: 0%;
    margin: 0%;
}
.searchBox p input[type="checkbox"] {
    background-color: gray;
    padding: 5px;
    margin-right: 10px;
    transform: scale(2);
    -ms-transform: scale(2);
    -webkit-transform: scale(2);
}
</style>
