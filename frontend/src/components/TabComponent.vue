<template>

    <div class="container">
        <div class="inner-container">
            <div style="width: 30px; border-bottom: 1px #999999 solid;" />
            <div v-for="tab of tabs" :key="tab">
                <div
                    :class="active == tab ? 'selected' : 'unselected'"
                    class="tab"
                    @click="updateTab(tab)"
                >
                    {{ tab }}
                </div>
            </div>
            <div style="width: 100%; border-bottom: 1px #999999 solid;" />
        </div>
    </div>

</template>

<script>

export default {
    name: "TabComponent",
    data() {
        return {
            tabs: [
                "Books",
                "Genres",
                "ISBN",
                "Users"
            ],
            active: "Books"
        }
    },
    methods: {
        updateTab(tab) {
            this.active = tab
            this.$emit("tabupdated", tab)
        }
     },
}

</script>

<style scoped>

.container {
    width: 100%;
    display: flex;
    justify-content: center;

    margin-top: 10px;
}

.inner-container {
    width: 90%;
    display: flex;
    justify-content: center;
}

.selected {
    color: #99DCFD;
    border: 1px #999999 solid;
    border-bottom: none;
    border-radius: 10px;
    border-bottom-right-radius: 0px;
    border-bottom-left-radius: 0px;
}

.unselected {
    color: white;
    border-bottom: 1px #999999 solid;
}

.tab {
    padding-left: 20px;
    padding-right: 20px;
    padding-top: 5px;
    padding-bottom: 5px;

    font-family: Lato;
    font-size: 26px;
    cursor: pointer;
}

.tab:hover {
    color: #77BAF9;
    transition: 0.2s all;
}
</style>
