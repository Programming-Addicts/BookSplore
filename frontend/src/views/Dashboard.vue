<template>
    <div class="dashboard">
        <nav-bar :fixed="true" />
        <div class="recentBooks">
            <recent-books :books="UserBooks" />
        </div>
        <div class="timeline">
            <timeline />
            </div>
    </div>
</template>

<script>
import RecentBooks from "../components/RecentBooks.vue";
import NavBar from "../components/NavBar.vue";
import Timeline from "../components/Timeline.vue";

export default {
    name: "Dashboard",
    components: {
        RecentBooks,
        NavBar,
        Timeline
    },
    data() {
        return {
            UserBooks: [
                {
                    name: "boooooooooooo0ooooooooooooo oooooook",
                    link: "#"
                },
                {
                    name: "book",
                    link: "#"
                },
                {
                    name: "book",
                    link: "#"
                },
                {
                    name: "book",
                    link: "#"
                },
                {
                    name: "book",
                    link: "#"
                },
                {
                    name: "book",
                    link: "#"
                },
                {
                    name: "book",
                    link: "#"
                },
                {
                    name: "book",
                    link: "#"
                },
                {
                    name: "book",
                    link: "#"
                }
            ]
        };
    }
};
</script>

<style scoped>
.recentBooks {
    width: 25%;
}
.timeline {
    width: 75%;
    height: 100%;
    padding-bottom: 100px;
}
</style>
