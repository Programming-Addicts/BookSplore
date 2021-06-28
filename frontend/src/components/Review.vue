<template>
    <div class="review">
        <div class="reviewHead">
            <img :src="review.imageUrl" />
            <div>
                <div class="userDate">
                    {{ review.user }}
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
            {{ review.reviewDesc }}
        </div>
    </div>
</template>
<script>

export default {
    name: "Review",
    props: ["review"],
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
    margin: 30px;
    padding: 25px;
    text-align: left;
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
    height: 80px;
    margin-right: 20px;
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

.reviewDesc {
    font-size: 20px;
    padding-top: 20px;
}
</style>