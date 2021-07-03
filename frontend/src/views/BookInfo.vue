<template>
    <div class="bookInfo" v-if="fetched" :style="cssVars(bookData)">
        <auth-component />
        <nav-bar :fixed="false" navbar_type="authenticated" :currentUser="currentUser" />
        <div class="bookInfoMain">
            <book-info-display :Book="bookData" />
            <div class="downloadButtons">
                <button id="pdf" v-on:click="readOnline()">
                    Read Online
                </button>
                <button
                    id="WebReader"
                    v-on:click="getWebReader(bookData.preview_link)"
                >
                    Preview
                </button>
            </div>
            <div class="bottomSection">
                <book-reviews :bookData="bookData" :currentUser="currentUser" />
                <more-by-author :mainBook="bookData" />
            </div>
        </div>
    </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import BookInfoDisplay from "../components/BookInfoDisplay.vue";
import BookReviews from "../components/BookReviews.vue";
import MoreByAuthor from "../components/MoreByAuthor.vue";
import AuthComponent from "../components/AuthComponent.vue";

export default {
    name: "BookInfo",
    components: {
        NavBar,
        BookInfoDisplay,
        BookReviews,
        MoreByAuthor,
        AuthComponent
    },
    data() {
        return {
            bookData: {},
            fetched: false,
            currentUser: {},
        };
    },
    methods: {
		readOnline() {
			window.location.href = `/read/${this.bookData.isbns[0].identifier}`
        },
        getWebReader: preview_link => {
            if (preview_link) {
                window.location.href = preview_link;
            }
        },
        cssVars: book => {
            let color = {
                background: "#7fb6f8",
                font: "black"
            };
            let gray = {
                background: "#95979A",
                font: "#444444"
            };
            return {
                "--pdf-button-color": color.background,
                "--WebReader-button-color": book.preview_link
                    ? color.background
                    : gray.background,

                "--pdf-font-color": color.font,
                "--WebReader-font-color": book.preview_link
                    ? color.font
                    : gray.font
            };
        }
    },
    created() {
        fetch(
            this.$backend_url + `/books/get?book_id=${this.$route.params.id}`,
            {
                headers: {
                    Authorization: window.localStorage.getItem("token")
                }
            }
        )
            .then(response => {
                if (!response.ok) {
                    this.$router.push("/404");
                }
                return response.json();
            })
            .then(result => {
                console.log(result);
                this.bookData = result;

                // for checking info about the user viewing the page -------
                fetch(this.$backend_url + `/users/get`, {
                    headers: {
                        Authorization: window.localStorage.getItem("token")
                    }
                })
                    .then(response => response.json())
                    .then(result_ => {
                        this.currentUser = result_;
                        console.log("current user :" , this.currentUser);
                        this.fetched = true;
                    })
                    .catch(error => {
                        console.error("current user: ", error);
                    });
                // ---------------------------------------------------------

            })
            .catch(error => {
                this.$router.push("/404");
                console.error(error);
            });
    }
};
</script>

<style scoped>
.bookInfoMain {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.downloadButtons {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    margin-bottom: 3%;
}
.downloadButtons button {
    background: #7fb6f8;
    border: none;
    border-radius: 10px;
    padding: 1.5%;
    width: fit-content;

    font-family: Lato;
    font-size: 3vh;
    font-weight: 400;

    cursor: pointer;
    transition: 300ms;
}
.downloadButtons button:hover {
    transform: scale(1.1);
}
.downloadButtons button:active {
    transform: scale(0.8);
}
.downloadButtons #pdf {
    background: var(--pdf-button-color);
    color: var(--pdf-font-color);
}
.downloadButtons #Epub {
    background: var(--Epub-button-color);
    color: var(--Epub-font-color);
}
.downloadButtons #WebReader {
    background: var(--WebReader-button-color);
    color: var(--WebReader-font-color);
}

.bottomSection {
    display: flex;
    flex-direction: row;
    margin: 5vw;
    justify-content: space-evenly;
}
</style>
