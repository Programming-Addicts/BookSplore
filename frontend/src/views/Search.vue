<template>
  <div>
	<auth-component />	
    <nav-bar :fixed="false" navbar_type="authenticated" />

    <div style="width: 100%; display: flex; flex-direction: column; margin-top: 30px;">
        <h1>{{ books && books.length > 0 ? books.length : 'No' }} results found for "{{ $route.params.query }}"</h1>
        
        <div style="width: 100%; display: flex; justify-content: center; margin-bottom: 20px;">
            <search-box
                placeholder_="Not what you're looking for? Try again with different search terms!"
                height="60px"
                width="86vw"
                font_size="23px"
                endpoint="/search/0/#"
            />
        </div>

        <TabComponent @tabupdated="updateTab" />

        
    </div>

    <div v-if="resultFoundGlobally" style="width: 100%; margin-top: 30px;">
        <div v-if="'Books Genres ISBN'.includes(activeTab)">
            <div v-for="book of books" :key="book.id" class="result-box">
                <search-result :book="book" />
            </div>
        </div>
    </div>

    <div v-if="!resultFoundGlobally" class="no-result-box">
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
import TabComponent from "@/components/TabComponent.vue"
import AuthComponent from "../components/AuthComponent.vue"


export default {
    name: "BookSearch",
    components: {
        NavBar,
        Footer,
        SearchResult,
        SearchBox,
        TabComponent,
		AuthComponent
    },
    data() {
        return {
            books: [],
            resultFound: true,
            resultFoundGlobally: true,
            num_results: 20,
            activeTab: "Books"
        }
    },
    created() {
        this.SearchBook(0, 10, this.$route.params.query, true).then(
            data => {
                this.books = data;
                this.length = this.books.length
                
                window.onscroll = () => {
                    
                    let bottomOfWindow = Math.max(
                        window.pageYOffset, document.documentElement.scrollTop, document.body.scrollTop
                    ) + window.innerHeight === document.documentElement.offsetHeight;
                   
                    if (bottomOfWindow && (this.activeTab == "Books" || this.activeTab == "Genres")) {
                        
                        let query = this.activeTab == "Books" ? "subject:#" : "#"
                        
                        this.SearchBook(this.num_results, 5, query.replace("#", this.$route.params.query), false).then(
                            data => {
                                if (this.resultFound) 
                                    this.books.push(...data)
                                this.length = this.books.length
                                this.num_results += 5;
                            }
                        )
                    }
                }
            }
        )
    },
    methods: {
        async SearchBook(offset, num, query, globallyUpdateResults) {
            let response = await fetch(
              `${this.$backend_url}/books/search?query=${query}&download=${this.$route.params.download_only}&limit=${num}&offset=${offset}`
            )

            if (globallyUpdateResults) {
                this.resultFoundGlobally = response.status == 200;
            } else {
                this.resultFound = response.status == 200;
            }

            return response.json()
        },
        updateTab(tab) {
            if (tab == "ISBN") {
                this.SearchBook(0, 10, `isbn:${this.$route.params.query}`, false).then(
                    data => {
                        this.books = data
                        this.activeTab = "ISBN"
                    }
                )
            } else if (tab == "Books") {
                this.SearchBook(0, 20, `${this.$route.params.query}`, false).then(
                    data => {
                        this.books = data
                        this.activeTab = "Books"
                    }
                )
            } else if (tab == "Genres") {
                console.log(tab)
                this.SearchBook(0, 20, `subject:${this.$route.params.query}`, false).then(
                    data => {
                        this.books = data
                        this.activeTab = "Genres"
                    }
                )
            }
        },
    }
}

</script>

<style scoped>



.result-box {
    border-radius: 5px;
    background-color: rgba(0, 0, 0, 0.1);
    width: 85%;
    padding: 15px;
    margin: auto;
    margin-bottom: 30px;
    transition: 300ms;
}
.result-box:hover {
    transform: scale(1.01);
}

.no-result-box {
    color: #AAAAAA;
    background-color: rgba(0, 0, 0, 0);
    width: 85%;
    padding: 15px;
    margin: auto;
    margin-bottom: 30px;
    text-align: center;
    font-family: Lato;
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
