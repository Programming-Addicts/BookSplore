<template>
    <div v-if="infoLoaded">
        <auth-component />
        <nav-bar navbar_type="authenticated" :currentUser="currentUser" />
        <main>
            <div class="left">
                <div class="userInfo">
                    <img
                        :src="
                            userInfo.pfp
                                ? userInfo.pfp
                                : require(`../assets/ProfilePicture.svg`)
                        "
                    />
                    <div class="userInfoText" :style="scaleFont(50)">
                        <p class="username">
                            {{ userInfo.name }}
                            <a
                                @click="
                                    follow(
                                        $router,
                                        $backend_url,
                                        userInfo,
                                        currentUser
                                    )
                                "
                                v-if="userInfo.id !== currentUser.id"
                            >
                                {{
                                    userInfo.followers.includes(currentUser.id)
                                        ? `Unfollow`
                                        : `Follow`
                                }}
                            </a>
                            <span
                                style="color: grey; font-size: 20px; margin-top: 15px;"
								v-if="userInfo.id <= 4 && userInfo.id > 0"
                            >
								BookSplore Admin
								</span>
                        </p>
                        <p class="followersEtc">
                            {{ userInfo.total_reviews }} Reviews
                            <a
                                @click="
                                    showList1 = !showList1;
                                    showList2 = false;
                                "
                            >
                                | {{ userInfo.followers.length }} Followers
                                <transition name="slide-fade">
                                    <div
                                        class="hoverList hoverList1"
                                        v-if="showList1"
                                    >
                                        <floating-list
                                            title="Followers"
                                            :items="userInfo.followersArr"
                                        />
                                    </div>
                                </transition>
                            </a>

                            <a
                                @click="
                                    showList2 = !showList2;
                                    showList1 = false;
                                "
                            >
                                | {{ userInfo.following.length }} Following
                                <transition name="slide-fade">
                                    <div
                                        class="hoverList hoverList2"
                                        v-if="showList2"
                                    >
                                        <floating-list
                                            title="Following"
                                            :items="userInfo.followingArr"
                                        />
                                    </div>
                                </transition>
                            </a>
                        </p>
                    </div>
                </div>
                <div
                    class="reviewsDiv"
                    @click="
                        showList2 = false;
                        showList1 = false;
                    "
                    v-if="reviewsFetched"
                >
                    Recent Reviews
                    <div class="reviews" v-if="reviews.length">
                        <Review
                            type="user"
                            v-for="(review, index) of reviews"
                            :key="index"
                            :raw_review="review"
                            coverType="user"
                            :descLength="280"
                            :currentUser="currentUser"
                        />
                        <p class="reviewPadding"></p>
                    </div>
                    <div class="noReviews" v-else>
                        This user has not reviewed any books yet
                    </div>
                </div>
            </div>
            <div
                class="recentBooksDiv"
                @click="
                    showList2 = false;
                    showList1 = false;
                "
                v-if="booksFetched"
            >
                <p class="recentTitle">Recent Books</p>
                <div class="recentBooks" v-if="recentBooks.length">
                    <a
                        v-for="(book, i) of recentBooks.slice(
                            0,
                            maxRecentBooks
                        )"
                        :key="i"
                        :href="book.link"
                    >
                        <Cover
                            :width="coverWidth"
                            :height="coverHeight"
                            :imgUrl="book.cover"
                        />
                    </a>
                </div>
                <div class="noRecentBooks" v-else>
                    User has not viewed any books recently
                </div>
            </div>
        </main>
    </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import Cover from "../components/Cover.vue";
import Review from "../components/Review.vue";
import FloatingList from "../components/FloatingList.vue";
import AuthComponent from "../components/AuthComponent.vue";

export default {
    name: "User",
    components: {
        NavBar,
        Review,
        Cover,
        FloatingList,
        AuthComponent,
    },
    data() {
        return {
            reviews: [],
            recentBooks: [],
            maxRecentBooks: screen.width <= 760 ? 4 : 8,
            userInfo: {},
            currentUser: {},
            showList1: false,
            showList2: false,
            infoLoaded: false,
            booksFetched: true,
            reviewsFetched: false,
            coverHeight: screen.width <= 760 ? `55vw` : `15vw`, 
            coverWidth: screen.width <= 760 ? `32vw` : `10vw`,
        };
    },
    methods: {
        follow: ($router, $backend_url, userInfo, currentUser) => {
            let action = userInfo.followers.includes(currentUser.id)
                ? `unfollow`
                : `follow`;
            fetch($backend_url + `/${action}?id=${userInfo.id}`, {
                headers: {
                    Authorization: window.localStorage.getItem("token"),
                },
                method: "POST",
            })
                .then((response) => response.json())
                .then((result) => {
                    console.log(result);
                    $router.go(0);
                });
        },
        scaleFont(num) {
            return {
                "font-size": `${(window.innerHeight * num) / 796}px`,
            };
        },
    },
    created() {
        // for fetching the user who's page is being viewed -----------(1)
        let id = this.$route.params.id;
        fetch(this.$backend_url + `/users/get?id=${id}`, {
            headers: {
                Authorization: window.localStorage.getItem("token"),
            },
        })
            .then((response) => response.json())
            .then((result) => {
                // fetching information about followers ----------------------(2)
                fetch(this.$backend_url + `/follow/get?id=${result.id}`, {
                    headers: {
                        Authorization: window.localStorage.getItem("token"),
                    },
                })
                    .then((response) => {
                        if (response.status != 200) {
                            this.$router.push("/404");
                        }

                        return response.json();
                    })
                    .then((result_) => {
                        this.userInfo = {
                            name: result.username,
                            pfp: result.avatar_url,
                            id: result.id,
                            followEndpoint:
                                this.$backend_url + `/follow?id=${result.id}`,
                            followersArr: result_.followers
                                ? result_.followers
                                : [],
                            followingArr: result_.following
                                ? result_.following
                                : [],
                            followers: result.followers,
                            following: result.following,
                            total_reviews: result.total_reviews,
                        };
                        // for fetching user's recent reviews ----------------------(3)

                        fetch(
                            this.$backend_url +
                                `/books/reviews?user_id=${this.userInfo.id}`
                        )
                            .then((response) => response.json())
                            .then((reviews) => {
                                this.reviews = reviews.reverse();
                                this.reviewsFetched = true;
                                this.infoLoaded = true;
                            })
                            .catch((error) => {
                                console.error("reviews :", error);
                            });

                        // ---------------------------------------------------------(3)

                        // for fetching recent books -------------------------------(3)

                        fetch(
                            this.$backend_url +
                                `/users/recent-books?user_id=${this.userInfo.id}`
                        )
                            .then((response) => response.json())
                            .then((books) => {
                                let modified = [];
                                books.forEach((element) => {
                                    modified.push({
                                        cover: element.image_links
                                            ? element.image_links.thumbnail
                                            : null,
                                        link: `/book-info/${element.book_id}`,
                                    });
                                });
                                this.recentBooks = modified;
                            });

                        // ---------------------------------------------------------(3)
                    })
                    .catch((error) => {
                        console.error("followers: ", error);
                        this.$router.push("/404");
                    });
                // ----------------------------------------------------(2)
            })
            .catch((error) => {
                console.error("main", error);
            });
        // ---------------------------------------------------------(1)

        // for checking info about the user viewing the page -------

        fetch(this.$backend_url + `/users/get`, {
            headers: {
                Authorization: window.localStorage.getItem("token"),
            },
        })
            .then((response) => response.json())
            .then((result) => {
                this.currentUser = result;
                console.log(result);
            })
            .catch((error) => {
                console.error("current user: ", error);
            });
        // ---------------------------------------------------------
    },
};
</script>

<style scoped>
.hoverList {
    height: 300px;
    width: 300px;
    margin-top: 30px;
    position: fixed;
    z-index: 99 !important;
}

.slide-fade-enter-active {
    transition: all 200ms ease;
}
.slide-fade-leave-active {
    transition: all 200ms cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter,
.slide-fade-leave-to {
    transform: translateY(10px);
    opacity: 0;
}

main {
    display: flex;
    flex-direction: row;
    margin-top: 4vh;
    margin-bottom: 5vh;
    justify-content: space-evenly;

    font-family: Lato;
    color: white;
}

.left {
    margin-left: 5vw;
    margin-right: 5vw;
    display: flex;
    flex-direction: column;
    width: 100%;
}
.userInfo {
    display: flex;
    flex-direction: row;
    margin-bottom: 4vh;
    column-gap: 1vw;
    width: 100%;
}
.userInfo img {
    --size: 10vw;
    height: var(--size);
    width: var(--size);
    border-radius: 50%;
}
.userInfo p {
    margin: 0%;
}
.userInfoText .username {
    font-weight: 500;
    display: inline-block;
    /* align-items: center; */
    column-gap: 1vw;
    font-size: inherit;

    word-wrap: break-word;
    word-break: break-all;
}
.userInfo .username a {
    font-size: 30px;
    font-weight: 400;
    color: #89c1f5;
    text-decoration: none;
    cursor: pointer;
    transition: 300ms;
}
.userInfo .username a:hover {
    text-decoration: underline;
}
.userInfo .username a:active {
    transform: scale(0.9);
}
.userInfoText .followersEtc {
    color: #aaaaaa;
    font-size: 25px;
    font-weight: 400;
    display: flex;
    flex-direction: row;
    column-gap: 5px;

    word-wrap: break-word;
    word-break: break-all;
}
.userInfoText .followersEtc a {
    text-decoration: none;
    cursor: pointer;
    user-select: none;
    transition: 300ms;
    display: grid;
}
.userInfoText .followersEtc a:hover {
    border: 3px solid rgb(199, 199, 199);
    border-radius: 10px;
    padding-left: 5px;
    padding-right: 5px;
}
/* .userInfoText .followersEtc a:active {
    transform: scale(0.9);
} */
.reviewsDiv {
    font-size: 35px;
    font-weight: 500;
    display: flex;
    flex-direction: column;
    row-gap: 1vw;
    width: 100%;
}
.reviewsDiv .reviews {
    display: flex;
    flex-direction: column;
    row-gap: 2vw;
}
.reviewsDiv .noReviews,
.recentBooksDiv .noRecentBooks {
    color: gray;
    font-size: 25px;
}
.reviewPadding {
    height: 10vh;
}
.noReviews {
    height: 50vh;
}
.recentBooksDiv {
    border: 2px solid white;
    border-radius: 10px;
    font-size: 35px;
    font-weight: 400;
    height: 100%;

    margin-right: 30px;
    padding-bottom: 50px;
    display: flex;
    flex-direction: column;
    text-align: center;
}

.recentBooksDiv .recentBooks {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 20px;
    gap: 20px;
    height: max-content;
}

.recentBooksDiv .recentBooks a {
    transition: 300ms;
}
.recentBooksDiv .recentBooks a:hover {
    transform: scale(1.1);
}
.recentBooksDiv .recentBooks a:active {
    transform: scale(0.9);
}

/* css for mobiles ------------------------ */

@media only screen and (max-width: 600px) {
    main {
        flex-direction: column;
        margin: 10px;
    }
    .left {
        margin: 0%;
    }
    .userInfo {
        flex-direction: column;
    }
    .userInfo img {
        --size: 24vw;
        height: var(--size);
        width: var(--size);
    }
    .userInfoText .username {
        display: inline-flex;
        flex-direction: column;
        font-size: 10vw;
        padding-right: 10px;

        word-wrap: break-word;
        word-break: break-all;
    }
    .userInfoText .username a {
        text-align: left;
    }
    .userInfoText .followersEtc {
        font-size: 5vw;
    }
    .followersEtc .hoverList2 {
        margin-left: -50%;
    }
    .followersEtc .hoverList1 {
        margin-left: -15%;
    }
    .followersEtc a {
        width: fit-content;
    }

    .reviewsDiv {
        row-gap: 30px;
    }
    .reviewPadding {
        height: 50px;
    }
    .noReviews {
        padding-right: 20px;
    }

    .recentBooksDiv {
        align-self: center;
        margin: 0%;
    }
    /* .recentBooks .cover {
        width: 39vw;
        height: 55vw;
    } */
}

/* ---------------------------------------- */
</style>
