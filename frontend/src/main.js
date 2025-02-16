import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import VueSession from "vue-session";

Vue.use(VueSession);

Vue.config.productionTip = false;
Vue.prototype.$backend_url = "/api";

new Vue({
    router,
    render: h => h(App)
}).$mount("#app");
