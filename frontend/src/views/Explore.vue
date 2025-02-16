<template>
    <div class="main">
        <auth-component />
        <nav-bar navbar_type="authenticated" :fixed="false" />
        <div class="searchBox" :style="scaleFont(50)">
            Explore our wide collection of Books!
            <search-box
                :endpoint="`/search/${downloadOnly ? 1 : 0}/#`"
                :height="scale(75)"
                :width="boxSize"
                :font_size="scale(35)"
            />
            <p :style="scaleFont(23)">
                <input type="checkbox" v-model="downloadOnly" />
                Only show books which are available for download
            </p>
            <recommendations />
        </div>
    </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import SearchBox from "../components/SearchBox.vue";
import Recommendations from "../components/Recommendations.vue";
import AuthComponent from "../components/AuthComponent.vue";

export default {
    name: "Explore",
    components: {
        NavBar,
        SearchBox,
        AuthComponent,
        Recommendations
    },
    data() {
        return {
            downloadOnly: false,
            boxSize: screen.width <= 760 ? `79vw` : `60vw`
        };
    },
    methods: {
        scale(num) {
            return `${(window.innerHeight * num) / 796}px`;
        },
        scaleFont(num) {
            return {
                "font-size": `${(window.innerHeight * num) / 796}px`
            };
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
    display: none;
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

@media only screen and (max-width: 600px) {
    .searchBox img {
        width: 90vw;
        padding: 30px;
    }
    .searchBox {
        font-size: 30px !important;
    }
    .searchBox p {
        font-size: 20px !important;
    }
}
</style>
