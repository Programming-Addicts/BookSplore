<template>
    <div class="bookInfo" :style="cssVars(bookData)">
        <nav-bar :fixed="true" navbar_type="authenticated" />
        <div class="bookInfoMain" v-if="fetched">
            <book-info-display :Book="bookData" />
            <div class="downloadButtons">
                <button id="pdf" v-on:click="getPdf(bookData.pdf)">
                    Download Ebook as PDF
                </button>
                <button id="Epub" v-on:click="getEpub(bookData.epub)">
                    Download Ebook as Epub
                </button>
                <button
                    id="WebReader"
                    v-on:click="getWebReader(bookData.preview_link)"
                >
                    Read on WebReader
                </button>
            </div>
            <div class="bottomSection">
                <book-reviews :bookData="bookData" />
                <more-by-author :book="moreBook" />
            </div>
        </div>
        <Footer />
    </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import Footer from "../components/Footer.vue";
import BookInfoDisplay from "../components/BookInfoDisplay.vue";
import BookReviews from "../components/BookReviews.vue";
import MoreByAuthor from "../components/MoreByAuthor.vue";

export default {
    name: "BookInfo",
    components: {
        NavBar,
        Footer,
        BookInfoDisplay,
        BookReviews,
        MoreByAuthor
    },
    data() {
        return {
            dummyData: {
                cover: null,
                title: "The ballad of songbirds and snakes",
                author: "suzanne collins",
                pageCount: 2000,
                language: "english",
                published: new Date(2020, 1, 1),
                desc:
                    "Ambition will fuel him. Competition will drive him. But power has its price. It is the morning of the reaping that will kick off the tenth annual Hunger Games. In the Capitol, eighteen-year-old Coriolanus Snow is preparing for his one shot at glory as a mentor in the Games Ambition will fuel him. Competition will drive him. But power has its price. It is the morning of the reaping that will kick off the tenth annual Hunger Games. In the Capitol, eighteen-year-old Coriolanus Snow is preparing for his one shot at glory as a mentor in the Games",
                pdf: " ",
                Epub: null,
                WebReader: " "
            },
            bookData: {},
            fetched: false,
            moreBook: {}
        };
    },
    methods: {
        getPdf: pdfData => {
            if (pdfData.acsTokenLink) {
                window.location.href = pdfData.acsTokenLink;
            }
        },
        getEpub: epubData => {
            if (epubData.acsTokenLink) {
                window.location.href = epubData.acsTokenLink;
            }
        },
        getWebReader: preview_link => {
            if (preview_link) {
                window.location.href = preview_link;
            }
        },
        filterMoreByAuthor: (bookArray, mainBook) => {
            const arr = bookArray.filter((value, index, arr) => {
                index;
                arr;
                return value.id !== mainBook.id;
            });
            return arr[Math.floor(Math.random() * arr.length)];
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
                "--pdf-button-color": book.pdf.acsTokenLink
                    ? color.background
                    : gray.background,
                "--Epub-button-color": book.epub.acsTokenLink
                    ? color.background
                    : gray.background,
                "--WebReader-button-color": book.preview_link
                    ? color.background
                    : gray.background,

                "--pdf-font-color": book.pdf.acsTokenLink
                    ? color.font
                    : gray.font,
                "--Epub-font-color": book.epub.acsTokenLink
                    ? color.font
                    : gray.font,
                "--WebReader-font-color": book.preview_link
                    ? color.font
                    : gray.font
            };
        }
    },
    mounted() {
        fetch(
            `http://localhost:8000/books/search?book_id=${this.$route.params.id}&limit=1&download=false&sorting=relevance`
        )
            .then(response => response.json())
            .then(result => {
                console.log(result);
                this.bookData = result;
                fetch(
                    `http://localhost:8000/books/search?query=inauthor:${this.bookData.authors[0]}&limit=10&download=false&sorting=relevance`
                )
                    .then(response => response.json())
                    .then(result => {
                        this.fetched = true;
                        console.log(result);
                        this.moreBook = this.filterMoreByAuthor(
                            result,
                            this.bookData
                        );
                    })
                    .catch(error => {
                        this.fetched = true;
                        console.error(error);
                    });
            })
            .catch(error => {
                console.error(error);
            });
    }
};
</script>

<style scoped>
.bookInfoMain {
    padding-top: 80px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.downloadButtons {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    width: 100%;
    margin-bottom: 3%;
}
.downloadButtons button {
    background: #7fb6f8;
    border: none;
    border-radius: 10px;
    padding: 1.5%;
    width: fit-content;

    font-family: Lato;
    font-size: 30px;
    font-weight: 400;

    cursor: pointer;
    transition: 300ms;
}
.downloadButtons button:active {
    transform: scale(0.9);
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
    margin: 50px;
}
</style>
