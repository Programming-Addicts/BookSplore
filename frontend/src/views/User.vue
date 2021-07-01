<template>
    <div>
		<auth-component />
        <nav-bar navbar_type="authenticated" />
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
                    <div class="userInfoText">
                        <p class="username">
                            {{ userInfo.name }}
                            <a :href="userInfo.followEndpoint">Follow</a>
                        </p>
                        <p class="followersEtc">
                            {{ userInfo.reviews }} Reviews |
                            <a
                                @click="
                                    showList1 = !showList1;
                                    showList2 = false;
                                "
                                >{{ userInfo.followers }} Followers
                                <transition name="slide-fade">
                                <div
                                    class="hoverList"
                                    @click="showList1 = true"
                                    v-if="showList1"
                                    style="margin-left:10vw;"
                                >
                                    <floating-list title="Followers" />
                                </div>
                                </transition>
                            </a>
                            |
                            <a
                                @click="
                                    showList2 = !showList2;
                                    showList1 = false;
                                "
                            >
                                Following {{ userInfo.following }}
                                <transition name="slide-fade">
                                <div
                                    class="hoverList"
                                    @click="showList2 = true"
                                    v-if="showList2"
                                    style="margin-left:22vw;"
                                >
                                    <floating-list title="Following" />
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
                >
                    Recent Reviews
                    <div class="reviews">
                        <Review
                            type="user"
                            v-for="(review, index) of reviews"
                            :key="index"
                            :review="review"
                            coverType="user"
                            :descLength="280"
                        />
                    </div>
                </div>
            </div>
            <div
                class="recentBooksDiv"
                @click="
                    showList2 = false;
                    showList1 = false;
                "
            >
                <p class="recentTitle">Recent Books</p>
                <div class="recentBooks">
                    <a
                        href=""
                        v-for="(book, i) of recentBooks.slice(
                            0,
                            maxRecentBooks
                        )"
                        :key="i"
                    >
                        <Cover
                            width="10vw"
                            height="15vw"
                            :imgUrl="book.cover"
                        />
                    </a>
                </div>
            </div>
        </main>
        <Footer />
    </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import Footer from "../components/Footer.vue";
import Cover from "../components/Cover.vue";
import Review from "../components/Review.vue";
import FloatingList from "../components/FloatingList.vue";
import AuthComponent from "../components/AuthComponent.vue"

class UReview {
    constructor(user, postDate, stars, imageUrl, reviewDesc, link) {
        this.user = user;
        this.postDate = postDate;
        this.stars = stars;
        this.imageUrl = imageUrl;
        this.reviewDesc = reviewDesc;
        this.link = link;
    }
}

export default {
    name: "User",
    components: {
        NavBar,
        Footer,
        Review,
        Cover,
        FloatingList,
        AuthComponent		
    },
    data() {
        return {
            reviews: [
                new UReview(
                    "The Hunger Games",
                    new Date(2021, 8, 12),
                    3,
                    require("../assets/ProfilePicture.svg"),
                    "I really want to dislike the Hunger Games series, but I can't put them down. I love a good, dystopian tale full of twists and turns. It had been many years since I read the original series so it took me a while to remember who Coriolanus would be later on. The tale covers the early Hunger Games and the changes that were employed to generate interest in them out in the districts. Coriolanus is a high school senior. HIs family has fallen on hard times during the war and he is raised by an older cousin and his grandmother. They live on their good name, but often go hungry. Coriolanus falls in love with the tribute he is assigned to, who is much like our later heroine Katniss. Coriolanus is set up numerous times by the Gamemaster and discovers how easily he can kill and betray others to defend himself. ",
                    ""
                ),
                new UReview(
                    "Catching Fire",
                    new Date(2021, 8, 12),
                    5,
                    require("../assets/ProfilePicture.svg"),
                    "I really want to dislike the Hunger Games series, but I can't put them down. I love a good, dystopian tale full of twists and turns. It had been many years since I read the original series so it took me a while to remember who Coriolanus would be later on. The tale covers the early Hunger Games and the changes that were employed to generate interest in them out in the districts. Coriolanus is a high school senior. HIs family has fallen on hard times during the war and he is raised by an older cousin and his grandmother. They live on their good name, but often go hungry. Coriolanus falls in love with the tribute he is assigned to, who is much like our later heroine Katniss. Coriolanus is set up numerous times by the Gamemaster and discovers how easily he can kill and betray others to defend himself. ",
                    ""
                )
            ],
            recentBooks: [
                {
                    cover: null,
                    link: ""
                },
                {
                    cover: null,
                    link: ""
                },
                {
                    cover: null,
                    link: ""
                },
                {
                    cover: null,
                    link: ""
                }
            ],
            maxRecentBooks: 8,
            userInfo: {
                name: "devnull03",
                pfp: null,
                reviews: 150,
                followers: 123,
                following: 56,
                followEndpoint: ``
            },
            showList1: false,
            showList2: false
        };
    },
    methods: {
        href: ($router, path) => {
            $router.push(path);
        },
    }
};
</script>

<style scoped>
.hoverList {
    height: 300px;
    width: 300px;
    margin: 30px;
    position: fixed;
}

.slide-fade-enter-active {
    transition: all 200ms ease;
}
.slide-fade-leave-active {
  transition: all 200ms cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to{
  transform: translateY(10px);
  opacity: 0;
}


main {
    display: flex;
    flex-direction: row;
    margin-top: 4vh;
    margin-bottom: 5vh;

    font-family: Lato;
    color: white;
}

.left {
    margin-left: 5vw;
    margin-right: 5vw;
    display: grid;
}
.userInfo {
    display: flex;
    flex-direction: row;
    margin-bottom: 4vh;
    column-gap: 1vw;
}
.userInfo img {
    height: 13vh;
}
.userInfo p {
    margin: 0%;
}
.userInfoText .username {
    font-size: 50px;
    font-weight: 500;
    display: flex;
    align-items: center;
    column-gap: 1vw;
}
.userInfo .username a {
    font-size: 30px;
    font-weight: 400;
    color: #89c1f5;
    text-decoration: none;
}
.userInfo .username a:hover {
    text-decoration: underline;
}
.userInfoText .followersEtc {
    color: #aaaaaa;
    font-size: 25px;
    font-weight: 400;
}
.userInfoText .followersEtc a {
    text-decoration: none;
    cursor: pointer;
    user-select: none;
    transition: 300ms;
}
.userInfoText .followersEtc a:hover {
    border: 3px solid rgb(199, 199, 199);
    border-radius: 10px;
    padding-left: 5px;
    padding-right: 5px;
}
.userInfoText .followersEtc a:active {
    transform: scale(0.9);
}
.reviewsDiv {
    font-size: 35px;
    font-weight: 500;
    display: flex;
    flex-direction: column;
    row-gap: 1vw;
}
.reviewsDiv .reviews {
    display: flex;
    flex-direction: column;
    row-gap: 2vw;
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
</style>
