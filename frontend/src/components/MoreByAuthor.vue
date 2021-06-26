<template>
    <div class="moreBook" v-on:click="$router.push(`/dev/book-info/${book.id}`);$router.go()">
        <p class="top">Similar Books</p>
        <a :href="`/dev/book-info/${book.id}`">
        <Cover :imgUrl="book.image_links.thumbnail" :height="300" :width="200" />
        </a>
        <p class="bookTitle">{{ book.title }}</p>
    </div>
</template>

<script>
import Cover from "./Cover.vue";

export default {
    name: "MoreByAuthor",
    components: {
        Cover
    },
    props: ["book"],
};
</script>

<style scoped>
.moreBook {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-family: Lato;
    padding-left: 40px;
    padding-right: 40px;

    border: 1px solid #C4C4C4;
    border-radius: 10px;
    color: white;
    cursor: pointer;
}
.top {
    font-size: 25px;
}
.bookTitle {
    font-size: 20px;
}

</style>
