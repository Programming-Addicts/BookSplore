<template>
  <div class="main">
    <div class="section1 section">
      <div class="circle">
        <div class="textTitle">
          <p class="title bold">Book</p>
          <p class="title italic">Splore</p>
        </div>
        <p class="welcomeWords">
          A platform for you to explore books with your friends!
        </p>
        <p class="grayWords">
          Experience a whole new world of books, all in your browser!
        </p>
        <button>Get Started Now!</button>
      </div>

      <img src="../assets/sun.svg" width="300" height="300" class="sun-img" />
      <img
        src="../assets/BooksImage.svg"
        width="720"
        height="720"
        class="reading-img"
      />
    </div>
    <div class="section2 section">
      <p class="outer1">Acquaint yourself with books you never knew about</p>
      <div class="outer2">

          <img src="../assets/reading_online.svg" class="reading_online"/>
          <div class="bottomLeft">
            <p>Well, what are you waiting for?</p>
            <p class="createAccount">
             <a href="#">Create an account on BookSplore for free!</a> 
            </p>
          </div>
          <p class="topRight">
            Browse through hundreds of books, review your favourite reads, and
            follow your friends’ progress, right in the comfort of your browser!
          </p>
          <img src="../assets/books.svg" class="bottomRight"/>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Footer from "./Footer.vue";

export default {
  name: "LandingPage1",
  components: {
    Footer,
  },
  methods: {
    getRadius() {
      return {
        width: `${window.innerHeight / 1.2}px`,
        height: `${window.innerHeight / 1.2}px`,
      };
    },
  },
};
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;

  /* scroll-snap-type: mandatory;
  scroll-snap-points-y: repeat(300px);
  scroll-snap-type: y mandatory; */

}

/* .section {
  scroll-snap-align: start;
} */

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
  height: 900px;
  width: 900px;
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
  font-size: 60px;
  font-weight: 700;

  margin-left: 23%;
  margin-top: 2%;
  margin-bottom: 0%;
  padding-right: 10%;
}
.grayWords {
  font-family: Lato;
  color: #b4b4b4;
  font-size: 35px;
  font-weight: 800;

  word-wrap: break-word;
  margin-left: 23%;
  margin-top: 2%;
  padding-right: 30%;
  padding-bottom: 0%;
}
.circle button {
  height: 65px;
  width: 300px;
  margin-left: 35%;
  border-radius: 10px;

  border-color: #8facf6;
  border-radius: 10px;
  background: inherit;

  font-family: Lato;
  font-size: 25px;
  font-weight: 600;
  color: #8facf6;

  transition: 300ms;
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
  height: 530px;
  width: 955px;
  margin-top: 280px;
  margin-left: -600px;

  grid-area: reading;
  z-index: 1;
}

.section2 {
  display: flex;
  flex-direction: column;
}

.outer1 {
  font-family: Lato;
  font-size: 60px;
  font-weight: 800;
  color: white;
  text-align: center;

  padding-left: 330px;
  padding-right: 330px;
  margin-top: 2%;
  margin: 0%;
}

.outer2 {
  display: grid;
  grid-template-areas: 
  "topLeft topRight"
  "bottomLeft bottomRight";

}

.reading_online {
  grid-area: topLeft;
  width: 700px;
  height: 400px;

  margin-left: 11%;
  margin-right: 0%;
  margin-top: 7%;
}
.topRight {
  grid-area: topRight;
  font-size: 35px;
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
  font-size: 38px;
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
  width: 700px;

  margin-top: -35%;
  margin-left: -10%;
}

</style>
