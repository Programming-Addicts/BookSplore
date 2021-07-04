<template>
    <div class="event">
        <div class="eventMsg">
            <img :src="myProfileUrl" class="performer-pfp" />
            <p name="action">
                {{ user.slice(0, -5) }}
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
                    <a name="targetName" class="targetName">{{
                        eventTarget
                    }}</a>
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
        eventType: String,
        eventDescription: String,
        eventTarget: String, // User that was followed / Book that was reviewed
        imageUrl: String,
        url: String,
        myProfileUrl: String
    }
};
</script>

<style scoped>
.performer-pfp {
    border-radius: 50%;
    width: 35px;
    height: 35px;
    margin-right: 5px;
    filter: drop-shadow(1px 5px 10px rgba(0, 0, 0, 0.6));
    border: 1px #fff solid;
}

.targetInfo {
    font-family: Lato;
    font-style: normal;
    font-weight: normal;
    font-size: 15px;
    line-height: 30px;
    color: rgba(255, 255, 255, 0.6);
    margin: 0px;
}

.targetName {
    font-family: Lato;
    font-style: normal;
    font-weight: normal;
    font-size: 20px;

    color: rgba(255, 255, 255, 0.8);
}

.event {
    display: flex;
    flex-direction: column;
    width: 90%;
    margin: 25px;
    margin-bottom: -10px;
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
    padding: 10px;
    padding-left: 15px;
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
/* .userInfo {} */
.eventBox img {
    height: 60px;
    padding-right: 10px;
}

.targetLink {
    color: #92bdfd;
    text-decoration: none;
    padding: 3px;
    padding-left: 5px;
}

.userLink {
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
    font-size: 18px;
    text-decoration: none !important;
}
</style>
