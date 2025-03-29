from flask import Flask, render_template, request

app = Flask(__name__)

# 工具数据（包含分类标签）
tools = [
    {
        "name": "斯坦福STORM",
        "url": "https://storm.genie.stanford.edu/",
        "desc": "斯坦福大学开发的AI系统",
        "tags": ["学术", "研究", "英文"]
    },
    {
        "name": "ChatGPT",
        "url": "https://chatgpt.com/",
        "desc": "OpenAI开发的对话AI",
        "tags": ["通用", "写作", "编程"]
    },
    {
        "name": "Claude",
        "url": "https://www.anthropic.com/",
        "desc": "Anthropic开发的AI助手",
        "tags": ["通用", "长文本", "英文"]
    },
    {
        "name": "Google AI Studio",
        "url": "https://aistudio.google.com/app/prompts/new_chat",
        "desc": "Google的AI开发平台",
        "tags": ["开发", "API", "英文"]
    },
    {
        "name": "Google Gemini",
        "url": "https://gemini.google.com/app/b44b532ed0873a7a",
        "desc": "Google最新AI模型",
        "tags": ["通用", "多模态", "英文"]
    },
    {
        "name": "Deepseek",
        "url": "https://chat.deepseek.com/",
        "desc": "深度求索的AI聊天",
        "tags": ["中文", "编程", "免费"]
    },
    {
        "name": "扣子",
        "url": "https://www.coze.cn/store/agent?cate_type=category&cate_value=7331636528340451366",
        "desc": "字节跳动的AI平台",
        "tags": ["中文", "创作", "Bot"]
    },
    {
        "name": "QWEN",
        "url": "https://chat.qwen.ai/c/e1d40db7-5265-4a77-a85f-f3b5dc15b4e4",
        "desc": "通义千问AI",
        "tags": ["中文", "阿里云", "免费"]
    },
    {
        "name": "GitHub镜像站",
        "url": "https://github.akams.cn/",
        "desc": "GitHub镜像访问",
        "tags": ["开发", "镜像", "加速"]
    },
    {
        "name": "智谱清言",
        "url": "https://chatglm.cn/main/alltoolsdetail?redirect=/main/alltoolsdetail&lang=zh",
        "desc": "清华智谱的AI",
        "tags": ["中文", "学术", "免费"]
    },
    {
        "name": "Hugging Face Spaces",
        "url": "https://huggingface.co/spaces",
        "desc": "托管和分享机器学习Demo的平台",
        "tags": ["开发", "AI模型", "开源"]
    }
]

@app.route('/')
def index():
    search = request.args.get('search', '').lower()
    filtered = [t for t in tools if 
                search in t['name'].lower() or 
                search in t['desc'].lower() or 
                any(search in tag.lower() for tag in t['tags'])]
    return render_template('index.html', tools=filtered)

if __name__ == '__main__':
    app.run(debug=True)