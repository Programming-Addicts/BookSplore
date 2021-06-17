<template>
	<div id="nav">
    <table><tr>
      <td class="logo-container">
        <img src="../assets/BookSploreIcon.svg" />
        <span class="title bold">Book</span>
        <span class="title italic">Splore</span>
      </td>
      <td class="fill-col" />
      <td class="button-container">
        <router-link class="login-link" to="/login">Log In</router-link>
      </td>
      <td class="button-container">
        <router-link class="signup-link" to="/signup">Sign Up</router-link>
      </td>
    </tr></table>
	</div>
</template>

<script>
export default {
	name: "NavBar",
};
</script>

<style scoped>

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
}

.title-div {
  display: flex;
  justify-content: center;
}

#nav {
	width: 100%;
	height: 80px;
  border-bottom: 0.1px white solid;
}

.title {
	font-family: "Cabin";
	font-size: 37px;
	text-align: center;
  position: absolute;
  top: 24px;
  color: white;
}

.bold {
	font-weight: bold;
}

.italic {
	font-style: italic;
  left: 160px;
}
</style>
