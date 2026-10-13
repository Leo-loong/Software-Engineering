import { Layout, Menu, Popconfirm } from 'antd'
import { useLocation, useNavigate, Outlet } from 'react-router-dom'
import { observer } from 'mobx-react-lite'
import {
  HomeOutlined,
  DiffOutlined,
  EditOutlined,
  LogoutOutlined
} from '@ant-design/icons'
import './index.scss'
import { useStore } from '@/store'
import { useEffect } from 'react'

const { Header, Sider } = Layout

const GeekLayout = () => {
  const { pathname } = useLocation()
  const { userStore, loginStore, channelStore } = useStore()

  useEffect(() => {
    userStore.getUserInfo()
    channelStore.loadChannelList()
  }, [userStore, channelStore])

  const navigate = useNavigate()
  const onConfirm = () => {
    loginStore.loginOut()
    navigate('/login')
  }

  // 1. 给菜单加点击跳转逻辑
  const handleMenuClick = ({ key }) => {
    navigate(key)
  }

  return (
    <Layout>
      <Header className="header">
        <div className="logo" />
        <div className="user-info">
          <span className="user-name">{userStore.userInfo.name}</span>
          <span className="user-logout">
            <Popconfirm
              onConfirm={onConfirm}
              title="是否确认退出？" okText="退出" cancelText="取消">
              <LogoutOutlined /> 退出
            </Popconfirm>
          </span>
        </div>
      </Header>
      <Layout>
        <Sider width={200} className="site-layout-background">
          <Menu
            mode="inline"
            theme="dark"
            selectedKeys={[pathname]}
            style={{ height: '100%', borderRight: 0 }}
            onClick={handleMenuClick} // 绑定点击事件
          >
            {/* 2. 补上菜单文字，key 对应路由路径 */}
            <Menu.Item icon={<HomeOutlined />} key="/home">
              数据概览
            </Menu.Item>
            <Menu.Item icon={<DiffOutlined />} key="/article">
              内容管理
            </Menu.Item>
            <Menu.Item icon={<EditOutlined />} key="/publish">
              发布文章
            </Menu.Item>
          </Menu>
        </Sider>
        <Layout className="layout-content" style={{ padding: 20 }}>
          {/* 3. 补上二级路由出口，这是页面内容显示的地方 */}
          <Outlet />
        </Layout>
      </Layout>
    </Layout>
  )
}

export default observer(GeekLayout)