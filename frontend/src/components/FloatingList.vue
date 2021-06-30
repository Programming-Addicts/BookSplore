<template>
    <div class="floatingMain">
        <div class="listTitle">{{title}} </div>
        <div class="flist">
            <div
                class="listItem"
                v-for="(item, index) of items"
                :key="index"
            >
            <img :src="item.pfp ? item.pfp: require(`../assets/ProfilePicture.svg`)">
            {{item.display_name}}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "FloatingList",
    props: ["title", "items"]
};
</script>

<style scoped>
.floatingMain {
    width: inherit;
    height: inherit;
    position: relative;
    background-color: inherit;
    font-family: Lato;
    color: white;

    display: flex;
    flex-direction: column;
    /* row-gap: 20px; */

    border: 4px solid #3d475c;
    border-radius: 10px;
    box-shadow: 0px 5px 10px 0px #00000080;
}
.floatingMain .listTitle {
    border-bottom: 1px solid white;
    width: 100%;
    margin-left: 10px;
    margin-right: 10px;

    font-size: 20px;
    font-weight: 500;
}
.floatingMain .flist {
    display: flex;
    flex-direction: column;
    row-gap: 20px;
}
</style>
