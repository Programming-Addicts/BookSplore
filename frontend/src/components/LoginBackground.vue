<template>
  <div class="mainDiv">
    <div class="sun">
      <img src="../assets/sun.svg" />
    </div>
    <div class="dudeGoingInDoor">
      <img src="../assets/login_image1.svg" />
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginBackground",
};
</script>

<style scoped>

.sun {
  position: absolute;
  width: 500px;
  height: 500px;
  right: -80px;
  top: -25px;
  border-radius: 310px;

  background: #151b26;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-bottom: 30px;
  padding-left: 10px;

  overflow: hidden;
}
.sun img {
  height: 370px;
}
.dudeGoingInDoor {
  position: absolute;
  width: 560px;
  height: 560px;
  top: 45%;
  left: -45px;

  background: #373D48;
  border-radius: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.dudeGoingInDoor img {
  height: 290px;
}
</style>