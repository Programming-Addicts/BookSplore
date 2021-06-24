<template>
    <div class="bookInfoDisplay">
        <img
            :src="
                bookData.cover !== null ? bookData.cover : require('../assets/ProfilePicture.svg')
            "
            class="cover"
        />
        <div class="info">
            <div class="head">
                <p class="title">{{ bookData.title }}</p>
                <p class="belowTitle">
                    Written by {{ bookData.author }} | Published in
                    {{ bookData.published.getFullYear() }}
                </p>
            </div>
            <div class="infoTable">
                <div class="left">
                    <div>
                        <p>Published</p>
                        {{
                            bookData.published
                                ? bookData.published.toDateString().slice(4)
                                : "-"
                        }}
                    </div>
                    <div>
                        <p>Publisher</p>
                        {{ bookData.publisher ? bookData.publisher : "-" }}
                    </div>
                    <div>
                        <p>Page count</p>
                        {{ bookData.pageCount ? bookData.pageCount : "-" }}
                    </div>
                    <div>
                        <p>Page count</p>
                        {{ bookData.language ? bookData.language : "-" }}
                    </div>
                </div>
                <div class="right">
                    <div><p>Ratings</p>{{bookData.ratings? bookData.ratings: "-"}} </div>
                    <div><p>Ratings</p>{{bookData.avgRatings? bookData.avgRatings: "-"}} </div>
                    <div><p>Ratings</p>{{bookData.reviewsAmount? bookData.reviewsAmount: "-"}} </div>
                </div>
            </div>
        </div>
        <div class="desc">{{ bookData.description }}</div>
    </div>
</template>

<script>
export default {
    name: "BookInfoDisplay",
    props: ["Book"],
    data() {
        return {
            bookData: {
                cover: this.Book.cover,
                title: this.Book.title,
                author: this.Book.author,
                published: this.Book.published,
                publisher: this.Book.publisher,
                language: this.Book.language,
                pageCount: this.Book.pageCount,
                ratings: this.Book.ratings,
                avgRating: this.Book.avgRating,
                reviewsAmount: this.Book.reviewsAmount,
                description: this.Book.desc
            }
        };
    }
};
</script>

<style scoped>
.bookInfoDisplay {
    display: grid;
    position: relative;
    grid-template-areas:
        "cover info"
        "desc desc";
}
.bookInfoDisplay img {
    grid-area: "cover";
}
.info {
    grid-area: "info";
}
.desc {
    grid-area: "desc";
}
</style>
