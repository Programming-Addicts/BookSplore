<template>
	<div id="nav" :class="[centred ? 'centred' : '']">
    <table><tr >
      <td class='logo-container'>
        <img src="../assets/BookSploreIcon.svg" />
        <p class="title bold">Book</p>
        <p class="title italic">Splore</p>
      </td>
      
      <td v-if="!centred" class="fill-col" />
      <td v-if="!centred" class="button-container">
        <router-link class="login-link" to="/login">Log In</router-link>
      </td>
      <td v-if="!centred" class="button-container">
        <router-link class="signup-link" to="/signup">Sign Up</router-link>
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
  }
};
</script>

<style scoped>

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

.login-link {
  color: white;
  text-decoration: none;
  font-family: Lato;
  font-size: 25px;
  font-style: normal;
  font-weight: 500;
  letter-spacing: 0.03em;
  text-align: center;
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

  background: #79A9D1;
  color: black;
  text-decoration: none;
  border-radius: 10px;
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
