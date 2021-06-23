<template>
    <div class="event">
        <div class="eventMsg">
            <img :src="imageUrl" />
            <a name="userName" href="#">{{ user }}</a>
            <p name="action">{{ eventType == 'follow' ? 'started following' : 'reviewed' }}</p>
            <a name="target" href="#" class="user-link">{{ eventTarget }}</a>
        </div>
        <div class="eventBox">
            <div class="userInfo">
                <img :src="imgUrl" />
                <div>
                    <a name="userName">{{ eventTarget }}</a>
                    <p name="info">eventDescription</p>
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
    props: {
        user: String,
        eventType: String,
        eventDescription: String,
        eventTarget: String, // User that was followed / Book that was reviewed
        imageUrl: String,
    },
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

.user-link {
  color: #92BDFD;
}

</style>
