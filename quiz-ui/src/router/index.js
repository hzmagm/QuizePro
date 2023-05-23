import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from "../views/NewQuizPage.vue"
import QuestionsManager from "../views/QuestionsManager.vue"
import ScorePage from "../views/ScorePage.vue"
import AdminPage from "../views/AdminPage.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:"/",
      redirect:{path:"/home"}
    },
    
    {
      path: '/home',
      name: 'home',
      component: HomePage
    },

    {
      path: '/start-new-quiz-page',
      name: 'start-new-quiz-page',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: NewQuizPage
    },

    {
      path: '/questions',
      name: 'questions',
      component: QuestionsManager
    },
    
    {
      path: '/score',
      name: 'score',
      component: ScorePage
    },

    {
      path: '/admin',
      name: 'admin',
      component: AdminPage
    }
  
  ]
})

export default router
