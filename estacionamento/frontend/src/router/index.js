import VueRouter from "vue-router";
import HomeView from "./../views/HomeView.vue";
import ApiDocView from "./../views/ApiDocView.vue";
import ApiTestView from "./../views/ApiTestView.vue";
import AuthenticatedLayout from "./../layouts/AuthenticatedLayout.vue";
import LandingView from "./../views/LandingView.vue";
import LoginView from "./../views/LoginView.vue";
import NotFoundView from './../views/NotFoundView.vue';
import { useAuthStore } from "./../store/index"

const auth = Number(process.env.VUE_APP_AUTH)

const routes = [
  { 
    path: "/", 
    name: "landing",
    // component: () => import("./../views/LandingView.vue"),
    component: LandingView,
    meta: {
      public: true
    },
  },
  {
    path: "/login",
    name: "login",
    // component: () => import("./../views/LoginView.vue"),
    component: LoginView,
    meta: {
      public: true
    },
  },
  {
    path: "/techpark",
    component: AuthenticatedLayout,
    meta: {
      public: false
    },
    redirect: "/techpark/home",
    children: [
      {
        path: "home",
        name: "home",
        component: HomeView,
        // component: () => import("./../views/HomeView.vue"),
      },
      {
        path: "api-doc",
        name: "apiDoc",
        component: ApiDocView,
        // component: () => import("./../views/ApiDocView.vue"),
      },
      {
        path: "api-test",
        name: "apiTest",
        component: ApiTestView,
        // component: () => import("./../views/ApiTestView.vue"),
      }
    ]
  },
  {
    path: '*',
    name: 'NotFound',
    component: NotFoundView
  }
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

function handleRedirect (to, next, isPublicRoute, authenticated) {
  const onlyLoggedOutRoute = to.matched.some(record => record.meta.public)
  // no-logged try to access private route
  if (!isPublicRoute && !authenticated) {
    return next("/login")
  }
  // logged try to access public route
  if (authenticated && onlyLoggedOutRoute) {
    return next("/techpark/home")
  }
  return next()
}

router.beforeEach((to, from, next) => {
  if (auth === 0) {
    return next()
  }
  const authStore = useAuthStore()
  let authenticated = authStore.isAuthenticated
  const isPublicRoute = to.matched.some(record => record.meta.public)
  // validation for user refresh page (F5) cenario
  if (authenticated === undefined) {
    authStore.loadAuthenticatedAndUserIdStateFromLocalStorage()
    authenticated = authStore.isAuthenticated
    if (!isPublicRoute) {
      if (authenticated) {
        return handleRedirect(to, next, isPublicRoute, authenticated)
      }
      return next("/login")
    }
  }
  return handleRedirect(to, next, isPublicRoute, authenticated)
})

// router.afterEach((to, from) => {
  // store.commit("setCurrentRouteName", to.name)
  // store.commit("setToolbarTitle", to.meta.pageTitle)
  // store.commit("setPreviousPage", from.path)
  // store.commit("setMaxHeightCurrentRoute", to.meta.maxHeight)
  // store.commit("setBackgroundColor", to.meta.backgroundColor)
  // resize.onResize()
// })

export default router