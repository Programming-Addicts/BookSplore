<template>
    <div class="bookInfoDisplay">
        <div class="top">
            <Cover :imgUrl="bookData.cover" width="230px" />
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
                            <p class="lable">Published</p>
                            <p class="notLable">
                                {{
                                    bookData.published
                                        ? bookData.published
                                              .toDateString()
                                              .slice(4)
                                        : "-"
                                }}
                            </p>
                        </div>
                        <div>
                            <p class="lable">Publisher</p>
                            <p class="notLable">
                                {{
                                    bookData.publisher
                                        ? bookData.publisher
                                        : "-"
                                }}
                            </p>
                        </div>
                        <div>
                            <p class="lable">Page count</p>
                            <p class="notLable">
                                {{
                                    bookData.pageCount
                                        ? bookData.pageCount
                                        : "-"
                                }}
                            </p>
                        </div>
                        <div>
                            <p class="lable">Language</p>
                            <p class="notLable">
                                {{
                                    bookData.language ? bookData.language : "-"
                                }}
                            </p>
                        </div>
                    </div>
                    <div class="right">
                        <div>
                            <p class="lable">Ratings</p>
                            <p class="notLable">
                                {{ bookData.ratings ? bookData.ratings : "-" }}
                            </p>
                        </div>
                        <div>
                            <p class="lable">Average Rating</p>
                            <p class="notLable">
                                {{
                                    bookData.avgRating
                                        ? bookData.avgRating
                                        : "-"
                                }}
                            </p>
                        </div>
                        <div>
                            <p class="lable">Reviews</p>
                            <p class="notLable">
                                {{
                                    bookData.reviewsAmount
                                        ? bookData.reviewsAmount
                                        : "-"
                                }}
                            </p>
                        </div>
                        <div>
                            <p class="lable">ISBN</p>
                            <p class="notLable">
                                {{ bookData.isbn }}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="descDiv">
            <p class="desc" ref="desc" v-if="bookData.description">
                {{ bookData.description.slice(0, descMaxSize) }} . . . .
            </p>
            <p class="noDesc" v-else style="color: gray;">
                No description provided
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
import Cover from "./Cover.vue";

export default {
    name: "BookInfoDisplay",
    components: {
        Cover,
    },
    props: ["Book"],
    data() {
        return {
            bookData: {
                cover:
                    this.Book.image_links && this.Book.image_links.thumbnail
                        ? this.Book.image_links.thumbnail
                        : require("../assets/BookSploreIcon.svg"),
                title: this.Book.title,
                author: this.Book.authors.join(", "),
                published: new Date(this.Book.publish_date),
                publisher: this.Book.publisher,
                language: this.Book.language,
                pageCount: this.Book.page_count,
                ratings: this.Book.total_ratings,
                avgRating: this.Book.avg_rating,
                reviewsAmount: this.Book.review_count,
                description: this.Book.description,
                isbn: this.Book.isbns
                    ? this.Book.isbns[0]
                        ? this.Book.isbns[0].identifier
                        : "-"
                    : "-",
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
            this.$refs.desc.innerHTML =
                descData.slice(0, this.descMaxSize) + " . . . .";
            this.$refs.descExpand.innerHTML = "Expand";
        },
        scaleDownHeight(num) {
            return (window.innerHeight * num) / 796;
        },
        scaleDownWidth(num) {
            return (window.innerWidth * num) / 1536;
        },
        scaleRadius(num) {
            return {
                width: `${(window.innerHeight * num) / 796}px`,
                height: `${(window.innerHeight * num) / 796}px`,
            };
        },
        scaleFont(num) {
            return {
                "font-size": `${(window.innerHeight * num) / 796}px`,
            };
        },
    },
    mounted() {
        this.collapse(this.bookData.description);
    },
};
</script>

<style scoped>
.bookInfoDisplay {
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
    column-gap: 50px;
    width: 100%;
}

.info {
    display: flex;
    flex-direction: column;
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
    font-size: 26px;
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
    width: 100%;
    font-size: 25px;
}
.infoTable .notLable {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    margin: 0%;
    padding-left: 10px;
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
    padding-right: 5px;
}
.left div .lable,
.right div .lable {
    margin: 0%;
    padding-bottom: 13px;
    color: #aac5fa;
}
</style>
