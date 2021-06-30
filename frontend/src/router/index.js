import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import BookInfo from "../views/BookInfo.vue"
import Dashboard from "../views/Dashboard.vue"
import Search from "../views/Search.vue"
import Explore from "../views/Explore.vue"
import NotFoundPage from "../views/NotFoundPage.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/book-info/:id',
    name: 'BookInfo',
    component: BookInfo
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/search/:download_only/:query/',
    name: 'Search',
    component: Search
  },
  {
    path: '/explore',
    name: 'Explore',
    component: Explore
  },
  {
    path: '/search',
    name: 'Search_Explore',
    component: Explore
  },
  {
    path: '/*',
    name: 'NotFoundPage',
    component: NotFoundPage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
