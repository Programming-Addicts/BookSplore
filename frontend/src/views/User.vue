<template>
<div>
    <nav-bar navbar_type="authenticated" />
    <main>

    </main>
    <Footer></Footer>
</div>
</template>

<script>
import NavBar from "../components/NavBar.vue"
import Footer from "../components/Footer.vue"
// import Cover from "../components/Cover.vue"
// import Review from "../components/Review.vue"

export default {
    name: "User",
    components: {
        NavBar,
        Footer,
        // Review,
        // Cover,
    },
}
</script>