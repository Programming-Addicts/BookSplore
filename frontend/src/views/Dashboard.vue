<template>
    <div class="dashboard">
        <auth-component />
        <nav-bar :fixed="true" navbar_type="dashboard" />
        <recent-books />

        <table style="width: 100%;">
            <tr>
                <td class="recent-books" style="width: 30%;" />

                <td>
                    <div v-if="events.length > 0" class="events-container">
                        <Event
                            v-for="(event, index) in events"
                            :key="index"
                            :user="event.user"
                            :eventType="event.eventType"
                            :eventDescription="event.eventDescription"
                            :eventTarget="event.eventTarget"
                            :imageUrl="event.imageUrl"
                            :myProfileUrl="event.myProfileUrl"
                            :url="event.url"
                        />
                    </div>
                    <div v-if="events.length == 0" class="not-found-container">
                        <p style="margin: auto; margin-bottom: 20px;">
                            Looks like you don't have any activity to show.
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
</template>

<script>
class BEvent {
    constructor(
        user,
        eventType,
        eventDescription,
        eventTarget,
        imageUrl,
        url,
        myProfileUrl
    ) {
        this.user = user;
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
                                "review",
                                `100 reviews`,
                                bsEvent.target_book.title.slice(0, 40) +
                                    " . . .",

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
    }
};
</script>

<style scoped>
.events-container {
    padding-top: 80px;
    overflow: hidden;
    padding-bottom: 20px;
}

.recent-books {
    width: 25%;
}

.not-found-container {
    margin-top: 120px;
    display: flex;
    justify-content: center;
    color: white;
    font-size: 24px;
    flex-direction: column;
    font: Lato;
}
</style>
