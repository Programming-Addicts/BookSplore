<template>
  <div class="footer">
    <div class="logo-container">
      <img src="../assets/BookSploreIcon.svg" />
      <p class="title bold">Book</p>
      <p class="title italic">Splore</p>
    </div>
    <a class="github" href="https://github.com/Programming-Addicts/BookSplore">
        <p>See the source code on Github</p>
        <img src="../assets/Github_Logo.svg">
    </a>
  </div>
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style scoped>
.footer {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  background: #18191e;
  min-width: 100%;
  height: 140px;

  display: relative;
}

.logo-container {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  display: flex;
  flex-direction: row;
  align-items: center;
}
.logo-container img {
  height: 46px;
}
.logo-container p {
  margin: 0%;
}

.title {
	font-family: "Cabin";
	font-size: 27px;
	text-align: center;
  color: white;
}

.bold {
	font-weight: bold;
}

.italic {
	font-style: italic;
}

.github {
    color: #9DD4F2;
    font-size: 25px;
    font-weight: 700;
    font-family: Lato;

    display: flex;
    cursor: pointer;
    justify-content: center;
}
.github p {
    margin: 0%;
    padding-top: 12px;
    padding-right: 10px;
    font-size: 20px;
}
.github p:hover {
    text-decoration: underline
}

.github:link {
    text-decoration: none;
}

</style>
