<template>
    <div class="floatingMain">
        <div class="listTitle">{{title}} </div>
        <div class="flist">
            <div
                class="listItem"
                v-for="(item, index) of test_items"
                :key="index"
                @click="go($router, item.link)"
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
    props: ["title", "items"],
    methods: {
        go: ($router, link) => {
            $router.push(link)
        }
    },
    data() {
        return {
            test_items: [
                {
                    pfp: null,
                    display_name: "class pythonaddict",
                    link: ``,
                },
                {
                    pfp: null,
                    display_name: "class pythonaddict",
                    link: ``,
                },
                {
                    pfp: null,
                    display_name: "class pythonaddict",
                    link: ``,
                },
                {
                    pfp: null,
                    display_name: "class pythonaddict",
                    link: ``,
                },
                {
                    pfp: null,
                    display_name: "class pythonaddict",
                    link: ``,
                },
                {
                    pfp: null,
                    display_name: "class pythonaddict",
                    link: ``,
                },
                {
                    pfp: null,
                    display_name: "class pythonaddict",
                    link: ``,
                },
            ]
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
    z-index: 4;
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
    color: #89C1F5;
    box-shadow: 0px 2px 4px 0px #00000080;
    border-radius: 10px;

    cursor: pointer;
    transition: 300ms;
    user-select: none;
}
.floatingMain .flist .listItem:hover {
    transform: scale(1.1);
}
.floatingMain .flist .listItem:active {
    transform: scale(0.9);
}
.floatingMain .flist img {
    height: 5vh;
}
</style>
