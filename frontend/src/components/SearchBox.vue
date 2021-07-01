<template>
    <div
        :style="
            cssVars({
                height: height,
                width: width,
            })
        "
        class="inputOuter"
    >
        <div class="inputBox">
            <input
                type="text"
                class="mainBox"
                :placeholder="placeholder_"
                v-model="query"
                v-on:keyup.enter="sendQuery(endpoint, query)"
                :style="`font-size: ${font_size};`"
            />
            <img
                :src="require(`../assets/MagnifyingGlass.svg`)"
                v-if="query"
                @click="sendQuery(endpoint, query)"
            />
        </div>
    </div>
</template>

<script>
export default {
    name: "SearchBox",
    props: {
        endpoint: {
            type: String,
            default: "/search/#",
            validator: value => {
                return value.includes("#");
            }
        },
        placeholder_: {
            type: String,
            default: "Search for a book"
        },
        height: {
            type: String,
            default: `95px`
        },
        width: {
            type: String,
            default: `60vw`
        },
        font_size: {
            type: String,
            default: "40px"
       },
        center: Boolean,
        test: String
    },
    data() {
        return {
            query: ""
        };
    },
    methods: {
        cssVars: vars => {
            return {
                "--box-width": vars.width,
                "--box-height": vars.height,
            };
        },
        sendQuery: (endpoint, query) => {
            window.location.href = endpoint.replace("#", query)
        }
    }
};
</script>

<style scoped>
.inputOuter {
    font-family: Lato;
}

input {
    color: white;
    font-family: inherit;
    outline: none;
}

.inputBox {
    height: var(--box-height);
    width: var(--box-width);
    border: 2px solid rgba(255, 255, 255, 0.8);
    border-radius: 10px;

    display: flex;
    flex-direction: row;
    padding-left: 20px;
    padding-right: 20px;
    align-items: center;
}
.inputBox input {
    width: inherit;
    height: inherit;
    background: inherit;
    border: none;

    text-decoration: none;
}
.inputBox img {
    height: 60px;
    cursor: pointer;

    transition: 200ms;
}
.inputBox img:hover {
    transform: scale(1.1);
}
.inputBox img:active {
    transform: scale(0.9);
}
</style>
