<template>
  <div>
    <nav-bar :fixed="false" navbar_type="authenticated" />

    <div style="width: 100%; display: flex; flex-direction: column; margin-top: 30px;">
        <h1>Search results for "{{ $route.params.query }}"</h1>
        
        <div style="width: 100%; display: flex; justify-content: center; margin-bottom: 20px;">
            <search-box
                placeholder_="Not what you're looking for? Try again with different search terms!"
                height="60px"
                width="80vw"
                font_size="23px"
                endpoint="/search/0/#"
            />
        </div>
        
        <h2 style="width: 100%; text-align: center; color: #BBBBBB;" v-if="books.length > 0 && resultFound">
            {{ books.length > 0 ? `${books.length} results found` : "" }}
        </h2>

    </div>

    <div v-if="resultFound" style="width: 100%;">
        <div v-for="book of books" :key="book.id" class="result-box">
            <search-result :book="book" />
        </div>
    </div>

    <div v-if="!resultFound" class="no-result-box">
        <div style="width: 100%; display: flex; justify-content: center; margin-bottom: 30px;">
            <img src="../assets/NoData.svg" width="400px" />
        </div>
        Looks like there aren't any results for that query. You might want to rephrase your search terms for better results!
    </div>

    <Footer />

  </div>
</template>

<script>

import NavBar from "@/components/NavBar.vue"
import Footer from "@/components/Footer.vue"
import SearchResult from "@/components/SearchResult.vue"
import SearchBox from "@/components/SearchBox.vue"

export default {
    name: "BookSearch",
    components: {
        NavBar,
        Footer,
        SearchResult,
        SearchBox
    },
    data() {
        return {
            books: [],
            resultFound: true,
            num_results: 20
        }
    },
    mounted() {
        this.SearchBook(10).then(
            data => {
                this.books = data;
                window.onscroll = () => {
                    let bottomOfWindow = 
                        Math.max(window.pageYOffset, document.documentElement.scrollTop, document.body.scrollTop) + window.innerHeight === document.documentElement.offsetHeight;
                    
                    if (bottomOfWindow) {
                        this.num_results += 5
                        this.SearchBook(this.num_results).then(
                            data => {this.books = data}
                        )
                    }
                }
            }
        )
    },
    methods: {
        async SearchBook(num) {
            let response = await fetch(
              `${this.$backend_url}/books/search?query=${this.$route.params.query}&download=${this.$route.params.download_only}&limit=${num}`
            )

            if (response.status == 200) {
                this.resultFound = true;
            } else {
                this.resultFound = false;
            }

            let data = response.json()
            return data
        },
    }
}

</script>

<style scoped>



.result-box {
    border: 0.5px white solid;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.1);
    width: 85%;
    padding: 15px;
    margin: auto;
    margin-bottom: 30px;
}

.no-result-box {
    color: #AAAAAA;
    background-color: rgba(0, 0, 0, 0);
    width: 85%;
    padding: 15px;
    margin: auto;
    margin-bottom: 30px;
    text-align: center;
}

.try-again {
    background: rgba(0, 0, 0, 0);
    width: 100%;
    display: flex;
    justify-content: center;
    font-size: 20px;
    color: #9DD4F2;
    font-family: Lato;
    padding: 15px;
    margin: auto;
    margin-top: 40px;
    margin-bottom: 50px;
    text-align: center;
}

h1 {
    margin: auto;
    margin-top: 20px;
    margin-bottom: 30px;
    color: white;
    font-family: Lato;
    font-style: normal;
    font-weight: normal;
    font-size: 45px;
}

</style>
