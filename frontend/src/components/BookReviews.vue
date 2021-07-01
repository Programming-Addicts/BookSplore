<template>
    <div class="bookReviewMain" v-if="fetched">
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
                <button
                    @click="
                        postReview($router, $backend_url, {
                            content: newReview,
                            book_id: bookData.id,
                            stay_anonymous: false,
                            rating: 4
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
            :review="review"
        />
    </div>
</template>

<script>
import Review from "./Review.vue";

class BReview {
    constructor(user, postDate, stars, imageUrl, reviewDesc, link) {
        this.user = user;
        this.link = link;
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
            reviews: [],
            newReview: "",
            fetched: false
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
        createReviews: response => {
            let modified = [];
            response.forEach(element => {
                modified.push(
                    new BReview(
                        element.user.username,
                        new Date(element.timestamp),
                        element.rating,
                        element.user.avatar_url,
                        element.content,
                        `/user/${element.user.id}`
                    )
                );
            });
            return modified;
        }
    },
    created() {
        fetch(this.$backend_url + `/books/reviews?book_id=${this.bookData.id}`)
            .then(response => response.json())
            .then(result => {
                console.log(result);
                this.reviews = this.createReviews(result);
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
    color: #84c4ff;
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
