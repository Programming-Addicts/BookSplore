<template>
    <div class="event">
        <div class="eventMsg">
            <img :src="myProfileUrl" class="performer-pfp" />
            <p name="action" class="event-desc">
                <router-link class="performer-url" :to="userUrl">{{
                    user.slice(0, -5)
                }}</router-link>
                {{ eventType == "follow" ? "started following" : "reviewed" }}
            </p>
            <a name="target" :href="url" class="targetLink"
                >{{ eventType == "follow" ? "@" : ""
                }}{{
                    eventType == "follow"
                        ? eventTarget.slice(0, -5)
                        : eventTarget
                }}</a
            >
        </div>
        <div class="eventBox">
            <div class="userInfo">
                <img :src="imageUrl" />
                <div>
                    <a name="targetName" class="targetName">
                        {{
                            window.innerWidth > 600
                                ? eventTarget.slice(0, 40) +
                                  (eventTarget.length > 40 ? ". . ." : "")
                                : eventTarget.slice(0, 20) +
                                  (eventTarget.length > 20 ? ". . ." : "")
                        }}
                    </a>
                    <p name="targetInfo" class="targetInfo">
                        {{ eventDescription }}
                    </p>
                </div>
            </div>
            <a href="/">
                <router-link class="action" :to="url">View</router-link>
            </a>
        </div>
    </div>
</template>

<script>
export default {
    name: "Event",
    props: {
        user: String,
        userUrl: String,
        eventType: String,
        eventDescription: String,
        eventTarget: String, // User that was followed / Book that was reviewed
        imageUrl: String,
        url: String,
        myProfileUrl: String
    },
    data() {
        return {
            window: window
        };
    }
};
</script>

<style scoped>
.performer-pfp {
    border-radius: 50%;
    width: 40px;
    height: 40px;
    margin-right: 5px;
    filter: drop-shadow(1px 5px 10px rgba(0, 0, 0, 0.6));
    border: 1px #fff solid;
}

.targetInfo {
    font-family: Lato;
    font-style: normal;
    font-weight: normal;
    font-size: 1.3vw;
    line-height: 30px;
    color: rgba(255, 255, 255, 0.6);
    margin: 0px;
}

.targetName {
    font-family: Lato;
    font-style: normal;
    font-weight: normal;
    font-size: 1.5vw;
    color: rgba(255, 255, 255, 0.8);
}

.event {
    display: flex;
    flex-direction: column;
    width: 90%;
    margin: 2vh;
    position: relative;

    font-family: Lato;
    color: white;
}

.eventMsg {
    display: flex;
    flex-direction: row;
    align-items: center;
}

.eventBox {
    display: flex;
    flex-direction: row;
    padding: 1.5vw;
    padding-left: 20px;
    align-items: center;
    justify-content: space-between;

    border-radius: 10px;
    border: 1px solid black;
    background: #20252f;
}

.eventBox .userInfo {
    display: flex;
    flex-direction: row;
    align-items: center;
}
.userInfo img {
    border-radius: 50%;
    height: 60px;
    width: 60px;
}
.userInfo div {
    padding-left: 10px;
}

.targetLink {
    color: #92bdfd;
    text-decoration: none;
    padding: 3px;
    padding-left: 5px;
}

.performer-url {
    text-decoration: underline;
    padding: 3px;
    color: white;
}

.action {
    padding-left: 25px;
    padding-right: 25px;
    padding-top: 7px;
    padding-bottom: 7px;

    background: #262c37;
    border: 1px solid #aaaaaa;
    box-sizing: border-box;
    border-radius: 10px;

    color: white;
    cursor: pointer;
    font-family: Lato;
    font-style: normal;
    font-weight: normal;
    font-size: 1.4vw;
    text-decoration: none !important;
}

.eventMsg {
    font-size: 1.6vw;
}

@media screen and (max-width: 600px) {
    .event-desc {
        font-size: 18px;
    }

    .action {
        font-size: 18px;
    }

    .targetName {
        font-size: 20px;
    }

    .targetInfo {
        font-size: 18px;
    }
}
</style>
