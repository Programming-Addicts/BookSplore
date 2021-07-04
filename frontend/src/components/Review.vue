<template>
    <div class="review">
        <div class="reviewHead">
            <div class="headLeft">
                <img
                    :src="review.imageUrl"
                    v-if="coverType === `book`"
                    class="pfp"
                />
                <Cover
                    :imgUrl="review.imageUrl"
                    :height="coverHeight"
                    width="75px"
                    v-else
                />
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
                    <div class="stars">
                        <img
                            :src="star"
                            v-for="(star, i) of renderStars(review.stars)"
                            :key="i"
                            style="height: 20px;"
                        />
                    </div>
                </div>
            </div>
            <img
                v-if="
                    coverType === `book`
                        ? raw_review.user.id === currentUser.id ||
                          [1, 2, 3, 4].includes(currentUser.id)
                        : false
                "
                :src="require(`@/assets/delete.png`)"
                class="deleteIcon"
                @click="deleteReview($router, $backend_url, raw_review)"
            />
        </div>
        <div class="reviewDesc">
            {{
                descLength
                    ? review.reviewDesc.slice(0, descLength) + `....`
                    : review.reviewDesc
            }}
        </div>
    </div>
</template>
<script>
import Cover from "./Cover.vue";

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
    name: "Review",
    props: {
        raw_review: Object,
        coverType: {
            type: String,
            default: "book"
        },
        descLength: Number,
        currentUser: Object
    },
    components: {
        Cover
    },
    data() {
        return {
            review: {},
            coverHeight: screen.width <= 760 ? `30vw`: `116px`,
        };
    },
    methods: {
        deleteReview: ($router, $backend_url, raw_review) => {
            fetch($backend_url + `/books/review?review_id=${raw_review.id}`, {
                headers: {
                    Authorization: window.localStorage.getItem("token")
                },
                method: "DELETE"
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
        renderStars: starsAmount => {
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
        },
        formatReviews: (type, response) => {
            if (type === "book") {
                return new BReview(
                    response.user.username,
                    new Date(response.timestamp),
                    response.rating,
                    response.user.avatar_url,
                    response.content,
                    `/user/${response.user.id}`
                );
            }
            return new BReview(
                response.book_data.title,
                new Date(response.timestamp),
                response.rating,
                response.book_data.image_links.thumbnail,
                response.content,
                `/book-info/${response.book_id}`
            );
        }
    },
    created() {
        this.review = this.formatReviews(this.coverType, this.raw_review);
    }
};
</script>

<style scoped>
.review {
    display: flex;
    flex-direction: column;
    border: 1px solid white;
    border-radius: 10px;
    padding: 25px;
    text-align: left;

    font-family: Lato;
    color: white;
}

.reviewHead {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    height: max-content;
}
.reviewHead .deleteIcon {
    height: 50px;
    transition: 300ms;
    cursor: pointer;
}
.reviewHead .deleteIcon:hover {
    transform: scale(1.1);
}
.reviewHead .deleteIcon:active {
    transform: scale(0.9);
}
.reviewHead .headLeft {
    display: flex;
    flex-direction: row;
    height: max-content;
}
.reviewHead .headLeft div {
    display: flex;
    flex-direction: column;
}
.reviewHead .headLeft img {
    margin-right: 20px;
    height: 80px;
    width: 80px;
}
.reviewHead .headLeft .pfp {
    height: 80px;
    border-radius: 50%;
}
.reviewHead .headLeft p {
    margin: 0%;
    font-size: 20px;
    color: #aaaaaa;
    padding-top: 5px;
}
.reviewHead .headLeft .userDate {
    display: flex;
    flex-direction: row;
    align-items: baseline;
    column-gap: 10px;
    padding-top: 5px;

    font-size: 28px;
    color: #9ac2ff;
}
.reviewHead .headLeft .userDate a {
    cursor: pointer;
    text-decoration: none;
    word-wrap: break-word;
    word-break: break-all;
}
.reviewHead .headLeft .userDate a:hover {
    text-decoration: underline;
}

.reviewDesc {
    font-size: 20px;
    padding-top: 20px;
}

a:any-link {
    color: #9ac2ff;
}
.stars {
    flex-direction: row !important;
    column-gap: 5px;
    margin-top: 10px;
    margin-left: 0%;
}
.stars img {
    width: 20px !important;
    margin: 0% !important;
    padding: 0%;
}

@media only screen and (max-width: 600px) {
    .reviewHead .headLeft {
        flex-direction: column !important;
    }
    .userDate {
        flex-direction: column !important;
    }
}
</style>
