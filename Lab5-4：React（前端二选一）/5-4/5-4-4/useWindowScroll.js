import { useState, useEffect } from 'react';

export function useWindowScroll() {
  // 1. 初始化状态，默认滚动距离为 0
  const [y, setY] = useState(window.scrollY);

  // 2. 监听滚动事件，更新状态
  useEffect(() => {
    // 滚动时更新 y 的值
    const handleScroll = () => {
      setY(window.scrollY);
    };

    // 监听窗口滚动事件
    window.addEventListener('scroll', handleScroll);

    // 组件卸载时移除事件监听，防止内存泄漏
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []); // 空依赖，只在组件挂载/卸载时执行一次

  // 3. 按照题目要求，返回数组 [y]
  return [y];
}