import Vue from "vue"
import VueRouter from "vue-router"
import App from "./App.vue"
import "./registerServiceWorker"
import router from "./router"
import { createPinia, PiniaVuePlugin } from "pinia"
import vuetify, { i18n } from "./plugins/vuetify"
import "roboto-fontface/css/roboto/roboto-fontface.css"
import "@mdi/font/css/materialdesignicons.css"
import "./assets/css/main.css"
import VueI18n from "vue-i18n";

Vue.use(PiniaVuePlugin)
const pinia = createPinia()

Vue.use(VueRouter)
Vue.use(VueI18n);

Vue.config.productionTip = false

new Vue({
  pinia,
  router,
  vuetify,
  i18n,
  render: h => h(App)
}).$mount("#app")
