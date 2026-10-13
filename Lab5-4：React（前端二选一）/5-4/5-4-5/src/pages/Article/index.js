import { Button } from 'antd'
import { useNavigate } from 'react-router-dom'

const Article = () => {
  const navigate = useNavigate()

  // 跳转函数
  const goPublish = () => {
    // 跳转到发布文章，并传递参数 id=100
    navigate('/publish?id=100')
  }

  return (
    <div>
      <h1>内容管理</h1>
      {/* 加一个按钮，点击触发跳转 */}
      <Button type="primary" onClick={goPublish} style={{ margin: '20px 0' }}>
        跳转到发布文章（传参 id=100）
      </Button>

      {/* 你原来的筛选、表格代码都保留在这里就行 */}
    </div>
  )
}

export default Article