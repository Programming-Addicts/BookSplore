<template>
    <div class="review">
        <div class="reviewHead">
            <img :src="review.imageUrl" v-if="coverType === `book`" class="pfp" />
            <Cover :imgUrl="review.imageUrl" height="115px" width="75px" v-else />
            <div>
                <div class="userDate">
                    <a :href="review.link">
                    {{ review.user }}
                    </a>
                    <p>
                        Posted on
                        {{ review.postDate.toDateString().slice(4) }}
                    </p>
                </div>
                <p>
                    <img
                        :src="star"
                        v-for="(star, i) of renderStars(review.stars)"
                        :key="i"
                        style="height: 20px;"
                    />
                </p>
            </div>
        </div>
        <div class="reviewDesc">
            {{ descLength? review.reviewDesc.slice(0, descLength) + `....` : review.reviewDesc }}
        </div>
    </div>
</template>
<script>
import Cover from "./Cover.vue"

export default {
    name: "Review",
    // props: ["review","type"],
    props: {
        review: Object,
        coverType: {
            type: String,
            default: "book"
        },
        descLength: Number,
    },
    components: {
        Cover

    },
    methods: {
        renderStars: starsAmount => {
            // let goldenStar = "⭐";
            // let greyStar = "★";
            let goldenStar = require("../assets/goldenStar.svg");
            let grayStar = require("../assets/grayStar.svg");
            if (starsAmount > 5) {
                console.error(`Invalid Amount of stars: ${starsAmount}`);
                return;
            }
            let arr = [];
            for (let index = 0; index < starsAmount; index++) {
                arr.push(goldenStar);
            }
            for (let index = 0; index < 5 - starsAmount; index++) {
                arr.push(grayStar);
            }
            return arr;
        }
    }
}
</script>


<style scoped>
.review {
    display: flex;
    flex-direction: column;
    border: 1px solid white;
    border-radius: 10px;
    /* margin: 30px; */
    padding: 25px;
    text-align: left;

    font-family: Lato;
    color: white;
}


.reviewHead {
    display: flex;
    flex-direction: row;
}
.reviewHead div {
    display: flex;
    flex-direction: column;
}
.reviewHead img {
    margin-right: 20px;
}
.reviewHead .pfp {
    height: 80px;
}
.reviewHead p {
    margin: 0%;
    font-size: 20px;
    color: #aaaaaa;
    padding-top: 5px;
}
.reviewHead .userDate {
    display: flex;
    flex-direction: row;
    align-items: baseline;
    column-gap: 10px;
    padding-top: 5px;

    font-size: 28px;
    color: #9ac2ff;
}
.reviewHead .userDate a:hover {
    text-decoration: underline;
}

.reviewDesc {
    font-size: 20px;
    padding-top: 20px;
}

a:link {
    text-decoration: none;
}
a:visited{
    color: inherit;
}
</style>