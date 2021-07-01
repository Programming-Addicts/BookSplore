<template>
    <div style="height: 100%;">
        <nav-bar :fixed="false"/>
        <landing-page />
    </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import LandingPage from "../components/LandingPage.vue";

export default {
    name: "Home",
	components: {
        NavBar,
        LandingPage
    },
    methods: {
        getHeight() {
            return {
                "height": `${window.innerHeight}px`
            }
        },
		sleep(ms) {
		  return new Promise(resolve => setTimeout(resolve, ms));
		}	
    },
    async mounted() {
		await this.sleep(200)
        let msg = this.$route.query.msg
        if (msg) {
			window.history.pushState("", "", "/")
            alert(msg)
        }

        let token = window.localStorage.getItem("token")
        if (token) {
			fetch(
			this.$backend_url + "/users/current",
			{
				headers: {
					Authorization: token
				}
			}
			).then(
				response => {
					if (response.status == 200) {
						this.$router.push("/dashboard")
					}
				}
			)
        }
    }
};
</script>
