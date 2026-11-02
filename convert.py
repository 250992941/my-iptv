import os
import urllib.request

def main():
    source_url = os.environ.get("SOURCE_M3U_URL")
    target_domain = os.environ.get("TARGET_PROXY_DOMAIN")
    naive_url = os.environ.get("NAIVE_NODE_URL") # 直接读取你的 HTTPS 节点
    
    if not source_url:
        print("错误: 未配置 SOURCE_M3U_URL")
        return

    print("正在通过 HTTPS 代理通道直接握手原始 M3U 列表中...")
    
    # 核心无客户端中转：直接将 NaiveProxy 节点作为底层标准代理注入 Python 传输层
    # 格式支持 https://user:pass@domain:port
    proxy_handler = urllib.request.ProxyHandler({
        'http': naive_url,
        'https': naive_url
    })
    
    opener = urllib.request.build_opener(proxy_handler)
    
    # 模拟最新版海外原生普通浏览器指纹，完美欺骗原服务器的 CF 防护
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'),
        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'),
        ('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7'),
        ('Connection', 'keep-alive')
    ]
    urllib.request.install_opener(opener)

    try:
        with urllib.request.urlopen(source_url, timeout=30) as response:
            m3u_content = response.read().decode('utf-8')
            print("原始列表通过代理直接抓取成功！")
    except Exception as e:
        print(f"抓取失败: {e}")
        return

    print(f"开始清洗流媒体地址并重写为目标路径: {target_domain}")
    
    original_domain = "caonima.898757.xyz"
    rewritten_content = m3u_content.replace(f"http://{original_domain}", f"https://{target_domain}")
    rewritten_content = rewritten_content.replace(f"https://{original_domain}", f"https://{target_domain}")

    output_path = "live.m3u"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rewritten_content)
    
    print(f"静态转换成功，已生成文件: {output_path}")

if __name__ == "__main__":
    main()
