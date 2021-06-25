<template>
    <div class="moreBook">
        <p class="top">More By Author</p>
        <Cover :imgUrl="cover" :height="300" :width="200" />
        <p class="bookTitle">{{ title }}</p>
    </div>
</template>

<script>
import Cover from "./Cover.vue";

export default {
    name: "MoreByAuthor",
    components: {
        Cover
    },
    props: ["cover", "title"]
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
}
.top {
    font-size: 25px;
}
.bookTitle {
    font-size: 20px;
}

</style>
