<template>
    <div class="bookInfo" :style="cssVars(dummyData)">
        <nav-bar :fixed="true" navbar_type="authenticated" />
        <div class="bookInfoMain">
            <book-info-display :Book="dummyData" />
            <div class="downloadButtons">
                <button id="pdf" v-on:click="getPdf()">Download Ebook as PDF</button>
                <button id="Epub" v-on:click="getEpub()">Download Ebook as Epub</button>
                <button id="WebReader" v-on:click="getWebReader()">Read on WebReader</button>
            </div>
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
                title: "The ballad of songbirds and snakes",
                author: "suzanne collins",
                pageCount: 2000,
                language: "english",
                published: new Date(2020, 1, 1),
                desc:
                    "Ambition will fuel him. Competition will drive him. But power has its price. It is the morning of the reaping that will kick off the tenth annual Hunger Games. In the Capitol, eighteen-year-old Coriolanus Snow is preparing for his one shot at glory as a mentor in the Games Ambition will fuel him. Competition will drive him. But power has its price. It is the morning of the reaping that will kick off the tenth annual Hunger Games. In the Capitol, eighteen-year-old Coriolanus Snow is preparing for his one shot at glory as a mentor in the Games",
                pdf: ' ',
                Epub: null,
                WebReader: ' ',
            },
        };
    },
    methods: {
        getPdf: () => {},
        getEpub: () => {},
        getWebReader: () => {},
        cssVars: (Book) => {
            let color = {
                background: '#7fb6f8',
                font: 'black'
            }
            let gray = {
                background: '#95979A',
                font: '#444444'
            }
            return {
            '--pdf-button-color': Book.pdf ? color.background: gray.background,
            '--Epub-button-color': Book.Epub ? color.background: gray.background,
            '--WebReader-button-color': Book.WebReader ? color.background: gray.background,

            '--pdf-font-color': Book.pdf ? color.font: gray.font,
            '--Epub-font-color': Book.Epub ? color.font: gray.font,
            '--WebReader-font-color': Book.WebReader ? color.font: gray.font,
            }
        }
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
    /* flex-direction: column; */
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
</style>
