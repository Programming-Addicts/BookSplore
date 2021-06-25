<template>
  <div>
    
    <nav-bar :fixed="false" navbar_type="authenticated" />
    <div style="width: 100%; display: flex; flex-direction: column; margin-top: 30px;">
        <h1>Search results for "{{ $route.params.query }}"</h1>
        <input type="text" class="search" placeholder="Search again"/>
    </div>
    
    <div v-for="book of books" :key="book.id" class="result-box">
        <table><tr>
            <td><img :src="book.image_links.thumbnail" height="210px" width="150px"/></td>
                <table style="height: 100%;">
                    <tr>
                        <div style="display: flex; justify-content: column; width: 100%; padding-bottom: 10px;">
                            <h3>{{book.title}}</h3>
                            <p class="author">{{ book.authors.join() }}</p>
                        </div>
                    </tr>
                    <tr style="height: 100%;" class="description">
                        <div>
                            {{ book.description.slice(0, 700) }}
                            {{ book.description.length > 700 ? " . . . ." : "" }}

                            <router-link
                                v-if="book.description.length > 700"
                                to="/dev/book-info"
                                class="link"
                            >
                                (Read More)
                            </router-link>

                        </div>
                        <div
                            style="width: 100%; display: flex; justify-content: center; font-size: 22px;"
                        >
                            View More
                        </div>
                    </tr>
                </table>
        </tr></table>
    </div>

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
  props: {
    "backend_url": {
      type: String,
      default: "http://localhost:8000"
    },
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
          `${this.backend_url}/books/search?query=${this.$route.params.query}`
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
    margin-bottom: 20px;
}

input {
    background: rgba(0, 0, 0, 0);
    border: 1px solid white;
    border-radius: 5px;
    width: 80%;
    font-size: 20px;
    color: #BBBBBB;
    font-family: Lato;
    padding: 15px;
    margin: auto;
    margin-top: 20px;
    margin-bottom: 50px;
}

h1 {
    margin: auto;
    margin-top: 20px;
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

p {
    color: #999999;
    margin: 0;
    padding-top: 9px;
    padding-left: 10px;
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

    color: #CCCCCC;
}

.link {
    text-decoration: none;
    color: #9DD4F2;
}

</style>
