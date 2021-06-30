<template>
    <div style="height: 100%;">
        <nav-bar :fixed="false"/>
        <landing-page />
    </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import LandingPage from "../components/LandingPage.vue";

export default {
    name: "Home",
	components: {
        NavBar,
        LandingPage
    },
    methods: {
        getHeight() {
            return {
                "height": `${window.innerHeight}px`
            }
        }
    },
    mounted() {
        let msg = this.$route.query.msg
        if (msg) {
            alert(msg)
            this.$router.push("/")
        }

        let token = window.localStorage.getItem("token")
        if (token) {
            this.$router.push("/dashboard")
        }
    }
};
</script>
