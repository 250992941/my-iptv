import os
import urllib.request
import ssl

def main():
    source_url = os.environ.get("SOURCE_M3U_URL")
    target_domain = os.environ.get("TARGET_PROXY_DOMAIN", "caonima.898757.xyz")
    proxy_url = os.environ.get("HTTPS_PROXY_URL")
    
    # 基础变量严格判定
    if not source_url:
        raise Exception("致命错误: 未在 GitHub Secrets 中配置 SOURCE_M3U_URL")
    if not proxy_url:
        raise Exception("致命错误: 未在 GitHub Secrets 中配置 HTTPS_PROXY_URL")

    print(f"当前准备抓取的完整源地址: {source_url}")
    print("正在配置标准全局 HTTPS 代理网关（德国节点）...")
    
    # 忽略 SSL 证书校验，防止 GitHub 环境阻断
    ssl_context = ssl._create_unverified_context()
    
    proxy_handler = urllib.request.ProxyHandler({
        'http': proxy_url,
        'https': proxy_url
    })
    
    opener = urllib.request.build_opener(proxy_handler, urllib.request.HTTPSHandler(context=ssl_context))
    
    # 高级浏览器 Header 指纹伪装
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'),
        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'),
        ('Accept-Language', 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7'),
        ('Connection', 'keep-alive')
    ]
    urllib.request.install_opener(opener)

    print("开始建立网络连接并直接抓取原始 M3U 列表...")
    
    # 取消所有 try-except，让底层报错直接暴露在 Actions 面板上
    with urllib.request.urlopen(source_url, timeout=45) as response:
        m3u_content = response.read().decode('utf-8')
        print(f"【成功】原始播放列表抓取成功！数据大小: {len(m3u_content)} 字节")

    print(f"开始重写媒体流链接，目标路径: {target_domain}")
    original_domain = "caonima.898757.xyz"
    rewritten_content = m3u_content.replace(f"http://{original_domain}", f"https://{target_domain}")
    rewritten_content = rewritten_content.replace(f"https://{original_domain}", f"https://{target_domain}")

    output_path = "live.m3u"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rewritten_content)
    
    print(f"静态转换成功，已物理生成本地文件: {output_path}")

if __name__ == "__main__":
    main()
