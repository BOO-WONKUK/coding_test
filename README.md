# coding_test
This is an auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).


import requests
import re
import os
from datetime import datetime

README_PATH = 'test.md'

def get_difficulty_icon_path(level):
    difficulty_levels = {
        'Bronze V': 1, 'Bronze IV': 2, 'Bronze III': 3, 'Bronze II': 4, 'Bronze I': 5,
        'Silver V': 6, 'Silver IV': 7, 'Silver III': 8, 'Silver II': 9, 'Silver I': 10,
        'Gold V': 11, 'Gold IV': 12, 'Gold III': 13, 'Gold II': 14, 'Gold I': 15,
        'Platinum V': 16, 'Platinum IV': 17, 'Platinum III': 18, 'Platinum II': 19, 'Platinum I': 20,
        'Diamond V': 21, 'Diamond IV': 22, 'Diamond III': 23, 'Diamond II': 24, 'Diamond I': 25,
        'Ruby V': 26, 'Ruby IV': 27, 'Ruby III': 28, 'Ruby II': 29, 'Ruby I': 30
    }
    return f'<div align="center"><img src="https://github.com/mag123c/Codingtest/blob/main/icon/{difficulty_levels.get(level, 0)}.svg" /></div>'

def get_commit_messages():
    output = "[Bronze III] Title: 웰컴 키트, Time: 152 ms, Memory: 15976 KB -BaekjoonHub"
    if '-BaekjoonHub' not in output:
        raise ValueError('This commit is not from BaekjoonHub.')
    problem_info_match = re.search(r'\[(.*?)\] Title: (.*?), Time:', output)
    if not problem_info_match:
        raise ValueError('Commit message format is incorrect.')
    problem_level = problem_info_match.group(1)
    problem_title = problem_info_match.group(2)
    return problem_level, problem_title

def fetch_problem_link(title):
    try:
        req_url = f'https://solved.ac/api/v3/search/problem?query={title}&page=1'
        response = requests.get(req_url)
        response.raise_for_status()
        data = response.json()
        return f'https://www.acmicpc.net/problem/{data["items"][0]["problemId"]}'
    except Exception as e:
        print('Failed to fetch problem link:', e)
        return None

def parse_last_date(content):
    lines = content.strip().split('\n')
    return lines[-1].split('|')[2].strip()

def parse_last_idx(content):
    lines = content.strip().split('\n')
    return lines[-1].split('|')[1].strip()

async def update_readme():
    content = ''
    default_div = '<div align="center">\n\n'
    problem_level, problem_title = get_commit_messages()
    problem_link = fetch_problem_link(problem_title)
    
    new_entry = {
        'date': datetime(2024, 7, 1).strftime('%Y.%m.%d'),
        'title': problem_title,
        'level': problem_level
    }

    if os.path.exists(README_PATH):
        with open(README_PATH, 'r', encoding='utf-8') as file:
            content = file.read()

    details_content = re.findall(r'<details[\s\S]*?<\/details>', content) or []
    if details_content:
        details_content = [f'{detail}\n\n' for detail in details_content]

    cur_content = re.split(r'\n\n\n\n', content)[1] if content else ''
    cur_date = parse_last_date(cur_content)
    cur_idx = parse_last_idx(cur_content)
    table_header = (
        "| #  | 날짜 | 문제 | 난이도 |\n"
        "|:---:|:---:|:---:|:---:|\n"
    )

    if new_entry['date'][5:7] != cur_date[5:7]:
        update_content = f'<details>\n<summary>{cur_date[:7]} 풀이 목록</summary>\n{cur_content}\n</details>\n\n'
        new_table_row = f'| {1} | {new_entry["date"]} | [{new_entry["title"]}]({problem_link}) | {get_difficulty_icon_path(new_entry["level"])} |'
        content = default_div + ''.join(details_content) + update_content + table_header + new_table_row + "\n"
    else:
        new_table_row = f'| {int(cur_idx) + 1} | {new_entry["date"]} | [{new_entry["title"]}]({problem_link}) | {get_difficulty_icon_path(new_entry["level"])} |'
        cur_content = cur_content + "\n" + new_table_row + "\n"
        content = default_div + ''.join(details_content) + cur_content

    with open(README_PATH, 'w', encoding='utf-8') as file:
        file.write(content)

import asyncio
asyncio.run(update_readme())
