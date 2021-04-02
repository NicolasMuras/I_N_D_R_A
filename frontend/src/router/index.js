import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListTag from '@/components/tag/ListTag'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/tags',
      name: 'ListTag',
      component: ListTag
    }
  ],
  mode: 'history'
})
