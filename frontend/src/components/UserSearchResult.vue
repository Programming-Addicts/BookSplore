<template>

<router-link :to="'/dev/user/' + user.username.replace('#', '%23')" class="container-link">
    <table style="width: 100%;"><tr style="width: 100%;">
        <td>
            <img
                :src="user.avatar_url ? user.avatar_url : require('../assets/BookSploreIcon.svg')"
                height="210px"
                width="150px"
            />
        </td>
            <table style="height: 100%;">
                <tr>
                    <div style="display: flex; justify-content: column; width: 100%; padding-bottom: 10px;">
                        <h3>
                            {{user.username}}
                            <div class="author">
                                {{ user.followers.length }} Followers | {{ user.following.length }} Following
                            </div>
                        </h3>
                    </div>
                </tr>
			</table>
    </tr></table>
</router-link>

</template>

<script>

export default {
	name: "UserSearchResult",
	props: [
		"user"
	],
	mounted() {
		console.log(this.user)
	}
}

</script>

<style scoped>
</style>
