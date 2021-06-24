<template>
    <div class="bookInfo">
        <nav-bar :fixed="true" navbar_type="authenticated" />
        <div class="bookInfoMain">
            <book-info-display :Book="dummyData" />
        </div>
        <Footer></Footer>
    </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import Footer from "../components/Footer.vue";
import BookInfoDisplay from "../components/BookInfoDisplay.vue";

export default {
    name: "BookInfo",
    components: {
        NavBar,
        Footer,
        BookInfoDisplay
    },
    data() {
        return {
            dummyData: {
                cover: null,
                title: "the ballad of songbirds and snakes",
                author: "suzanne collins",
                pageCount: 2000,
                language: "english",
                published: new Date(2020, 1, 1),
                desc:
                    "Ambition will fuel him. Competition will drive him. But power has its price. It is the morning of the reaping that will kick off the tenth annual Hunger Games. In the Capitol, eighteen-year-old Coriolanus Snow is preparing for his one shot at glory as a mentor in the Games",
            }
        };
    }
};
</script>

<style scoped>
.bookInfoMain {
    padding-top: 80px;
}
</style>
