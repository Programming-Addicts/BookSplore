<template>
    <div class="footer">
        <div class="logo-container">
            <img src="../assets/BookSploreIcon.svg" />
            © Copyright {{ new Date().getFullYear() }}
            <p class="title bold">Book</p>
            <p class="title italic">Splore</p>
        </div>
    </div>
</template>

<script>
export default {
    name: "Footer"
};
</script>

<style scoped>
.footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100px;
    padding-left: 40px;
    padding-right: 40px;
    margin-top: 20px;
}

.logo-container {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    display: flex;
    flex-direction: row;
    align-items: center;
    padding-right: 10px;
    padding-top: 5px;
    color: white;
    font-family: "Cabin";
    font-size: 25px;
}
.title {
    font-family: "Cabin";
    font-size: 25px;
    text-align: center;
    color: white;
}

.bold {
    font-weight: bold;
    margin-left: 5px;
}

.italic {
    font-style: italic;
}
</style>
