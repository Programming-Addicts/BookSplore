<template>
    <div class="recent" v-if="fetched">
        <p class="readsTitle">Your Reads</p>
        <div class="bookList" v-if="books.length > 0">
            <div v-for="(book, index) in books" :key="index" class="book">
                <img
                :src="book.image_links.smallThumbnail ? book.image_links.smallThumbnail : require('../assets/BookSploreIcon.svg')"
                :height="scaleHeight(45)"
                />
                <a :href="`/book-info/${book.book_id}`" :style="scaleFont(23)">
                    {{
                        book.title.length > 29
                            ? book.title.slice(0, 23) + " . . ."
                            : book.title
                    }}
                </a>
            </div>
        </div>
        <div v-if="books.length == 0" style="color: white;">
            No books read recently
        </div>
    </div>
</template>

<script>
export default {
    name: "RecentBooks",
    data() {
        return {
            books: null,
            fetched: false
        };
    },
    methods: {
        scaleFont(num) {
            return {
                "font-size": `${(num * window.innerHeight) / 796}px`
            };
        },
        scaleHeight(num) {
            return (num * window.innerHeight) / 796;
        }
    },
    created() {
        fetch(this.$backend_url + "/users/get", {
            headers: {
                Authorization: window.localStorage.getItem("token")
            }
        })
            .then(response => response.json())
            .then(data => {
                fetch(
                    this.$backend_url +
                        `/users/recent-books?user_id=${data.id}`,
                    {
                        headers: {
                            Authorization: window.localStorage.getItem("token")
                        }
                    }
                )
                    .then(response => response.json())
                    .then(data => {
                        this.books = data;
                        this.fetched = true;
                    });
            });
    }
};
</script>

<style scoped>
.recent {
    display: flex;
    flex-direction: column;
    position: fixed;
    padding-top: 80px;
    padding-right: 5px;
    width: 27%;
    height: 100%;
    border-right: 2px solid white;
    font-family: Lato;
    align-items: center;
}

.readsTitle {
    font-weight: 600;
    font-size: 30px;
    color: white;
}

.bookList {
    display: flex;
    flex-direction: column;
    margin-top: 0px;
    width: 100%;
    row-gap: 10px;
    height: 100%;
    margin-bottom: 21%;
    padding-bottom: 20px;
    overflow-y: scroll;
    margin-right: 6px;
    padding-top: 10px;
}

.bookList div {
    display: flex;
    flex-direction: row;
    align-items: center;
    font-family: Lato;
    font-weight: 600;
    font-style: normal;
    column-gap: 10px;
    margin-left: 32px;
    padding-bottom: 0%;
    margin-bottom: 0%;
    cursor: pointer;
    color: #a2dcee;
}
.bookList div a {
    margin: 0%;
    color: inherit;
}
.bookList div:hover {
    text-decoration: underline;
}
.bookList div a:link {
    text-decoration: none;
}
.bookList div img {
    margin: 0%;
}
</style>
