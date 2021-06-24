<template>
    <div class="event">
        <div class="eventMsg">
            <img :src="imageUrl" /> <!-- Change to user pfp later -->
            <a name="userName" href="#" class="userLink">{{ user }}</a>
            <p name="action">{{ eventType == 'follow' ? 'started following' : 'reviewed' }}</p>
            <a name="target" href="#" class="targetLink">{{ eventType == 'follow' ? '@' : '' }}{{ eventTarget }}</a>
        </div>
        <div class="eventBox">
            <div class="userInfo">
                <img :src="imageUrl" />
                <div>
                    <a name="targetName" class="targetName">{{ eventTarget }}</a>
                    <p name="targetInfo" class="targetInfo">{{ eventDescription }}</p>
                </div>
            </div>
            <a href="/">
                <button class="action">{{ eventType == 'follow' ? 'Follow' : 'Read' }}</button>
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
  color: #92BDFD;
  text-decoration: none;
  padding: 3px;
}

.userLink {
  text-decoration: underline;
  padding: 3px;
  color: white
}

.action {
  padding-left: 25px;
  padding-right: 25px;
  padding-top: 7px;
  padding-bottom: 7px;

  background: #262C37;
  border: 1px solid #AAAAAA;
  box-sizing: border-box;
  border-radius: 10px;
  
  color: white;
  cursor: pointer;
  font-family: Lato;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
}

</style>
