<template>
    <div class="floatingMain">
        <div class="listTitle">{{ title }}</div>
        <div class="flist">
            <a
                :href="`/user/${item.id}`"
                v-for="(item, index) of items"
                :key="index"
            >
                <div class="listItem">
                    <img
                        :src="
                            item.avatar_url
                                ? item.avatar_url
                                : require(`../assets/ProfilePicture.svg`)
                        "
                    />
                    {{ item.username }}
                </div></a
            >
        </div>
    </div>
</template>

<script>
export default {
    name: "FloatingList",
    props: ["title", "items"],
    methods: {
        go: ($router, link) => {
            $router.push(link);
        }
    }
};
</script>

<style scoped>
.floatingMain {
    width: inherit;
    height: inherit;
    position: relative;
    background-color: #262c37;
    font-family: Lato;
    color: white;

    display: flex;
    flex-direction: column;
    z-index: 10;
    padding: 10px;
    /* row-gap: 20px; */

    border: 4px solid #3d475c;
    border-radius: 10px;
    box-shadow: 0px 5px 10px 0px #00000080;
}
.floatingMain .listTitle {
    border-bottom: 1px solid white;
    /* width: 100%; */
    margin-left: 10px;
    margin-right: 10px;

    font-size: 25px;
    font-weight: 600;
}
.floatingMain .flist {
    display: flex;
    flex-direction: column;
    row-gap: 15px;
    overflow-y: auto;
    overflow-x: hidden;
    padding: 1vh;
    margin-top: 5px;
    border-radius: 10px;
}
.floatingMain .flist .listItem {
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 5px;
    column-gap: 5px;

    font-size: 20px;
    font-weight: 500;
    color: #89c1f5;
    box-shadow: 0px 2px 4px 0px #00000080;
    border-radius: 10px;

    cursor: pointer;
    transition: 300ms;
    user-select: none;
}
.floatingMain .flist .listItem:hover {
    transform: scale(1.01);
}
.floatingMain .flist .listItem:active {
    transform: scale(0.95);
}
.floatingMain .flist img {
    height: 5vh;
    border-radius: 50%;
}
a {
    text-decoration: none;
}
</style>
