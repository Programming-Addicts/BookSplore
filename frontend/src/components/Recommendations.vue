<template>
    <div>
        <h5 style="width: 100%;">Recommended for you -</h5>

        <div class="recommendations-container">
            <div
                v-for="book in recommendations.slice(
                    0,
                    recommendations.length / 2
                )"
                class="book"
                :key="book.id"
            >
                <router-link :to="`/book-info/${book.id}`">
                    <img
                        :src="
                            book.image_links
                                ? book.image_links.thumbnail
                                    ? book.image_links.thumbnail
                                    : require('../assets/BookSploreIcon.svg')
                                : require('../assets/BookSploreIcon.svg')
                        "
                        class="cover"
                    />
                </router-link>
            </div>
        </div>
        <div class="recommendations-container">
            <div
                v-for="book in recommendations.slice(
                    recommendations.length / 2,
                    recommendations.length
                )"
                class="book"
                :key="book.id"
            >
                <router-link :to="`/book-info/${book.id}`">
                    <img
                        :src="
                            book.image_links
                                ? book.image_links.thumbnail
                                    ? book.image_links.thumbnail
                                    : require('../assets/BookSploreIcon.svg')
                                : require('../assets/BookSploreIcon.svg')
                        "
                        class="cover"
                    />
                </router-link>
            </div>
        </div>

        <img :src="require(`../assets/searching.svg`)" v-if="!recommended" />
    </div>
</template>

<script>
export default {
    name: "Recommendations",
    data() {
        return {
            recommended: false,
            recommendations: []
        };
    },
    created() {
        let token = window.localStorage.getItem("token");

        fetch(
            // Get recommended books
            this.$backend_url + "/users/recommendations",
            {
                headers: {
                    Authorization: token
                }
            }
        )
            .then(response => {
                if (!response.ok) {
                    return null;
                }
                return response.json();
            })
            .then(data => {
                if (data == null || data.length == 0) return;

                let mostViewed = "Computer Science"; // Fallback value
                let mostViewedCount = 0;

                for (let subject in data) {
                    if (data.hasOwnProperty(subject)) {
                        if (data[subject] > mostViewedCount) {
                            mostViewed = subject;
                            mostViewedCount = data[subject];
                        }
                    }
                }

                // Get books under the subject which is most viewed

                fetch(
                    this.$backend_url +
                        `/books/search?query=subject:${mostViewed}&limit=16`,
                    {
                        headers: {
                            Authorization: token
                        }
                    }
                )
                    .then(response => {
                        if (response.ok) {
                            this.recommended = true;
                            return response.json();
                        }

                        this.recommended = false;
                        return null;
                    })
                    .then(data => {
                        if (data != null) this.recommendations = data;

                        console.log(this.recommendations);

                        if (window.innerWidth <= 600) this.recommended = false;
                    });
            });
    }
};
</script>

<style scoped>
* {
    font-family: Lato;
}

.recommendations-container {
    display: flex;
    justify-content: center;

    padding: 15px;
    padding-bottom: 0px;
}

.cover {
    width: 10vw;
    height: 14vw;
    margin: 1vw;
    margin-bottom: 0px;

    transition: 0.5s all;
}

.cover:hover {
    transform: scale(1.1);
    transition: 0.5s all;
}

.cover:active {
    transform: scale(0.8);
    transition: 0.2s all;
}

h5 {
    margin: 0;
}

@media screen and (max-width: 600px) {
    .recommendations-container {
        display: none;
    }

    img {
        display: block;
        width: 80vw;
    }

    h5 {
        display: none;
    }
}
</style>
