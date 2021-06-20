<template>
  <div class="main">
    <div class="section1">
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
    <div class="section2">

    </div>
  </div>
</template>

<script>
export default {
  name: "LandingPage1",
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
}

.circle {
  display: flex;
  flex-direction: column;
  /* align-items: center; */
  /* justify-content: center; */

  background: #111722;
  height: 900px;
  width: 900px;
  border-radius: 50%;
  position: absolute;
  top: -20%;
  left: -10%;

  word-wrap: break-word;
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

.sun-img {
  margin-top: 5%;
  margin-left: 53%;

  height: 420px;
}

.reading-img {
  position: absolute;
  right: 1%;
  bottom: 0%;

  height: 530px;
  width: 955px;
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
</style>
