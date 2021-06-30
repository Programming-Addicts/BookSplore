<template>
    <div class="bookReviewMain">
        <div class="reviewTitle">Reviews</div>
        
        <div class="addReview">
            <div class="addReviewTop">
                <div class="left">
                    <div class="top">
                        Review
                        <a class="bookName">{{ bookData.title }}</a>
                    </div>
                    <div class="belowTop">
                        ⭐⭐⭐⭐⭐
                    </div>
                </div>
                <button>Publish</button>
            </div>
            <textarea cols="30" rows="10" v-model="newReview" placeholder="Publish a public review...." />
        </div>

        <Review v-for="(review, index) of reviews" :key="index" :review="review" />
    </div>
</template>

<script>
import Review from "./Review.vue"

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
    components: {
        Review
    },
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
            ],
            newReview: "",
        };
    },
};
</script>

<style scoped>
.bookReviewMain {
    display: flex;
    flex-direction: column;
    row-gap: 50px;
    text-align: center;
    padding: 30px;

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

.addReview {
    display: flex;
    flex-direction: column;
    text-align: left;
    row-gap: 30px;
    padding: 30px;

    border: 1px solid white;
    border-radius: 10px;
}
.addReview textarea {
    resize: none;
    background-color: inherit;
    color: inherit;
    font-family: inherit;
    font-size: 20px;
    padding: 15px;
    height: 30vh;

    border: 2px solid white;
    border-radius: 10px;
    outline: none;
    overflow: auto;
}
.addReview .addReviewTop {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
.addReview .addReviewTop .left .top {
    font-size: 25px;
    font-weight: 500;
    margin-right: 20px;
}
.addReview .addReviewTop .left .top a {
    font-style: italic;
    color: #84C4FF;
}
.addReview .addReviewTop button {
    background: #7fb6f8;
    border: none;
    border-radius: 10px;
    padding: 2vh;
    width: fit-content;
    height: fit-content;

    font-family: Lato;
    font-size: 3vh;
    font-weight: 400;

    cursor: pointer;
    transition: 300ms;
}
.addReview .addReviewTop button:active {
    transform: scale(0.9);
}
.addReview .addReviewTop button:hover {
    transform: scale(1.1);
}
</style>
