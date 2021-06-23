<template>
    <div class="event">
        <div class="eventMsg">
            <img src="../assets/ProfilePicture.svg" />
            <a name="userName" href="#">Millind </a>
            <p name="action">started following </p>
            <a name="target" href="#">@devnull</a>
        </div>
        <div class="eventBox">
            <div class="userInfo">
                <img src="../assets/ProfilePicture.svg" />
                <div>
                    <a name="userName">devnull</a>
                    <p name="info">8 books, 64 followers</p>
                </div>
            </div>
            <a href="#">
                <button>Follow</button>
            </a>
        </div>
    </div>
</template>

<script>
export default {
    name: "Event",
    data() {
        return {
            eventType: "follow",
            eventMsgUser: {
                pfp: null,
                username: "devnull",
                link: "#"
            },
            eventBoxInfo: {
                pfp: null
            }
        };
    }
};
</script>

<style scoped>
.event {
    display: flex;
    flex-direction: column;
    margin: 30px;
    margin-bottom: 0%;
    position: relative;

    font-family: Lato;
    color: white;
}

.eventMsg {
    display: flex;
    flex-direction: row;
    align-items: center;
}
.eventMsg img {
    height: 40px;
}
.eventMsg a:link {
    text-decoration: none;
}
.eventMsg a {
    color: white;
    padding: 3px;
}
.eventMsg a[name="userName"]:hover {
    text-decoration: underline;
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
</style>
