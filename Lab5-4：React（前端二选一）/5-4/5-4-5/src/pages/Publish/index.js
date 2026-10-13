import { useLocation } from 'react-router-dom'

const Publish = () => {
  const location = useLocation()
  // 解析 url 里的参数
  const query = new URLSearchParams(location.search)
  const id = query.get('id')

  return (
    <div>
      <h1>发布文章</h1>
      {/* 如果有参数，就显示出来 */}
      {id && <p>收到内容管理传递的参数：id = {id}</p>}

      {/* 你原来的编辑器代码都保留在这里就行 */}
    </div>
  )
}

export default Publish