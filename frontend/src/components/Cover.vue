<template>
    <img
        :src="imgUrl ? imgUrl : require(`../assets/BookSploreIcon.svg`)"
        class="cover"
        :style="cssVars(width, height)"
    />
</template>

<script>
export default {
    name: "Cover",
    props: {
        imgUrl: {
            default: require("../assets/BookSploreIcon.svg")
        },
        width: {
            type: String,
            default: "250px"
        },
        height: {
            type: String,
            default: "350px"
        }
    },
    methods: {
        cssVars: (width, height) => {
            return {
                "--width": width,
                "--height": height
            };
        }
    }
};
</script>

<style scoped>
.cover {
    width: var(--width);
    height: var(--height);
    background: #181c23;
    border: 3px solid #3d475c;
    border-radius: 10px;
    box-shadow: 0px 5px 10px 0px #00000080;
    position: relative;
}
</style>
