<template>
	<div id="nav" :class="[centred ? 'centred' : '']" :style="cssVars()">
    <table><tr>
      <td class='logo-container' @click="redirectToHome()">
        <img src="../assets/BookSploreIcon.svg" />
        <p class="title bold">Book</p>
        <p class="title italic">Splore</p>
      </td>
      
      <td v-if="!centred" class="button-container" >
        <a
        v-if="navbar_type=='landingpage'"
        class="signup-link"
        :href="this.$backend_url + '/login'"
        >
          Sign In With
          <img src="../assets/google.svg" width="23" height="23" />
        </a>

        <!---- Navbar items for pages other than landing page ---->
        <div v-if="navbar_type != 'landingpage'" class="link-container">
          <a href="/dashboard">Dashboard</a>
          <a href="/explore">Explore Books</a>
        </div>
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
        fixed: {
            type: Boolean,
            default: false,
        },
        navbar_type: {
            type: String,
            default: "landingpage"
        },
    },
    methods: {
        cssVars() {
            return {
                '--position': this.fixed ? 'fixed': 'relative'
            }
        },
        redirectToHome() {
            this.$router.push("/")
        },
    }
  }
</script>

<style scoped>

a {
  text-decoration: none;
  color: #ffffff;
  font-size: 27px;
  font-weight: 400;
  font-family: Lato;
  float: right;
  margin: 15px;
  transition: 0.2s all;

}

a:hover {
    color: #79A9D1;
    transition: 0.2s all;
}

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
  padding-left: 7px;
  margin-top: -3px;
}

.signup-link:active {
  transform: scale(0.9);
}

.signup-link:hover {
    color: black;
}

.logo-container {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  display: flex;
  flex-direction: row;
  align-items: center;
  cursor: pointer;
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
    background: #181C23;
    position: var(--position);
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
