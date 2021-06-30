<template>
    <div class="bookReviewMain">
        <div class="reviewTitle">Reviews</div>
        <div class="review" v-for="(review, index) of reviews" :key="index">
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

        <Review v-for="(review, index) of reviews" :key="index" :review="review" />
    </div>
</template>

<script>
class BReview {
    constructor(user, postDate, stars, imageUrl, reviewDesc) {
        this.user = user;
        this.postDate = postDate;
        this.stars = stars;
        this.imageUrl = imageUrl;
        this.reviewDesc = reviewDesc;
    }
}

export default {
    name: "BookReviews",
    props: ["bookData"],
    data() {
        return {
            reviews: [
                new BReview(
                    "class PythonAddict",
                    new Date(2021, 8, 12),
                    3,
                    require("../assets/ProfilePicture.svg"),
                    "I really want to dislike the Hunger Games series, but I can't put them down. I love a good, dystopian tale full of twists and turns. It had been many years since I read the original series so it took me a while to remember who Coriolanus would be later on. The tale covers the early Hunger Games and the changes that were employed to generate interest in them out in the districts. Coriolanus is a high school senior. HIs family has fallen on hard times during the war and he is raised by an older cousin and his grandmother. They live on their good name, but often go hungry. Coriolanus falls in love with the tribute he is assigned to, who is much like our later heroine Katniss. Coriolanus is set up numerous times by the Gamemaster and discovers how easily he can kill and betray others to defend himself. "
                ),
                new BReview(
                    "devnull03",
                    new Date(2021, 8, 12),
                    5,
                    require("../assets/ProfilePicture.svg"),
                    "I really want to dislike the Hunger Games series, but I can't put them down. I love a good, dystopian tale full of twists and turns. It had been many years since I read the original series so it took me a while to remember who Coriolanus would be later on. The tale covers the early Hunger Games and the changes that were employed to generate interest in them out in the districts. Coriolanus is a high school senior. HIs family has fallen on hard times during the war and he is raised by an older cousin and his grandmother. They live on their good name, but often go hungry. Coriolanus falls in love with the tribute he is assigned to, who is much like our later heroine Katniss. Coriolanus is set up numerous times by the Gamemaster and discovers how easily he can kill and betray others to defend himself. "
                )
            ]
        };
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
};
</script>

<style scoped>
.bookReviewMain {
    display: flex;
    flex-direction: column;
    text-align: center;

    border: 1px solid #c4c4c4;
    border-radius: 10px;

    font-family: Lato;
    color: white;
}
.reviewTitle {
    font-size: 45px;
    font-weight: 600;
    margin: 40px;
}

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
.addReview .addReviewTop button:hover {
    transform: scale(1.1);
}
</style>
