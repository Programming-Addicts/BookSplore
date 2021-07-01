<template>
  <div style="width: 0; height: 0;" />
</template>

<script>
export default {
    name: "AuthComponent",
    created() {
        let token = window.localStorage.getItem("token")

        if (!token && !this.$route.query.token) {
            this.$router.push("/?msg=You are not logged in. Please authenticate yourself to continue")
        }

		fetch(
			this.$backend_url + "/users/current",
			{
				headers: {
					Authorization: token
				}
			}
		).then(
			response => {
				if (response.status != 200) {
					window.localStorage.removeItem("token")
					this.$router.push("/?msg=You are not logged in. Please authenticate yourself to continue")
				}
			}
		).catch(
			_ => {
				window.localStorage.removeItem("token")
				this.$router.push("/?msg=You are not logged in. Please authenticate yourself to continue")
			}
		)
    }
}
</script>
