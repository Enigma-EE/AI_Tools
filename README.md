# AI_Tools
 导航小工具


## 📌 简介

一个集成了多种在线生成式AI模型和服务的导航，方便快速访问当前主流AI服务平台。


## 🛠️ 包含的AI工具

| 工具名称 | 类别 | 特点 |
|---------|------|------|
| 斯坦福STORM | 学术研究 | 斯坦福大学开发的AI系统 |
| ChatGPT | 通用对话 | OpenAI旗舰产品 |
| Claude | 长文本处理 | Anthropic开发的AI助手 |
| Google AI Studio | 开发平台 | Google AI开发工具 |
| Deepseek | 中文AI | 深度求索的聊天AI |
| 智谱清言 | 中文AI | 清华智谱开发 |
...


## 🚀 快速开始

### 基本要求
- Python 3.10+
- Windows/macOS/Linux

### 安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/yourusername/ai-tools-navigator.git
cd ai-tools-navigator
```

2. **设置虚拟环境**
```bash
python -m venv venv
```

3. **激活环境**
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. **安装依赖**
```bash
pip install -r requirements.txt
```

### 运行应用

**方法1：使用启动脚本**
```bash
# Windows
双击 run.bat

# macOS/Linux
chmod +x run.sh
./run.sh
```

**方法2：手动运行**
```bash
python app.py
```

访问 [http://localhost:5000](http://localhost:5000)

## 🛠️ 自定义配置

1. **添加新工具**：
   修改 `app.py` 中的 `tools` 列表，按格式添加：
   ```python
   {
       "name": "工具名称",
       "url": "https://example.com",
       "desc": "简短描述",
       "tags": ["标签1", "标签2"]
   }
   ```

2. **修改样式**：
   编辑 `static/style.css` 文件

