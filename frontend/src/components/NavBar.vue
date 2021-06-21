<template>
	<div id="nav" :class="[centred ? 'centred' : '']">
    <table><tr>
      <td class='logo-container'>
        <img src="../assets/BookSploreIcon.svg" />
        <p class="title bold">Book</p>
        <p class="title italic">Splore</p>
      </td>
      
      <td v-if="!centred" class="button-container">
        <a
        class="signup-link"
        :href="BASE_URL + '/login'"
        >
        Sign In With <img src="../assets/google.svg" width="22" height="22" /></a> <!-- Fix the aligment and change the font please -->
      </td>
    </tr></table>
	</div>
</template>

<script>
export default {
	name: "NavBar",
  props: {
    centred: {
      type: Boolean,
      default: false
    },
    BASE_URL: {
      type: String,
      default: "http://127.0.0.1:8000"
    }
  }
};
</script>

<style scoped>

table {
  width: 100%;
}

.centred {
  display: flex;
  align-items: center;
  justify-content: center;
}

.fill-col {
  width: 100%;
}


.button-container {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  text-decoration: none;
}

.signup-link {
  font-family: Lato;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  text-align: center;
  letter-spacing: 0.03em;
  padding-left: 25px;
  padding-right: 25px;
  padding-top: 15px;
  padding-bottom: 15px;
  margin-left: 10px;
  margin-right: 10px;
  margin-top: 8px;
  float: right;

  background: #79A9D1;
  color: black;
  text-decoration: none;
  border-radius: 10px;

  transition: 300ms;

  display: flex;  
  justify-content: center;
  align-items: center;
}
.signup-link img {
  padding-left: 5px;
}
.signup-link:active {
  transform: scale(0.9);
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
  height: 66px;
}
.logo-container p {
  margin: 0%;
}

.title-div {
  display: flex;
  justify-content: center;
}

#nav {
	width: 100%;
	height: 80px;
  border-bottom: 0.1px white solid;
  background: #181C23;
  position: relative;
  z-index: 2;
}

.title {
	font-family: "Cabin";
	font-size: 37px;
	text-align: center;
  color: white;
}

.bold {
	font-weight: bold;
}

.italic {
	font-style: italic;
}
</style>
