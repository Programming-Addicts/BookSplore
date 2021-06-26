<template>
  <div class="main">
    <div class="section1 section">
      <div class="circle" :style="scaleRadius(900)">
        <div class="textTitle">
          <p class="title bold">Book</p>
          <p class="title italic">Splore</p>
        </div>
        <p class="welcomeWords" :style="scaleFont(55)">
          A platform for you to explore books with your friends!
        </p>
        <p class="grayWords" :style="scaleFont(30)">
          Experience a whole new world of books, all in your browser!
        </p>
        <a :href="backend_url + '/login'">
          <button :style="scaleFont(25)">
            Get Started Now!
          </button>
        </a>
      </div>

      <img
        src="../assets/sun.svg"
        :width="scaleDownHeight(250) + 'px'"
        :height="scaleDownHeight(250) + 'px'"
        class="sun-img"
      />

      <img
        src="../assets/BooksImage.svg"
        :height="scaleDownHeight(450) + 'px'"
        :width="scaleDownHeight(900) + 'px'"
        class="reading-img"
      />
    </div>
    <div class="section2 section">
      <div class="outer1" style="width: 100%;">
        <p class="outer1-text" :style="scaleFont(60)">
          Acquaint yourself with books you never knew about
        </p>
      </div>
      <div class="outer2">

          <img
            src="../assets/reading_online.svg"
            class="reading_online"
            :width="scaleDownHeight(700)"
            :height="scaleDownHeight(400)"
          />

          <div class="bottomLeft" :style="scaleFont(35)">
            <p>Well, what are you waiting for?</p>
            <p class="createAccount">
              <a href="http://booksplore.milind.me/login">
                Create an account on BookSplore for free!
              </a> 
            </p>
          </div>
          <p class="topRight" :style="scaleFont(35)">
            Browse through hundreds of books, review your favourite reads, and
            follow your friends’ progress, right in the comfort of your browser!
          </p>
          <img
            src="../assets/books.svg"
            class="bottomRight"
            :width="scaleDownHeight(700)"
          />
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Footer from "./Footer.vue";

export default {
  name: "LandingPage1",
  props: {
    backend_url: String
  },
  components: {
    Footer,
  },
  methods: {
    scaleDownHeight(num) {
      return window.innerHeight * num / 796
    },
    scaleDownWidth(num) {
      return window.innerWidth * num / 1536
    },
    scaleRadius(num) {
      return {
        width: `${window.innerHeight * num / 796}px`,
        height: `${window.innerHeight * num / 796}px`
      }
    },
    scaleFont(num) {
      return {
        "font-size": `${window.innerHeight * num / 796}px`
      }
    },
  }
};
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
}

.section1 {
  display: grid;
  grid-auto-flow: row;
  gap: 0%;

  grid-template-areas: "circle sun reading";
  margin-top: -5%;
}

/* circle styling start ----------------------- */
.circle {
  display: flex;
  flex-direction: column;
  background: #111722;
  border-radius: 50%;

  margin-top: -150px;
  margin-left: -150px;
  margin-right: 0%;

  word-wrap: break-word;
  grid-area: circle;
}
.welcomeWords {
  font-family: Lato;
  color: white;
  font-weight: 700;

  margin-left: 23%;
  margin-top: 2%;
  margin-bottom: 0%;
  padding-right: 10%;
}
.grayWords {
  font-family: Lato;
  color: #b4b4b4;
  font-weight: 800;

  word-wrap: break-word;
  margin-left: 23%;
  margin-top: 2%;
  padding-right: 30%;
  padding-bottom: 0%;
}
.circle button {
  width: 300px;
  margin-left: 32%;
  margin-left: 32%;
  padding-top: 20px;
  padding-bottom: 20px;

  border-color: #8facf6;
  border-radius: 10px;
  background: inherit;
  border-radius: 10px;
  background: inherit;
  font-weight: 600;
  text-decoration: none;
  text-align:center;
  color: #8facf6;

  transition: 300ms;
}

.circle button:hover {
  cursor: pointer;
}

.circle button:active {
  transform: scale(0.9);
}

.title {
  font-family: "Cabin";
  font-size: 60px;
  text-align: center;
  color: white;
  margin-bottom: 0%;
}
.bold {
  font-weight: bold;
}
.italic {
  font-style: italic;
}
.textTitle {
  display: flex;
  flex-direction: row;
  margin-bottom: 0%;
  margin-left: 23%;
  margin-top: 22%;
}

/* circle styling end ----------------------- */

.sun-img {
  margin-top: 20%;
  margin-left: 15%;
  height: 420px;
  grid-area: sun;
}

.reading-img {

  margin-top: 280px;
  margin-left: -600px;

  grid-area: reading;
  z-index: 1;

  margin-bottom: 30px;
}

.section2 {
  display: flex;
  flex-direction: column;
}

.outer1, .outer1-text {
  font-family: Lato;
  font-weight: 800;
  color: white;
  text-align: center;

  margin-top: 2%;
  margin: 0%;
  width: 60%;

  display: flex;
  justify-content: center;
}

.outer2 {
  display: grid;
  grid-template-areas: 
  "topLeft topRight"
  "bottomLeft bottomRight";

}

.reading_online {
  grid-area: topLeft;

  margin-left: 11%;
  margin-right: 0%;
  margin-top: 7%;
}
.topRight {
  grid-area: topRight;
  font-weight: 700;
  color: white;
  font-family: Lato;

  margin-right: 8%;
  margin-left: -6%;
  margin-top: 5%;
  z-index: 2;
}
.bottomLeft {
  grid-area: bottomLeft;
  color: white;
  font-family: Lato;
  font-weight: 700;

  margin-left: 10%;
  margin-top: 5%;
  z-index: 2;

  word-wrap: none;
}
.bottomLeft p {
  margin: 0%;
  padding: 0%;
}
.bottomLeft .createAccount a {
  color: #AED8FF;
  cursor: pointer;
  text-decoration: none;
}
.bottomLeft .createAccount:hover {
  text-decoration: underline;
}

.bottomRight {
  grid-area: bottomRight;
  z-index: 0;

  margin-top: -35%;
  margin-left: -10%;
}

</style>
