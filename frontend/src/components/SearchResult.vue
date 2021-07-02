<template>

	<table style="width: 100%;"><tr style="width: 100%;">
        <td>
            <img
                :src="book.image_links ? (book.image_links.thumbnail ? book.image_links.thumbnail : require('../assets/BookSploreIcon.svg')) : require('../assets/BookSploreIcon.svg')"
                height="210px"
                width="150px"
            />
        </td>
            <table style="height: 100%;">
                <tr>
                    <div style="display: flex; justify-content: column; width: 100%; padding-bottom: 10px;">
                        <h3>
                            {{book.title}}
                            <span class="author">
                                {{ book.authors ? book.authors.join(", ") : 'Anonymous' }}
                            </span>
                        </h3>
                    </div>
                </tr>
                <tr style="height: 100%;" class="description">
                <div>
                    {{ book.description ? book.description.slice(0, 700) : 'No description provided' }}
                    {{ book.description ? book.description.length > 700 ? " . . . ." : "" : '' }}

                <router-link
                    v-if="book.description ? book.description.length > 700 : false"
                    to="/book-info"
                    class="link"
                >
                    (Read More)
                </router-link>
                </div>
            </tr>
        </table>
    </tr></table>
</template>

<script>

export default {
    name: "SearchResult",
    props: [
        "book"
    ],
}

</script>

<style scoped>



img {
    filter: drop-shadow(0px 5px 10px rgba(0, 0, 0, 0.5));
    padding-right: 10px;
}

span {
    color: #999999;
    margin: 0;
    padding-top: 9px;
    padding-left: 10px;
    font-size: 18px;
}

h3 {
    font-family: Lato;
    font-weight: 400;
    font-size: 24px;
    text-shadow: 0px 4px 4px rgba(255, 255, 255, 0.15);
    color: inherit;
    height: min-content;
    margin: 0;
}

.description {
    
    font-family: Lato;
    font-style: normal;
    font-weight: normal;
    font-size: 16.5px;
    line-height: 27px;
    width: 100%;

    color: inherit;
}

.link {
    text-decoration: none;
    color: #9DD4F2;
}

table {
    width: 100%;
    display: unset;
}

</style>
