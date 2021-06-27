<template>
  <div>
    
    <nav-bar :fixed="false" navbar_type="authenticated" />
    <div style="width: 100%; display: flex; flex-direction: column; margin-top: 30px;">
        <h1>Search results for "{{ $route.params.query }}"</h1>
    </div>
    
    <div v-for="book of books" :key="book.id" class="result-box">
        <table style="width: 100%;"><tr style="width: 100%;">
            <td><img :src="book.image_links ? (book.image_links.thumbnail ? book.image_links.thumbnail : '../assets/BookSploreIcon.svg') : require('../assets/BookSploreIcon.svg')" height="210px" width="150px"/></td>
                <table style="height: 100%;">
                    <tr>
                        <div style="display: flex; justify-content: column; width: 100%; padding-bottom: 10px;">
                            <h3>
                                {{book.title}}
                                <span class="author">
                                    {{ book.authors ? book.authors.join(", ") : 'Anonymous' }}
                                </span>
                            </h3>
                        </div>
                    </tr>
                    <tr style="height: 100%;" class="description">
                        <div>
                            {{ book.description !== null ? book.description.slice(0, 700) : 'No description provided' }}
                            {{ book.description !== null ? book.description.length > 700 ? " . . . ." : "" : '' }}

                            <router-link
                                v-if="book.description ? book.description.length > 700 : false"
                                to="/dev/book-info"
                                class="link"
                            >
                                (Read More)
                            </router-link>

                        </div>
                        <router-link class="view-more" to="/" >
                            <button>
                                View More &#8599;
                            </button>
                        </router-link>
                    </tr>
                </table>
        </tr></table>
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

export default {
  name: "BookSearch",
  components: {
    NavBar,
    Footer
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

.view-more {
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin: auto;
    margin-top: 20px;
    text-decoration: none;
}

.view-more button {
    border: 1px #9DD4F2 solid;
    background-color: rgba(0, 0, 0, 0.1);
    padding-top: 15px;
    padding-bottom: 15px;
    padding-left: 60px;
    padding-right: 60px;
    border-radius: 10px;
    color: #9DD4F2;
    font-size: 20px;
    cursor: pointer;
}

.result-box {
    border: 0.5px white solid;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.1);
    width: 85%;
    padding: 15px;
    margin: auto;
    margin-bottom: 20px;
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

img {
    filter: drop-shadow(0px 5px 10px rgba(0, 0, 0, 0.5));
    padding-right: 10px;
}

span {
    color: #999999;
    margin: 0;
    padding-top: 9px;
    padding-left: 10px;
    font-size: 18px;
}

h3 {
    font-family: Lato;
    font-weight: 400;
    font-size: 24px;
    text-shadow: 0px 4px 4px rgba(255, 255, 255, 0.15);
    color: white;
    height: min-content;
    margin: 0;
}

.description {
    
    font-family: Lato;
    font-style: normal;
    font-weight: normal;
    font-size: 16.5px;
    line-height: 27px;
    width: 100%;

    color: #CCCCCC;
}

.link {
    text-decoration: none;
    color: #9DD4F2;
}

table {
    width: 100%;
    display: unset;
}

</style>
