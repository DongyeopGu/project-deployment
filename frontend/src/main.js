import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies'
import axios from 'axios'
import VueAwesomeSwiper from 'vue-awesome-swiper'
import VueSession from 'vue-session'
import 'swiper/css/swiper.css'

Vue.use(VueSession)
Vue.use(VueAwesomeSwiper, /* { default global options } */)

Vue.use(VueCookies)

Vue.config.productionTip = false

Vue.prototype.$axios = axios

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
