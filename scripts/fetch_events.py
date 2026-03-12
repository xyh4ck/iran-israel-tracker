#!/usr/bin/env python3
"""
伊朗以色列冲突自动更新脚本
自动抓取新闻源并更新事件数据
"""

import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import re
import os

# 新闻源配置
NEWS_SOURCES = [
    {
        "name": "Al Jazeera",
        "url": "https://www.aljazeera.com/news/2026/3/12/iran-war-what-is-happening-on-day-13-of-us-israel-attacks",
        "language": "en"
    },
    {
        "name": "BBC",
        "url": "https://www.bbc.com/news/articles/c4g0pnnj8xyo",
        "language": "en"
    },
    {
        "name": "Reuters",
        "url": "https://www.reuters.com/business/energy/oil-climbs-tankers-are-attacked-iraqi-waters-amid-middle-east-war-2026-03-12/",
        "language": "en"
    }
]

def fetch_news(url):
    """抓取新闻页面"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_events_from_html(html, source_name):
    """从HTML中提取事件信息"""
    events = []
    if not html:
        return events
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # 这里需要根据具体网站的HTML结构来解析
    # 示例: 提取标题和摘要
    # 实际使用时需要针对每个新闻源编写特定的解析逻辑
    
    # 这是一个占位符实现
    print(f"Extracting events from {source_name}...")
    
    return events

def generate_event_id(date, title):
    """生成事件ID"""
    # 将标题转换为拼音或简单的英文标识
    title_clean = re.sub(r'[^\w\s-]', '', title)
    title_clean = re.sub(r'[\s]+', '-', title_clean)
    title_clean = title_clean[:50]  # 限制长度
    return f"{date}-{title_clean}"

def update_events_json(events_file='data/events.json'):
    """更新事件JSON文件"""
    
    # 读取现有数据
    existing_data = {"events": []}
    if os.path.exists(events_file):
        with open(events_file, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    
    # 抓取新闻
    new_events = []
    for source in NEWS_SOURCES:
        html = fetch_news(source['url'])
        events = extract_events_from_html(html, source['name'])
        new_events.extend(events)
    
    # 合并新旧事件
    if new_events:
        # 简单的合并逻辑:实际需要更复杂的去重和验证
        existing_events = existing_data.get('events', [])
        all_events = existing_events + new_events
        
        # 更新元数据
        existing_data['metadata']['last_updated'] = datetime.now(timezone.utc).isoformat()
        existing_data['metadata']['total_events'] = len(all_events)
        
        # 保存
        with open(events_file, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)
        
        print(f"Updated {len(new_events)} new events")
    else:
        print("No new events found")

def update_html_from_json(events_file='data/events.json', html_file='index.html'):
    """根据JSON数据更新HTML文件"""
    
    # 读取JSON数据
    with open(events_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 这里需要生成HTML内容
    # 实际实现需要完整的HTML模板和渲染逻辑
    print(f"Generating HTML from {len(data['events'])} events...")

def main():
    """主函数"""
    print("=== 伊朗以色列冲突自动更新脚本 ===")
    print(f"运行时间: {datetime.now()}")
    
    # 更新JSON数据
    update_events_json()
    
    # 更新HTML
    update_html_from_json()
    
    print("=== 更新完成 ===")

if __name__ == '__main__':
    main()
