import './index.css'
import avatar from './images/avatar.png'
import React from 'react'

// 时间格式化
function formatDate (time) {
  return `${time.getFullYear()}-${time.getMonth()+1}-${time.getDate()}`
}

class App extends React.Component {
  state = {
    tabs: [
      { id: 1, name: '热度', type: 'hot' },
      { id: 2, name: '时间', type: 'time' }
    ],
    active: 'hot',
    content: '', // 发表评论内容
    list: [
      {
        id: 1,
        author: '刘德华',
        comment: '给我一杯忘情水',
        time: new Date('2021-10-10 09:09:00'),
        attitude: 1
      },
      {
        id: 2,
        author: '周杰伦',
        comment: '哎哟，不错哦',
        time: new Date('2021-10-11 09:09:00'),
        attitude: 0
      },
      {
        id: 3,
        author: '五月天',
        comment: '不打扰，是我的温柔',
        time: new Date('2021-10-11 10:09:00'),
        attitude: -1
      }
    ]
  }

  // ===== 下面是我给你加的 2 个核心功能 =====

  // 1. Tab 点击切换
  switchTab = (type) => {
    this.setState({ active: type })
  }

  // 2. 发表评论
  handleInput = (e) => {
    this.setState({ content: e.target.value })
  }
  addComment = () => {
    if (!this.state.content.trim()) return
    const newComment = {
      id: Date.now(),
      author: '我',
      comment: this.state.content,
      time: new Date(),
      attitude: 0
    }
    this.setState({
      list: [newComment, ...this.state.list],
      content: ''
    })
  }

  render () {
    return (
      <div className="App">
        <div className="comment-container">
          <div className="comment-head">
            <span>5 评论</span>
          </div>

          {/* Tab 我加了 onClick */}
          <div className="tabs-order">
            <ul className="sort-container">
              {this.state.tabs.map(tab => (
                <li
                  key={tab.id}
                  className={tab.type === this.state.active ? 'on' : ''}
                  onClick={() => this.switchTab(tab.type)}
                >
                  按{tab.name}排序
                </li>
              ))}
            </ul>
          </div>

          {/* 发表评论 我加了绑定 */}
          <div className="comment-send">
            <div className="user-face">
              <img className="user-head" src={avatar} alt="" />
            </div>
            <div className="textarea-container">
              <textarea
                cols="80"
                rows="5"
                placeholder="发条友善的评论"
                className="ipt-txt"
                value={this.state.content}
                onChange={this.handleInput}
              />
              <button
                className="comment-submit"
                onClick={this.addComment}
              >
                发表评论
              </button>
            </div>
            <div className="comment-emoji">
              <i className="face"></i>
              <span className="text">表情</span>
            </div>
          </div>

          {/* 评论列表 */}
          <div className="comment-list">
            {this.state.list.map(item => (
              <div className="list-item" key={item.id}>
                <div className="user-face">
                  <img className="user-head" src={avatar} alt="" />
                </div>
                <div className="comment">
                  <div className="user">{item.author}</div>
                  <p className="text">{item.comment}</p>
                  <div className="info">
                    <span className="time">{formatDate(item.time)}</span>
                    <span className={item.attitude === 1 ? 'like liked' : 'like'}>
                      <i className="icon" />
                    </span>
                    <span className={item.attitude === -1 ? 'hate hated' : 'hate'}>
                      <i className="icon" />
                    </span>
                    <span className="reply btn-hover">删除</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    )
  }
}

export default App