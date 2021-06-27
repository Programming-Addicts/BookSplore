<template>
    <div class="moreBook" v-if="fetched">
        <p class="top">Similar Book</p>
        <a :href="`/dev/book-info/${book.id}`">
            <Cover
                :imgUrl="book.image_links.thumbnail"
                :height="300"
                :width="200"
            />
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
    props: ["mainBook", "backend_url"],
    methods: {
        filterMoreByAuthor: (bookArray, mainBook) => {
            const arr = bookArray.filter((value, index, arr) => {
                index;
                arr;
                return value.id !== mainBook.id;
            });
            return arr[Math.floor(Math.random() * arr.length)];
        }
    },
    data() {
        return {
            fetched: false,
            book: {},
        };
    },
    mounted() {
        console.log(this.mainBook);
        fetch(
            this.backend_url + `/books/search?query=inauthor:${this.mainBook.authors[0]}&limit=10&download=false&sorting=relevance`
        )
            .then(response => response.json())
            .then(result => {
                console.log(result);
                this.book = this.filterMoreByAuthor(result, this.mainBook);
                this.fetched = true;
            })
            .catch(error => {
                this.fetched = true;
                console.error(error);
            });
    }
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
    width: min-content;
    height: min-content;

    margin-left: 30px;
    margin-right: 50px;
    border: 1px solid #c4c4c4;
    border-radius: 10px;
    color: white;
    cursor: pointer;
}
.top {
    font-size: 25px;
}
.bookTitle {
    font-size: 20px;
    padding-bottom: 5px;
}
</style>
