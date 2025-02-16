<template>
    <router-link
        :to="'/user/' + user.id"
        class="container-link"
        v-if="currentUser !== null"
    >
        <table style="width: 100%;">
            <tr style="width: 100%;">
                <td style="width: 100px;">
                    <img
                        :src="
                            user.avatar_url
                                ? user.avatar_url
                                : require('../assets/BookSploreIcon.svg')
                        "
                        height="80px"
                        width="80px"
                        class="profile"
                    />
                </td>
                <table style="height: 100%; width: 100%;">
                    <tr style="width: 100%">
                        <div
                            style="display: flex; justify-content: column; width: 100%; padding-bottom: 10px;"
                        >
                            <h3>
                                {{ user.username }}
                                <div class="follower">
                                    {{ JSON.parse(user.followers).length }}
                                    Followers |
                                    {{ JSON.parse(user.following).length }}
                                    Following
                                </div>
                            </h3>
                        </div>
                        <td>
                            <div class="button-container">
                                <div
                                    class="follow"
                                    @click="follow()"
                                    :class="[
                                        user.id == currentUser.id
                                            ? 'same'
                                            : 'different'
                                    ]"
                                >
                                    {{
                                        user.followers.includes(currentUser.id)
                                            ? "Unfollow"
                                            : "Follow"
                                    }}
                                </div>
                            </div>
                        </td>
                    </tr>
                </table>
            </tr>
        </table>
    </router-link>
</template>

<script>
export default {
    name: "UserSearchResult",
    props: ["user"],
    data() {
        return {
            currentUser: null
        };
    },
    created() {
        console.log(this.user, this.currentUser);

        fetch(this.$backend_url + `/users/get`, {
            headers: {
                Authorization: window.localStorage.getItem("token")
            }
        })
            .then(response => response.json())
            .then(result => {
                this.currentUser = result;
                console.log(result);
            })
            .catch(error => {
                console.error("current user: ", error);
            });
    },
    methods: {
        follow() {
            if (this.user.id == this.currentUser.id) {
                return;
            }

            let action = this.user.followers.includes(this.currentUser.id)
                ? `unfollow`
                : `follow`;

            fetch(this.$backend_url + `/${action}?id=${this.user.id}`, {
                headers: {
                    Authorization: window.localStorage.getItem("token")
                },
                method: "POST"
            })
                .then(response => response.json())
                .then(result => {
                    console.log("Followed:", result);
                    this.$router.go(0);
                });
        }
    }
};
</script>

<style scoped>
* {
    font-family: Lato;
}
.profile {
    border-radius: 50%;
    filter: drop-shadow(0px 5px 10px rgba(0, 0, 0, 0.5));
    padding: 0;
    margin: 0;
}

a {
    text-decoration: none;
    color: white;
}

.follower {
    font-size: 23px;
    font-weight: 400;
    color: #999999;
}

h3 {
    font-size: 29px;
    font-weight: 500;
}

.follow {
    padding-left: 25px;
    padding-right: 25px;
    padding-top: 10px;
    padding-bottom: 10px;
    float: right;
    background-color: rgba(255, 255, 255, 0.01);
    border-radius: 10px;
    border: 1px white solid;
    color: white;
    font-size: 21px;
}

.same {
    cursor: not-allowed;
}

.different {
    cursor: pointer;
}
</style>
