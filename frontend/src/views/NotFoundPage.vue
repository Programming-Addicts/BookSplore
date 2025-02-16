<template>
    <div
        style="width: 100%; color: white; display: flex; flex-direction: column;"
    >
        <h1 style="width: 100%; text-align: center;">Page Not Found</h1>
        <h4 style="width: 100%; text-align: center;">
            Looks like you followed a broken link. Click
            <router-link to="/dashboard">here</router-link> to go back to
            safety.
        </h4>
        <img src="../assets/404_error.svg" :height="height - 200" />
    </div>
</template>

<script>
export default {
    name: "NotFoundPage",
    data() {
        return {
            height: window.innerHeight
        };
    }
};
</script>

<style scoped>
* {
    font-family: Lato;
}

a {
    text-decoration: none;
    color: #9dd4f2;
}
</style>
