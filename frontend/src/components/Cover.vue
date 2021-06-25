<template>
    <img :src="imgUrl" class="cover" :style="cssVars(width, height)" />
</template>

<script>
export default {
    name: "Cover",
    props: {
        imgUrl: {
            default: require("../assets/ProfilePicture.svg")
        },
        width: {
            type: Number,
            default: 250
        },
        height: {
            type: Number,
            default: 350
        }
    },
    mounted() {
        this.imgUrl = this.imgUrl? this.imgUrl: require("../assets/ProfilePicture.svg")
    },
    methods: {
        cssVars: (width, height) => {
            return {
                '--width': width + 'px',
                '--height': height + 'px',
            }
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
