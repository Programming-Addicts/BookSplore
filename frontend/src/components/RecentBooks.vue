<template>
  <div class="recent" :style="cssVars">
    <p class="readsTitle">Your Reads</p>
    <!-- temporart search field -->
    <input type="text" class="search" placeholder="Find a book...."/>
    <!-- going to be replaced by the search component -->
    <div class="bookList">
        <div v-for="book in books" :key="book" class="book">
            <img src="../assets/BookIcon.svg">
            <a :href="book.link">{{book.name}}</a>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RecentBooks",
  props: ["books"],
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
  left: 0%;
  width: 25%;
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
    margin-top: 35px;
    width: 100%;
    row-gap: 20px;
    height: 100%;
    margin-bottom: 21%;
    padding-bottom: 100px;

    overflow-y: scroll;
    margin-right: 6px;
}
.bookList div {
    display: flex;
    flex-direction: row;
    align-items: center;

    font-family: inherit;
    font-size: 25px;
    font-weight: 600;
    color: #A2DCEE;

    column-gap: 10px;
    margin-left: 32px;
    padding-bottom: 0%;
    margin-bottom: 0%;

    word-break: break-all;
    cursor: pointer;
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
    height: 45px;
}


</style>