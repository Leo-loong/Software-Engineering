import { useState } from 'react';

function App() {
  // Tab 切换
  const [activeTab, setActiveTab] = useState('hot');

  // 评论数据
  const [commentList, setCommentList] = useState([
    {
      id: 1,
      username: '小明',
      content: '这个功能太好用了！',
      like: 12,
      dislike: 1,
    },
    {
      id: 2,
      username: '小红',
      content: '学习前端冲鸭！',
      like: 25,
      dislike: 0,
    },
    {
      id: 3,
      username: '小刚',
      content: 'React 真有趣～',
      like: 8,
      dislike: 2,
    },
  ]);

  // 点赞
  const handleLike = (id) => {
    setCommentList(
      commentList.map(item => 
        item.id === id ? { ...item, like: item.like + 1 } : item
      )
    );
  };

  // 点踩
  const handleDislike = (id) => {
    setCommentList(
      commentList.map(item => 
        item.id === id ? { ...item, dislike: item.dislike + 1 } : item
      )
    )
  };

  return (
    <div className="comment-container" style={{ 
      width: '750px', 
      margin: '50px auto',
      fontFamily: 'Arial'
    }}>
      {/* Tab 切换栏 */}
      <div className="tab-wrap" style={{ 
        display: 'flex', 
        borderBottom: '1px solid #eee', 
        marginBottom: '20px'
      }}>
        <button
          onClick={() => setActiveTab('hot')}
          style={{
            padding: '10px 20px',
            border: 'none',
            background: 'none',
            fontSize: '16px',
            cursor: 'pointer',
            borderBottom: activeTab === 'hot' ? '2px solid #1677ff' : 'none',
            color: activeTab === 'hot' ? '#1677ff' : '#333',
          }}
        >
          按热度排序
        </button>
        <button
          onClick={() => setActiveTab('time')}
          style={{
            padding: '10px 20px',
            border: 'none',
            background: 'none',
            fontSize: '16px',
            cursor: 'pointer',
            borderBottom: activeTab === 'time' ? '2px solid #1677ff' : 'none',
            color: activeTab === 'time' ? '#1677ff' : '#333',
          }}
        >
          按时间排序
        </button>
      </div>

      {/* 评论列表 */}
      <div className="comment-list">
        {commentList.map((item) => (
          <div key={item.id} style={{
            padding: '15px',
            borderBottom: '1px solid #f0f0f0',
            marginBottom: '10px'
          }}>
            <h4 style={{ margin: '0 0 8px 0' }}>{item.username}</h4>
            <p style={{ margin: '0 0 12px 0', color: '#444' }}>{item.content}</p>

            {/* 点赞 点踩 */}
            <div style={{ display: 'flex', gap: '20px' }}>
              <button 
                onClick={() => handleLike(item.id)}
                style={{ border: 'none', background: '#f5f5f5', padding: '4px 10px', borderRadius: '4px', cursor: 'pointer' }}
              >
                👍 {item.like}
              </button>
              <button 
                onClick={() => handleDislike(item.id)}
                style={{ border: 'none', background: '#f5f5f5', padding: '4px 10px', borderRadius: '4px', cursor: 'pointer' }}
              >
                👎 {item.dislike}
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;