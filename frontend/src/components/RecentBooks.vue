<template>
  <div class="recent">
    <p class="readsTitle">Your Reads</p>
    <!-- temporart search field -->
    <input type="text" class="search" placeholder="Find a book...."/>
    <!-- going to be replaced by the search component -->
    <div class="bookList">
        <div v-for="book in books" :key="book" class="book">
            <img src="../assets/BookIcon.svg" :height="scaleHeight(45)">
            <a :href="book.link" :style="scaleFont(23)">
              {{ book.name.length > 29 ? book.name.slice(0, 23) + " . . ." : book.name}}
            </a>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RecentBooks",
  props: ["books"],
  methods: {
    scaleFont(num) {
      return {
        "font-size": `${num * window.innerHeight / 796}px`
      }
    },
    scaleHeight(num) {
      return num * window.innerHeight / 796
    }
  }
};
</script>

<style scoped>
/* temporart code vvvvvv */
.recent input {
    background: #161C27;
    border: 1px solid white;
    border-radius: 5px;
    width: 80%;
    color: #BBBBBB;
    font-family: inherit;
    font-size: 20px;
    padding: 10px;
}
/* temporart code ^^^^^^ */
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
  margin-top: 20px;
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
  color: #A2DCEE;
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
