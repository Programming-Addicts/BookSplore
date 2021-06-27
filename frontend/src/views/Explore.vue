<template>
    <div class="main">
        <nav-bar navbar_type="authenticated"/>
        <div class="searchBox">
            Explore our wide collection of Books!
            <search-box />
        </div>
        <div class="footer">
        <Footer />
        </div>
    </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import Footer from "../components/Footer.vue";
import SearchBox from "../components/SearchBox.vue"

export default {
    name: "Explore",
    components: {
        NavBar,
        Footer,
        SearchBox
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
    margin-top: 50px;
    align-items: center;
    justify-content: center;

    font-size: 50px;
    font-weight: 500;
    row-gap: 50px;
}
.footer {
    bottom: 0%;
    position: fixed;
}

</style>
