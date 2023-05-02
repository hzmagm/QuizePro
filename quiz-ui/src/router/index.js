import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from "../views/NewQuizPage.vue"
import QuestionsManager from "../views/QuestionsManager.vue"
import QuestionDisplay from "../views/QuestionDisplay.vue"
import QuestionsPage from "../views/QuestionsPage.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
    }
  ]
})

export default router
