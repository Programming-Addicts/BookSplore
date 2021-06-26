<template>
    <div class="bookReviewMain">
        <div class="reviewTitle">Reviews</div>
        <div class="review" v-for="(review, index) of reviews" :key="index">
            <div class="reviewHead">
                <img :src="review.imageUrl">
                <div>
                    {{review.user}} <p>Posted on {{review.postDate}} </p>
                </div>
            </div>
            <div class="reviewDesc"></div>
        </div>
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
                    "Class PythonAddict",
                    new Date(2021, 8, 12),
                    4,
                    require("../assets/ProfilePicture.svg"),
                    "I really want to dislike the Hunger Games series, but I can't put them down. I love a good, dystopian tale full of twists and turns. It had been many years since I read the original series so it took me a while to remember who Coriolanus would be later on. The tale covers the early Hunger Games and the changes that were employed to generate interest in them out in the districts. Coriolanus is a high school senior. HIs family has fallen on hard times during the war and he is raised by an older cousin and his grandmother. They live on their good name, but often go hungry. Coriolanus falls in love with the tribute he is assigned to, who is much like our later heroine Katniss. Coriolanus is set up numerous times by the Gamemaster and discovers how easily he can kill and betray others to defend himself. "
                ),
                new BReview(
                    "devnull03",
                    new Date(2021, 8, 12),
                    4,
                    require("../assets/ProfilePicture.svg"),
                    "I really want to dislike the Hunger Games series, but I can't put them down. I love a good, dystopian tale full of twists and turns. It had been many years since I read the original series so it took me a while to remember who Coriolanus would be later on. The tale covers the early Hunger Games and the changes that were employed to generate interest in them out in the districts. Coriolanus is a high school senior. HIs family has fallen on hard times during the war and he is raised by an older cousin and his grandmother. They live on their good name, but often go hungry. Coriolanus falls in love with the tribute he is assigned to, who is much like our later heroine Katniss. Coriolanus is set up numerous times by the Gamemaster and discovers how easily he can kill and betray others to defend himself. "
                )
            ]
        };
    },
    methods: {
        renderStars: (starsAmount) => {
            let goldenStar = "⭐";
            let greyStar = "★";
            if (starsAmount > 5) {
                console.error(`Invalid Amount of stars: ${starsAmount}`);
                return
            }
            return goldenStar*starsAmount + greyStar*(5-starsAmount)
        }
    }
};
</script>

<style scoped>
.bookReviewMain {
    display: flex;
    flex-direction: column;
    position: relative;
    width: 75%;

    border: 1px solid #C4C4C4;
    border-radius: 10px;

}

.review {
    display: flex;
    flex-direction: column;
    border: 1px solid white;
    border-radius: 10px;
}

</style>
