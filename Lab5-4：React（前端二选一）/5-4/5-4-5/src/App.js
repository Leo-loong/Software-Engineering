import { unstable_HistoryRouter as HistoryRouter, Routes, Route, Navigate } from 'react-router-dom'
import { history } from './utils'

import './App.css'
import { AuthComponent } from '@/components/AuthComponent'
import { lazy, Suspense } from 'react'

// 懒加载所有页面
const Login = lazy(() => import('./pages/Login'))
const Layout = lazy(() => import('./pages/Layout'))
const Home = lazy(() => import('./pages/Home'))
const Article = lazy(() => import('./pages/Article'))
const Publish = lazy(() => import('./pages/Publish'))

function App () {
  return (
    <HistoryRouter history={history}>
      <div className="App">
        <Suspense fallback={<div style={{ textAlign: 'center', marginTop: 200 }}>loading...</div>}>
          <Routes>
            {/* 一级路由：Layout，嵌套二级路由 */}
            <Route path='/' element={
              <AuthComponent>
                <Layout />
              </AuthComponent>
            }>
              {/* 二级路由：默认渲染数据概览 */}
              <Route index element={<Navigate to="/home" replace />} />
              <Route path="home" element={<Home />} />
              <Route path="article" element={<Article />} />
              <Route path="publish" element={<Publish />} />
            </Route>

            {/* 登录页 */}
            <Route path='/login' element={<Login />} />

            {/* 404 兜底路由 */}
            <Route path='*' element={<div style={{ textAlign: 'center', marginTop: 200 }}><h1>404 页面不存在</h1></div>} />
          </Routes>
        </Suspense>
      </div>
    </HistoryRouter>
  )
}

export default App