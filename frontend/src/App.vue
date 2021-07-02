<template>
    <div class="outerMost">
        <div class="r">
            <router-view />
        </div>
        <div class="f">
            <Footer v-if="$route.path != '/dashboard'" />
        </div>
    </div>
</template>

<script>
import Footer from "@/components/Footer.vue";

export default {
    name: "App",
    components: {
        Footer
    },
    methods: {
        getHeight() {
            return {
                width: "100%",
                height: `${window.innerHeight}px`
            };
        }
    }
};
</script>

<style scoped>
.outerMost {
    display: flex;
    flex-direction: column;
    width: 100%;
    justify-content: space-between;
}
.outerMost .f {
    margin-top: auto;
    position: relative;
}
.outerMost .r {
    margin-bottom: auto;
}
</style>
