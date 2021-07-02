<template>
    <div class="bookReviewMain" v-if="fetched">
        <div class="reviewTitle">Reviews</div>

        <div class="addReview">
            <div class="addReviewTop">
                <div class="left">
                    <div class="top">
                        Reviewing
                        <a class="bookName">{{ bookData.title }}</a>
                    </div>
                    <div class="belowTop">
                        <img
                            v-for="(star, s) of newReviewStars"
                            :key="s"
                            :src="
                                star
                                    ? require(`../assets/goldenStar.svg`)
                                    : require(`../assets/grayStar.svg`)
                            "
                            @click="newReviewStars = changeStars(s)"
                        />
                    </div>
                </div>
                <button
                    @click="
                        postReview($router, $backend_url, {
                            content: newReview,
                            book_id: bookData.id,
                            stay_anonymous: false,
                            rating: newReviewStars.reduce((a, b) => a + b, 0)
                        })
                    "
                >
                    Publish
                </button>
            </div>
            <textarea
                cols="30"
                rows="10"
                v-model="newReview"
                placeholder="Publish a public review...."
            />
        </div>
        <Review
            v-for="(review, index) of reviews"
            :key="index"
            :raw_review="review"
        />
    </div>
</template>

<script>
import Review from "./Review.vue";

export default {
    name: "BookReviews",
    props: ["bookData"],
    components: {
        Review
    },
    data() {
        return {
            reviews: [],
            newReview: "",
            fetched: false,
            newReviewStars: [0, 0, 0, 0, 0]
        };
    },
    methods: {
        postReview: ($router, $backend_url, data) => {
            if (!data.content || data.content.trim() === "") {
                return;
            }
            fetch($backend_url + `/books/review`, {
                headers: {
                    Authorization: window.localStorage.getItem("token")
                },
                method: "POST",
                body: new URLSearchParams(data)
            })
                .then(response => response.json())
                .then(result => {
                    console.log(result);
                    $router.go(0);
                })
                .catch(error => {
                    console.error(error);
                });
        },
        changeStars: starClicked => {
            console.log(starClicked);
            if (starClicked > 4) {
                console.error(`Invalid Amount of stars: ${starClicked}`);
                return;
            }
            let arr = [];
            for (let i = 0; i < 5; i++) {
                arr.push(starClicked - i >= 0);
            }
            console.log(arr);
            return arr;
        }
    },
    created() {
        fetch(this.$backend_url + `/books/reviews?book_id=${this.bookData.id}`)
            .then(response => response.json())
            .then(result => {
                console.log(result);
                this.reviews = result;
                this.fetched = true;
            })
            .catch(error => {
                console.error(error);
            });
    }
};
</script>

<style scoped>
.bookReviewMain {
    display: flex;
    flex-direction: column;
    row-gap: 50px;
    text-align: center;
    padding: 30px;
    width: 100%;

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
    row-gap: 25px;
    padding: 30px;

    border: 1px solid white;
    border-radius: 10px;
}
.addReview textarea {
    resize: none;
    background-color: inherit;
    color: inherit;
    font-family: inherit;
    font-size: 22px;
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
    color: #84c4ff;
}

.addReview .addReviewTop .left .belowTop {
    display: flex;
    flex-direction: row;
    column-gap: 5px;
    width: min-content;
    padding: 5px;
    margin: 0%;
    margin-top: 5px;
    user-select: none;
}
.addReview .addReviewTop .left .belowTop img {
    cursor: pointer;
    transition: 300ms;
}
.addReview .addReviewTop .left .belowTop img:hover {
    transform: scale(1.1);
}
.addReview .addReviewTop .left .belowTop img:active {
    transform: scale(0.9);
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
.addReview .addReviewTop button:active {
    transform: scale(0.9);
}
</style>
