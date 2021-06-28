import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import BookInfo from "../views/BookInfo.vue"
import Dashboard from "../views/Dashboard.vue"
import Search from "../views/Search.vue"
import Explore from "../views/Explore.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/dev/book-info/:id',
    name: 'BookInfo',
    component: BookInfo
  },
  {
    path: '/dev/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/dev/search/:query',
    name: 'Search',
    component: Search
  },
  {
    path: '/dev/explore',
    name: 'Explore',
    component: Explore
  },
  {
    path: '/dev/search',
    name: 'Explore',
    component: Explore
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
