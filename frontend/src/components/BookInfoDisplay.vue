<template>
    <div class="bookInfoDisplay">
        <div class="top">
            <Cover :imgUrl="bookData.cover"/>
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
                            <p>Language</p>
                            {{ bookData.language ? bookData.language : "-" }}
                        </div>
                    </div>
                    <div class="right">
                        <div>
                            <p>Ratings</p>
                            {{ bookData.ratings ? bookData.ratings : "-" }}
                        </div>
                        <div>
                            <p>Average Ratings</p>
                            {{
                                bookData.avgRating ? bookData.avgRating : "-"
                            }}
                        </div>
                        <div>
                            <p>Reviews</p>
                            {{
                                bookData.reviewsAmount
                                    ? bookData.reviewsAmount
                                    : "-"
                            }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="descDiv">
            <p class="desc" ref="desc">
                {{ bookData.description.slice(0, descMaxSize) }}....
            </p>
            <p
                v-on:click="descMode(bookData.description)"
                ref="descExpand"
                class="descExpand"
            >
                Expand
            </p>
        </div>
    </div>
</template>

<script>
import Cover from "./Cover.vue"

export default {
    name: "BookInfoDisplay",
    components: {
        Cover
    },
    props: ["Book"],
    data() {
        return {
            bookData: {
                cover: this.Book.image_links.thumbnail,
                title: this.Book.title,
                author: this.Book.authors[0],
                published: new Date(this.Book.publish_date),
                publisher: this.Book.publisher,
                language: this.Book.language,
                pageCount: this.Book.page_count,
                ratings: this.Book.total_ratings,
                avgRating: this.Book.avg_rating,
                reviewsAmount: this.Book.reviews,
                description: this.Book.description
            },
            descExpanded: false,
            descMaxSize: 300,
        };
    },
    methods: {
        descMode: function(desc) {
            this.descExpanded ? this.collapse(desc) : this.expand(desc);
            this.descExpanded = !this.descExpanded;
        },
        expand: function(descData) {
            this.$refs.desc.innerHTML = descData;
            this.$refs.descExpand.innerHTML = "Collapse";
        },
        collapse: function(descData) {
            this.$refs.desc.innerHTML = descData.slice(0, this.descMaxSize) + "....";
            this.$refs.descExpand.innerHTML = "Expand";
        }
    },
    mounted() {
        // console.log(this.$props.Book);
        this.collapse(this.bookData.description);
    }
};
</script>

<style scoped>
.bookInfoDisplay {
    position: relative;
    display: flex;
    flex-direction: column;

    font-family: Lato;
    color: white;

    margin: 50px;
}

.top {
    display: flex;
    flex-direction: row;
    padding-bottom: 40px;
    width: 100%;
}

.info {
    grid-area: info;
    display: flex;
    flex-direction: column;
    margin-left: 50px;
    width: 100%;
}

.head {
    display: flex;
    flex-direction: column;
}
.head p {
    padding: 0%;
    margin: 0%;
    padding-bottom: 5px;
}

.descDiv {
    font-size: 27px;
    font-weight: 400;
    display: flex;
    flex-direction: column;
    row-gap: 0%;
    align-items: center;
    border: 3px solid #3d475c;
    border-radius: 5px;
    padding: 40px;
}
.descDiv p {
    margin: 0%;
    padding: 5px;
}
.descDiv .desc {
    padding-left: 15px;
}
.descDiv .descExpand {
    color: #aac5fa;
    cursor: pointer;
    user-select: none;
    padding-top: 30px;
}
.descDiv .descExpand:hover {
    text-decoration: underline;
}

.title {
    font-size: 50px;
    font-weight: 600;
    padding-bottom: 5px;
}
.belowTitle {
    font-size: 25px;
    font-weight: 400;
}

.infoTable {
    display: flex;
    flex-direction: row;
    padding-top: 44px;
    font-size: 27px;
    margin-right: 20%;
}

.left {
    border-right: 1px solid white;
    display: flex;
    flex-direction: column;
    width: 50%;

    padding-right: 20px;
}
.right {
    display: flex;
    flex-direction: column;
    width: 45%;
    padding-left: 20px;
}
.left div,
.right div {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding-right: 5px;

}
.left div p,
.right div p {
    margin: 0%;
    padding-bottom: 13px;
    color: #aac5fa;
    align-items: center;
}
</style>
