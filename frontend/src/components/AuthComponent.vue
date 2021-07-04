<template>
    <div style="width: 0; height: 0;" />
</template>

<script>
export default {
    name: "AuthComponent",
    created() {

		// Check if the token exists, or is provided in the url
        let token = window.localStorage.getItem("token");

        if (!token && !this.$route.query.token) {
            this.$router.push(
                "/?msg=You are not logged in. Please authenticate yourself to continue"
            );
        }

		// Check if the token is valid, by trying to authenticate with it
        fetch(this.$backend_url + "/users/current", {
            headers: {
                Authorization: token
            }
        })
            .then(response => {
                if (response.status != 200) {
                    window.localStorage.removeItem("token");
                    this.$router.push(
                        "/?msg=You are not logged in. Please authenticate yourself to continue"
                    );
                }
            })
            .catch(_ => {
                window.localStorage.removeItem("token");
                this.$router.push(
                    "/?msg=You are not logged in. Please authenticate yourself to continue"
                );
                console.error(_);
            });
    }
};
</script>
