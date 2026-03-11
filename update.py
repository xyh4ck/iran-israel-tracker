#!/usr/bin/env python3
"""
伊朗以色列冲突追踪器 - 数据更新脚本
自动抓取最新消息并更新网页
"""

import requests
import json
from datetime import datetime
from pathlib import Path
import os

# 数据源配置
SOURCES = {
    'brave_search': 'https://api.search.brave.com/res/v1/web/search',
    'wikipedia': 'https://zh.wikipedia.org/wiki/2026年伊朗战争',
    'bbc': 'https://www.bbc.com/zhongwen',
    'xinhua': 'https://www.news.cn/world/index.htm',
}

def fetch_latest_news():
    """抓取最新新闻"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始抓取最新消息...")
    
    # 使用 Brave Search API
    try:
        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip',
        }
        
        params = {
            'q': '伊朗以色列最新进展 2026年3月',
            'count': 10,
            'freshness': 'day'
        }
        
        # 从环境变量获取 API key
        api_key = os.environ.get('BRAVE_SEARCH_API_KEY')
        
        if api_key:
            headers['X-Subscription-Token'] = api_key
            
            response = requests.get(
                SOURCES['brave_search'],
                headers=headers,
                params=params,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"✓ 成功获取 {len(data.get('web', {}).get('results', []))} 条新闻")
                return data.get('web', {}).get('results', [])
            else:
                print(f"✗ API 请求失败: {response.status_code}")
        else:
            print("⚠ 未设置 BRAVE_SEARCH_API_KEY 环境变量，跳过新闻抓取")
    except Exception as e:
        print(f"✗ 抓取失败: {str(e)}")
    
    return []

def update_html(news_data):
    """更新 HTML 文件"""
    # 使用相对路径或当前工作目录
    html_path = Path(__file__).parent / 'index.html'
    
    if not html_path.exists():
        print(f"✗ index.html 不存在: {html_path}")
        return False
    
    # 读取现有 HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 更新时间戳（在 JavaScript 中）
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    html_content = html_content.replace(
        "最后更新: <span id=\"last-update-time\">加载中...</span>",
        f"最后更新: <span id=\"last-update-time\">{now}</span>"
    )
    
    # 如果有新数据，可以在这里添加新的时间线项
    # TODO: 实现智能添加新事件的逻辑
    
    # 写回文件
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ 已更新时间戳: {now}")
    return True

def main():
    """主函数"""
    print("=" * 50)
    print("伊朗以色列冲突追踪器 - 数据更新脚本")
    print("=" * 50)
    
    # 抓取最新新闻
    news_data = fetch_latest_news()
    
    if news_data:
        print(f"\n最新 {len(news_data)} 条消息:")
        for i, item in enumerate(news_data[:5], 1):
            print(f"{i}. {item.get('title', 'N/A')[:60]}...")
    
    # 更新 HTML
    update_html(news_data)
    
    print("\n更新完成！")
    print("=" * 50)

if __name__ == '__main__':
    main()
