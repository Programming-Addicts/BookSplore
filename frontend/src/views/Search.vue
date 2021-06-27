<template>
  <div>
    
    <nav-bar :fixed="false" navbar_type="authenticated" />
    <div style="width: 100%; display: flex; flex-direction: column; margin-top: 30px;">
        <h1>Search results for "{{ $route.params.query }}"</h1>
    </div>
    
    <div v-for="book of books" :key="book.id" class="result-box">
        <search-result :book="book" />
    </div>

    <router-link to="/dev/search" class="try-again">
        Not what you're looking for? Try again
    </router-link>


    <Footer />

  </div>
</template>

<script>

import NavBar from "@/components/NavBar.vue"
import Footer from "@/components/Footer.vue"
import SearchResult from "@/components/SearchResult.vue"

export default {
  name: "BookSearch",
  components: {
    NavBar,
    Footer,
    SearchResult
  },
  data() {
    return {
      books: []
    }
  },
  mounted() {
    this.SearchBook().then(data => {this.books = data; console.log(this.books)})
  },
  methods: {
    async SearchBook() {
      let response = await fetch(
          `${this.$backend_url}/books/search?query=${this.$route.params.query}`
        )

      return response.json()
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
