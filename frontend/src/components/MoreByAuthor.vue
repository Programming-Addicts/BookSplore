<template>
    <div class="moreBook" v-if="fetched">
        <p class="top">Similar Book</p>
        <a :href="`/book-info/${book.id}`">
            <Cover
                :imgUrl="
                    book.image_links
                        ? book.image_links.thumbnail
                        : require('../assets/BookSploreIcon.svg')
                "
                height="25vw"
                width="17vw"
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
    props: ["mainBook"],
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
            book: {}
        };
    },
    mounted() {
        console.log(this.mainBook);
        fetch(
            this.$backend_url +
                `/books/search?query=inauthor:${this.mainBook.authors[0]}&limit=15&download=false&sorting=relevance`,
            {
                headers: {
                    Authorization: window.localStorage.getItem("token")
                }
            }
        )
            .then(response => response.json())
            .then(result => {
                console.log(result);
                this.book = this.filterMoreByAuthor(result, this.mainBook);
                this.fetched = true;
            })
            .catch(error => {
                console.error("more book search : ", error);
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
    height: min-content;
    width: min-content;

    margin-left: 30px;
    /* margin-right: 50px; */
    border: 1px solid #c4c4c4;
    border-radius: 10px;
    color: white;
}

a {
    cursor: pointer;
    transition: 300ms;
}
a:hover {
    transform: scale(1.05);
}
a:active {
    transform: scale(0.95);
}

.top {
    font-size: 25px;
}
.bookTitle {
    font-size: 20px;
    padding-bottom: 5px;
}

@media only screen and (max-width: 600px) {
    .cover {
        width: 65vw;
        height: 95vw;
    }
    .moreBook {
        margin: 0%;
    }
}

</style>
