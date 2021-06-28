<template>
    <div class="main">
        <nav-bar navbar_type="authenticated" />
        <div class="searchBox">
            Explore our wide collection of Books!
            <search-box />
            <p>
                <input type="checkbox" v-model="downloadOnly" />
                Only show books which are available for download
            </p>
            <img :src="require(`../assets/searching.svg`)" />
        </div>
        <Footer />
    </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import Footer from "../components/Footer.vue";
import SearchBox from "../components/SearchBox.vue";

export default {
    name: "Explore",
    components: {
        NavBar,
        Footer,
        SearchBox
    },
    data() {
        return {
            downloadOnly: false
        };
    }
};
</script>

<style scoped>
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

    font-size: 50px;
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
    transform: scale(2);
    -ms-transform: scale(2);
    -webkit-transform: scale(2);
}
</style>
