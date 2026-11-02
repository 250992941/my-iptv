import os
import urllib.request
import base64
from urllib.parse import urlparse

def main():
    source_url = os.environ.get("SOURCE_M3U_URL")
    target_domain = os.environ.get("TARGET_PROXY_DOMAIN")
    naive_url = os.environ.get("NAIVE_NODE_URL")
    
    if not source_url or not naive_url:
        print("错误: 未在 Secrets 中配置 SOURCE_M3U_URL 或 NAIVE_NODE_URL")
        return

    print("正在通过 Python 原生传输层解析并配置 NaiveProxy 节点...")
    
    try:
        # 解析你的 Naive 节点信息
        # 格式: https://user:pass@host:port
        parsed_node = urlparse(naive_url)
        node_host = parsed_node.hostname
        node_port = parsed_node.port if parsed_node.port else 443
        node_user = parsed_node.username
        node_pass = parsed_node.password
        
        # 构造 HTTPS 代理在传输层所需的密文认证头部 (Base64)
        auth_str = f"{node_user}:{node_pass}"
        auth_encoded = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
        
        # 组装纯 Python 识别的标准高级代理 Handler
        proxy_address = f"http://{node_host}:{node_port}" if parsed_node.scheme == "http" else f"https://{node_host}:{node_port}"
        
        print(f"正在建立与海外节点的 HTTPS 安全隧道: {node_host}:{node_port}")
        proxy_handler = urllib.request.ProxyHandler({
            'http': proxy_address,
            'https': proxy_address
        })
        
        opener = urllib.request.build_opener(proxy_handler)
        
        # 注入带有代理认证（Proxy-Authorization）和 Chrome 指纹的高级头部
        # 这样请求到达对方的 Cloudflare 盾时，会显示为由合法的海外代理完美转发
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'),
            ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
            ('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7'),
            ('Proxy-Authorization', f"Basic {auth_encoded}"),
            ('Connection', 'keep-alive')
        ]
        urllib.request.install_opener(opener)
        
        # 发起高匿名抓取
        print(f"开始抓取原始 M3U 播放列表...")
        req = urllib.request.Request(source_url)
        with urllib.request.urlopen(req, timeout=35) as response:
            m3u_content = response.read().decode('utf-8')
            print(f"【成功】播放列表成功越盾抓取！数据大小: {len(m3u_content)} 字节")
            
    except Exception as e:
        print(f"【失败】通过节点抓取遭遇网络或认证阻断: {e}")
        return

    print(f"正在进行国内播放地址重写重构...")
    original_domain = "caonima.898757.xyz"
    rewritten_content = m3u_content.replace(f"http://{original_domain}", f"https://{target_domain}")
    rewritten_content = rewritten_content.replace(f"https://{original_domain}", f"https://{target_domain}")

    output_path = "live.m3u"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rewritten_content)
    
    print(f"静态文件物理转换保存成功: {output_path}")

if __name__ == "__main__":
    main()
