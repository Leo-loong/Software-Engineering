import { useState, useEffect } from 'react';

export function useLocalStorage(key, defaultValue) {
  // 1. 初始化状态：优先从 localStorage 读取，没有则用 defaultValue
  const [message, setMessage] = useState(() => {
    // 读取 localStorage 中对应 key 的值
    const storedValue = localStorage.getItem(key);
    if (storedValue !== null) {
      // 如果有值，解析后返回（localStorage 只能存字符串）
      return JSON.parse(storedValue);
    }
    // 如果没有值，返回默认值
    return defaultValue;
  });

  // 2. 每次 message 变化时，自动同步到 localStorage
  useEffect(() => {
    // 把 message 转成字符串存入 localStorage
    localStorage.setItem(key, JSON.stringify(message));
  }, [key, message]); // key 或 message 变化时触发

  // 3. 按照题目要求，返回数组 [message, setMessage]
  return [message, setMessage];
}