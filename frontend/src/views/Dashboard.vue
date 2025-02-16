<template>
    <div class="dashboard">
        <auth-component />
        <nav-bar :fixed="true" navbar_type="dashboard" />
        <div class="mainStuff">
            <div class="recentWraper">
                <recent-books />
            </div>

            <table>
                <tr>
                    <td>
                        <p class="activityTitle">
                            All Activity
                        </p>
                        <div v-if="events.length > 0" class="events-container">
                            <Event
                                v-for="(event, index) in events"
                                :key="index"
                                :user="event.user"
                                :userUrl="event.userUrl"
                                :eventType="event.eventType"
                                :eventDescription="event.eventDescription"
                                :eventTarget="event.eventTarget"
                                :imageUrl="event.imageUrl"
                                :myProfileUrl="event.myProfileUrl"
                                :url="event.url"
                            />
                        </div>
                        <div
                            v-if="events.length == 0"
                            class="not-found-container"
                        >
                            <p style="margin: auto; margin-bottom: 20px;">
                                Looks like you don't have any activity to show.
                                Try searching for books, or following users on
                                our
                                <router-link
                                    to="/explore"
                                    class="link-to-explore"
                                    >Explore page</router-link
                                >!
                            </p>
                            <img
                                :src="require('../assets/NoData.svg')"
                                width="500px"
                                height="500px"
                                style="margin: auto;"
                            />
                        </div>
                    </td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
class BEvent {
    constructor(
        user, // User who performed the action
        userUrl, // Link to the users profile page
        eventType, // What the user did
        eventDescription, // Description of the event
        eventTarget, // What the action was performed on
        imageUrl, // Profile pic / cover image of the target
        url, // Link to the target
        myProfileUrl // profile of the user who performed the action
    ) {
        this.user = user;
        this.userUrl = userUrl;
        this.eventType = eventType;
        this.eventDescription = eventDescription;
        this.eventTarget = eventTarget;
        this.imageUrl = imageUrl;
        this.url = url;
        this.myProfileUrl = myProfileUrl;
    }
}

import AuthComponent from "../components/AuthComponent.vue";
import RecentBooks from "../components/RecentBooks.vue";
import NavBar from "../components/NavBar.vue";
import Event from "../components/Event.vue";

export default {
    name: "Dashboard",
    components: {
        RecentBooks,
        NavBar,
        AuthComponent,
        Event
    },
    created() {
        let token = this.$route.query.token;
        if (token) {
            window.localStorage.setItem("token", `${token}`);
            this.$router.push("dashboard");
        }

        fetch(this.$backend_url + "/users/events", {
            headers: {
                Authorization: window.localStorage.getItem("token")
            }
        })
            .then(response => response.json())
            .then(data => {
                for (var bsEvent of data) {
                    if (
                        bsEvent.type == "follow-you" ||
                        bsEvent.type == "follow-user"
                    ) {
                        this.events.push(
                            new BEvent(
                                bsEvent.performer.username,
                                `/user/${bsEvent.performer.id}`,
                                "follow",
                                `${bsEvent.target_user.total_reviews} reviews, ${bsEvent.target_user.followers} followers`,
                                bsEvent.target_user.username,
                                bsEvent.target_user.avatar_url,
                                `/user/${bsEvent.target_user.id}`,
                                bsEvent.performer.avatar_url
                            )
                        );
                    } else {
                        let isJson = false;

                        try {
                            isJson =
                                JSON.parse(bsEvent.target_book.image_links) &&
                                !!bsEvent.target_book.image_links;
                        } catch (e) {
                            isJson = false;
                        }

                        this.events.push(
                            new BEvent(
                                bsEvent.performer.username,
                                `/user/${bsEvent.performer.id}`,
                                "review",
                                this.renderStars(bsEvent.rating_given),
                                bsEvent.target_book.title,

                                isJson
                                    ? JSON.parse(
                                          bsEvent.target_book.image_links
                                      ).thumbnail
                                    : require("../assets/BookSploreIcon.svg"),

                                `/book-info/${bsEvent.target_book.book_id}`,
                                bsEvent.performer.avatar_url
                            )
                        );
                    }
                }
            });
    },
    data() {
        return {
            events: []
        };
    },
    methods: {
        renderStars: starsAmount => {
            let goldenStar = "⭐";
            let grayStar = "★";
            if (starsAmount > 5) {
                console.error(`Invalid Amount of stars: ${starsAmount}`);
                return;
            }
            let arr = [];
            for (let index = 0; index < starsAmount; index++) {
                arr.push(goldenStar);
            }
            for (let index = 0; index < 5 - starsAmount; index++) {
                arr.push(grayStar);
            }
            return arr.join(" ");
        }
    }
};
</script>

<style scoped>
.link-to-explore {
    color: #aac5fa;
}
table {
    width: 70%;
    position: absolute;
    right: 0%;
}
.activityTitle {
    font-size: 30px;
    color: white;
    font-family: Lato;
    font-weight: 600;
    padding-top: 80px;
    padding-left: 30px;
    margin-bottom: 0px;
}
.events-container {
    overflow: hidden;
    padding-bottom: 20px;
}

.recent {
    position: fixed;
    height: 100%;
    width: 25%;
}

.not-found-container {
    /* margin-top: 120px; */
    display: flex;
    justify-content: center;
    color: white;
    font-size: 24px;
    flex-direction: column;
    font: Lato;
    font-family: Lato;
}
@media only screen and (max-width: 600px) {
    .recent {
        position: relative;

        width: 92vw;
        background: #20242b;
        height: 52vh;
        border: 3px solid #3d475c;
        box-shadow: 0px 5px 10px 0px #00000080;
        border-radius: 15px;
        top: 100px;
        margin: 0%;
        padding-top: 0%;
    }
    .bookList {
        margin-bottom: 0%;
    }
    .mainStuff {
        display: flex;
        flex-direction: column;
        align-items: center;
        row-gap: 6vh;
    }
    table {
        position: relative !important;
        text-align: center;
    }
    .event {
        text-align: left;
    }
    .activityTitle {
        padding-top: 50px;
        margin-bottom: 0%;
    }
    .events-container,
    .not-found-container {
        position: relative;
    }
}
</style>
